---
name: live-transcript-summary
description: 边听边总结：实时监听当前 WPS 笔记中的音频转写，每 60 秒自动循环一次，识别场景后按对应模板整理内容，并写回笔记。当用户提到正在录音、开会、听课、听播客、做采访、开始录制，或者希望 AI 帮忙整理、总结、记录当前正在发生的内容时使用此 skill。也适用于用户说「帮我跟着听」「你帮我记」「边听边整理」「录完帮我整理」「实时帮我总结」，或在笔记中输入 *** 希望 AI 结合录音补全内容的场景。
metadata:
  author: Yicheng Xu
  version: "2.0.0"
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
  "speaker_map": {"发言人 1": "张总", "发言人 2": "李工❓"}
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
  4. 若无新增 → 更新状态 → sleep 60 → continue
  5. 场景识别（首轮）+ 发言人推断
  6. 只用新增句子生成摘要
  7. wpsnote-cli batch-edit              → 写回笔记
  8. wpsnote-cli search "***"            → 检测补全请求
  9. 更新状态文件（last_end_time、round 等）
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

### Step 2：风格学习（节省 token 版）

只读 **1 篇**历史总结笔记的**前 500 字**：

```bash
# CLI 方式
NOTES=$(wpsnote-cli find --keyword "总结 纪要 摘要" --limit 3 --json)
STYLE_NOTE_ID=$(echo $NOTES | python3 -c "import sys,json; notes=json.load(sys.stdin)['data']['notes']; print(notes[0]['note_id'] if notes else '')")

# 只读前 500 字
if [ -n "$STYLE_NOTE_ID" ]; then
  wpsnote-cli read --note_id "$STYLE_NOTE_ID" --max_length 500 --json
fi
```

从前 500 字提取风格特征：语言风格（口语/书面）、结构偏好（扁平/层级）、详略程度。**不需要读完整篇**。

### Step 3：初始化状态文件

```python
import json, os, time

state = {
    "note_id": note_id,
    "shorthand_id": None,      # 首轮扫描到 AudioCard 后填入
    "scene": None,             # 首轮场景识别后填入
    "last_end_time": -1.0,     # -1 代表从头开始
    "summary_anchor_id": None, # 摘要区域的最后一个 block_id
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
  ② 停止：告诉我「停止总结」即可
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

### Step 5：生成摘要（只用新增句子）

**输入给 AI 的内容**：

```
[场景: {scene}] [发言人映射: {speaker_map}]

新增转写（{len(new_sentences)} 句，{duration:.0f}秒）：
{speaker}: {text}
{speaker}: {text}
...

请按{模板名}模板提取要点，生成 WPS XML 格式的增量摘要。
只写本段新增内容对应的要点，不要重复已有内容。
```

**约束**：
- 严格基于新增句子，不添加推断性内容
- 跳过空内容章节
- 模糊信息标注「待确认」
- **参考用户风格**（启动时学习）
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
state["round"] += 1
json.dump(state, open(state_path, "w"), ensure_ascii=False)
```

### Step 9：输出本轮简报

```
✓ 第 3 轮完成（新增 18 句 / 142 秒 → 摘要 +85 字）
  场景：会议记录  发言人：张总、李工❓
  新增行动项：2 条  ***补全：1 处
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

启动时通过读 **1 篇**历史笔记的**前 500 字**，提取用户写作习惯。

提取维度（按前 500 字足以判断的维度）：
- 语言风格：口语（「感觉」「其实」）vs 书面（「经讨论」「本次」）
- 结构偏好：全 bullet list vs 分章节标题
- 详略程度：每条 ≤10 字 vs 每条 ≥30 字
- 是否中英混写

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

### 通用转写模板

```xml
<h2>转写摘要</h2>
<p><strong>时间</strong>：[日期时间] &nbsp; <strong>主题</strong>：[主题]</p>
<h3>[主题一]</h3>
<columns>
  <column columnBackgroundColor="#EBF2FF">
    <h4>[发言人 / 子主题]</h4>
    <p listType="bullet" listLevel="0">[要点]</p>
    <blockquote>「[原话]」</blockquote>
  </column>
</columns>
<h3>后续行动</h3>
<p listType="todo" listLevel="0" checked="0">[行动项]</p>
```

### 会议纪要模板

```xml
<h2>会议纪要</h2>
<p><strong>主题</strong>：[主题] &nbsp; <strong>时间</strong>：[时间] &nbsp; <strong>参会</strong>：[人员]</p>
<h3>[议题一]</h3>
<columns>
  <column columnBackgroundColor="#EBF2FF">
    <h4>[发言人]</h4>
    <p listType="bullet" listLevel="0">[观点]</p>
    <blockquote>「[原话]」</blockquote>
  </column>
</columns>
<columns>
  <column columnBackgroundColor="#E8FCEF">
    <h4>结论 / 决策</h4>
    <p listType="bullet" listLevel="0">[决策]</p>
  </column>
</columns>
<h3>行动项</h3>
<p listType="todo" listLevel="0" checked="0">[任务]（负责人：XX，截止：XX）</p>
```

### 课堂笔记模板

```xml
<h2>课堂笔记</h2>
<p><strong>课程</strong>：[课程名] &nbsp; <strong>时间</strong>：[时间]</p>
<h3>核心知识点</h3>
<h4>[知识点一]</h4>
<p>[核心概念与讲解]</p>
<h3>重点强调</h3>
<p listType="bullet" listLevel="0">[重点1]</p>
<h3>作业与任务</h3>
<p listType="todo" listLevel="0" checked="0">[作业]（截止：XX）</p>
```

### 知识分享模板

```xml
<h2>知识分享记录</h2>
<p><strong>主题</strong>：[主题] &nbsp; <strong>分享人</strong>：[姓名]</p>
<h3>核心知识</h3>
<h4>[知识点一]</h4>
<p>[核心概念与实践经验]</p>
<h3>学习要点</h3>
<p listType="bullet" listLevel="0">[要点1]</p>
<h3>后续学习</h3>
<p listType="todo" listLevel="0" checked="0">[学习任务]</p>
```

### 直播/播客模板

```xml
<h2>内容纪要</h2>
<p><strong>标题</strong>：[标题] &nbsp; <strong>类型</strong>：[直播/播客]</p>
<h3>[主题一]</h3>
<columns>
  <column columnBackgroundColor="#FFF5EB">
    <h4>[嘉宾一] · [身份]</h4>
    <p listType="bullet" listLevel="0">[核心观点]</p>
    <blockquote>「[原话]」</blockquote>
  </column>
</columns>
<columns>
  <column columnBackgroundColor="#EBF2FF">
    <h4>[嘉宾二] · [身份]</h4>
    <p listType="bullet" listLevel="0">[核心观点]</p>
  </column>
</columns>
```

### 商务谈判模板

```xml
<h2>谈判记录</h2>
<p><strong>主题</strong>：[主题] &nbsp; <strong>各方</strong>：[甲方] vs [乙方]</p>
<h3>[议题一]</h3>
<columns>
  <column columnBackgroundColor="#EBF2FF">
    <h4>[甲方]</h4>
    <p listType="bullet" listLevel="0">[立场]</p>
  </column>
  <column columnBackgroundColor="#FFECEB">
    <h4>[乙方]</h4>
    <p listType="bullet" listLevel="0">[立场]</p>
  </column>
</columns>
<columns>
  <column columnBackgroundColor="#E8FCEF">
    <h4>达成协议</h4>
    <p listType="bullet" listLevel="0">[协议内容]</p>
  </column>
</columns>
<h3>待确认事项</h3>
<p listType="todo" listLevel="0" checked="0">[待确认]</p>
```

### 项目复盘模板

```xml
<h2>项目复盘</h2>
<p><strong>项目</strong>：[名称] &nbsp; <strong>时间</strong>：[时间]</p>
<h3>成果总结</h3>
<p>[量化与质化成果]</p>
<h3>问题与分析</h3>
<h4>[问题一]</h4>
<p>[原因分析与解决方案]</p>
<h3>经验教训</h3>
<p listType="bullet" listLevel="0">[成功经验/失败教训]</p>
<h3>改进行动</h3>
<p listType="todo" listLevel="0" checked="0">[改进项]（负责人：XX）</p>
```

### 其他专业场景

- **庭审**：按庭审程序（庭前准备→法庭调查→举证质证→法庭辩论→最后陈述）
- **病例**：按主诉→现病史→诊断→治疗方案→医嘱
- **新闻采访**：按 5W1H 要素 + 精彩引用 + 后续跟进
- **电话录音**：按通话目的→讨论内容→承诺事项→后续行动
- **采访记录**：按话题→核心观点→精彩引用→后续跟进
- **培训课程**：按课程大纲→知识点→实践练习→课后作业
- **口述转文章**：按引言→章节→结论，口语转书面语

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
参考风格：找到「Q1 复盘」（前 500 字，书面+扁平列表风格）
模式：增量（只处理新增转写）
轮询间隔：60 秒

---
如需 AI 援助：
  ① 补全：在笔记任意位置输入 ***，AI 结合录音自动补全
  ② 停止：告诉我「停止总结」即可
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
