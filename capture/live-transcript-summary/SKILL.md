---
name: live-transcript-summary
description: 边听边总结：实时监听当前 WPS 笔记中的音频转写，每 60 秒自动循环一次，识别场景后按对应模板整理内容，并写回笔记。当用户提到正在录音、开会、听课、听播客、做采访、开始录制，或者希望 AI 帮忙整理、总结、记录当前正在发生的内容时使用此 skill。也适用于用户说「帮我跟着听」「你帮我记」「边听边整理」「录完帮我整理」「实时帮我总结」，或在笔记中输入 *** 希望 AI 结合录音补全内容的场景。
metadata:
  author: Yicheng Xu
  version: "2.1.0"
  tags: [audio, transcript, summary, real-time, wps-note]
---

# 边听边总结 Skill

实时监听当前 WPS 笔记中的音频录音转写，每 60 秒轮询一次，**只处理新增句子（增量模式）**，根据场景自动选择模板整理内容并写回笔记。

---

## 工具优先级

**优先使用 `wpsnote-cli`（CLI），不支持时才退回 MCP 工具调用。**

| 操作 | CLI 命令 | MCP 工具 |
|------|----------|----------|
| 获取当前笔记 | `wpsnote-cli current --json` | `get_current_note()` |
| 获取大纲 | `wpsnote-cli outline --note_id ID --json` | `get_note_outline()` |
| 获取转写 | `wpsnote-cli audio --shorthand_id ID --json` | `get_audio_transcript()` |
| 搜索笔记 | `wpsnote-cli find --keyword KW --json` | `search_notes()` |
| 搜索笔记内内容 | `wpsnote-cli search --note_id ID --query Q --json` | `search_note_content()` |
| 插入内容 | `wpsnote-cli edit --json-args '...' ` | `edit_block(op="insert")` |
| 替换内容 | `wpsnote-cli edit --json-args '...'` | `edit_block(op="replace")` |
| 批量编辑 | `wpsnote-cli batch-edit --json-args '...'` | `batch_edit()` |

> CLI 中 XML 含尖括号时，**统一用 `--json-args` 传 JSON 对象**，避免 shell 转义问题。

---

## Token 节省策略（核心）

**最重要的优化：增量处理，只看新句子。**

每轮维护一个本地状态文件 `/tmp/lts_state_{note_id}.json`：

```json
{
  "note_id": "501327067631",
  "shorthand_id": "sh_abc123",
  "scene": "meeting",
  "last_end_time": 342.5,
  "summary_anchor_id": "blockId_xyz",
  "round": 3,
  "speaker_map": {"发言人 1": "张总", "发言人 2": "李工❓"},
  "person_cache": {"张总": [{"note_title": "Q4 复盘", "snippet": "张总提出..."}]}
}
```

**每轮流程**：
1. `wpsnote-cli audio --json` 拉全量转写（无法增量拉取，全量是必须的）
2. **过滤**：只保留 `start_time > last_end_time` 的句子 → **新增句子**
3. 只把新增句子喂给 AI 做摘要 → **token 消耗恒定，不随录音时长增长**
4. 更新 `last_end_time` 为本轮最后一句的 `end_time`

```python
# 每轮 token 消耗 = 新增句子量，而非全量转写
new_sentences = [s for s in all_sentences if s["start_time"] > state["last_end_time"]]
if not new_sentences:
    print("⏭  无新增内容，跳过本轮")
    # 更新 state 后 sleep 60
```

**其他节省策略**：
- 风格学习只读笔记的**前 500 字**（`wpsnote-cli read --max_length 500`），不读全文
- 大纲只用于找 AudioCard block 和定位锚点，不读正文
- `***` 补全：只读取 `***` 所在 block 的前后 3 个 block，不读全文

---

## 核心工作流

```
启动时（仅一次）:
  1. wpsnote-cli status            → 检查 CLI 是否可用
  2. wpsnote-cli current --json    → 获取 note_id
  3. 风格学习（read 前 500 字，1 篇即可）
  4. 初始化状态文件
  5. 输出启动告知

loop（每 60 秒）:
  1. wpsnote-cli outline --json          → 扫描 NoteAudioCard
  2. wpsnote-cli audio --json            → 全量拉取转写
  3. 过滤新增句子（start_time > last_end_time）
  4. 若无新增 → 检测临时区 → 更新状态 → sleep 60 → continue
  5. 场景识别（首轮）+ 发言人推断
  5.5 人名联动：提取人名 → 拆字搜索笔记库 → 注入背景上下文（缓存已搜过的人名）
  6. 只用新增句子 + 人物背景上下文生成摘要
  7. wpsnote-cli batch-edit              → 写回笔记 + 插入/更新临时区（hr + 提示块）
  6.5 检测临时区用户内容 → 合并到正文对应位置 → 清空临时区用户 block
  8. wpsnote-cli search "***"            → 检测补全请求
  9. 更新状态文件（last_end_time、round、temp_zone_anchor_id 等）
  10. sleep 60 → loop
```

---

## 启动阶段

### Step 0：检查 CLI 可用性

```bash
wpsnote-cli status
# 输出包含"连接中... 成功" → CLI 可用
# 否则 → 退回 MCP 模式
```

### Step 1：获取当前笔记

```bash
# CLI 方式（首选）
NOTE=$(wpsnote-cli current --json)
NOTE_ID=$(echo $NOTE | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['data']['note_id'])")
```

```
# MCP 备选
get_current_note() → { note_id, title }
```

若返回 `NO_ACTIVE_EDITOR_WINDOW`，提示用户打开笔记后重试。

### Step 2：风格学习（多篇会议纪要版）

读 **3-5 篇**历史会议纪要/总结笔记，每篇最多 **3000 字**，综合归纳风格：

```bash
# CLI 方式：搜索多关键词，取前 5 篇
NOTES=$(wpsnote-cli find --keyword "会议纪要 纪要 会议总结 周会 月会" --limit 5 --json)

# Python 逐篇读取（最多 3000 字/篇）
python3 - <<'EOF'
import json, subprocess, sys

notes = json.loads(subprocess.check_output(
    ["wpsnote-cli", "find", "--keyword", "会议纪要 纪要 会议总结 周会 月会", "--limit", "5", "--json"]
))["data"]["notes"]

style_samples = []
for note in notes[:5]:
    result = subprocess.check_output(
        ["wpsnote-cli", "read", "--note_id", note["note_id"], "--max_length", "3000", "--json"]
    )
    content = json.loads(result)["data"].get("content", "")
    style_samples.append({"title": note["title"], "content": content[:3000]})

print(json.dumps(style_samples, ensure_ascii=False))
EOF
```

从多篇样本**综合归纳**风格特征（投票取多数）：
- 语言风格：口语（「感觉」「其实」）vs 书面（「经讨论」「本次」）
- 结构偏好：全 bullet list vs 分章节标题
- 详略程度：每条 ≤10 字 vs 每条 ≥30 字
- 是否中英混写
- 是否常用色块/分栏排版

若搜索结果不足 3 篇，降级为 1 篇，风格学习标注「样本不足，参考有限」。

### Step 3：初始化状态文件

```python
import json, os, time

state = {
    "note_id": note_id,
    "shorthand_id": None,      # 首轮扫描到 AudioCard 后填入
    "scene": None,             # 首轮场景识别后填入
    "last_end_time": -1.0,     # -1 代表从头开始
    "summary_anchor_id": None, # 摘要区域的最后一个 block_id
    "temp_zone_anchor_id": None, # 临时区 highlightBlock 的 block_id
    "round": 0,
    "speaker_map": {},         # {"发言人 1": "真实姓名"}
    "started_at": time.time(),
}

state_path = f"/tmp/lts_state_{note_id}.json"
json.dump(state, open(state_path, "w"), ensure_ascii=False)
```

### Step 4：启动告知

```
已开始边听边总结 ✓

当前笔记：[笔记标题]
识别场景：等待录音开始后自动识别
参考风格：[找到/未找到历史总结]
轮询间隔：60 秒
模式：增量（每轮只处理新增转写内容）

---
如需 AI 援助：
  ① 补全：在笔记任意位置输入 ***，AI 结合录音自动补全
  ② 临时区：每轮摘要末尾有一个灰色提示区，把想法/补充/纠正贴到那里，AI 下轮自动合并到正文
  ③ 停止：告诉我「停止总结」即可
---
```

---

## 轮询主循环

### Step 1：扫描音频卡片

```bash
OUTLINE=$(wpsnote-cli outline --note_id "$NOTE_ID" --json)
# 从 JSON 中找 type="note_audio_card" 的 block
# 提取 attrs.shorthand_id 和 attrs.status
```

```python
import json
outline_data = json.loads(outline_output)
audio_blocks = [b for b in outline_data["data"]["blocks"] if b["type"] == "note_audio_card"]

if not audio_blocks:
    print("当前笔记未检测到录音，等待中...")
    # sleep 60, continue

# 取第一个（或 status=recording 的那个）
audio_block = audio_blocks[0]
shorthand_id = audio_block["attrs"]["shorthand_id"]
status = audio_block["attrs"].get("status", "unknown")
```

**状态判断**：
- `recording` / `paused` / `stopped`：均继续获取转写
- 无音频卡片：跳过本轮

### Step 2：增量获取转写

```bash
TRANSCRIPT=$(wpsnote-cli audio --shorthand_id "$SHORTHAND_ID" --json)
```

```python
transcript_data = json.loads(transcript_output)
all_sentences = transcript_data["data"]["sentences"]  
# 每个 sentence: { text, speaker, start_time, end_time }

# ★ 关键：只取新增句子
last_end = state["last_end_time"]  # 上轮最后处理到的时间点
new_sentences = [s for s in all_sentences if s["start_time"] > last_end]

if not new_sentences:
    print(f"⏭  第 {state['round']+1} 轮：无新增内容，跳过")
    # 更新 state round，sleep 60, continue
```

**为什么要拉全量再过滤**：`wpsnote-cli audio` 只支持全量获取，没有增量接口。但过滤在本地完成，**只把新增句子（通常几百字）发给 AI，不是全量几千字**。

### Step 3：场景识别（首轮有新内容时执行）

首轮才做场景识别，后续沿用缓存结果：

```python
if state["scene"] is None and new_sentences:
    # 取前 10 句 + 笔记标题做场景判断
    sample = " ".join(s["text"] for s in new_sentences[:10])
    # 根据关键词表识别场景（见"场景识别表"章节）
    state["scene"] = detect_scene(note_title, sample)
```

### Step 4：发言人身份推断

```python
# 检测新句子中是否有身份线索
for s in new_sentences:
    if "我是" in s["text"] or "我叫" in s["text"]:
        # 提取真实姓名，更新 speaker_map
        state["speaker_map"][s["speaker"]] = extracted_name

# 若发现纠正，用 CLI 批量替换笔记中旧名称
if name_changed:
    OLD_BLOCKS=$(wpsnote-cli search --note_id "$NOTE_ID" --query "旧名❓" --json)
    # 逐个替换
```

### Step 4.5：人名知识联动（跨笔记）

从新增句子和 speaker_map 中提取人名，搜索笔记库，将背景上下文注入本轮摘要 prompt。

**提取规则**：speaker_map 中已确认姓名 + 正则匹配「姓名+职位词」（总/经理/主任/老师等）

**搜索策略**（依次降级）：
1. 全名搜索（如「张三」）
2. 后两字搜索（三字名时，如「李建国」→「建国」）
3. 名字单字搜索（两字名时取名，噪音大，慎用）

每人最多取 2 篇笔记 × 3 段上下文，结果缓存在 `state["person_cache"]`，同一 session 不重复搜索。

**注入原则**：
- 背景信息作为 prompt 附加上下文，供 AI 丰富人物描述
- 与当前转写无关联时不引用，引用时在色块内注明「（背景来自《笔记标题》）」
- 与当前笔记相同的笔记搜索结果跳过

> 详细代码见 [person-linking.md](person-linking.md)

### Step 5：生成摘要（新增句子 + 人物背景）

**输入给 AI 的内容**：

```
[场景: {scene}] [发言人映射: {speaker_map}]

新增转写（{len(new_sentences)} 句，{duration:.0f}秒）：
{speaker}: {text}
{speaker}: {text}
...

[人物背景（来自笔记库，供参考，不强行引用）]:
- 张总（来自《Q4 复盘》）：张总提出要压缩研发周期，目标 Q1 上线...
- 李工（来自《架构评审》）：负责后端服务，主导过 3 个核心模块...

请按{模板名}模板提取要点，生成 WPS XML 格式的增量摘要。
只写本段新增内容对应的要点，不要重复已有内容。
若人物背景与当前发言有关联，可在该人物的色块内用小字补充背景（如角色、历史决策），注明来源。
```

**约束**：
- 严格基于新增句子，不添加推断性内容
- 跳过空内容章节
- 模糊信息标注「待确认」
- **参考用户风格**（启动时综合 3-5 篇样本学习）
- **人物背景仅供参考**：与当前发言无关联时不引用；引用时注明来源笔记
- 默认使用带色块的富文本排版（见「排版规范」章节）

### Step 6：写回笔记

**首轮**：在笔记末尾插入摘要标题 + 内容

```bash
# 获取最后一个 block ID
LAST_BLOCK=$(wpsnote-cli outline --note_id "$NOTE_ID" --json | \
  python3 -c "import sys,json; blocks=json.load(sys.stdin)['data']['blocks']; print(blocks[-1]['id'])")

# 插入摘要
wpsnote-cli edit --json-args "{
  \"note_id\": \"$NOTE_ID\",
  \"op\": \"insert\",
  \"anchor_id\": \"$LAST_BLOCK\",
  \"position\": \"after\",
  \"content\": \"<h2>转写摘要</h2><p>...</p>\"
}"
```

**后续轮次**：追加到上一轮摘要内容之后（使用 `summary_anchor_id`）

```bash
# 若有 Todo 块，先删后重插（保证 Todo 始终在末尾）
wpsnote-cli batch-edit --json-args "{
  \"note_id\": \"$NOTE_ID\",
  \"operations\": [
    {\"op\": \"delete\", \"block_ids\": [\"$TODO_BLOCK_ID\"]},
    {\"op\": \"insert\", \"anchor_id\": \"$SUMMARY_ANCHOR\", \"position\": \"after\",
     \"content\": \"<p>新增要点...</p>\"},
    {\"op\": \"insert\", \"anchor_id\": \"$NEW_CONTENT_LAST_ID\", \"position\": \"after\",
     \"content\": \"<p listType=\\\"todo\\\" listLevel=\\\"0\\\" checked=\\\"0\\\">...</p>\"}
  ]
}"
```

### 临时区写入（每轮必做）

临时区始终位于**整篇笔记的最末尾**。每轮摘要写完后，需要把临时区保持在最后。

**流程**：
1. 若临时区尚不存在（`state["temp_zone_anchor_id"]` 为 None）：在笔记最末尾插入 `<hr/>` + 提示块，记录 `temp_zone_anchor_id`
2. 若临时区已存在：先处理临时区用户内容（Step 6.5），再把新摘要内容插入到**临时区之前**（而非末尾），保证临时区始终压底

**首轮首次创建临时区**（摘要写完后）：

```bash
# 获取当前笔记最后一个 block（此时已是刚写完的摘要内容）
LAST_BLOCK=$(wpsnote-cli outline --note_id "$NOTE_ID" --json | \
  python3 -c "import sys,json; blocks=json.load(sys.stdin)['data']['blocks']; print(blocks[-1]['id'])")

wpsnote-cli edit --json-args "{
  \"note_id\": \"$NOTE_ID\",
  \"op\": \"insert\",
  \"anchor_id\": \"$LAST_BLOCK\",
  \"position\": \"after\",
  \"content\": \"<hr/><highlightBlock emoji=\\\"💬\\\" highlightBlockBackgroundColor=\\\"#EBEBEB\\\" highlightBlockBorderColor=\\\"#C5C5C5\\\"><p><span fontColor=\\\"#757575\\\">临时区：把你的想法、补充、纠正贴到这里，AI 下轮自动合并到正文对应位置。也可以直接改上面的正文。</span></p></highlightBlock>\"
}"
# state["temp_zone_anchor_id"] = 返回的 last_block_id（highlightBlock 的 id）
```

**后续轮次**：新摘要内容插入到**临时区的 hr 块之前**，临时区自然保持在最末尾，不需要移动。

```bash
# 后续轮次写摘要时，anchor 用临时区 hr 块的前一个 block（即上轮摘要最后一个内容块）
# 而非直接插到末尾，这样临时区始终压底
wpsnote-cli edit --json-args "{
  \"note_id\": \"$NOTE_ID\",
  \"op\": \"insert\",
  \"anchor_id\": \"$SUMMARY_ANCHOR_ID\",
  \"position\": \"after\",
  \"content\": \"<p>新增摘要内容...</p>\"
}"
# summary_anchor_id 更新为本轮最后一个摘要 block，仍在临时区 hr 之前
```

### Step 6.5：处理临时区用户输入（每轮必做）

在写回摘要之后、检测 `***` 之前，检查用户是否在临时区里写了内容。

```python
# 读取临时区 anchor_id（来自 state["temp_zone_anchor_id"]）
temp_anchor_id = state.get("temp_zone_anchor_id")
if not temp_anchor_id:
    # 临时区还未创建，跳过
    pass
else:
    # 读取临时区下方的 blocks
    # 临时区结构：<hr/> → <highlightBlock>提示文字</highlightBlock> → [用户插入的内容...]
    # 用 read-blocks 读取 temp_zone_anchor_id 后方若干 block
    # 过滤掉提示文字本身（通过检测是否含「临时区：把你的想法」来识别提示块）
```

**判断临时区是否有用户内容**：

```bash
# 读取临时区 anchor 后方 10 个 block
TEMP_BLOCKS=$(wpsnote-cli read-blocks --note_id "$NOTE_ID" \
  --json-args "{\"note_id\":\"$NOTE_ID\",\"block_id\":\"$TEMP_ANCHOR_ID\",\"after\":10}")
```

```python
import json
blocks_data = json.loads(temp_blocks_output)["data"]["blocks"]

# 过滤掉提示块（含关键文字「临时区：」的高亮块）和 hr 块
user_blocks = [
    b for b in blocks_data
    if b["type"] not in ("hr",)
    and "临时区：" not in b.get("content_text", "")
]

if not user_blocks:
    # 临时区无用户内容，跳过
    pass
else:
    # 有用户内容，触发合并流程
    merge_temp_zone_content(user_blocks)
```

**合并流程**：

1. 将用户写入的内容文本喂给 AI，结合本轮摘要上下文，判断每条内容应合并到哪个位置（哪个 h2/h3 节或哪个 column 内）
2. 用 `batch_edit` 把内容插入到对应位置
3. **清空临时区**：删除用户写入的 block，保留 `<hr/>` 和提示 block

```bash
# 合并后清理用户 block（只删用户写的，保留提示）
USER_BLOCK_IDS=$(echo "$user_blocks" | python3 -c "import sys,json; print(' '.join(b['id'] for b in json.load(sys.stdin)))")

wpsnote-cli batch-edit --json-args "{
  \"note_id\": \"$NOTE_ID\",
  \"operations\": [
    {\"op\": \"delete\", \"block_ids\": $USER_BLOCK_IDS}
  ]
}"
```

4. 在本轮简报中注明「临时区：合并了 N 条用户输入」

**合并 prompt 示例**：

```
以下是用户写在「临时区」的内容：
{user_temp_content}

以下是当前笔记的摘要大纲（含各 block_id）：
{summary_outline}

请判断每条临时内容应该插入到哪个位置（哪个 block_id 之后），
并生成对应的 WPS XML 插入内容。
规则：
- 若是对某个观点的补充，插入该观点 block 之后
- 若是新话题，插入摘要末尾（Todo 之前）
- 若是对某条信息的纠正，替换对应 block
- 保持原有排版风格（色块/bullet 等）
```

---

### Step 7：检测 *** 补全请求

```bash
STARS=$(wpsnote-cli search --note_id "$NOTE_ID" --query "***" --json)
```

若找到 `***`，读取其前后 **3 个** block（不是 5 个，进一步节省 token）：

```bash
wpsnote-cli read-blocks --note_id "$NOTE_ID" \
  --json-args "{\"note_id\":\"$NOTE_ID\",\"block_id\":\"$STAR_BLOCK\",\"before\":3,\"after\":3}"
```

生成补全内容后替换：

```bash
wpsnote-cli edit --json-args "{
  \"note_id\": \"$NOTE_ID\",
  \"op\": \"replace\",
  \"block_id\": \"$STAR_BLOCK\",
  \"content\": \"<p>补全后的内容</p>\"
}"
```

### Step 8：更新状态文件

```python
if new_sentences:
    state["last_end_time"] = new_sentences[-1]["end_time"]
    state["summary_anchor_id"] = last_inserted_block_id
    # temp_zone_anchor_id 首次写入后持久保留，后续轮次不覆盖
    if state.get("temp_zone_anchor_id") is None and temp_zone_block_id:
        state["temp_zone_anchor_id"] = temp_zone_block_id
state["round"] += 1
json.dump(state, open(state_path, "w"), ensure_ascii=False)
```

### Step 9：输出本轮简报

```
✓ 第 3 轮完成（新增 18 句 / 142 秒 → 摘要 +85 字）
  场景：会议记录  发言人：张总、李工❓
  人名联动：张总→《Q4 复盘》、李工→未找到相关笔记
  新增行动项：2 条  ***补全：1 处  临时区合并：1 条
  下一轮：60 秒后
```

---

## 场景识别表

| 场景关键词 | 场景类型 | 使用模板 |
|-----------|---------|---------|
| 会议、讨论、周会、评审 | 会议记录 | 会议纪要模板 |
| 课堂、授课、教学、老师 | 课堂笔记 | 课堂笔记模板 |
| 培训、讲师、学员 | 培训课程 | 培训课程模板 |
| 知识分享、分享会、经验分享 | 知识分享 | 知识分享模板 |
| 直播、主播、观众 | 直播内容 | 直播记录模板 |
| 播客、嘉宾、节目 | 播客/视频 | 播客纪要模板 |
| 采访、记者、被采访 | 采访记录 | 采访记录模板 |
| 谈判、甲方、乙方、合同 | 商务谈判 | 商务谈判模板 |
| 复盘、总结、里程碑 | 项目复盘 | 项目复盘模板 |
| 庭审、原告、被告、法庭 | 庭审记录 | 庭审纪要模板 |
| 患者、诊断、医嘱、症状 | 病例记录 | 病例记录模板 |
| 口述、文章、博客 | 口述转文章 | 文章模板 |
| 电话、通话、客服 | 电话录音 | 电话记录模板 |
| 无明显特征 | 通用场景 | 通用转写模板 |

---

## 风格学习

启动时读 **3-5 篇**历史会议纪要/总结笔记，每篇上限 **3000 字**，综合归纳风格。

**搜索关键词**（依次尝试，直到凑够 3 篇）：
1. `会议纪要 纪要`
2. `周会 月会 复盘`
3. `总结 摘要`

**综合归纳维度**（多篇投票取多数）：
- 语言风格：口语 vs 书面
- 结构偏好：全 bullet list vs 分章节标题
- 详略程度：每条 ≤10 字 vs 每条 ≥30 字
- 是否中英混写
- 是否常用色块/分栏排版

样本 < 3 篇时标注「风格样本不足，参考有限」，仍继续。

风格学习是参考，不是复制。转写内容决定信息，用户风格决定表达方式。

---

## 排版规范

默认使用富文本排版。用户明确说「纯文本」「不要排版」时才退回普通段落。

### 核心排版元素

**① 单栏 columns（带色块）**：承载一个发言人的完整观点或一个主题块

颜色语义（`columnBackgroundColor`）：
- 蓝色 `#EBF2FF`：中性信息、发言人观点
- 绿色 `#E8FCEF`：结论、共识
- 黄色 `#FFF5EB`：注意事项、待确认
- 红色 `#FFECEB`：风险、问题、争议点
- 紫色 `#FAF0FF`：补充信息、延伸内容

```xml
<columns>
  <column columnBackgroundColor="#EBF2FF">
    <h4>发言人 · 身份信息</h4>
    <p listType="bullet" listLevel="0">要点一</p>
    <blockquote>「原话片段」</blockquote>
  </column>
</columns>
```

**② 双栏 columns**：仅用于内容天然对立的场景（谈判双方、优缺点对比）

**③ blockquote**：保留有价值的原话，1-2 句，放在色块内紧跟相关要点

**④ 颜色强调**：仅用于行内关键词、数字，不大段上色

```xml
<span fontHighlightColor="#FBF5B3">关键数据</span>
<span fontColor="#C21C13">风险词</span>
```

### 使用判断

**应该用色块**：有明确发言人且有 2+ 条观点；一个完整主题超过 3 条要点

**不应该用色块**：只有 1 条信息；行动项/Todo；内容少结构简单时

### 结构原则

先按**主题/议题**分 `h2`/`h3` 章节，再在章节内用色块区分发言人。

```
h2 主题一
  ├── columns(蓝) 发言人 A
  ├── columns(蓝) 发言人 B
  └── columns(绿) 结论/共识
h2 行动项
  └── todo list（不套色块）
```

---

## 场景模板

各模板均遵循「严格基于转写、跳过空章节、默认富文本排版」原则。

| 场景 | 主结构 | 特殊要求 |
|------|--------|---------|
| 通用 | h2摘要 → h3主题 → columns(蓝) → todo | — |
| 会议纪要 | h2纪要 → h3议题 → columns(蓝)发言人 → columns(绿)结论 → todo | 含参会人、决策标注 |
| 课堂笔记 | h2笔记 → h3知识点 → h4细节 → h3重点 → todo作业 | 无色块，以层级代替 |
| 知识分享 | h2记录 → h3核心知识 → h4知识点 → h3要点 → todo学习 | — |
| 直播/播客 | h2纪要 → h3主题 → columns(黄)嘉宾A → columns(蓝)嘉宾B | 注明嘉宾身份 |
| 商务谈判 | h2记录 → h3议题 → 双栏(蓝/红)甲乙方 → columns(绿)协议 → todo | 双栏对立布局 |
| 项目复盘 | h2复盘 → h3成果 → h3问题 → h3经验 → todo改进 | 量化成果 |
| 庭审/病例/采访/电话/培训 | 按各专业流程顺序组织，见下方说明 | — |

**专业场景结构**：
- **庭审**：庭前准备→法庭调查→举证质证→法庭辩论→最后陈述
- **病例**：主诉→现病史→诊断→治疗方案→医嘱
- **采访**：5W1H要素→精彩引用→后续跟进
- **电话录音**：通话目的→讨论内容→承诺事项→后续行动
- **培训课程**：课程大纲→知识点→实践练习→课后作业
- **口述转文章**：引言→章节→结论（口语转书面语）

> 完整 XML 模板见 [templates.md](templates.md)

---

## Todo 提取规则

从新增转写中识别任务：

1. **明确任务**：含动作动词（完成、提交、准备、跟进）+ 时间限定或责任人
2. **承诺事项**：「我会/我们将...」「XX 时候给您...」
3. **学习任务**：「需要学习/实践/应用...」

```xml
<p listType="todo" listLevel="0" checked="0">[任务]（负责人：XX，截止：XX）</p>
```

---

## 停止条件

以下情况停止循环：
- 用户明确说「停止」「结束总结」「stop」
- 连续 **5 轮**无新增转写（之前是 3 轮，延长以防止录音短暂停顿误停）
- 音频 `status=stopped` 且已完成最终总结

停止时清理状态文件：`rm /tmp/lts_state_{note_id}.json`

---

## 错误处理

| 错误 | 处理方式 |
|------|---------|
| CLI 不可用 | 退回 MCP 模式 |
| `NO_ACTIVE_EDITOR_WINDOW` | 提示用户打开笔记，等待 30 秒后重试 |
| `WEBSOCKET_NOT_CONNECTED` | 等待 10 秒后重试转写获取 |
| `EDITOR_NOT_READY` | 等待 2 秒后重试写入 |
| `BLOCK_NOT_FOUND` | 重新 `outline` 刷新 ID 后重试 |
| `DOCUMENT_READ_ONLY` | 告知用户笔记为只读，停止写入但继续读取 |
| 转写返回空 | 等待 30 秒（可能正在转写中）后重试 |

---

## 输出示例

### 启动告知

```
已开始边听边总结 ✓

当前笔记：2026-03 产品周会
识别场景：等待录音开始后自动识别
参考风格：找到 5 篇会议纪要（综合归纳：书面+分章节+色块排版）
模式：增量（只处理新增转写）+ 人名联动（自动搜索笔记库）
轮询间隔：60 秒

---
如需 AI 援助：
  ① 补全：在笔记任意位置输入 ***，AI 结合录音自动补全
  ② 临时区：每轮摘要末尾有一个灰色提示区，把想法/补充/纠正贴到那里，AI 下轮自动合并到正文
  ③ 停止：告诉我「停止总结」即可
---
```

### 每轮完成简报

```
✓ 第 3 轮完成
  新增：18 句 / 142 秒 → 摘要 +85 字
  场景：会议记录  发言人：张总、李工❓
  行动项新增：2 条  ***补全：1 处
  下一轮：60 秒后
```

### 无新增时

```
⏭  第 4 轮：无新增内容（转写停在 342.5s），等待中...
```
