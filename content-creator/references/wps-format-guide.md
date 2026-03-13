# WPS 笔记丰富格式指南

> 基于 WPS Note MCP 能力，提供丰富的文档格式编排指导

---

## MCP 工具约束（重要）

使用 WPS MCP 工具写入内容时，需遵守以下约束：

### 内容长度限制

| 操作 | 最大长度 | 建议策略 |
|------|----------|----------|
| `edit_block` (replace) | ~2000 字符 | 单次替换不要超过此长度 |
| `edit_block` (insert) | ~3000 字符 | 分批插入，使用 `last_block_id` 作为锚点 |
| `batch_edit` | ~5000 字符 | 复杂操作拆分为多个 batch |

### 不支持的内联元素

**❌ 以下元素在 MCP XML 中不支持，会被移除或报错：**

1. **行内代码** `<code>` - 会被自动剥离
   ```xml
   <!-- ❌ 错误 -->
   <p>使用 <code>search_notes</code> 工具</p>

   <!-- ✅ 正确 -->
   <p>使用 search_notes 工具</p>
   <codeblock lang="python">search_notes()</codeblock>
   ```

2. **Blockquote 内嵌段落** - 会导致错误
   ```xml
   <!-- ❌ 错误 -->
   <blockquote><p>引用内容</p></blockquote>

   <!-- ✅ 替代方案 -->
   <highlightBlock emoji="💡" highlightBlockBackgroundColor="#FAF1E6" highlightBlockBorderColor="#FEC794">
     <p>提示内容</p>
   </highlightBlock>
   ```

### Block ID 管理

- **编辑后 block_id 会变化**，必须重新获取
- **连续插入**时使用返回的 `last_block_id` 作为锚点
- **容器内部**的 block_id（表格、高亮块内的段落）不能用于写入

### 常见错误代码

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `Position X out of range` | 内容过长 | 拆分内容，每批 < 2000 字符 |
| `<code> is not supported` | 使用了行内代码 | 移除 `<code>` 标签 |
| `Invalid content for <blockquote>` | blockquote 格式错误 | 使用高亮块替代 |
| `Block not found` | block_id 过期 | 重新调用 `get_note_outline` |

---

## 一、块级元素最佳实践

### 1.1 高亮提示块（HighlightBlock）

用于突出重要信息、提示、警告等场景。

**推荐使用场景**：
- 💡 提示（Tips）：补充说明、小技巧
- ⚠️ 警告（Warning）：注意事项、风险提示
- 📝 笔记（Note）：重要观点记录
- 💻 代码（Code）：技术相关说明
- 📊 数据（Data）：统计、图表相关
- 📌 重点（Key）：核心要点强调

**颜色搭配建议**（WPS 预设）：

| 类型 | 背景色 | 边框色 | 图标 |
|------|--------|--------|------|
| 提示 | #FAF1E6 | #FEC794 | 💡 |
| 警告 | #FAE6E6 | #F2A7A7 | ⚠️ |
| 成功 | #E6FAEB | #AFE3BB | ✅ |
| 信息 | #E6EEFA | #98C1FF | ℹ️ |
| 创意 | #F5EBFA | #E5B5FD | 💡 |

**Markdown 转 WPS XML 示例**：

```markdown
💡 **提示**
这是一个重要的提示信息。
```

转换为 WPS XML：
```xml
<highlightBlock emoji="💡" highlightBlockBackgroundColor="#FAF1E6" highlightBlockBorderColor="#FEC794">
  <p><strong>提示</strong></p>
  <p>这是一个重要的提示信息。</p>
</highlightBlock>
```

---

### 1.2 分栏布局（Columns）

用于内容对比、并列展示。

**推荐使用场景**：
- 产品对比（Before/After）
- 优缺点列表
- 双栏图文混排
- 步骤分解（左图右文）

**颜色搭配建议**：

```xml
<columns>
  <column columnBackgroundColor="#EBF2FF">
    <p><strong>方案 A</strong></p>
    <p>优点：...</p>
  </column>
  <column columnBackgroundColor="#E8FCEF">
    <p><strong>方案 B</strong></p>
    <p>优点：...</p>
  </column>
</columns>
```

---

### 1.3 表格（Table）

用于数据展示、对比列表。

**推荐使用场景**：
- 功能对比表
- 参数列表
- 时间线/日程表
- 评分/评价表

**表格样式建议**：

```xml
<table>
  <tr>
    <td><p><strong>维度</strong></p></td>
    <td><p><strong>方案 A</strong></p></td>
    <td><p><strong>方案 B</strong></p></td>
  </tr>
  <tr>
    <td><p>成本</p></td>
    <td><p>低</p></td>
    <td><p>高</p></td>
  </tr>
</table>
```

**首行高亮技巧**：
使用背景色区分表头（浅灰 #F2F2F2 或浅蓝 #D9EEFB）

---

### 1.4 代码块（CodeBlock）

用于技术文档、命令展示。

**推荐语言高亮**：
- `python` - Python 代码
- `javascript` / `js` - JavaScript
- `bash` / `shell` - 命令行
- `json` - JSON 数据
- `xml` / `html` - 标记语言
- `markdown` / `md` - Markdown

**代码块最佳实践**：

```xml
<codeblock lang="python">
def extract_template(text):
    """提取写作模板"""
    return analyze_structure(text)
</codeblock>
```

---

### 1.5 引用块（Blockquote）

用于引用他人观点、金句摘录。

**样式特点**：
- 左边框（默认或自定义颜色）
- 斜体或正常字体
- 可嵌套其他格式

**引用块样式建议**：

```xml
<blockquote>
  <p><em>"设计的本质不是装饰，而是解决问题。"</em></p>
  <p>—— Dieter Rams</p>
</blockquote>
```

---

## 二、行内标记进阶用法

### 2.1 颜色系统

**文字颜色（fontColor）预设值**：

```
重点红:    #C21C13
警示橙:    #DB7800
成功绿:    #078654
链接蓝:    #0E52D4
信息青:    #0080A0
强调金:    #D1A300
```

**高亮背景（fontHighlightColor）预设值**：

```
重点标记:  #FBF5B3 (黄色)
关键信息:  #F8D7B7 (橙色)
核心概念:  #F7C7D3 (粉色)
成功提示:  #DFF0C4 (绿色)
代码标记:  #D9EEFB (蓝色)
```

**使用示例**：

```xml
<p>
  这是一个<span fontColor="#C21C13">重点警告</span>，
  需要<span fontHighlightColor="#FBF5B3">特别关注</span>。
</p>
```

---

### 2.2 标签系统（Tag）

WPS 笔记中的标签（以 # 开头）：

**格式规范**：
- 必须以 `#` 开头
- 多级用 `//` 分隔: `#工作//项目//前端`
- 每级最多 20 字，最多 10 级
- 不支持 emoji、空格、方括号

**推荐使用场景**：
- 文章分类: `#技术//AI//大模型`
- 状态标记: `#进行中` `#已完成`
- 优先级: `#P0` `#P1` `#P2`
- 人员标记: `#负责-小明`

---

### 2.3 链接（Link）

**内链**（WPS 笔记内部）：
```xml
<a href="wpsnote://note_id">相关笔记</a>
```

**外链**（外部网址）：
```xml
<a href="https://example.com">外部资源</a>
```

---

## 三、列表样式指南

### 3.1 无序列表（Bullet）

**使用场景**：并列要点、无序项

```xml
<p listType="bullet" listLevel="0">一级项目</p>
<p listType="bullet" listLevel="1">二级项目（嵌套）</p>
```

### 3.2 有序列表（Ordered）

**使用场景**：步骤说明、排名、顺序重要的事项

```xml
<p listType="ordered" listLevel="0" listId="step1">第一步</p>
<p listType="ordered" listLevel="0" listId="step1">第二步</p>
```

### 3.3 待办列表（Todo）

**使用场景**：任务清单、检查项

```xml
<p listType="todo" listLevel="0" checked="0">待完成任务</p>
<p listType="todo" listLevel="0" checked="1">已完成任务</p>
```

---

## 四、排版美学建议

### 4.1 视觉层次

**三级标题体系**：

```
📌 一级标题（H1）- 文章主标题
  📍 二级标题（H2）- 章节标题
    ▸ 三级标题（H3）- 小节标题
      ▪ 四级标题（H4）- 细分要点
```

**段落间距建议**：
- 段前距: 0-6pt
- 段后距: 6-12pt
- 行距: 1.5-1.8

### 4.2 颜色搭配原则

**单色搭配**：
- 主色 + 深浅变化
- 适用于：专业、简洁风格

**互补色搭配**：
- 蓝-橙、红-绿
- 适用于：对比、强调

**类比色搭配**：
- 蓝-青-绿、红-橙-黄
- 适用于：和谐、渐变

### 4.3 图文混排建议

**左图右文**：
```xml
<columns>
  <column>
    <img src="..." />
  </column>
  <column>
    <p>文字说明...</p>
  </column>
</columns>
```

**居中插图**：
- 图片宽度：建议 60-80% 容器宽度
- 上下留白：16-24px
- 图片说明：小字、居中、灰色

---

## 五、内容创作模板

### 5.1 技术文档模板

```xml
<h1>技术方案标题</h1>

<highlightBlock emoji="💡" ...>
  <p><strong>一句话总结</strong></p>
  <p>方案核心要点...</p>
</highlightBlock>

<h2>背景与问题</h2>
<p>...</p>

<h2>解决方案对比</h2>
<table>...</table>

<h2>实现细节</h2>
<codeblock lang="python">...</codeblock>

<highlightBlock emoji="⚠️" ...>
  <p><strong>注意事项</strong></p>
  <p>...</p>
</highlightBlock>
```

### 5.2 产品分析模板

```xml
<h1>产品名称分析</h1>

<columns>
  <column columnBackgroundColor="#E6FAEB">
    <p><strong>优点</strong></p>
    <p listType="bullet">...</p>
  </column>
  <column columnBackgroundColor="#FAE6E6">
    <p><strong>缺点</strong></p>
    <p listType="bullet">...</p>
  </column>
</columns>

<h2>核心功能</h2>
<table>...</table>

<h2>评分</h2>
<p>易用性: <span fontColor="#078654">★★★★☆</span></p>
```

### 5.3 个人随笔模板

```xml
<h1>文章标题</h1>

<p>开头引入...</p>

<blockquote>
  <p><em>"金句摘录..."</em></p>
</blockquote>

<h2>主体内容</h2>
<p>...</p>

<highlightBlock emoji="📝" ...>
  <p><strong>我的感悟</strong></p>
  <p>...</p>
</highlightBlock>
```

---

## 六、格式检查清单

发布前检查以下格式项：

### 结构层面
- [ ] 标题层级清晰（不超过 4 级）
- [ ] 段落长度适中（不超过 5 行）
- [ ] 重要内容使用高亮块突出
- [ ] 对比内容使用分栏或表格

### 视觉层面
- [ ] 颜色搭配协调（不超过 3 种主色）
- [ ] 重点内容有颜色/背景标记
- [ ] 代码块有语法高亮
- [ ] 列表使用正确的类型（有序/无序/待办）

### 内容层面
- [ ] 关键概念使用「」框住
- [ ] 引用内容使用引用块
- [ ] 标签正确使用 # 格式
- [ ] 链接可点击且有效

---

## 七、MCP 工具使用建议

### 7.1 创建丰富格式内容的步骤

1. **创建空白笔记**：`create_note(title)`
2. **批量插入内容**：`batch_edit(operations)`
3. **插入图片**：`insert_image(anchor_id, position, src)`
4. **同步云端**：`sync_note(note_id)`

### 7.2 格式转换注意事项

**Markdown → WPS XML**：
- `**粗体**` → `<strong>`
- `*斜体*` → `<em>`
- `` `代码` `` → `<code>`
- `> 引用` → `<blockquote>`
- `- 列表` → `<p listType="bullet">`
- `1. 列表` → `<p listType="ordered">`
- `- [ ] 待办` → `<p listType="todo" checked="0">`

**需要特殊处理的元素**：
- 高亮块 → `<highlightBlock>`
- 分栏 → `<columns><column>`
- 表格 → `<table><tr><td>`
- 图片 → `insert_image` 工具

### 7.3 性能优化建议

- 批量编辑使用 `batch_edit` 而非多次 `edit_block`
- 大量内容分页处理（每页 100 个 block 左右）
- 编辑后刷新 outline 获取新 block_id

---

**版本**: 1.0
**更新日期**: 2026-03-12
**适用**: WPS Note MCP + Content Creator Skill
