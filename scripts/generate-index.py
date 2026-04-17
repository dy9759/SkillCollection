#!/usr/bin/env python3
"""从 skills-registry.json 生成 SKILLS_INDEX.md"""

import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

# 仓库来源表
REPO_SOURCES = [
    ("(根目录)", "wpsnote/wpsnote-skills", "WPS笔记全套AI技能（30+技能）"),
    ("baoyu-skills/", "JimLiu/baoyu-skills", "内容生成/翻译/社交媒体发布套件"),
    ("James-Skills/", "James19890801/Skills", "简历生成与流程监控"),
    ("wechat_article_skills/", "BND-1/wechat_article_skills", "微信公众号写作与发布工具链"),
    ("ClaWiser/", "MattWenJun/ClaWiser", "Agent记忆与工作流增强"),
    ("wechat-skills/", "gainubi/wechat-skills", "微信公众号写作四件套"),
    ("awesome-claude-code-subagents/", "VoltAgent/awesome-claude-code-subagents", "127+专业Claude Code子代理"),
    ("MiniMax-skills/", "MiniMax-AI/skills", "全栈开发与多模态生成技能"),
    ("dbskill/", "dontbesilent2025/dbskill", "商业诊断工具箱"),
    ("markdown-proxy/", "joeseesun/markdown-proxy", "URL转Markdown代理服务"),
    ("ljg-skills/", "lijigang/ljg-skills", "个人技能集（15技能）"),
    ("anything-to-md/", "1596941391qq/anything-to-md", "万能文件转Markdown"),
    ("marketing-skills/", "atypica-ai/marketing-skills", "市场调研/用户访谈/产品创新（6技能）"),
]


def rank_label(rank: int, total: int) -> str:
    if rank == 1:
        return "首选"
    elif rank == 2:
        return "备选"
    elif rank == total:
        return "保底"
    else:
        return ""


def status_label(status: str) -> str:
    if status == "experimental":
        return "实验性"
    return ""


def generate():
    registry_file = ROOT_DIR / "skills-registry.json"
    registry = json.loads(registry_file.read_text())

    lines = []
    lines.append("# Skills Collection Index")
    lines.append("")
    lines.append("> 本仓库收录了多个 Claude Code / AI Agent 技能合集，按功能聚类分类，每个聚类内按综合评分排名。")
    lines.append(f"> 基于 `skills-registry.json` 自动生成 | 更新时间: {registry['updated_at'][:10]}")
    lines.append("")
    lines.append("**Fallback 机制**: 同一聚类内，优先使用排名靠前的 skill；如果首选 skill 失败（依赖缺失/API 报错），自动降级到下一个。")
    lines.append("")

    total_skills = sum(len(c["skills"]) for c in registry["clusters"])
    total_clusters = len(registry["clusters"])
    lines.append(f"**总计**: {total_clusters} 个聚类, {total_skills} 个技能")
    lines.append("")
    lines.append("---")
    lines.append("")

    for idx, cluster in enumerate(registry["clusters"], 1):
        lines.append(f"## {idx}. {cluster['name']}")
        lines.append("")
        lines.append(f"{cluster['description']}")
        lines.append("")
        lines.append("| # | 技能 | 来源 | 评分 | 说明 | Fallback |")
        lines.append("|---|------|------|------|------|----------|")

        for skill in cluster["skills"]:
            rank = skill["rank"]
            total = len(cluster["skills"])
            fb = rank_label(rank, total)
            st = status_label(skill["status"])
            label = st if st else fb

            desc = skill["description"]
            if len(desc) > 60:
                desc = desc[:57] + "..."

            lines.append(
                f"| {rank} | {skill['name']} | {skill['source']} "
                f"| {skill['score']:.0f} | {desc} | {label} |"
            )

        lines.append("")
        lines.append("---")
        lines.append("")

    # 仓库来源
    lines.append("## 仓库来源")
    lines.append("")
    lines.append("| 目录 | GitHub 仓库 | 简介 |")
    lines.append("|------|-------------|------|")
    for d, repo, desc in REPO_SOURCES:
        lines.append(f"| {d} | {repo} | {desc} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 线上推荐
    lines.append("## 线上推荐 Skills（未下载，仅索引）")
    lines.append("")
    lines.append("> 详见 [feishu-skills-recommend.md](feishu-skills-recommend.md)，来源：[飞书文档](https://my.feishu.cn/wiki/Mqsuw5G4ViNpCokHP5FcoPrWnYe)")
    lines.append("")
    lines.append("| 分类 | 技能 | 说明 |")
    lines.append("|------|------|------|")
    lines.append("| 技能管理 | skill-vetter, find-skills, skill-creator, model-usage, free-ride | 安全审查、技能搜索、创建、Token追踪、免费模型 |")
    lines.append("| 搜索与研究 | tavily-search, brave-search, multi-search-engine, summarize, web-search-exa | 多引擎搜索、内容摘要、结构化查询 |")
    lines.append("| 文案与营销 | copywriting, social-content, product-marketing | 文案润色、社媒适配、营销策略 |")
    lines.append("| 设计与体验 | ui-ux-pro-max, nano-banana-pro, frontend-design, diagram-generator | UI设计、AI绘图、前端组件、流程图 |")
    lines.append("| 文档与办公 | pdf, docx, xlsx | PDF处理、Word/Excel生成 |")

    output = ROOT_DIR / "SKILLS_INDEX.md"
    output.write_text("\n".join(lines) + "\n")
    print(f"Generated SKILLS_INDEX.md: {total_clusters} clusters, {total_skills} skills")


if __name__ == "__main__":
    generate()
