# SkillCollection

> Claude Code / AI Agent 技能聚合仓库

聚合 13 个上游开源仓库的 **222 个 Skill**，按功能自动聚类、评分与排名，在同一个目录下统一浏览与调用。

- **可读索引**：[SKILLS_INDEX.md](./SKILLS_INDEX.md) — 按聚类呈现的全部 Skill 列表
- **核心数据源**：[skills-registry.json](./skills-registry.json) — 聚类 / 评分 / 排名 / 依赖信息
- **Skill 选择规则**：[CLAUDE.md](./CLAUDE.md) — 同一聚类内的优先顺序与 fallback 机制

## 统计

| 维度 | 数量 |
|------|------|
| 上游仓库 | 13 |
| Skill 总数 | 222 |
| 聚类 | 11 |

## 上游仓库

| 仓库目录 | 来源 | Skills | 说明 |
|---------|------|-------:|------|
| [lenny-skills](./lenny-skills) | [RefoundAI/lenny-skills](https://github.com/RefoundAI/lenny-skills) | 86 | 商业诊断 / 产品研发 / 市场分析 等 |
| wpsnote-skills (根目录 `skills/`) | [wpsnote/wpsnote-skills](https://github.com/wpsnote/wpsnote-skills) | 36 | WPS 笔记生态：wps-note、内容创作、信息捕获、灵感引擎等 |
| [MiniMax-skills](./MiniMax-skills) | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | 22 | MiniMax 官方：音视频生成、图像、文本 |
| [baoyu-skills](./baoyu-skills) | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | 21 | 宝玉：封面图、小红书、公众号、翻译 |
| [ljg-skills](./ljg-skills) | [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) | 17 | 李继刚：论文研读、单词流、文本简化 |
| [dbskill](./dbskill) | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | 13 | 不要沉默：小红书标题、内容工作流 |
| [ClaWiser](./ClaWiser) | [MattWenJun/ClaWiser](https://github.com/MattWenJun/ClaWiser) | 9 | Claude 写作辅助 |
| [marketing-skills](./marketing-skills) | [atypica-ai/marketing-skills](https://github.com/atypica-ai/marketing-skills) | 6 | 营销文案与策略 |
| [wechat-skills](./wechat-skills) | [gainubi/wechat-skills](https://github.com/gainubi/wechat-skills) | 5 | 公众号排版与生成 |
| [wechat_article_skills](./wechat_article_skills) | [BND-1/wechat_article_skills](https://github.com/BND-1/wechat_article_skills) | 4 | 公众号文章辅助 |
| [markdown-proxy](./markdown-proxy) | [joeseesun/markdown-proxy](https://github.com/joeseesun/markdown-proxy) | 1 | Markdown 转换 |
| [anything-to-md](./anything-to-md) | [1596941391qq/anything-to-md](https://github.com/1596941391qq/anything-to-md) | 1 | 任意格式转 Markdown |
| [James-Skills](./James-Skills) | [James19890801/Skills](https://github.com/James19890801/Skills) | 1 | 个人 Skill |
| [awesome-claude-code-subagents](./awesome-claude-code-subagents) | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | — | Claude Code 子智能体集合（非 SKILL.md 结构，未纳入评分） |

每个子目录都是独立的 git 仓库，以 **gitlink** 形式提交。Clone 本仓库后需要手动补充子仓库内容（见 [更新流程](#更新流程)）。

## 聚类概览

| 聚类 | Skill 数 |
|------|--------:|
| 商业诊断与分析 | 85 |
| 图片与视觉生成 | 23 |
| 笔记管理与知识整理 | 23 |
| 内容创作与写作 | 21 |
| 信息采集与知识提取 | 18 |
| 开发与工程 | 17 |
| 翻译与格式转换 | 12 |
| 社交媒体发布与排版 | 8 |
| 学习与教育 | 7 |
| 未分类 | 7 |
| 简历与专业文档 | 1 |

每个聚类内按综合评分（功能完整度 35% · 依赖简洁度 20% · 版本活跃度 25% · 稳定性 20%）排名。详情见 [SKILLS_INDEX.md](./SKILLS_INDEX.md)。

## 工作机制

1. **发现**：`scripts/scan-all-skills.py` 递归扫描所有子目录下的 `SKILL.md`，提取 frontmatter 与外部依赖
2. **聚类 + 评分**：`scripts/build-registry.py` 基于关键词匹配分配到 11 个预定义聚类，按 4 维评分排名写入 `skills-registry.json`
3. **生成索引**：`scripts/generate-index.py` 从 registry 生成人类可读的 `SKILLS_INDEX.md`
4. **Fallback 选择**：同一聚类内优先用 rank=1 的 Skill，失败时自动降级到 rank=2、rank=3…（规则见 [CLAUDE.md](./CLAUDE.md)）

## 更新流程

### 同步所有子仓库到最新版本

```bash
bash scripts/update-skills.sh
```

该脚本会依次：拉取所有子仓库最新提交 → 重新扫描 → 重建 registry → 重新生成索引 → 显示变更 diff。

### 添加新的 Skill 仓库

```bash
git clone https://github.com/<owner>/<repo>.git
bash scripts/update-skills.sh
```

新仓库的 `SKILL.md` 会被自动发现并根据描述分配到已有聚类。如果想让它进入 README 的上游表或改善聚类精度，可手动编辑 [scripts/generate-index.py](./scripts/generate-index.py) 的 `REPO_SOURCES` 表或 [scripts/build-registry.py](./scripts/build-registry.py) 的 `CLUSTERS` 关键词。

### 克隆本仓库的完整流程

```bash
git clone https://github.com/dy9759/SkillCollection.git
cd SkillCollection
# 按 README 上游仓库表，逐个 git clone 需要的子仓库
git clone https://github.com/RefoundAI/lenny-skills.git
# ... 其他
bash scripts/update-skills.sh   # 重建 registry 与索引
```

## 目录结构

```
SkillCollection/
├── CLAUDE.md                     Skill 选择 / fallback 规则
├── README.md
├── SKILLS_INDEX.md               生成：按聚类呈现的可读索引
├── skills-registry.json          生成：核心数据源
├── scripts/
│   ├── scan-all-skills.py        扫描 SKILL.md 元数据
│   ├── build-registry.py         聚类 + 评分 + 排名
│   ├── generate-index.py         registry → 可读索引
│   └── update-skills.sh          一键更新
├── lenny-skills/                 上游子仓库（gitlink）
├── wpsnote-skills 原始资源/       skills/ · comm_script/ · skill-creator/ ...
└── ... (其他子仓库)
```

## License

各子仓库的许可证遵从其原始仓库。聚合脚本（`scripts/`）与索引（`SKILLS_INDEX.md` / `skills-registry.json`）可自由使用。

---

> 所有内容，都值得等到被用到的那天。
