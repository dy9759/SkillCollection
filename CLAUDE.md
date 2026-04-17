# CLAUDE.md — SkillCollection

本仓库是多个 Claude Code / AI Agent 技能合集的聚合仓库，包含 118+ 技能，来源于 12 个独立 GitHub 仓库。

## 仓库结构

```
SkillCollection/
├── skills-registry.json       # 核心数据源：所有技能的聚类、评分、排名
├── SKILLS_INDEX.md             # 从 registry 自动生成的可读索引
├── CLAUDE.md                   # 本文件：skill 选择与 fallback 规则
├── scripts/
│   ├── scan-all-skills.py      # 扫描所有 SKILL.md 元数据
│   ├── build-registry.py       # 聚类 + 评分 + 排名 → registry
│   ├── generate-index.py       # registry → SKILLS_INDEX.md
│   └── update-skills.sh        # 一键更新：git pull + 重新扫描 + 生成
├── baoyu-skills/               # JimLiu/baoyu-skills
├── ljg-skills/                 # lijigang/ljg-skills
├── MiniMax-skills/             # MiniMax-AI/skills
├── dbskill/                    # dontbesilent2025/dbskill
├── ClaWiser/                   # MattWenJun/ClaWiser
├── ... (更多子仓库)
```

## Skill 选择与 Fallback 规则

**核心原则**: 同一功能聚类内的 skill 按综合评分排名，优先使用排名靠前的 skill，失败时自动降级。

### 选择流程

1. **识别用户意图** → 匹配 `skills-registry.json` 中的 cluster（通过 `cluster.description` 和 `skills[].description`）
2. **优先使用 rank=1 的 skill**（首选方案）
3. **如果首选失败**（依赖缺失、API 报错、功能不匹配），**自动降级**到 rank=2
4. **继续降级**直到找到可用 skill 或全部失败
5. **失败时告知用户**正在切换备选方案并说明原因

### 暴露规则

- 同一 cluster 内**只在对话中提及当前正在使用的 skill**，不主动列举同类所有备选
- 标记 `status: "experimental"` 的 skill 仅在用户明确指定或所有 active skill 都失败时使用
- 用户可通过 `/skill-name` 直接指定某个 skill，跳过 fallback 逻辑

### 评分维度

| 维度 | 权重 | 说明 |
|------|------|------|
| 功能完整度 | 35% | 描述丰富度、SKILL.md 行数、references 存在 |
| 依赖简洁度 | 20% | 纯 prompt > 需 Node > 需 Chrome/CDP |
| 版本活跃度 | 25% | 版本号 + 仓库最近 commit 时间 |
| 稳定性 | 20% | 非 experimental + user_invocable |

### 聚类概览

查阅 `skills-registry.json` 获取完整聚类数据，或查看 `SKILLS_INDEX.md` 获取可读索引。

## 更新流程

```bash
# 一键更新所有子仓库 + 重新扫描 + 重新生成
bash scripts/update-skills.sh

# 或分步执行：
python3 scripts/scan-all-skills.py > scripts/scan-output.json   # 1. 扫描
python3 scripts/build-registry.py                                 # 2. 构建 registry
python3 scripts/generate-index.py                                 # 3. 生成索引
```

## 添加新技能仓库

1. `git clone <repo-url>` 到本目录
2. 运行 `bash scripts/update-skills.sh`
3. 检查 `skills-registry.json` 中新 skill 的聚类是否合理
4. 如需调整聚类，修改 `scripts/build-registry.py` 中的 `CLUSTERS` 定义
