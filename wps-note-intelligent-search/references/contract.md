# WPS Note 智能搜索 - 契约速查表

> 快速参考：输入什么、输出什么、有哪些选项

---

## 输入

### 自然语言查询（主要方式）

```json
{
  "query": "找一下上周关于项目规划的笔记",
  "context": {
    "current_note_id": "可选-当前笔记ID"
  },
  "options": {
    "max_results": 10,
    "search_depth": "standard",
    "include_archived": false
  }
}
```

### 字段说明

| 字段 | 必填 | 默认值 | 说明 |
|------|------|--------|------|
| `query` | 是 | - | 自然语言描述搜索需求 |
| `context.current_note_id` | 否 | null | 当前笔记ID，用于关联搜索 |
| `options.max_results` | 否 | 10 | 最大返回结果数 (1-100) |
| `options.search_depth` | 否 | "standard" | 深度: quick/standard/deep |
| `options.include_archived` | 否 | false | 是否包含归档笔记 |

### 搜索深度

| 深度 | 场景 | 特点 |
|------|------|------|
| `quick` | 实时建议 | 仅标题+标签，最快 |
| `standard` | 常规搜索 | 标题+标签+内容，平衡 |
| `deep` | 全面检索 | 全维度+关联推荐，最全面 |

---

## 输出

### 成功响应

```json
{
  "success": true,
  "data": {
    "results": [
      {
        "note_id": "note-uuid",
        "title": "笔记标题",
        "snippet": "匹配内容摘要...",
        "matched_dimensions": ["content", "time"],
        "metadata": {
          "created_at": "2024-03-05T10:30:00Z",
          "tags": ["会议", "项目"]
        }
      }
    ],
    "search_info": {
      "total_found": 15,
      "returned_count": 10,
      "search_dimensions": ["time", "content"]
    },
    "reasoning": {
      "intent_type": "FIND_SPECIFIC",
      "explanation": "识别到时间维度（上周）和主题维度（项目规划）"
    }
  }
}
```

### 字段说明

| 字段 | 说明 |
|------|------|
| `results` | 结果列表，按相关性排序 |
| `results[].note_id` | 笔记唯一标识 |
| `results[].title` | 笔记标题 |
| `results[].snippet` | 匹配内容摘要 |
| `results[].matched_dimensions` | 匹配上的维度 |
| `search_info.total_found` | 总匹配数 |
| `search_info.search_dimensions` | 实际使用的搜索维度 |
| `reasoning.intent_type` | 识别的意图类型 |
| `reasoning.explanation` | 搜索策略说明 |

### 意图类型

| 类型 | 说明 | 示例查询 |
|------|------|---------|
| `FIND_SPECIFIC` | 精确查找 | "找上周的会议纪要" |
| `EXPLORE` | 探索浏览 | "看看我最近关于AI的笔记" |
| `RELATE` | 关联搜索 | "和这个项目相关的笔记" |
| `AGGREGATE` | 聚合整理 | "整理所有待办事项" |

---

## 错误处理

### 错误响应

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "用户友好的错误描述",
    "suggestion": "如何解决"
  }
}
```

### 错误码

| 错误码 | 说明 | 建议处理 |
|--------|------|---------|
| `INVALID_QUERY` | 查询无效 | 提供更具体的搜索描述 |
| `NO_RESULTS` | 无匹配结果 | 扩大关键词范围或放宽时间限制 |
| `MCP_UNAVAILABLE` | MCP服务不可用 | 稍后重试 |
| `SEARCH_TIMEOUT` | 搜索超时 | 减少搜索深度或缩小范围 |

---

## 快速示例

### 示例1：精确查找
```json
// 输入
{"query": "找一下上周的会议纪要"}

// 输出
{
  "success": true,
  "data": {
    "results": [...],
    "reasoning": {
      "intent_type": "FIND_SPECIFIC",
      "explanation": "识别到时间维度（上周）和主题维度（会议纪要）"
    }
  }
}
```

### 示例2：关联搜索
```json
// 输入
{
  "query": "和当前笔记相关的内容",
  "context": {"current_note_id": "note-abc-123"}
}
```

### 示例3：深度搜索
```json
// 输入
{
  "query": "整理所有关于架构设计的笔记",
  "options": {"search_depth": "deep", "max_results": 50}
}
```
