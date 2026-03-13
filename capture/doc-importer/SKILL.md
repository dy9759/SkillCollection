---
name: doc-importer
description: >
  将本地文档批量导入到 WPS 笔记。支持扫描 Obsidian Vault、思源笔记、下载目录
  或任意用户指定目录，自动识别 Markdown、PDF、DOCX、PPTX、XLSX 等格式，
  转换为 WPS 笔记可读内容并保留图片。
  当用户说「导入文档到 WPS 笔记」「把我的 Obsidian 笔记导入」「导入思源笔记」
  「把下载的 PDF/Word/PPT 导入笔记」「同步本地文档到 WPS 笔记」时触发。
  不适用于直接编辑 WPS 笔记内容、文档格式转换（不导入到笔记）。
license: MIT
metadata:
  author: 洛小山 (itshen)
  version: 1.1.0
  mcp-server: user-wpsnote
  category: productivity
  tags: [obsidian, siyuan, import, pdf, docx, pptx, markdown]
---

# 文档导入器（Doc Importer）

将本地文档（Obsidian、思源笔记、下载目录或任意目录）批量导入到 WPS 笔记。

## 导入方式选择

**优先使用 `wpsnote-cli` 脚本方式**，比 MCP 逐步操作更快（减少来回通信开销，批量写入更高效）：

```
第一步：检查 CLI 是否可用
wpsnote-cli status

若输出"连接中... 成功"→ 使用 scripts/import_to_wps.py 一键导入
若失败 → 退回 MCP 逐步操作（见"完整工作流"章节）
```

### 方式一：CLI 一键完整流水线（推荐）

```bash
# 基本用法：扫描目录 → 询问选择 → 转换 → 导入（全自动）
python3 scripts/import_to_wps.py ~/Documents/MyVault

# 指定来源类型（可省略，会自动检测）
python3 scripts/import_to_wps.py ~/Documents/MyVault --source obsidian

# 思源笔记
python3 scripts/import_to_wps.py ~/SiYuan --source siyuan

# 只导入最近7天修改的 PDF 和 Word
python3 scripts/import_to_wps.py ~/Downloads --days 7 --formats pdf,docx

# 跳过冲突（不询问）
python3 scripts/import_to_wps.py ~/Downloads --on-conflict skip

# 预先选择文件编号，不进入交互（如导入第1、3、5-10个文件）
python3 scripts/import_to_wps.py ~/Downloads --select 1,3,5-10

# 添加额外标签
python3 scripts/import_to_wps.py ~/Downloads --tag "#项目A"

# 先演习，不实际写入
python3 scripts/import_to_wps.py ~/Downloads --dry-run
```

### 方式二：分步骤（转换 + 导入分离）

```bash
# 第一步：扫描目录，列出文件
python3 scripts/scan_docs.py ~/Downloads --display

# 第二步：转换单个文件（生成 WPS XML + 提取图片）
python3 scripts/convert.py ~/Downloads/report.pdf --output-dir /tmp/converted/

# 第三步：用 CLI 导入转换产物
python3 scripts/import_to_wps.py /tmp/converted/ --on-conflict ask
```

### 方式三：MCP 逐步操作（CLI 不可用时的备选）

见下方"完整工作流"章节。

## 支持的文档来源

| 来源 | 说明 |
|------|------|
| Obsidian Vault | 扫描 .md 文件，保留 Obsidian wiki 链接语法 |
| 思源笔记 | 扫描 .sy 文件（JSON格式），提取笔记内容 |
| 任意目录 | 用户指定路径，支持递归扫描子目录 |

## 支持的文件格式

| 格式 | 转换方式 | 图片处理 |
|------|----------|----------|
| `.md` / `.markdown` | 直接解析，转为 WPS XML | 本地图片读取为 base64 |
| `.pdf` | pdfplumber 提取文本 + pdfimages 提取图片 | 提取嵌入图片 |
| `.docx` | pandoc 转 markdown，提取媒体文件 | unpack 解包提取 word/media/ |
| `.pptx` | markitdown 提取文本 + unpack 提取媒体 | unpack 解包提取 ppt/media/ |
| `.xlsx` | pandas 读取，表格转 WPS XML table | 不含图片 |
| `.txt` | 直接读取 | 不含图片 |
| `.sy` | JSON 解析，提取思源 block tree | 提取 assets 图片 |

---

## 完整工作流

### 第一步：确定扫描目录

**优先检测常见目录（不要直接问用户，先尝试自动探测）：**

```bash
# 检测 Obsidian Vault（macOS 默认位置）
ls ~/Documents/ | grep -i obsidian
ls ~/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/ 2>/dev/null

# 检测思源笔记工作空间（macOS 默认位置）
ls ~/Documents/SiYuan/ 2>/dev/null
ls ~/SiYuan/ 2>/dev/null

# 检测下载目录
ls ~/Downloads/ | grep -E "\.(pdf|docx|pptx|xlsx|md)$" | head -10
```

**如果用户已指定路径，直接使用。否则展示探测结果，让用户确认。**

---

### 第二步：扫描文档列表

使用扫描脚本列出目标目录中所有支持的文档：

```bash
python3 scripts/scan_docs.py <目录路径> [--recursive] [--days N]
```

参数说明：
- `--recursive`：递归扫描子目录（默认启用）
- `--days N`：只列出最近 N 天内修改的文件（不传则全部列出）
- `--source obsidian|siyuan|generic`：声明来源类型，影响解析方式

**脚本输出 JSON，格式如下：**
```json
{
  "source_type": "obsidian",
  "root_path": "/Users/xxx/Documents/MyVault",
  "files": [
    {
      "path": "/Users/xxx/Documents/MyVault/工作/项目笔记.md",
      "rel_path": "工作/项目笔记.md",
      "size_bytes": 2048,
      "modified": "2025-03-10T14:23:00",
      "format": "md",
      "estimated_images": 2
    }
  ],
  "total": 42,
  "formats": {"md": 30, "pdf": 8, "docx": 4}
}
```

---

### 第三步：展示文件列表，询问用户选择

扫描完成后，**必须展示文件清单并询问用户**。展示格式如下：

```
扫描到 42 个文件：
  - Markdown: 30 个
  - PDF:       8 个
  - DOCX:      4 个

文件列表：
 1. 工作/项目笔记.md          (2025-03-10, 2.0KB, 含2张图片)
 2. 工作/会议记录-0310.md     (2025-03-10, 1.5KB)
 3. 资料/API设计文档.pdf      (2025-03-08, 560KB, 含5张图片)
 ...（截断超过20个时只展示前20个，告知总数）

请问你想如何导入？
 [A] 全部导入（42个文件）
 [B] 只导入 Markdown 文件（30个）
 [C] 只导入 PDF 文件（8个）
 [D] 手动选择（输入文件编号，如：1,3,5-10）
```

**选择规则：**
- 默认推荐选项 [A] 全部导入
- 如果文件数量超过 100，提示用户注意导入时间
- 等待用户输入后再继续

---

### 第四步：冲突检测

导入前检查 WPS 笔记中是否已有同名笔记：

```
# 通过 MCP 搜索
search_notes({ keyword: "<文件名不含扩展名>" })
```

**如果发现同名笔记，询问用户：**
```
发现以下文件在 WPS 笔记中已存在同名笔记：
 - 项目笔记.md → WPS笔记《项目笔记》（最后更新：2025-03-08）

请问如何处理？
 [O] 覆盖（替换笔记全部内容）
 [S] 跳过（保留现有笔记，不导入）
 [A] 追加（在现有笔记末尾追加，加时间戳分隔）
 [RA] 对所有冲突应用相同策略
```

---

### 第五步：转换并导入

**如果 `wpsnote-cli` 可用（推荐）**，直接用 `import_to_wps.py` 一键完成，跳过 5.1～5.3：

```bash
python3 scripts/import_to_wps.py <扫描目录或单个文件>
```

---

**如果 CLI 不可用**，对每个选定文件手动执行以下流程：

#### 5.1 转换文档

```bash
python3 scripts/convert.py <文件路径> --output-dir /tmp/doc_import_<timestamp>/
```

输出（`--output-dir` 下）：
- `content.xml`：转换后的 WPS XML 内容
- `meta.xml`：meta 引用块 XML
- `images.json`：图片 {placeholder: base64_data_uri}
- `meta.json`：元数据（原始路径、文件名、修改时间、大小等）

详细转换规则见 `references/conversion-guide.md`。

#### 5.2 构建 WPS 笔记 Meta 信息块

每篇导入的笔记**顶部必须插入**一个引用格式的 meta 信息块：

```xml
<blockquote>
  <p>📄 <strong>导入来源</strong>：<code>{rel_path}</code></p>
  <p>📁 <strong>原始路径</strong>：<code>{abs_path}</code></p>
  <p>🕒 <strong>文件修改时间</strong>：{modified_time}</p>
  <p>📦 <strong>文件大小</strong>：{size}</p>
  <p>🔄 <strong>导入时间</strong>：{import_time}</p>
  <p>📂 <strong>来源类型</strong>：{source_type}（Obsidian / 思源笔记 / 通用目录）</p>
</blockquote>
```

#### 5.3 创建或更新 WPS 笔记（MCP 方式）

```
# 创建新笔记
create_note({ title: "<文件名不含扩展名>" })

# 获取空笔记的初始 block ID
get_note_outline({ note_id })

# 批量写入：先写 meta 块，再写正文内容
batch_edit({ note_id, operations: [
  { op: "replace", block_id: "<空段落id>", content: "<blockquote>...meta...</blockquote>" },
  { op: "insert", anchor_id: "<meta块id>", position: "after", content: "<正文XML>" }
]})
```

**等效的 CLI 写法：**

```bash
# 创建笔记
NOTE_ID=$(wpsnote-cli create --title "笔记标题" --json | jq -r '.data.fileId')

# 获取初始 block ID
BLOCK_ID=$(wpsnote-cli outline --note_id "$NOTE_ID" --json | jq -r '.data.blocks[0].id')

# 写入 meta 块（替换初始空段落）
wpsnote-cli edit --json-args "{\"note_id\":\"$NOTE_ID\",\"op\":\"replace\",\"block_id\":\"$BLOCK_ID\",\"content\":\"<blockquote>...</blockquote>\"}"

# 获取最新 last block ID 后插入正文
wpsnote-cli edit --json-args "{\"note_id\":\"$NOTE_ID\",\"op\":\"insert\",\"anchor_id\":\"$BLOCK_ID\",\"position\":\"after\",\"content\":\"<h1>正文...</h1>\"}"
```

> 提示：命令行中 XML 含特殊字符时，推荐用 `--json-args` 传 JSON 对象，避免 shell 转义问题。

#### 5.4 插入图片

**MCP 方式：**

```
insert_image({
  note_id,
  anchor_id: "<图片占位符的前一个 block_id>",
  position: "after",
  src: "data:image/png;base64,<base64数据>"
})
```

**CLI 方式（推荐，大图片用 --src_file 避免命令行长度限制）：**

```bash
# 小图片直接内联（< 4KB）
wpsnote-cli insert-image \
  --note_id "$NOTE_ID" \
  --anchor_id "$ANCHOR_ID" \
  --position after \
  --src "data:image/png;base64,iVBORw0KGgo..."

# 大图片：先写到文件，再用 --src_file 传入
echo "data:image/png;base64,$(base64 -i image.png)" > /tmp/img_b64.txt
wpsnote-cli insert-image \
  --note_id "$NOTE_ID" \
  --anchor_id "$ANCHOR_ID" \
  --position after \
  --src_file /tmp/img_b64.txt
```

> `--src_file` 是 wpsnote-cli 的特有功能，专为大图片设计，避免命令行参数长度限制。
> `import_to_wps.py` 内部已自动处理：图片数据超过 4KB 时自动切换为临时文件方式。

---

### 第六步：进度报告

导入过程中**实时报告进度**：

```
正在导入 (3/42)：工作/API设计文档.pdf...
  ✓ 提取文本：8页，1.2K字
  ✓ 提取图片：5张
  ✓ 创建笔记：《API设计文档》
  ✓ 插入图片：5/5
  ✓ 完成

进度：████████░░░░░░░░  19% (8/42)
预计剩余时间：约3分钟
```

**导入完成后输出汇总：**

```
导入完成！汇总：
✓ 成功导入：38 篇笔记
⏭ 跳过（冲突）：3 篇
✗ 失败：1 篇（files/corrupted.pdf - 文件损坏）

可在 WPS 笔记中搜索标签 #导入/2025-03-14 查看所有导入的笔记。
```

---

## 各来源特殊处理

### Obsidian Vault

1. **Wiki 链接**：`[[文件名]]` 转为普通文本 `文件名`，`[[文件名|显示名]]` 转为 `显示名`
2. **标签**：`#标签名` 保留，写入 WPS 笔记时转为 `<tag>#标签名</tag>`
3. **Frontmatter**：YAML 头部（`---`之间）提取为 meta 信息的一部分，追加在 blockquote 末尾
4. **图片路径**：Obsidian 图片通常在 `attachments/` 或 Vault 根目录，需要相对于 Vault 根目录解析
5. **Callouts**：`> [!NOTE]` 等 Obsidian Callout 转为 WPS `<highlightBlock>` 格式

**Obsidian 图片路径解析规则：**
```python
# Obsidian 图片嵌入语法：![[image.png]] 或 ![alt](./attachments/image.png)
# 搜索顺序：同目录 → attachments/ → Vault根目录/attachments/
```

### 思源笔记（SiYuan）

思源笔记数据保存在工作空间 `data/` 文件夹下：

- `assets/`：所有插入的资源文件（图片等）
- `<笔记本名>/`：笔记本文件夹，下面有 `.sy` 文件（JSON 格式）
- `.sy` 文件结构是思源的 Block Tree，根节点为 `NodeDocument`

**SiYuan .sy 文件解析：**

```python
# .sy 文件是 JSON，根结构：
{
  "ID": "20250310143052-abc123",
  "Type": "NodeDocument",
  "Children": [
    { "Type": "NodeHeading", "Data": "标题文本", "HeadingLevel": 1 },
    { "Type": "NodeParagraph", "Children": [
      { "Type": "NodeText", "Data": "段落文本" }
    ]},
    { "Type": "NodeBlockquote", ... },
    { "Type": "NodeCodeBlock", "Data": "代码内容", "CodeBlockInfo": "python" },
    { "Type": "NodeImage", "Data": "assets/image-xxx.png" }
  ]
}
```

**思源节点类型映射：**

| 思源 NodeType | WPS XML 标签 |
|--------------|-------------|
| `NodeHeading` | `<h1>`-`<h6>`（根据 HeadingLevel） |
| `NodeParagraph` | `<p>` |
| `NodeBlockquote` | `<blockquote>` |
| `NodeCodeBlock` | `<codeblock lang="...">` |
| `NodeList` | `<p listType="bullet">` 或 `<p listType="ordered">` |
| `NodeListItem` | `<p listType="bullet" listLevel="N">` |
| `NodeTable` | `<table>` |
| `NodeImage` | 提取后用 `insert_image` 插入 |
| `NodeThematicBreak` | `<hr/>` |
| `NodeStrong` | `<strong>` |
| `NodeEmphasis` | `<em>` |
| `NodeCodeSpan` | `<code>`（注：WPS 无 inline code，用等宽字体 span 代替） |

**思源图片路径**：`.sy` 中图片路径格式为 `assets/xxx.png`，实际文件在 `<工作空间>/data/assets/xxx.png`。

---

## 故障排查

### pandoc 未安装
```bash
brew install pandoc  # macOS
sudo apt-get install pandoc  # Ubuntu/Debian
```

### pdfplumber 未安装
```bash
pip3 install pdfplumber
```

### markitdown 未安装
```bash
pip3 install "markitdown[pptx]"
```

### DOCX 图片提取失败
DOCX 解包需要 `defusedxml`：
```bash
pip3 install defusedxml
```

### insert_image 报 IMAGE_FETCH_FAILED
- base64 data URI 格式不正确，确保格式为 `data:image/png;base64,<数据>`
- 图片文件损坏，跳过该图片继续导入

### PDF 扫描版无文字
扫描版 PDF 需要 OCR：
```bash
pip3 install pytesseract pdf2image
brew install tesseract  # macOS
```
导入时会自动检测并提示用户是否启用 OCR（较慢）。

---

## 依赖项清单

| 工具 | 用途 | 安装 |
|------|------|------|
| `wpsnote-cli` | CLI 一键导入（首选方式） | `npm install -g @wpsnote/cli`，然后运行 `wpsnote-cli setup` |
| `pandoc` | DOCX → Markdown | `brew install pandoc` |
| `pdfplumber` | PDF 文本/表格提取 | `pip3 install pdfplumber` |
| `pypdf` | PDF 基本操作 | `pip3 install pypdf` |
| `markitdown` | PPTX → Markdown | `pip3 install "markitdown[pptx]"` |
| `pandas` | XLSX 读取 | `pip3 install pandas openpyxl` |
| `defusedxml` | 安全 XML 解析（DOCX 解包备选） | `pip3 install defusedxml` |
| `pillow` | 图片处理/base64转换 | `pip3 install pillow` |
| `python-frontmatter` | YAML Frontmatter 解析 | `pip3 install python-frontmatter` |
| `jq` | CLI 脚本 JSON 解析（可选）| `brew install jq` |

详细转换逻辑见 `references/conversion-guide.md`。
