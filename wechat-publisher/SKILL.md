---
name: wechat-publisher
description: |
  【公众号发布助手】将 WPS 笔记排版并导出为微信公众号 HTML。
  当用户说"发公众号""排版公众号""导出到公众号""我要发布了""文章排版""发一下""排版这篇文章"时使用。
  这是创作流程的最后一步：内容已完成，需要排版发布到公众号。
  核心能力：1)自动套用排版模板 2)占位符标签转样式 3)生成可直接粘贴的 HTML。
  输入：WPS 笔记 ID（内容已完成的笔记）。输出：带内联样式的 HTML 文件。
  不要用于创作内容，只用于已完成的排版发布。
metadata:
  version: "1.0.0"
  category: publishing
  tags: [wechat, publishing, html-export, content-formatting]
  dependencies: [wps-note]
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

### MCP 工具方式

通过 `wps-note` SKILL 的 MCP 工具读取笔记内容，再转换为 HTML：

```
# 1. 搜索并获取笔记
search_notes({ keyword: "文章标题" }) → note_id

# 2. 读取笔记内容
read_note({ note_id }) → xml_content

# 3. 转换为 HTML（本地脚本处理）
python scripts/export-to-html.py --xml-input content.xml --template blue-theme
```

### 完整 MCP 工作流示例

```
# 步骤 1：获取当前笔记（或搜索）
get_current_note()
→ { note_id: "abc123", title: "AI 工具介绍", word_count: 3500 }

# 步骤 2：读取笔记内容（根据大小选择方式）
get_note_outline({ note_id: "abc123" })
→ blocks: [...]

read_note({ note_id: "abc123" })
→ xml_content: "<h1>AI 工具介绍</h1><p>...</p>"

# 步骤 3：导出为 HTML（本地脚本转换）
python scripts/export-to-html.py --note-id "abc123" --template blue-theme
→ 生成 "AI 工具介绍_formatted.html"
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

## 常用编排模式

### 模式 1：直接导出当前笔记

用户已有内容，直接排版导出：

```
get_current_note() → note_id
export-to-html.py --note-id <id> --template blue-theme
```

### 模式 2：搜索后导出

用户不记得笔记 ID，先搜索再导出：

```
search_notes({ keyword: "文章标题" }) → note_id
export-to-html.py --note-id <id>
```

---

## Troubleshooting

### 笔记读取失败 (NOTE_NOT_FOUND)

**现象**：`search_notes` 或 `get_current_note` 返回笔记不存在
**原因**：笔记 ID 错误、笔记被删除、编辑器未就绪
**解决**：
1. 重新搜索确认正确的 `note_id`
2. 检查 WPS 笔记应用是否正常打开
3. 如使用 `get_current_note`，确保笔记窗口是激活状态

### 内容为空或格式错乱

**现象**：导出的 HTML 内容为空或格式异常
**原因**：笔记 XML 解析失败、包含不支持的 block 类型
**解决**：
1. 检查笔记是否确实包含内容（不是空笔记）
2. 查看笔记是否包含 embed、note_audio_card 等只读内容
3. 手动检查 XML 结构是否有异常标签

### 图片无法显示

**现象**：公众号后台图片显示为空白或红叉
**原因**：图片 URL 失效、本地图片未正确转 base64、图片格式不支持
**解决**：
1. 网络图片：检查 URL 是否直接指向图片资源（不是 HTML 页面）
2. 本地图片：确认已转为 base64 data URI
3. 图片格式：优先使用 PNG、JPG，避免 WebP

### 占位符标签不生效

**现象**：`<b/>`、`<h2/>` 等标签在 HTML 中显示为纯文本
**原因**：标签格式错误、嵌套不当
**解决**：
1. 确保标签正确闭合：`<b/>文字</b>` ✓ `<b/>文字` ✗
2. 检查标签是否嵌套在其他标签内导致解析失败
3. 参考占位符标签章节的正确用法

### 模板加载失败

**现象**：指定模板后样式未生效，使用默认样式
**原因**：模板名称拼写错误、模板文件缺失、YAML 解析错误
**解决**：
1. 检查模板名称拼写（`blue-theme`、`default`、`minimal`、`elegant`）
2. 确认 `templates/` 目录存在对应 `.yaml` 文件
3. 检查模板 YAML 格式是否正确

### HTML 粘贴到公众号后样式丢失

**现象**：本地预览正常，但粘贴到公众号后台样式错乱
**原因**：公众号编辑器过滤部分 CSS、微信内置浏览器兼容性问题
**解决**：
1. 使用内联样式（`style="..."`），避免 class 选择器
2. 避免使用复杂 CSS 特性（grid、flex 谨慎使用）
3. 在公众号后台预览后，用手机扫码查看实际效果

### MCP 工具调用失败

**现象**：`mcp__wpsnote__read_note` 等工具报错
**原因**：EDITOR_NOT_READY、BLOCK_NOT_FOUND、网络问题
**解决**：
1. 检查 WPS 笔记应用是否正常运行
2. 重新获取 `note_id` 或 `block_id`
3. 参考 `wps-note` SKILL 的 Troubleshooting

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
