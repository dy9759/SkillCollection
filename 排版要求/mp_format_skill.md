---
name: mp-format
description: 微信公众号排版助手。用户需要将文章排版成公众号格式时使用。输出符合自定义 MD 扩展语法的稿件，后续由 md_to_html.py 脚本一键转为内联样式 HTML。
---

# 微信公众号排版助手

## 指令

收到文章内容后，按照本 Skill 的**自定义 MD 扩展语法**输出排版后的稿件。

**不要输出 HTML**，只输出 Markdown 文本。脚本会自动转换。

---

## 自定义 MD 扩展语法

### 块级元素

#### 普通段落
直接写正文，不加任何前缀。渲染为灰色正文（`rgb(100,106,115)`）。

```
Skill 是以文件夹形式打包的一组指令，用来教会 Claude 处理特定任务。
```

#### 章节大标题 `##`
**蓝色**加粗，用于一级章节分隔。

```markdown
## 01｜基础知识
```

#### 小节标题 `###`
**蓝色**加粗，用于章节内二级分节（比 `##` 视觉权重低一级）。

```markdown
### 核心设计原则
```

> 注意：`##` 和 `###` 都是蓝色，不是橙色。

#### 橙色加粗整段 `!!...!!`
整段橙色加粗，用于核心结论或行动号召。**必须独占一行**，首尾各两个感叹号。

```markdown
!!用 Skill 一次性教会 Claude，之后每次都能直接用。!!
```

#### 无序列表 `- `
橙色圆点列表。

```markdown
- SKILL.md（必须）：带有 YAML 前置元数据的 Markdown 格式指令
- scripts/（可选）：可执行代码
- references/（可选）：按需加载的参考文档
```

#### 有序列表 `1. `
橙色序号列表。

```markdown
1. 第一步：克隆仓库
2. 第二步：安装依赖
3. 第三步：运行脚本
```

#### 引用块 `> `
灰底蓝边引用块。**连续多行 `>` 自动合并为一个块**，内部用 `<br>` 换行也可以。

```markdown
> 译者注：Level 1 元数据大约只消耗 ~100 tokens。<br>Level 2 的 SKILL.md 正文建议控制在 5,000 tokens 以内。
```

或多行写法（自动合并）：

```markdown
> 第一行内容
> 第二行内容
> 第三行内容
```

#### 代码块（有语言标注）
浅灰底白框 + 语法高亮 + 右上角语言标签。支持：`python`、`javascript`/`js`、`typescript`/`ts`、`bash`/`sh`、`yaml`、`json`、`css`、`html`。

````markdown
```python
def hello():
    print("Hello, world!")
```
````

#### 代码块（无语言标注）
灰底框 + 普通字体，用于结构化说明文本、示例格式等非代码内容。

````markdown
```
用例：项目 Sprint 规划
触发条件：用户说「帮我规划这个 Sprint」
结果：Sprint 完整规划，任务已创建
```
````

#### 分隔线 `---`
用于章节间的视觉分隔。

```markdown
---
```

#### 注释小字 `~~...~~`（独立行）
小号灰色注释文字。**必须独占一行**，整行被 `~~` 包裹。

```markdown
~~注：本文仅代表个人观点，具体产品选择请根据自身需求判断。~~
```

---

### 行内元素

#### 黑色加粗 `**...**`（行内）
用于段落内个别重要词句，渲染为**橙色加粗**。不要整段加粗。

```markdown
这是针对自己需求定制 Claude **最直接**的方式之一。
```

#### 整行加粗 `**整行**`
整行被 `**` 包裹时，渲染为独立橙色加粗段落（同 `!!...!!` 效果）。

```markdown
**「你觉得现在用哪个模型最好？」**
```

#### 行内代码 `` `code` ``
灰底深灰字等宽字体，用于模型名、参数名、命令等。

```markdown
以 `qwen3.5-plus` 为基准，`deepseek-v3.2` 反而贵 47.7%。
```

#### MD 链接 `[文字](url)`
渲染为蓝色可点击链接。

```markdown
平台地址：[xsct.ai](https://xsct.ai)
```

#### 行内高亮 `==...==`

| 语法 | 效果 |
|---|---|
| `==关键词==` | 橙色字（默认强调） |
| `==🔴文字==` | 红色字 |
| `==🟠文字==` | 橙色字 |
| `==🟡文字==` | 黄色字 |
| `==🟢文字==` | 绿色字 |
| `==🔵文字==` | 蓝色字 |
| `==🟣文字==` | 紫色字 |
| `==⚫️文字==` | 黑色字 |
| `==⚪️文字==` | 灰色字 |
| `==🟥文字==` | 红色底 |
| `==🟧文字==` | 橙色底 |
| `==🟨文字==` | 黄色底 |
| `==🟩文字==` | 绿色底 |
| `==🟦文字==` | 蓝色底 |
| `==🟪文字==` | 紫色底 |
| `==⬛文字==` | 黑色底 |
| `==⬜文字==` | 灰色底 |
| `==🔴🟥文字==` | 红字+红底（字色+底色可任意组合） |

**使用原则：高亮是稀缺资源，一篇文章不超过 5 处，用于真正需要读者注意的关键词。**

---

### 图片

本地图片或网络图片均可，脚本自动处理：
- 本地路径 → 自动转 base64 内嵌，不依赖外部文件
- 网络 URL → 直接引用

```markdown
![图片说明](./素材/截图.jpg)
![图片说明](https://example.com/image.jpg)
```

---

## 排版风格规范

1. **标题不加句号**
2. `##` 标题建议加章节序号，如 `## 01｜基础知识`
3. 引用块用于**补充说明、译者注、重要提示**，不用于普通正文
4. `!!橙色加粗!!` 用于**全文最重要的 1-3 句话**，不要滥用
5. 列表项末尾不加句号（除非是完整句子）
6. 代码块必须标注语言（`python`、`bash`、`yaml` 等）；说明性文本用无语言代码块
7. `==高亮==` 一篇文章不超过 5 处，用于关键数字、核心词

---

## 完整示例

```markdown
## 01｜Skill 是什么？

Skill 是以文件夹形式打包的一组指令，用来教会 Claude 怎么处理特定任务或工作流。这是针对自己需求定制 Claude **最直接**的方式之一。

每次对话都要重新解释偏好和流程太低效了——用 Skill 一次性教会 Claude，之后每次都能直接用。

### Skill 的文件结构

一个 Skill 文件夹包含：

- `SKILL.md`（必须）：带有 YAML 前置元数据的指令文件
- `scripts/`（可选）：可执行代码
- `references/`（可选）：按需加载的参考文档

### 三级加载机制

> Level 1（YAML 元数据）始终加载，约消耗 ~100 tokens。<br>Level 2（SKILL.md 正文）相关时才加载，建议控制在 5,000 tokens 以内。<br>Level 3（链接文件）按需读取，不读不占 token。

!!装几十个 Skill 也不会撑爆上下文，性能损耗极低。!!

---

### 快速上手

```bash
git clone https://github.com/example/skill-creator
cd skill-creator
python3 scripts/init_skill.py my-skill
```

更多文档见 [ClawHub](https://clawhub.ai)。

~~注：skill-creator 工具本身也是一个 Skill，可以用来构建其他 Skill。~~
```

---

## 转换命令

写完稿件保存为 `.md` 文件后，运行：

```bash
python3 scripts/md_to_html.py "推文/xxx/初稿.md"
```

输出：同目录下 `初稿_formatted.html`，直接粘贴到公众号编辑器即可。

参考样张：`排版要求/demo_sample.md` → `排版要求/demo_sample_formatted.html`

---

## 转换脚本源码

`scripts/md_to_html.py`：

```python
#!/usr/bin/env python3
import re
import sys
import base64
import html as html_module
from pathlib import Path

FONT_FAMILY = "mp-quote, 'PingFang SC', -apple-system-font, BlinkMacSystemFont, 'Helvetica Neue', 'Hiragino Sans GB', 'Microsoft YaHei UI', 'Microsoft YaHei', Arial, sans-serif"
MONO_FAMILY = "'Menlo', 'Monaco', 'Courier New', monospace"

COLOR_ORANGE  = "rgb(255, 104, 39)"
COLOR_BLUE    = "rgb(0, 128, 255)"
COLOR_GRAY    = "rgb(100, 106, 115)"
COLOR_LGRAY   = "rgb(153, 153, 153)"
COLOR_BG_GRAY = "rgb(245, 245, 245)"
COLOR_BORDER  = "rgb(230, 230, 230)"

STYLES = {
    "p":            f'style="margin: 0px 0px 15px 0px; padding: 0px; outline: 0px; max-width: 100%; clear: both; min-height: 20px; word-break: break-all; color: {COLOR_GRAY}; font-size: 16px; line-height: 2;"',
    "span":         f'style="font-size: 16px; color: {COLOR_GRAY}; font-family: {FONT_FAMILY}; white-space: pre-wrap;"',
    "bold_inline":  f'style="font-size: 16px; font-weight: bold; color: {COLOR_ORANGE}; font-family: {FONT_FAMILY};"',
    "hb":           f'style="font-size: 16px; font-weight: bold; color: {COLOR_ORANGE}; font-family: {FONT_FAMILY}; white-space: pre-wrap;"',
    "h2":           f'style="margin: 30px 0px 15px 0px; padding: 0px; font-size: 18px; font-weight: bold; color: {COLOR_BLUE}; line-height: 1.6;"',
    "h3":           f'style="margin: 20px 0px 10px 0px; padding: 0px; font-size: 16px; font-weight: bold; color: {COLOR_BLUE}; line-height: 1.6;"',
    "blockquote":   f'style="margin: 20px 0px; padding: 15px 20px; background-color: {COLOR_BG_GRAY}; border-left: 4px solid {COLOR_BLUE}; font-size: 15px; color: {COLOR_GRAY}; line-height: 1.8;"',
    "blockquote_p": f'style="margin: 0px; padding: 0px; font-family: {FONT_FAMILY};"',
    "hr":           f'style="margin: 25px 0px; border: none; border-top: 1px solid {COLOR_BORDER};"',
    "note":         f'style="margin: 20px 0px 0px 0px; padding: 0px; font-size: 14px; color: {COLOR_LGRAY}; line-height: 1.8;"',
    "img":          'style="max-width: 100%; height: auto; display: block; margin: 15px 0;"',
    "section":      f'style="max-width: 677px; margin: 0 auto; background-color: #fff; padding: 20px; font-family: {FONT_FAMILY};"',
    "body":         'style="margin: 0; padding: 20px; background-color: #f5f5f5;"',
    "table":        'style="width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 15px;"',
    "th":           f'style="padding: 10px 14px; background-color: {COLOR_BLUE}; color: #fff; font-weight: bold; text-align: center; border: 1px solid rgb(0, 100, 220);"',
    "td":           f'style="padding: 10px 14px; color: {COLOR_GRAY}; border: 1px solid rgb(210, 215, 220); vertical-align: top; line-height: 1.7;"',
    "td_alt":       f'style="padding: 10px 14px; color: {COLOR_GRAY}; border: 1px solid rgb(210, 215, 220); vertical-align: top; line-height: 1.7; background-color: rgb(248, 249, 250);"',
}

FONT_COLORS = {
    "🔴": "rgb(194, 28, 19)", "🟠": "rgb(255, 104, 39)", "🟡": "rgb(209, 163, 0)",
    "🟢": "rgb(7, 134, 84)",  "🔵": "rgb(0, 128, 255)",  "🟣": "rgb(140, 60, 200)",
    "⚫": "rgb(60, 60, 60)",  "⚫️": "rgb(60, 60, 60)",
    "⚪": "rgb(153, 153, 153)", "⚪️": "rgb(153, 153, 153)",
}
BG_COLORS = {
    "🟥": "rgb(255, 200, 200)", "🟧": "rgb(255, 228, 196)", "🟨": "rgb(255, 249, 180)",
    "🟩": "rgb(200, 240, 210)", "🟦": "rgb(200, 225, 255)", "🟪": "rgb(230, 210, 255)",
    "⬛": "rgb(60, 60, 60)",    "⬜": "rgb(230, 230, 230)",
}

# 语法高亮（浅色 GitHub 风格）
CODE_COLORS = {
    "keyword":  "rgb(207, 34, 46)",   "string":   "rgb(14, 118, 50)",
    "comment":  "rgb(140, 149, 159)", "number":   "rgb(5, 80, 174)",
    "builtin":  "rgb(111, 66, 193)",  "operator": "rgb(60, 80, 100)",
    "decorator":"rgb(207, 34, 46)",   "default":  "rgb(36, 41, 47)",
}
LANG_RULES = {
    "python": [
        (r'#[^\n]*', "comment"),
        (r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'', "string"),
        (r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'', "string"),
        (r'@\w+', "decorator"),
        (r'\b(def|class|import|from|return|if|elif|else|for|while|in|not|and|or|is|None|True|False|try|except|finally|with|as|pass|break|continue|raise|lambda|yield|async|await)\b', "keyword"),
        (r'\b(print|len|range|str|int|float|list|dict|set|tuple|bool|type|open|super|self|cls)\b', "builtin"),
        (r'\b\d+\.?\d*\b', "number"),
        (r'[+\-*/=<>!&|^~%]+', "operator"),
    ],
    "javascript": [
        (r'//[^\n]*', "comment"), (r'/\*[\s\S]*?\*/', "comment"),
        (r'`(?:\\.|[^`\\])*`', "string"),
        (r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'', "string"),
        (r'\b(const|let|var|function|return|if|else|for|while|do|switch|case|break|continue|new|this|class|extends|import|export|default|from|async|await|try|catch|finally|throw|typeof|instanceof|in|of|null|undefined|true|false)\b', "keyword"),
        (r'\b(console|Math|Object|Array|String|Number|Boolean|Promise|fetch|setTimeout|setInterval|JSON|window|document)\b', "builtin"),
        (r'\b\d+\.?\d*\b', "number"), (r'[+\-*/=<>!&|^~%?:]+', "operator"),
    ],
    "typescript": [
        (r'//[^\n]*', "comment"), (r'/\*[\s\S]*?\*/', "comment"),
        (r'`(?:\\.|[^`\\])*`', "string"),
        (r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'', "string"),
        (r'\b(const|let|var|function|return|if|else|for|while|do|switch|case|break|continue|new|this|class|extends|import|export|default|from|async|await|try|catch|finally|throw|typeof|instanceof|in|of|null|undefined|true|false|type|interface|enum|namespace|declare|abstract|implements|readonly|private|public|protected|as|keyof|typeof)\b', "keyword"),
        (r'\b(string|number|boolean|any|void|never|unknown|object|Array|Promise|Record|Partial|Required|Readonly)\b', "builtin"),
        (r'\b\d+\.?\d*\b', "number"), (r'[+\-*/=<>!&|^~%?:]+', "operator"),
    ],
    "bash": [
        (r'#[^\n]*', "comment"),
        (r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'', "string"),
        (r'\b(if|then|else|elif|fi|for|while|do|done|case|esac|function|return|export|local|echo|exit|in|true|false)\b', "keyword"),
        (r'\$\{?[\w@#?*!]+\}?', "builtin"),
        (r'\b\d+\b', "number"), (r'[|&;<>]+', "operator"),
    ],
    "yaml": [
        (r'#[^\n]*', "comment"),
        (r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'', "string"),
        (r'^(\s*[\w\-]+)(?=\s*:)', "keyword"),
        (r'\b(true|false|null|yes|no)\b', "builtin"),
        (r'\b\d+\.?\d*\b', "number"), (r'[:\-\[\]{}|>]+', "operator"),
    ],
    "json": [
        (r'"(?:\\.|[^"\\])*"(?=\s*:)', "keyword"),
        (r'"(?:\\.|[^"\\])*"', "string"),
        (r'\b(true|false|null)\b', "builtin"),
        (r'\b-?\d+\.?\d*(?:[eE][+-]?\d+)?\b', "number"),
        (r'[{}\[\]:,]+', "operator"),
    ],
    "css": [
        (r'/\*[\s\S]*?\*/', "comment"),
        (r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'', "string"),
        (r'[.#]?[\w-]+(?=\s*\{)', "keyword"),
        (r'(?<=:\s)[\w-]+', "builtin"),
        (r'#[0-9a-fA-F]{3,8}\b', "string"),
        (r'\b\d+\.?\d*(?:px|em|rem|%|vh|vw|s|ms)?\b', "number"),
        (r'[:;{}()]+', "operator"),
    ],
    "html": [
        (r'<!--[\s\S]*?-->', "comment"),
        (r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'', "string"),
        (r'</?\w[\w-]*', "keyword"),
        (r'[\w-]+=', "builtin"),
        (r'[<>/=]+', "operator"),
    ],
}
LANG_RULES["sh"] = LANG_RULES["bash"]
LANG_RULES["js"] = LANG_RULES["javascript"]
LANG_RULES["ts"] = LANG_RULES["typescript"]
LANG_RULES["py"] = LANG_RULES["python"]


def highlight_code(code: str, lang: str) -> str:
    lang = lang.lower().strip()
    rules = LANG_RULES.get(lang)
    if not rules:
        return html_module.escape(code)
    length = len(code)
    colors = [None] * length
    for pattern, color_key in rules:
        for m in re.finditer(pattern, code, re.MULTILINE):
            start, end = m.start(), m.end()
            if all(colors[j] is None for j in range(start, end)):
                for j in range(start, end):
                    colors[j] = color_key
    result = []
    i = 0
    while i < length:
        color_key = colors[i]
        j = i + 1
        while j < length and colors[j] == color_key:
            j += 1
        segment = html_module.escape(code[i:j])
        color = CODE_COLORS[color_key] if color_key else CODE_COLORS["default"]
        result.append(f'<span style="color: {color};">{segment}</span>')
        i = j
    return ''.join(result)


def process_inline(text: str) -> str:
    def replace_inline_code(m):
        code = html_module.escape(m.group(1))
        style = (f'background-color: rgb(235, 236, 240); color: rgb(80, 90, 105); '
                 f'font-family: {MONO_FAMILY}; font-size: 13px; padding: 1px 5px; '
                 f'border-radius: 3px; white-space: nowrap;')
        return f'<code style="{style}">{code}</code>'

    placeholders = {}
    placeholder_idx = [0]
    def protect_inline_code(m):
        key = f'\x00CODE{placeholder_idx[0]}\x00'
        placeholder_idx[0] += 1
        placeholders[key] = replace_inline_code(m)
        return key
    text = re.sub(r'`([^`]+)`', protect_inline_code, text)

    def replace_highlight(m):
        inner = m.group(1)
        font_color = None
        bg_color = None
        i = 0
        while i < len(inner):
            matched = False
            for emoji_len in [2, 1]:
                candidate = inner[i:i+emoji_len]
                if candidate in FONT_COLORS and font_color is None:
                    font_color = FONT_COLORS[candidate]; i += emoji_len; matched = True; break
                elif candidate in BG_COLORS and bg_color is None:
                    bg_color = BG_COLORS[candidate]; i += emoji_len; matched = True; break
            if not matched:
                break
        content = inner[i:]
        style_parts = [f"color: {font_color or COLOR_ORANGE};"]
        if bg_color:
            style_parts.append(f"background-color: {bg_color}; padding: 0 2px; border-radius: 2px;")
        return f'<span style="{" ".join(style_parts)}">{content}</span>'

    text = re.sub(r'==([\s\S]+?)==', replace_highlight, text)
    text = re.sub(r'\*\*(.+?)\*\*', lambda m: f'<span {STYLES["bold_inline"]}>{m.group(1)}</span>', text)
    for key, val in placeholders.items():
        text = text.replace(key, val)
    text = re.sub(
        r'\[([^\]]+)\]\((https?://[^\)]+)\)',
        lambda m: f'<a href="{m.group(2)}" style="color: {COLOR_BLUE}; text-decoration: none;">{m.group(1)}</a>',
        text
    )
    return text


def render_p(text):
    return f'<p {STYLES["p"]}><span {STYLES["span"]}>{process_inline(text)}</span></p>'

def render_hb(text):
    return f'<p {STYLES["p"]}><span {STYLES["hb"]}>{process_inline(text)}</span></p>'

def render_bold_line(text):
    return f'<p {STYLES["p"]}><span {STYLES["bold_inline"]}>{process_inline(text)}</span></p>'

def render_h2(text):
    return f'<h2 {STYLES["h2"]}>{text}</h2>'

def render_h3(text):
    return f'<p {STYLES["p"]}><span {STYLES["h3"]}>{process_inline(text)}</span></p>'

def render_blockquote(text):
    return (f'<blockquote {STYLES["blockquote"]}>\n'
            f'    <p {STYLES["blockquote_p"]}>{process_inline(text)}</p>\n'
            f'</blockquote>')

def render_hr():
    return f'<hr {STYLES["hr"]}>'

def render_note(text):
    return f'<p {STYLES["note"]}><span style="font-family: {FONT_FAMILY};">{process_inline(text)}</span></p>'

def render_ul(items):
    return '\n'.join(
        f'<p {STYLES["p"]}><span {STYLES["span"]}>'
        f'<span style="color: {COLOR_ORANGE}; margin-right: 6px;">•</span>'
        f'{process_inline(item)}</span></p>'
        for item in items
    )

def render_ol(items):
    return '\n'.join(
        f'<p {STYLES["p"]}><span {STYLES["span"]}>'
        f'<span style="color: {COLOR_ORANGE}; font-weight: bold; margin-right: 6px;">{i}.</span>'
        f'{process_inline(item)}</span></p>'
        for i, item in enumerate(items, 1)
    )

def render_codeblock(code, lang=""):
    if not lang:
        lines = code.strip().split('\n')
        inner = '\n'.join(
            f'<p style="margin: 0 0 4px 0; padding: 0; font-size: 15px; color: {COLOR_GRAY}; '
            f'font-family: {FONT_FAMILY}; line-height: 1.8;">'
            f'{process_inline(html_module.escape(ln)) if ln.strip() else "&nbsp;"}</p>'
            for ln in lines
        )
        return (f'<section style="margin: 16px 0px; padding: 16px 20px; '
                f'background-color: rgb(248, 249, 250); border-radius: 6px; '
                f'border: 1px solid {COLOR_BORDER};">{inner}</section>')
    highlighted = highlight_code(code, lang)
    highlighted = highlighted.replace('\n', '<br>')
    highlighted = re.sub(r'  ', '&nbsp;&nbsp;', highlighted)
    lang_label = (f'<span style="position: absolute; top: 8px; right: 12px; font-size: 11px; '
                  f'color: rgb(130, 140, 150); font-family: {MONO_FAMILY}; '
                  f'text-transform: uppercase; letter-spacing: 0.5px;">{html_module.escape(lang)}</span>')
    pre_style = (f'margin: 0px; padding: 0px; font-family: {MONO_FAMILY}; font-size: 13px; '
                 f'line-height: 1.7; white-space: pre; word-break: normal; overflow-wrap: normal;')
    return (f'<section style="position: relative; margin: 16px 0px; padding: 16px 20px; '
            f'background-color: rgb(246, 248, 250); border-radius: 6px; overflow-x: auto; '
            f'border: 1px solid rgb(210, 215, 220);">'
            f'{lang_label}<p style="{pre_style}">{highlighted}</p></section>')

def render_img(src, input_dir=None):
    if not src.startswith(('http://', 'https://', 'data:')):
        img_path = Path(src) if Path(src).is_absolute() else (input_dir / src if input_dir else Path(src))
        if img_path.exists():
            mime_map = {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png',
                        '.gif': 'image/gif', '.webp': 'image/webp', '.svg': 'image/svg+xml'}
            mime = mime_map.get(img_path.suffix.lower(), 'image/png')
            with open(img_path, 'rb') as f:
                src = f'data:{mime};base64,{base64.b64encode(f.read()).decode()}'
        else:
            print(f"  ⚠️  图片不存在：{img_path}")
    return f'<img src="{src}" {STYLES["img"]}/>'

def render_table(rows):
    html = f'<table {STYLES["table"]}>\n'
    for row_idx, row in enumerate(rows):
        html += '  <tr>\n'
        for cell in row:
            cell = cell.strip()
            if row_idx == 0:
                html += f'    <th {STYLES["th"]}>{cell}</th>\n'
            else:
                style = STYLES["td_alt"] if row_idx % 2 == 0 else STYLES["td"]
                html += f'    <td {style}>{cell}</td>\n'
        html += '  </tr>\n'
    return html + '</table>'


def parse_md(md, input_dir=None):
    lines = md.split('\n')
    result = []
    i = 0
    ul_items, ol_items = [], []

    def flush_ul():
        if ul_items: result.append(render_ul(ul_items)); ul_items.clear()
    def flush_ol():
        if ol_items: result.append(render_ol(ol_items)); ol_items.clear()
    def flush_lists(): flush_ul(); flush_ol()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            flush_lists(); i += 1; continue

        if stripped.startswith('```'):
            flush_lists()
            lang = stripped[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i]); i += 1
            result.append(render_codeblock('\n'.join(code_lines), lang))
            i += 1; continue

        if stripped.startswith('# ') and not stripped.startswith('## '):
            flush_lists(); result.append(render_h2(stripped[2:].strip())); i += 1; continue
        if stripped.startswith('## '):
            flush_lists(); result.append(render_h2(stripped[3:].strip())); i += 1; continue
        if stripped.startswith('### '):
            flush_lists(); result.append(render_h3(stripped[4:].strip())); i += 1; continue
        if re.match(r'^#{4,}\s', stripped):
            flush_lists(); result.append(render_h3(re.sub(r'^#{4,}\s+', '', stripped))); i += 1; continue

        if stripped.startswith('!!') and stripped.endswith('!!') and len(stripped) > 4:
            flush_lists(); result.append(render_hb(stripped[2:-2])); i += 1; continue

        if re.match(r'^>\s*\S', stripped) or stripped == '>':
            flush_lists()
            bq_lines = []
            while i < len(lines):
                s = lines[i].strip()
                if s.startswith('> '): bq_lines.append(s[2:]); i += 1
                elif s == '>': i += 1; break
                else: break
            if bq_lines: result.append(render_blockquote('<br>'.join(bq_lines)))
            continue

        if stripped == '>': i += 1; continue

        if re.match(r'^[-*_]{3,}$', stripped):
            flush_lists(); result.append(render_hr()); i += 1; continue

        if stripped.startswith('~~') and stripped.endswith('~~') and len(stripped) > 4:
            inner = stripped[2:-2]
            if '~~' not in inner:
                flush_lists(); result.append(render_note(inner)); i += 1; continue

        ul_match = re.match(r'^[-*+]\s+(.+)$', stripped)
        if ul_match:
            flush_ol(); ul_items.append(ul_match.group(1)); i += 1; continue

        ol_match = re.match(r'^\d+\.\s+(.+)$', stripped)
        if ol_match:
            flush_ul(); ol_items.append(ol_match.group(1)); i += 1; continue

        if stripped.startswith('|'):
            flush_lists()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i].strip()); i += 1
            rows = []
            for tl in table_lines:
                cells = [c for c in tl[1:-1].split('|')]
                if not all(set(c.strip()) <= set('-: ') for c in cells):
                    rows.append(cells)
            if rows: result.append(render_table(rows))
            continue

        img_match = re.match(r'^!\[.*?\]\((.+?)\)$', stripped)
        if img_match:
            flush_lists(); result.append(render_img(img_match.group(1), input_dir)); i += 1; continue

        if stripped == '---' and i == 0:
            i += 1
            while i < len(lines) and lines[i].strip() != '---': i += 1
            i += 1; continue

        if re.match(r'^-\s+\[.+?\]\(#.+?\)$', stripped):
            i += 1; continue

        if stripped.startswith('**') and stripped.endswith('**') and len(stripped) > 4:
            inner = stripped[2:-2]
            if '**' not in inner:
                flush_lists(); result.append(render_bold_line(inner)); i += 1; continue

        flush_lists()
        if stripped.startswith(':') and not stripped.startswith('::'):
            stripped = stripped[1:].strip()
        result.append(render_p(stripped))
        i += 1

    flush_lists()
    return '\n\n'.join(result)


COPY_BUTTON_HTML = """
<div id="copy-bar" style="position: fixed; bottom: 24px; right: 24px; z-index: 9999;">
  <button id="copy-btn" onclick="copyContent()" style="
    background: rgb(0, 128, 255); color: #fff; border: none; border-radius: 8px;
    padding: 10px 20px; font-size: 14px; font-family: 'PingFang SC', sans-serif;
    cursor: pointer; box-shadow: 0 4px 12px rgba(0,128,255,0.35); transition: all 0.2s;
  ">复制内容</button>
</div>
<script>
function copyContent() {
  const section = document.getElementById('mp-section');
  const btn = document.getElementById('copy-btn');
  const range = document.createRange();
  range.selectNode(section);
  const sel = window.getSelection();
  sel.removeAllRanges();
  sel.addRange(range);
  try {
    document.execCommand('copy');
    btn.textContent = '✓ 已复制';
    btn.style.background = 'rgb(7, 134, 84)';
    setTimeout(() => { btn.textContent = '复制内容'; btn.style.background = 'rgb(0, 128, 255)'; }, 2000);
  } catch(e) {
    btn.textContent = '复制失败，请手动选择';
    btn.style.background = 'rgb(194, 28, 19)';
  }
  sel.removeAllRanges();
}
</script>
"""


def convert_md_to_html(md, title="微信公众号文章", input_dir=None):
    content = parse_md(md, input_dir)
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body {STYLES["body"]}>
<section id="mp-section" {STYLES["section"]}>
{content}
</section>
{COPY_BUTTON_HTML}
</body>
</html>'''


def main():
    if len(sys.argv) < 2:
        print("使用方法: python3 scripts/md_to_html.py <输入.md>")
        sys.exit(1)
    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"错误：文件不存在 → {input_path}"); sys.exit(1)
    with open(input_path, 'r', encoding='utf-8') as f:
        md = f.read()
    html = convert_md_to_html(md, input_path.stem, input_dir=input_path.parent)
    output_path = input_path.parent / (input_path.stem + '_formatted.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"转换完成！\n输入: {input_path}\n输出: {output_path}")


if __name__ == '__main__':
    main()
```
