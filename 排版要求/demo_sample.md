# 年初五，我花了 11000 块，测了 34205 条大模型用例

> 原文来自「洛小山」公众号<br>本文为排版格式样张，展示所有支持的排版元素

---

Hi，我是洛小山，你学习 AI 的搭子。

先说最重要的一件事：

!!你再也不用自己花钱花时间测模型了。!!

我替你做了这件事。==34205 条用例==，==42 个模型==，==11000 块人民币==，全部跑完了，结论汇成一个平台，免费给你用。

以后再有人问你「哪个模型好」，你不用再凭感觉答了。

先看榜单。

![榜单截图](../推文/02.21 大模型测评平台/素材/搜索 - 文风迁移结果 - 模型能力排序.jpg)

↑ 文字综合榜。第一名 Claude Sonnet 4.6，综合 95.4，成本 $3/$15。第二名 Qwen3.5-plus，综合 95.3，成本 $0.12/$0.69。两个差不到 0.2 分，但价格差了将近 **20 倍**。

---

## 01｜一个让我头疼了很久的问题

做 AI 产品这几年，被问最多的问题是：

**「你觉得现在用哪个模型最好？」**

每次我都卡住。不是不知道，是这个问题根本就没有答案。

因为真正的问题从来不是「哪个最好」。

**是：我这个具体任务，用哪个模型，花多少钱，最划算。**

---

## 02｜但你自己测，代价太大了

### 你面对的局面

假设你是 AI 产品经理，老板要你降本，要你认真选一次模型。想认真测一轮？那就要：

- 自己设计用例
- 自己打 API
- 自己写评估脚本
- 等结果出来了再人工复核打分

### 这笔账我算过

一轮认真的横评，覆盖主流模型，光 API 费用就得小几千块起。大公司可以养团队专门干这个。但对于大部分 AI 产品经理、独立开发者、小团队来说，这个代价根本扛不住。

---

## 03｜所以我自己跑了一遍，账单在这里

先上账单，不然你不会相信我说的数字。

![OpenRouter 账单截图](../推文/02.21 大模型测评平台/素材/测评到一半的费用.jpg)

↑ **$819，101K 次请求，365M tokens——而且这只是跑到一半。**

为了保证数据准确，我的原则是：==🔵国内模型一律用官方 API，不走第三方中转。==

![官方供应商配置](../推文/02.21 大模型测评平台/素材/做这个平台的开销.jpg)

↑ Cursor Ultra 套餐 $200/月，On-Demand 用量这个月又花了 **$469**。两项加起来，光 Cursor 这个月就快 $700 了。

把所有账单加在一起：**前后大概花了 1500 刀，折合约 11000 块人民币。**

这 11000 块，摊到每一个来用这个平台的人身上，就是 ==🟨0==。

---

## 04｜跑完之后，我发现了几个「意外」

跑了 **34205 条测试用例**，覆盖三大类：

1. **文本类**：写作、翻译、推理、代码、幻觉对抗、角色扮演……
2. **图像生成类**：风格还原、文字渲染、多语言排版、创意构图……
3. **网页生成类**：交互设计、响应式布局、表单、游戏、电商落地页……

每个大类下，用例分**基础 / 进阶 / 困难**三档难度。

![能力雷达图](../推文/02.21 大模型测评平台/素材/AI 帮你指出图片问题 1.jpg)

### DeepSeek 的意外

批判性思维这个维度，DeepSeek 得了 ==🔴66.1 分==，Claude 是 ==🟢92.5 分==，差距 26 分。

用大白话说：DeepSeek 容易被带节奏。你给它一个方向，它就顺着往下走，不太会反驳你。这在客服问答、知识问答类场景，风险比我想象的大。

### GLM-5 的意外

它在创意写作上出奇地好，L-Context 上下文理解 ==🟢98.1 分==，L-Creative 创意写作 SOTA。但数学推理和中文拼音处理，碰到复杂任务就掉得厉害。

> 这些结论不是我拍脑袋说的，是几万条用例跑出来的。<br>数据会说话，感觉会骗人。

---

## 05｜你真正需要的，不是总分，而是场景

!!光看总分没用。!!

有一件事很多人没意识到：**你的场景，根本不需要最强的模型。**

### 一个具体的数字

同样是文言文翻译，同样是基础难度：

| 模型 | 得分 | 1 万次调用成本 |
|---|---|---|
| 豆包 Seed2-Light | 99.4 | 157.93 元 |
| 通义 Qwen3.5-plus | 99.1 | 101 元 |
| DeepSeek-V3 | 98.8 | 149 元 |

1 万次就差了 **56 块**。如果你的产品每天跑几十万次请求，一个月下来这个差距是什么量级，你自己算。

!!在你没有这个平台之前，你根本不知道那些便宜的模型，其实也能做好这件事。!!

---

## 06｜还能帮你直接算这笔账

找到合适的模型之后，下一步是算成本。比如同等调用量（输入 10k token，输出 2k，调用 100 次），以 `qwen3.5-plus` 为基准：

- `OpenAI gpt-oss-20b`：比 qwen3.5 便宜 ==🟩77.2%==
- `doubao-seed-2-0-mini`：便宜 ==🟩65.9%==
- `deepseek-v3.2`：反而贵 ==🟥47.7%==

很多人以为 DeepSeek 便宜。这张表算出来，它比 Qwen3.5-plus 贵将近一半。

**每 1 万次调用省几十块，听起来不多。但如果你的产品日调用量是 10 万次，一个月就是几十万次。这笔账，值得算清楚。**

![费用测算页](../推文/02.21 大模型测评平台/素材/提需求页.jpg)

↑ 选好要对比的模型，填你的 token 用量和调用次数，平台直接给你算钱，多个模型横向对比。

---

## 07｜代码块示例（各语言）

### Python

```python
import openai

client = openai.OpenAI(api_key="your-key")

def evaluate_model(model: str, prompt: str) -> dict:
    """调用模型并返回结果"""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return {
        "model": model,
        "content": response.choices[0].message.content,
        "tokens": response.usage.total_tokens,
    }

# 批量测试多个模型
models = ["gpt-4o", "claude-sonnet-4-6", "qwen3.5-plus"]
results = [evaluate_model(m, "写一首关于 AI 的诗") for m in models]
```

### JavaScript

```javascript
const OpenAI = require('openai');

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

async function batchEvaluate(models, prompt) {
  const results = await Promise.all(
    models.map(async (model) => {
      const response = await client.chat.completions.create({
        model,
        messages: [{ role: 'user', content: prompt }],
      });
      return {
        model,
        score: null, // 待评分
        output: response.choices[0].message.content,
      };
    })
  );
  return results;
}
```

### TypeScript

```typescript
interface EvalResult {
  model: string;
  score: number;
  passed: boolean;
  tokens: number;
}

async function runEval(
  model: string,
  testCase: string,
  criteria: string[]
): Promise<EvalResult> {
  const response = await fetch('/api/evaluate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ model, testCase, criteria }),
  });
  return response.json() as Promise<EvalResult>;
}
```

### Bash

```bash
#!/bin/bash
# 批量跑测评，记录结果

MODELS=("gpt-4o" "claude-sonnet-4-6" "qwen3.5-plus")
OUTPUT_DIR="./results/$(date +%Y%m%d)"
mkdir -p "$OUTPUT_DIR"

for model in "${MODELS[@]}"; do
  echo "正在测试: $model"
  curl -s https://openrouter.ai/api/v1/chat/completions \
    -H "Authorization: Bearer $OPENROUTER_API_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"model\": \"$model\", \"messages\": [{\"role\": \"user\", \"content\": \"$PROMPT\"}]}" \
    > "$OUTPUT_DIR/${model//\//-}.json"
done

echo "完成！结果保存到 $OUTPUT_DIR"
```

### YAML

```yaml
# 测评配置文件
eval_config:
  name: 文字综合场景测评
  version: "2.0"
  models:
    - id: claude-sonnet-4-6
      provider: anthropic
      cost: { input: 3.0, output: 15.0 }
    - id: qwen3.5-plus
      provider: aliyun
      cost: { input: 0.12, output: 0.69 }
  test_cases:
    - category: writing
      difficulty: basic
      count: 100
    - category: translation
      difficulty: advanced
      count: 50
  scoring:
    method: llm_judge
    rubric: detailed
    pass_threshold: 80
```

### JSON

```json
{
  "eval_result": {
    "run_id": "eval-20260310-001",
    "total_cases": 34205,
    "models_tested": 42,
    "summary": {
      "top_model": "claude-sonnet-4-6",
      "top_score": 95.4,
      "avg_score": 85.25,
      "pass_rate": 0.78
    },
    "categories": {
      "text": { "cases": 18000, "avg": 88.1 },
      "image": { "cases": 12000, "avg": 82.4 },
      "web": { "cases": 4205, "avg": 79.6 }
    }
  }
}
```

---

## 08｜绝对独立，这件事我要单独说清楚

XSCT Bench，绝对独立运营。三条原则：

1. 不接受任何模型厂商赞助
2. 不接受暗箱排名，不做改分
3. 所有数据与输出真实、透明、可追溯

![About 页](../推文/02.21 大模型测评平台/素材/About 页.jpg)

↑ 这三条写在 About 页上，不是说着玩的。

这 11000 块是我自己花的。34205 条用例是我自己跑的。

!!我不需要向任何厂商交代，只需要对用这个平台的人负责。!!

---

## 09｜如果你有想测的场景，告诉我

![提需求页](../推文/02.21 大模型测评平台/素材/提需求页.jpg)

↑ 填你的场景描述、评测维度、刚需程度，我们帮你跑一遍，结论发给你。

---

## 终｜年初五，送你一个不花冤枉钱的工具

选错模型，是最隐形的浪费。性能浪费了，钱也浪费了，时间还浪费了。

我花了 11000 块，把这个坑替你踩完了。

XSCT Bench，平台免费，你只需要进来看结论。

以后再有人问你「用哪个模型好」，把这个链接甩给他就行了。

**地址：[xsct.ai](https://xsct.ai)**

欢迎把这篇文章转给，正在选模型选到头疼的朋友。

---

### 关于我

我是洛小山，一个在 AI 浪潮中不断思考和实践的大厂产品总监。
我不追热点，只分享那些能真正改变我们工作模式的观察和工具。
关注我，我们一起进化。

~~本文知识产权归洛小山所有。未经授权，禁止抓取本文内容，用于模型训练以及二次创作等用途。~~
