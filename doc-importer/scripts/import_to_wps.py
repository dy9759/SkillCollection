#!/usr/bin/env python3
"""
import_to_wps.py - 使用 wpsnote-cli 将转换好的文档批量导入到 WPS 笔记

这是导入流水线的最后一步，使用 wpsnote-cli 直接操作 WPS 笔记，
比通过 MCP 更快（减少来回通信），适合批量导入。

用法：
    python3 import_to_wps.py <文件路径> [选项]
    python3 import_to_wps.py <目录路径> [选项]   # 批量导入整个目录

选项：
    --convert-dir DIR       已转换的文件目录（convert.py 的 --output-dir）
    --on-conflict STR       冲突处理：ask | overwrite | skip | append（默认 ask）
    --dry-run               只打印操作，不实际执行
    --tag STR               为导入的笔记打额外标签（如 "#项目A"）
    --source TYPE           来源类型（用于自动打标签）：obsidian|siyuan|generic
    --no-tag                不自动打来源标签
    --batch-size N          每批并发处理的文件数（默认 1，串行）

前置要求：
    wpsnote-cli 已安装并配置好 API Key
    （运行 wpsnote-cli status 确认连接正常）
"""

import os
import sys
import json
import subprocess
import argparse
import datetime
import tempfile
import time
from pathlib import Path


# ─── CLI 封装 ─────────────────────────────────────────────────────────────────

def cli_run(args: list, check: bool = True) -> dict:
    """执行 wpsnote-cli 命令，返回 JSON 结果"""
    cmd = ['wpsnote-cli'] + args + ['--json']
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        data = {'ok': False, 'error': result.stderr or result.stdout}
    if check and not data.get('ok', False):
        raise RuntimeError(f"CLI 错误: {data.get('error', data)}")
    return data


def cli_check() -> bool:
    """检查 wpsnote-cli 是否可用且已连接"""
    try:
        result = subprocess.run(
            ['wpsnote-cli', 'status'],
            capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def cli_find_note_by_title(title: str) -> str:
    """按标题搜索笔记，返回 note_id 或 None"""
    try:
        data = cli_run(['find', '--keyword', title, '--limit', '5'], check=False)
        notes = data.get('data', {}).get('notes', [])
        for note in notes:
            if note.get('title') == title:
                return note.get('note_id')
    except Exception:
        pass
    return None


def cli_create_note(title: str) -> str:
    """创建笔记，返回 note_id"""
    data = cli_run(['create', '--title', title])
    return data.get('data', {}).get('fileId') or data.get('data', {}).get('note_id')


def cli_get_outline(note_id: str) -> dict:
    """获取笔记大纲，返回 blocks 列表"""
    data = cli_run(['outline', '--note_id', note_id])
    return data.get('data', {})


def cli_batch_edit(note_id: str, operations: list) -> dict:
    """批量编辑，使用 --json-args 避免引号转义问题"""
    args_json = json.dumps({
        'note_id': note_id,
        'operations': operations,
    })
    return cli_run(['batch-edit', '--json-args', args_json])


def cli_edit_insert(note_id: str, anchor_id: str, content: str) -> dict:
    """在 anchor_id 后插入内容"""
    args_json = json.dumps({
        'note_id': note_id,
        'op': 'insert',
        'anchor_id': anchor_id,
        'position': 'after',
        'content': content,
    })
    return cli_run(['edit', '--json-args', args_json])


def cli_edit_replace(note_id: str, block_id: str, content: str) -> dict:
    """替换 block 内容"""
    args_json = json.dumps({
        'note_id': note_id,
        'op': 'replace',
        'block_id': block_id,
        'content': content,
    })
    return cli_run(['edit', '--json-args', args_json])


def cli_insert_image(note_id: str, anchor_id: str, src_or_file: str, is_file: bool = False) -> dict:
    """
    插入图片
    - is_file=True：src_or_file 是包含 base64 数据的文件路径（避免命令行长度限制）
    - is_file=False：src_or_file 是 base64 data URI 或 HTTP URL
    """
    if is_file:
        args_json = json.dumps({
            'note_id': note_id,
            'anchor_id': anchor_id,
            'position': 'after',
            'src_file': src_or_file,
        })
    else:
        args_json = json.dumps({
            'note_id': note_id,
            'anchor_id': anchor_id,
            'position': 'after',
            'src': src_or_file,
        })
    return cli_run(['insert-image', '--json-args', args_json])


def cli_add_tag(note_id: str, last_block_id: str, tag: str) -> str:
    """在笔记末尾追加标签，返回新的 last_block_id"""
    # WPS 标签：#a/b/c → <tag>#a//b//c</tag>
    wps_tag = tag.replace('/', '//')
    if not wps_tag.startswith('#'):
        wps_tag = '#' + wps_tag
    content = f'<p><tag>{wps_tag}</tag></p>'
    result = cli_edit_insert(note_id, last_block_id, content)
    return result.get('data', {}).get('last_block_id', last_block_id)


# ─── 导入单篇笔记 ─────────────────────────────────────────────────────────────

def import_one(
    convert_dir: Path,
    on_conflict: str = 'ask',
    extra_tags: list = None,
    source_type: str = 'generic',
    auto_tag: bool = True,
    dry_run: bool = False,
    verbose: bool = True,
) -> dict:
    """
    将一个 convert.py 输出目录导入到 WPS 笔记

    Returns:
        dict: {success, note_id, note_title, images_ok, skipped, error}
    """

    # 读取转换产物
    meta_path = convert_dir / 'meta.json'
    xml_path = convert_dir / 'content.xml'
    meta_xml_path = convert_dir / 'meta.xml'
    images_path = convert_dir / 'images.json'

    if not meta_path.exists() or not xml_path.exists():
        return {'success': False, 'error': f'转换产物不完整：{convert_dir}'}

    meta = json.loads(meta_path.read_text(encoding='utf-8'))
    xml_content = xml_path.read_text(encoding='utf-8')
    meta_xml = meta_xml_path.read_text(encoding='utf-8') if meta_xml_path.exists() else ''
    images = json.loads(images_path.read_text(encoding='utf-8')) if images_path.exists() else {}

    note_title = meta.get('note_title', convert_dir.name)
    if verbose:
        print(f"  → 准备导入：《{note_title}》（{len(images)} 张图片）")

    # ── 冲突检测 ─────────────────────────────────────────
    existing_note_id = cli_find_note_by_title(note_title)
    action = 'create'

    if existing_note_id:
        if on_conflict == 'skip':
            if verbose:
                print(f"  ⏭ 跳过（已存在）：《{note_title}》")
            return {'success': True, 'skipped': True, 'note_title': note_title}

        elif on_conflict == 'ask':
            print(f"\n  ⚠️  WPS 笔记中已存在《{note_title}》")
            print("     [O] 覆盖  [S] 跳过  [A] 追加末尾  > ", end='', flush=True)
            choice = input().strip().upper()
            if choice == 'S':
                return {'success': True, 'skipped': True, 'note_title': note_title}
            elif choice == 'A':
                action = 'append'
            else:
                action = 'overwrite'

        elif on_conflict == 'overwrite':
            action = 'overwrite'
        elif on_conflict == 'append':
            action = 'append'

    if dry_run:
        print(f"  [DRY RUN] 将 {'创建' if not existing_note_id else action}：《{note_title}》")
        return {'success': True, 'dry_run': True, 'note_title': note_title}

    # ── 创建或使用现有笔记 ────────────────────────────────
    if action == 'create' or (action == 'overwrite' and not existing_note_id):
        note_id = cli_create_note(note_title)
        if verbose:
            print(f"  ✓ 创建笔记：note_id={note_id}")
    else:
        note_id = existing_note_id

    # ── 获取初始大纲，找到锚点 block ──────────────────────
    outline = cli_get_outline(note_id)
    blocks = outline.get('blocks', [])
    if not blocks:
        return {'success': False, 'error': f'获取大纲失败：note_id={note_id}'}

    # overwrite：清空现有内容（替换第一个 block，删除其余）
    if action == 'overwrite' and len(blocks) > 0:
        first_id = blocks[0]['id']
        # 替换第一个 block 为 meta
        if meta_xml:
            cli_edit_replace(note_id, first_id, meta_xml)
        # 删除其余 blocks（如有）
        if len(blocks) > 1:
            block_ids = [b['id'] for b in blocks[1:]]
            args_json = json.dumps({
                'note_id': note_id,
                'op': 'delete',
                'block_ids': block_ids,
            })
            cli_run(['edit', '--json-args', args_json], check=False)
        # 重新获取大纲
        outline = cli_get_outline(note_id)
        blocks = outline.get('blocks', [])
        anchor_id = blocks[-1]['id']

    elif action == 'create':
        # 新建笔记：替换初始空 block 为 meta
        first_id = blocks[0]['id']
        if meta_xml:
            cli_edit_replace(note_id, first_id, meta_xml)
            outline = cli_get_outline(note_id)
            blocks = outline.get('blocks', [])
        anchor_id = blocks[-1]['id']

    else:
        # append：直接追加到末尾
        anchor_id = blocks[-1]['id']
        # 追加分隔线
        result = cli_edit_insert(note_id, anchor_id, '<hr/>')
        anchor_id = result.get('data', {}).get('last_block_id', anchor_id)

    # ── 写入正文内容 ──────────────────────────────────────
    # 将 XML 内容分成若干批（每批最多约 20 个块，避免单次请求过大）
    # 先把图片占位符提取出来，按位置顺序排列
    placeholders_in_order = []
    for ph in images:
        pos = xml_content.find(ph)
        if pos >= 0:
            placeholders_in_order.append((pos, ph))
    placeholders_in_order.sort(key=lambda x: x[0])

    # 分段写入：每个图片占位符之间为一段文本
    segments = []
    last_pos = 0
    for pos, ph in placeholders_in_order:
        text_before = xml_content[last_pos:pos].strip()
        if text_before:
            segments.append(('xml', text_before))
        segments.append(('image', ph, images[ph]))
        last_pos = pos + len(ph)
    remaining = xml_content[last_pos:].strip()
    if remaining:
        segments.append(('xml', remaining))

    images_ok = 0
    images_fail = 0

    for seg in segments:
        if seg[0] == 'xml':
            content = seg[1]
            if not content:
                continue
            try:
                result = cli_edit_insert(note_id, anchor_id, content)
                anchor_id = result.get('data', {}).get('last_block_id', anchor_id)
            except Exception as e:
                if verbose:
                    print(f"  ⚠️  写入文本段失败：{e}")

        elif seg[0] == 'image':
            ph, img_data = seg[1], seg[2]
            try:
                if img_data.startswith('data:') and len(img_data) > 4096:
                    # 大图片：写入临时文件，用 --src_file 传入
                    with tempfile.NamedTemporaryFile(
                        mode='w', suffix='.txt', delete=False, encoding='utf-8'
                    ) as f:
                        f.write(img_data)
                        tmp_path = f.name
                    try:
                        result = cli_insert_image(note_id, anchor_id, tmp_path, is_file=True)
                    finally:
                        os.unlink(tmp_path)
                else:
                    result = cli_insert_image(note_id, anchor_id, img_data)
                anchor_id = result.get('data', {}).get('block_id', anchor_id)
                images_ok += 1
            except Exception as e:
                images_fail += 1
                if verbose:
                    print(f"  ⚠️  图片插入失败：{e}")

    # ── 打标签 ────────────────────────────────────────────
    if auto_tag:
        today = datetime.date.today().isoformat()
        source_label = {'obsidian': 'Obsidian', 'siyuan': '思源', 'generic': '文档'}.get(source_type, '文档')
        auto_tag_str = f'#导入//{source_label}//{today}'
        try:
            anchor_id = cli_add_tag(note_id, anchor_id, auto_tag_str)
        except Exception as e:
            if verbose:
                print(f"  ⚠️  自动标签失败：{e}")

    if extra_tags:
        for tag in extra_tags:
            try:
                anchor_id = cli_add_tag(note_id, anchor_id, tag)
            except Exception as e:
                if verbose:
                    print(f"  ⚠️  标签 {tag} 失败：{e}")

    if verbose:
        img_info = f'，图片 {images_ok}/{images_ok + images_fail}' if images else ''
        print(f"  ✓ 导入完成：《{note_title}》{img_info}")

    return {
        'success': True,
        'note_id': note_id,
        'note_title': note_title,
        'images_ok': images_ok,
        'images_fail': images_fail,
        'action': action,
    }


# ─── 批量导入入口 ─────────────────────────────────────────────────────────────

def import_batch(
    input_path: Path,
    on_conflict: str = 'ask',
    extra_tags: list = None,
    source_type: str = 'generic',
    auto_tag: bool = True,
    dry_run: bool = False,
    convert_dir_root: Path = None,
) -> dict:
    """
    批量导入：input_path 可以是：
    - 单个文档文件（.md/.pdf/.docx/.pptx/.xlsx/.sy）
    - convert.py 的输出目录（含 meta.json）
    - 包含多个 convert 输出目录的父目录
    """
    results = []

    # 判断 input_path 类型
    if input_path.is_dir() and (input_path / 'meta.json').exists():
        # 单个 convert 输出目录
        dirs_to_import = [input_path]
    elif input_path.is_dir():
        # 多个 convert 输出目录
        dirs_to_import = [d for d in sorted(input_path.iterdir())
                          if d.is_dir() and (d / 'meta.json').exists()]
    else:
        # 直接是文件，先用 convert.py 转换
        dirs_to_import = []
        if not convert_dir_root:
            convert_dir_root = Path(tempfile.mkdtemp(prefix='doc_import_'))
        out_dir = convert_dir_root / input_path.stem
        print(f"📄 转换：{input_path.name} ...")
        convert_result = subprocess.run(
            [
                'python3',
                str(Path(__file__).parent / 'convert.py'),
                str(input_path),
                '--output-dir', str(out_dir),
                '--source', source_type,
            ],
            capture_output=True, text=True
        )
        if convert_result.returncode == 0:
            dirs_to_import = [out_dir]
        else:
            print(f"  ❌ 转换失败：{convert_result.stderr}")
            return {'total': 0, 'success': 0, 'failed': 1, 'skipped': 0}

    total = len(dirs_to_import)
    success = skip = fail = 0

    for i, d in enumerate(dirs_to_import, 1):
        print(f"\n[{i}/{total}] 导入 {d.name}")
        try:
            r = import_one(
                convert_dir=d,
                on_conflict=on_conflict,
                extra_tags=extra_tags,
                source_type=source_type,
                auto_tag=auto_tag,
                dry_run=dry_run,
            )
            if r.get('skipped'):
                skip += 1
            elif r.get('success'):
                success += 1
            else:
                fail += 1
                print(f"  ❌ 失败：{r.get('error')}")
        except Exception as e:
            fail += 1
            print(f"  ❌ 异常：{e}")

    return {'total': total, 'success': success, 'failed': fail, 'skipped': skip}


# ─── 完整扫描→转换→导入一体化流程 ────────────────────────────────────────────

def full_pipeline(
    scan_dir: Path,
    on_conflict: str = 'ask',
    extra_tags: list = None,
    source_type: str = 'auto',
    auto_tag: bool = True,
    dry_run: bool = False,
    days: int = None,
    formats: list = None,
    selected_indices: list = None,
):
    """
    完整流水线：扫描 → 询问用户选择 → 转换 → 用 wpsnote-cli 导入

    这是最终用户直接调用的函数。
    """
    import importlib.util, sys

    # 动态加载同目录的 scan_docs 和 convert
    scripts_dir = Path(__file__).parent

    def load_module(name, path):
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    scan_mod = load_module('scan_docs', scripts_dir / 'scan_docs.py')
    convert_mod = load_module('convert', scripts_dir / 'convert.py')

    # 1. 扫描
    print(f"\n🔍 扫描目录：{scan_dir}")
    scan_result = scan_mod.scan_directory(
        root_path=scan_dir,
        days=days,
        source_type=source_type,
        formats=formats,
    )

    if 'error' in scan_result:
        print(f"❌ 扫描失败：{scan_result['error']}")
        return

    detected_source = scan_result['source_type']
    files = scan_result['files']

    # 2. 展示文件清单
    print(scan_mod.format_file_list_for_display(scan_result))

    # 3. 读取用户选择（如果已通过参数传入则跳过）
    if selected_indices is None:
        choice = input("\n请输入选项 > ").strip().upper()
        if choice == 'A':
            selected_files = files
        elif len(choice) == 1:
            # 按格式过滤
            ext_map = {'M': 'md', 'P': 'pdf', 'D': 'docx', 'X': 'xlsx', 'S': 'sy'}
            ext = ext_map.get(choice)
            if ext:
                selected_files = [f for f in files if f['ext'] == ext]
            else:
                selected_files = files
        else:
            # 手动选择：解析 "1,3,5-10"
            selected_files = []
            for part in choice.split(','):
                part = part.strip()
                if '-' in part:
                    start, end = part.split('-', 1)
                    for idx in range(int(start), int(end) + 1):
                        if 1 <= idx <= len(files):
                            selected_files.append(files[idx - 1])
                elif part.isdigit():
                    idx = int(part)
                    if 1 <= idx <= len(files):
                        selected_files.append(files[idx - 1])
    else:
        selected_files = [files[i - 1] for i in selected_indices if 1 <= i <= len(files)]

    if not selected_files:
        print("⚠️  没有选择任何文件，退出。")
        return

    print(f"\n✅ 已选择 {len(selected_files)} 个文件，开始转换并导入...")

    # 4. 转换 + 导入
    tmp_root = Path(tempfile.mkdtemp(prefix='doc_import_'))
    total = success = skip = fail = 0
    fail_list = []

    for i, file_info in enumerate(selected_files, 1):
        file_path = Path(file_info['path'])
        name_safe = re.sub(r'[^\w\u4e00-\u9fa5\-]', '_', file_path.stem)
        out_dir = tmp_root / f"{i:04d}_{name_safe}"

        print(f"\n[{i}/{len(selected_files)}] {file_info['rel_path']}")
        print(f"  ▸ 转换中...", end='', flush=True)

        try:
            convert_result = convert_mod.convert_file(
                file_path=file_path,
                output_dir=out_dir,
                source_type=detected_source,
                root_path=scan_dir,
            )
            if not convert_result.get('success'):
                raise RuntimeError(convert_result.get('error', '未知错误'))
            print(f" ✓ (图片:{convert_result['image_count']})")
        except Exception as e:
            fail += 1
            fail_list.append((file_info['rel_path'], str(e)))
            print(f" ❌ {e}")
            continue

        print(f"  ▸ 导入中...")
        try:
            r = import_one(
                convert_dir=out_dir,
                on_conflict=on_conflict,
                extra_tags=extra_tags,
                source_type=detected_source,
                auto_tag=auto_tag,
                dry_run=dry_run,
                verbose=True,
            )
            total += 1
            if r.get('skipped'):
                skip += 1
            elif r.get('success'):
                success += 1
            else:
                fail += 1
                fail_list.append((file_info['rel_path'], r.get('error', '未知')))
        except Exception as e:
            fail += 1
            fail_list.append((file_info['rel_path'], str(e)))
            print(f"  ❌ 导入失败：{e}")

    # 5. 汇总报告
    source_label = {'obsidian': 'Obsidian', 'siyuan': '思源', 'generic': '文档'}.get(detected_source, '文档')
    today = datetime.date.today().isoformat()

    print(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 导入完成！汇总：
   ✓ 成功：{success} 篇
   ⏭ 跳过：{skip} 篇
   ✗ 失败：{fail} 篇
   📂 来源：{source_label}
""")
    if fail_list:
        print("  失败详情：")
        for name, err in fail_list:
            print(f"    - {name}：{err}")

    if auto_tag and not dry_run:
        tag = f"#导入//{source_label}//{today}"
        print(f"\n  可在 WPS 笔记搜索标签 {tag} 查看所有导入的笔记。")


import re


def main():
    parser = argparse.ArgumentParser(description='使用 wpsnote-cli 将文档导入到 WPS 笔记')
    parser.add_argument('input', help='文档文件、convert 输出目录，或要扫描的目录')
    parser.add_argument('--on-conflict', default='ask',
                        choices=['ask', 'overwrite', 'skip', 'append'],
                        help='冲突处理策略（默认 ask）')
    parser.add_argument('--tag', action='append', dest='tags', help='额外标签（可多次传入）')
    parser.add_argument('--no-tag', action='store_true', help='不自动打来源标签')
    parser.add_argument('--source', default='auto',
                        choices=['auto', 'obsidian', 'siyuan', 'generic'],
                        help='来源类型（默认自动检测）')
    parser.add_argument('--days', type=int, help='只导入最近 N 天内修改的文件')
    parser.add_argument('--formats', help='只导入指定格式，逗号分隔（如 md,pdf）')
    parser.add_argument('--dry-run', action='store_true', help='只打印操作，不实际执行')
    parser.add_argument('--select', help='预先选择文件编号，如 1,3,5-10（跳过交互）')
    args = parser.parse_args()

    # 检查 CLI 连接
    if not cli_check():
        print("❌ wpsnote-cli 未连接，请运行：wpsnote-cli status")
        sys.exit(1)

    input_path = Path(args.input).resolve()
    formats = [f.strip().lower() for f in args.formats.split(',')] if args.formats else None

    # 解析预选文件
    selected = None
    if args.select:
        selected = []
        for part in args.select.split(','):
            part = part.strip()
            if '-' in part:
                s, e = part.split('-', 1)
                selected.extend(range(int(s), int(e) + 1))
            elif part.isdigit():
                selected.append(int(part))

    # 判断调用方式
    if input_path.is_dir() and (input_path / 'meta.json').exists():
        # 直接是 convert 输出目录
        r = import_one(
            convert_dir=input_path,
            on_conflict=args.on_conflict,
            extra_tags=args.tags,
            source_type=args.source if args.source != 'auto' else 'generic',
            auto_tag=not args.no_tag,
            dry_run=args.dry_run,
        )
        print(json.dumps(r, ensure_ascii=False, indent=2))

    else:
        # 完整流水线
        full_pipeline(
            scan_dir=input_path,
            on_conflict=args.on_conflict,
            extra_tags=args.tags,
            source_type=args.source,
            auto_tag=not args.no_tag,
            dry_run=args.dry_run,
            days=args.days,
            formats=formats,
            selected_indices=selected,
        )


if __name__ == '__main__':
    main()
