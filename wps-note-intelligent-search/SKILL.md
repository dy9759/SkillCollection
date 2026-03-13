---
name: wps-deep-search
description: |
  【深度搜索】深挖笔记关联，构建知识图谱的 WPS 笔记查询助手。
  当用户说"深度搜索""帮我深挖""关联查询""全面梳理"时使用。
  支持跨笔记关联挖掘、语义发散扩展、知识沉淀，不同于简单关键词匹配。
  不要用于单关键词查询（那用 search_notes MCP 工具）。
---

## Contract（契约）

### Input Contract
- **类型**: 自然语言查询或结构化搜索请求
- **必填字段**:
  - `query`: 用户搜索意图描述（自然语言或关键词）
- **可选字段**:
  - `context`: 当前对话上下文，用于消歧
  - `filters`: 过滤条件对象（时间范围、标签、笔记类型等）
  - `max_results`: 最大返回结果数，默认 10
  - `search_depth`: 搜索深度（quick/standard/deep），默认 standard
- **验证规则**:
  - query 长度 >= 2 个字符
  - max_results 范围 1-100

### Output Contract
- **类型**: 结构化搜索结果
- **保证字段**:
  - `results`: 笔记列表（含相关性分数）
  - `search_dimensions`: 实际使用的搜索维度
  - `reasoning`: 搜索策略说明
- **约束**:
  - 结果按相关性降序排列
  - 每个结果包含笔记 ID、标题、摘要、匹配原因

### Error Handling
- **无效查询** → 返回 400，提示优化建议
- **无匹配结果** → 返回空列表 + 扩展搜索建议
- **MCP 调用失败** → 返回 503，启用本地降级策略

## Tools（工具列表）

本 Skill 使用以下 WPS MCP 工具执行搜索：

| 工具名 | 用途 | 调用方式 |
|--------|------|----------|
| `search_notes` | 笔记全文搜索（关键词、标签、时间范围） | `mcp__wpsnote__search_notes` |
| `search_note_content` | 单笔记内容精确搜索 | `mcp__wpsnote__search_note_content` |
| `get_note_outline` | 获取笔记结构大纲 | `mcp__wpsnote__get_note_outline` |
| `get_note_info` | 批量获取笔记元数据 | `mcp__wpsnote__get_note_info` |
| `find_tags` | 标签查找 | `mcp__wpsnote__find_tags` |

## Workflow（工作流程）

### 步骤 1：意图解析
分析用户深度查询意图，提取挖掘维度：

**时间维度识别：**
- "今天" → since=today, before=today
- "昨天/昨日" → since=yesterday, before=yesterday
- "本周" → since=this_week_start, before=now
- "上周" → since=last_week_start, before=last_week_end
- "本月" → since=this_month_start, before=now
- "最近/近期" → since=7_days_ago, before=now

**标签维度识别：**
- 提取以 # 开头的标签，如 #项目 #会议

**关键词提取：**
- 去除时间词、停用词（的、笔记、关于、查找等）
- 保留核心搜索词

### 步骤 2：策略规划
根据意图选择搜索策略：

| 意图类型 | 策略 | 搜索维度 |
|----------|------|----------|
| 查找特定笔记 | 精确匹配 | 标题 + 关键词 |
| 时间范围查询 | 时间过滤 | 时间范围 + 关键词 |
| 主题探索 | 发散搜索 | 关键词 + 标签 + 相关概念 |
| 任务聚合 | 多关键词 | 同义词并行搜索 |

### 步骤 3：执行深度挖掘
1. 调用 `search_notes` 执行多维度深度查询
2. 如有需要，调用 `find_tags` 获取相关标签
3. 对高相关性笔记，调用 `get_note_outline` 获取结构信息
4. 聚合、去重、排序结果

### 步骤 4：结果呈现
1. 生成结果摘要，说明使用的挖掘维度
2. 为每个结果提供匹配原因
3. 提供关联建议（相关标签、相关笔记）

> **关键验证点**: 每次深度查询必须说明使用了哪些维度，便于用户理解结果来源

## Scripts（外部脚本）

scripts/ 目录包含轻量级 CLI 工具，通过 subprocess 调用，不进入 Context Window：

### 意图解析脚本
```bash
python scripts/__init__.py parse --query "上周的会议纪要"
```

输出：
```json
{
  "query": "上周的会议纪要",
  "keywords": "会议纪要",
  "time_range": {
    "since": "last_week_start",
    "before": "last_week_end"
  },
  "tags": null,
  "max_results": 10
}
```

### 资产管理脚本
```bash
# 读取资产
python scripts/asset_manager.py read search_patterns.json

# 写入资产
python scripts/asset_manager.py write search_patterns.json --data '{"patterns":[]}'

# 列出资产
python scripts/asset_manager.py list
```

资产存储位置：`~/.claude/wps-search-assets/`

## Examples（使用示例）

### 示例 1：模糊查询
**输入**: "深度搜索：上周关于项目规划的内容"

**执行过程**:
1. 解析意图：时间维度（上周）+ 主题维度（项目规划）
2. 调用 `search_notes`：
   - 关键词："项目规划"
   - 时间范围：上周（自动计算日期范围）
3. 调用 `find_tags`：查找与"项目"、"规划"相关的标签
4. 聚合结果，按时间+相关性排序

**输出**:
```
找到 5 条相关笔记：
1. [项目规划-2024Q1] - 匹配：时间(上周) + 主题(项目规划)
2. [产品路线图讨论] - 匹配：主题相关(规划)
3. ...
挖掘维度：关键词 + 时间范围 + 标签关联
```

### 示例 2：关联挖掘（展示跨笔记关联）
**输入**: "深度搜索：和前端架构相关的所有内容"

**执行过程**:
1. 解析意图：主题维度（前端架构）
2. 发散扩展：
   - 核心词："前端"、"架构"
   - 扩展词："React"、"Vue"、"组件"、"工程化"、"性能优化"
3. 并行调用 `search_notes`：
   - 查询 1：关键词 "前端" + "架构"
   - 查询 2：关键词 "组件" + "设计"
   - 查询 3：关键词 "工程化"
4. 调用 `find_tags`：查找技术相关标签
5. 聚合去重，计算综合相关性

**输出**:
```
找到 8 条跨笔记相关内容：
1. [前端技术选型] - 直接匹配：前端架构
2. [组件库设计规范] - 扩展匹配：组件设计
3. [前端性能优化方案] - 扩展匹配：工程化
4. [React 最佳实践] - 标签关联：前端技术
...
挖掘维度：关键词(3组) + 标签关联 + 语义扩展
关联挖掘说明：除直接匹配外，还扩展了组件、工程化、性能等相关内容
```

### 示例 3：任务型深度查询
**输入**: "深度搜索：整理我所有的待办事项"

**执行过程**:
1. 解析意图：任务类型（待办事项）
2. 多关键词并行搜索：
   - "待办"、"待办事项"、"TODO"、"任务清单"
3. 对找到的笔记，调用 `search_note_content` 定位具体待办段落
4. 聚合展示

**输出**:
```
在 3 条笔记中找到待办事项：
1. [每日工作计划] - 包含 5 项待办
2. [项目跟进清单] - 包含 3 项待办
3. [会议待办] - 包含 2 项待办
挖掘维度：多关键词任务类型深度匹配
```

## Resources（资源引用）

- 架构设计: [references/architecture.md](references/architecture.md)
- 契约详情: [references/contract.md](references/contract.md)
- 外部脚本: [scripts/](scripts/)
