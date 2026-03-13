---
name: wechat-publisher
description: |
  【公众号发布助手】将 WPS 笔记排版并导出为微信公众号 HTML。
  当用户说"发公众号""排版公众号""导出到公众号""我要发布了""文章排版""发一下""排版这篇文章"时使用。
  这是创作流程的最后一步：内容已完成，需要排版发布到公众号。
  核心能力：1)自动套用排版模板 2)占位符标签转样式 3)生成可直接粘贴的 HTML。
  输入：WPS 笔记 ID（内容已完成的笔记）。输出：带内联样式的 HTML 文件。
  不要用于创作内容，只用于已完成的排版发布。
---

# WeChat Publisher - 公众号发布助手

将已完成的 WPS 笔记内容，一键排版并导出为微信公众号 HTML 格式。这是创作流程的最后一步：内容已完成，只需排版发布。

## 使用场景

**典型工作流**：
1. 用 `content-creator` 创作文章内容
2. 保存到 WPS 笔记
3. **用本 skill 导出排版好的 HTML** ← 你在这里
4. 粘贴到公众号后台直接发布

---

## Contract（契约）

### Input Contract

**触发条件**：
- "发公众号"
- "排版公众号"
- "导出到公众号"
- "我要发布了"
- "文章排版"
- "生成公众号 HTML"
- "这篇可以发了"
- "帮我排版一下"

**输入类型**：
1. **WPS 笔记 ID**（必填）：内容已完成的笔记
2. **模板名称**（可选）：`default`/`minimal`/`elegant`，默认 `default`
3. **输出路径**（可选）：默认生成 `{标题}_formatted.html`

**前置条件**：
- 笔记内容已完成（不是空笔记）
- 笔记已保存并同步到云端
- 内容建议 < 20000 字符

### Output Contract

| 文件 | 说明 |
|------|------|
| `{标题}_formatted.html` | 带内联样式的公众号排版文件，可直接粘贴到公众号编辑器 |

**排版特性**：
- 自动套用公众号友好字体、间距
- 代码块语法高亮
- 图片自适应处理
- 移动端阅读优化

### Error Contract

| 错误场景 | 错误码 | 处理方式 |
|---------|--------|----------|
| 笔记不存在 | `NOTE_NOT_FOUND` | 检查 note_id 是否正确 |
| 笔记为空 | `EMPTY_CONTENT` | 提示先完成内容创作 |
| 内容过长 | `CONTENT_TOO_LONG` | 建议拆分为多篇发布 |
| 图片处理失败 | `IMAGE_ERROR` | 检查图片链接有效性 |

---

## 快速开始

### 基础用法

```bash
# 基本导出
python scripts/export-to-html.py --note-id "abc123"

# 指定模板风格
python scripts/export-to-html.py --note-id "abc123" --template "elegant"

# 搜索笔记并导出
python scripts/export-to-html.py --search "文章标题"
```

### Python API

```python
from scripts.export_to_html import WPSNoteExporter

exporter = WPSNoteExporter()
exporter.export(
    note_id="abc123",
    template_name="default",
    output_path="./article.html"
)
```

---

## 占位符标签（快速排版）

在 WPS 笔记中使用这些标签，导出时自动转换为对应样式：

| 标签 | 用法 | 效果 |
|------|------|------|
| `<b/>` | `<b/>文字</b>` | 橙色加粗（整段或行内） |
| `<h2/>` | `<h2/>大标题</h2>` | 蓝色大标题（一级章节） |
| `<h3/>` | `<h3/>小标题</h3>` | 蓝色小标题（二级分节） |
| `<bq/>` | `<bq/>引用文字</bq>` | 灰底蓝边引用块 |
| `<note/>` | `<note/>注释文字</note>` | 灰色小字注释 |

**使用示例**：

```
<h2/>01｜核心观点

<b/>整段橙色加粗，适合核心金句。</b>

<b/>行内加粗</b> 用于强调重点词汇。

<h3/>深入分析

正文段落正常书写...

<bq/>引用块适合摘录观点或补充说明。</bq>

<note/>注：本文仅代表个人观点。</note>
```

---

## 模板风格

| 模板 | 特点 | 适用场景 |
|------|------|----------|
| `blue-theme` ⭐默认 | 蓝色强调色，现代简洁 | 科技、企业、正式文档 |
| `default` | 橙色风格风格，专业美观 | 通用场景 |
| `minimal` | 极简风格，干净利落 | 技术文档、教程 |
| `elegant` | 优雅精致，细节丰富 | 深度长文、品牌内容 |

### blue-theme 蓝色主题

基于样本 HTML 的蓝色主题，特点：
- **主色**: `rgb(36, 91, 219)` 深蓝色
- **正文字号**: 15px（比默认更小更紧凑）
- **行距**: 2.0（更舒适的可读性）
- **引用块**: 左边框 3px + 浅灰背景
- **分栏**: Flex 布局，居中对齐

使用方法：
```bash
python scripts/export-to-html.py --note-id "abc123" --template blue-theme
```

---

## 与 content-creator 的组合

```
创作流程：

┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  content-       │     │   WPS 笔记      │     │  wechat-        │
│  creator        │ --> │   （内容完成）   │ --> │  publisher      │
│  （创作内容）    │     │                 │     │  （排版发布）    │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                              你在这里 ↑
```

**完整示例**：

```bash
# 1. 创作内容
python scripts/create-content.py --topic "AI 工具介绍"

# 2. 写入 WPS
python scripts/wps-write.py --input draft.md --title "AI 工具介绍"

# 3. 排版发布（本 skill）
python scripts/export-to-html.py --search "AI 工具介绍"
```

---

## 文件结构

```
wechat-publisher/
├── SKILL.md               # 本文件
├── scripts/
│   └── export-to-html.py  # 核心导出脚本
├── templates/
│   ├── default.yaml       # 默认模板（橙色风格橙色风格）
│   ├── blue-theme.yaml    # 蓝色主题模板
│   ├── minimal.yaml       # 极简模板
│   └── elegant.yaml       # 优雅模板
└── references/
    └── format-guide.md    # 格式规范
```

---

## 注意事项

1. **这是最后一步**：只用于内容已完成的笔记，不要在这里创作
2. **行内代码**：WPS XML 不支持行内代码，会被转为纯文本
3. **内容长度**：超过 20000 字符建议拆分多篇
4. **图片处理**：本地图片自动转 base64，网络图片直接引用

---

## Resources

- 格式规范：`references/format-guide.md`
- 模板配置：`templates/`
- 核心脚本：`scripts/export-to-html.py`
