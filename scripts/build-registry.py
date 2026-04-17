#!/usr/bin/env python3
"""从扫描结果生成 skills-registry.json（聚类 + 评分 + 排名）"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

# ============================================================
# 聚类定义：id, name, description, keywords (用于匹配)
# ============================================================
CLUSTERS = [
    {
        "id": "content-writing",
        "name": "内容创作与写作",
        "description": "文章撰写、文案生成、风格提取、小说写作等创作场景",
        "keywords": [
            "writing", "writer", "写作", "文章", "content-creator", "novel",
            "copywriter", "draft", "writes", "创作", "comic", "漫画",
            "style-profiler", "topic", "outline", "title-generator",
        ],
    },
    {
        "id": "image-visual",
        "name": "图片与视觉生成",
        "description": "AI绘图、信息图、封面、卡片、幻灯片等视觉内容生成与分析",
        "keywords": [
            "image", "图片", "imagine", "infographic", "cover", "slide",
            "card", "铸", "poster", "visual", "xhs-image", "xiaohongshu",
            "vision", "shader", "gif", "sticker", "illustrat", "绘",
            "logo", "brand mark", "icon design", "SVG",
        ],
    },
    {
        "id": "social-publish",
        "name": "社交媒体发布与排版",
        "description": "微信公众号、微博、X(Twitter)、小红书等平台的发布与格式化",
        "keywords": [
            "post-to", "publish", "wechat-publisher", "weibo", "twitter",
            "发布", "排版", "formatter", "draft-publisher", "markdown-to-html",
        ],
    },
    {
        "id": "translate-convert",
        "name": "翻译与格式转换",
        "description": "翻译、白话改写、Markdown格式化、图片压缩、文件格式转换",
        "keywords": [
            "translat", "翻译", "format", "convert", "compress", "plain",
            "白话", "anything-to-md", "markdown-proxy", "grok",
            "html-to-pdf", "export", "PDF",
        ],
    },
    {
        "id": "info-extract",
        "name": "信息采集与知识提取",
        "description": "网页抓取、论文阅读、新闻解读、内容摘要、视频字幕、媒体下载",
        "keywords": [
            "import", "digest", "paper", "论文", "transcript", "youtube",
            "url-to-markdown", "x-to-markdown", "x-download", "web-import",
            "literature", "research", "news", "抓取", "download", "travel",
            "fetch",
        ],
    },
    {
        "id": "note-knowledge",
        "name": "笔记管理与知识整理",
        "description": "笔记美化、标签整理、知识关联、灵感发现、记忆系统",
        "keywords": [
            "note", "笔记", "tag", "beautif", "insight", "memory",
            "calendar", "search", "知识", "clawiser", "recall",
            "connect-dot", "save-game", "load-game", "deposit", "noise",
        ],
    },
    {
        "id": "learning-edu",
        "name": "学习与教育",
        "description": "概念解剖、单词精通、闪卡、知识漏洞诊断等学习辅助",
        "keywords": [
            "learn", "flashcard", "lesson", "class-note", "lecture",
            "misconception", "prerequisite", "study", "word", "概念",
            "教育",
        ],
    },
    {
        "id": "dev-engineering",
        "name": "开发与工程",
        "description": "前端/移动端/全栈开发、Office自动化、子代理编排、技能管理",
        "keywords": [
            "frontend", "fullstack", "mobile", "android", "ios", "flutter",
            "react", "coding", "skill-map", "skill-creator", "subagent",
            "office", "ppt", "excel", "docx", "pdf", "pr-review",
            "multimodal", "design-style", "color-font",
        ],
    },
    {
        "id": "business-analysis",
        "name": "商业诊断与分析",
        "description": "商业模式诊断、市场调研、用户访谈、投资分析、产品创新、咨询框架",
        "keywords": [
            "diagnos", "诊断", "benchmark", "标杆", "invest", "投资",
            "rank", "降秩", "roundtable", "圆桌", "relationship", "关系",
            "action", "执行", "概念解构", "dbs", "chatroom", "austrian",
            "短视频", "content-diagnos",
            "market-sizing", "TAM", "SAM", "SOM", "market",
            "consultant", "framework", "JTBD", "KANO", "McKinsey",
            "user-interview", "focus group", "atypica", "persona",
            "product-rnd", "innovation", "NPD",
        ],
    },
    {
        "id": "resume-docs",
        "name": "简历与专业文档",
        "description": "简历生成、流程监控等专业文档场景",
        "keywords": [
            "resume", "cv", "简历", "process-monitor", "monitor",
        ],
    },
]


def classify_skill(skill: dict) -> str:
    """根据 skill 名称和描述匹配到最佳聚类"""
    name = skill["name"].lower()
    desc = skill["description"].lower()
    text = f"{name} {desc}"

    best_cluster = None
    best_score = 0

    for cluster in CLUSTERS:
        score = 0
        for kw in cluster["keywords"]:
            kw_lower = kw.lower()
            if kw_lower in name:
                score += 3  # 名称匹配权重更高
            if kw_lower in desc:
                score += 1
        if score > best_score:
            best_score = score
            best_cluster = cluster["id"]

    return best_cluster or "uncategorized"


def compute_score(skill: dict) -> dict:
    """计算综合评分（0-100）"""
    # 功能完整度 (35%): 描述丰富度 + SKILL.md 行数 + references
    desc_len = len(skill.get("description", ""))
    lines = skill.get("skill_md_lines", 0)
    has_refs = "references" in skill.get("external_deps", [])

    completeness = min(100, (desc_len / 150) * 40 + (lines / 300) * 40 + (20 if has_refs else 0))

    # 依赖简洁度 (20%): 纯prompt最高，依赖越多越低
    deps = skill.get("external_deps", [])
    dep_count = len([d for d in deps if d not in ("references",)])
    dependency_simplicity = max(0, 100 - dep_count * 25)

    # 版本活跃度 (25%): version 存在性 + 版本号大小 + 最近commit
    version = skill.get("version")
    version_score = 0
    if version:
        version_score += 30
        # 解析版本号
        parts = re.findall(r"\d+", str(version))
        if parts:
            major = int(parts[0])
            minor = int(parts[1]) if len(parts) > 1 else 0
            version_score += min(40, major * 10 + minor)
    last_commit = skill.get("last_repo_commit", "unknown")
    if last_commit != "unknown":
        try:
            commit_date = datetime.fromisoformat(last_commit)
            days_ago = (datetime.now() - commit_date).days
            if days_ago < 7:
                version_score += 30
            elif days_ago < 30:
                version_score += 20
            elif days_ago < 90:
                version_score += 10
        except Exception:
            pass
    version_activity = min(100, version_score)

    # 稳定性 (20%): danger前缀扣分、user_invocable加分
    stability = 80
    if skill.get("status") == "experimental":
        stability = 30
    if skill.get("user_invocable"):
        stability += 20
    stability = min(100, stability)

    # 加权综合
    total = (
        completeness * 0.35
        + dependency_simplicity * 0.20
        + version_activity * 0.25
        + stability * 0.20
    )

    return {
        "total": round(total, 1),
        "completeness": round(completeness, 1),
        "dependency_simplicity": round(dependency_simplicity, 1),
        "version_activity": round(version_activity, 1),
        "stability": round(stability, 1),
    }


def main():
    # 读取扫描结果
    scan_file = ROOT_DIR / "scripts" / "scan-output.json"
    if scan_file.exists():
        skills = json.loads(scan_file.read_text())
    else:
        # 直接从 stdin 或运行扫描
        import subprocess
        result = subprocess.run(
            [sys.executable, str(ROOT_DIR / "scripts" / "scan-all-skills.py")],
            capture_output=True, text=True
        )
        skills = json.loads(result.stdout)

    # 聚类
    clustered: dict[str, list] = {}
    for skill in skills:
        cluster_id = classify_skill(skill)
        clustered.setdefault(cluster_id, []).append(skill)

    # 构建 registry
    registry = {
        "version": "1.0.0",
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "clusters": [],
    }

    for cluster_def in CLUSTERS:
        cid = cluster_def["id"]
        cluster_skills = clustered.get(cid, [])
        if not cluster_skills:
            continue

        # 评分并排序
        scored_skills = []
        for skill in cluster_skills:
            scores = compute_score(skill)
            scored_skills.append({
                "name": skill["name"],
                "source": skill["source"],
                "path": skill["path"],
                "description": skill["description"],
                "version": skill["version"],
                "user_invocable": skill["user_invocable"],
                "score": scores["total"],
                "score_breakdown": {
                    "completeness": scores["completeness"],
                    "dependency_simplicity": scores["dependency_simplicity"],
                    "version_activity": scores["version_activity"],
                    "stability": scores["stability"],
                },
                "rank": 0,  # 稍后填入
                "external_deps": skill["external_deps"],
                "status": skill["status"],
            })

        # 按评分降序排序
        scored_skills.sort(key=lambda x: x["score"], reverse=True)
        for i, s in enumerate(scored_skills):
            s["rank"] = i + 1

        registry["clusters"].append({
            "id": cid,
            "name": cluster_def["name"],
            "description": cluster_def["description"],
            "skills": scored_skills,
        })

    # 处理未分类
    uncategorized = clustered.get("uncategorized", [])
    if uncategorized:
        scored = []
        for skill in uncategorized:
            scores = compute_score(skill)
            scored.append({
                "name": skill["name"],
                "source": skill["source"],
                "path": skill["path"],
                "description": skill["description"],
                "version": skill["version"],
                "user_invocable": skill["user_invocable"],
                "score": scores["total"],
                "score_breakdown": {
                    "completeness": scores["completeness"],
                    "dependency_simplicity": scores["dependency_simplicity"],
                    "version_activity": scores["version_activity"],
                    "stability": scores["stability"],
                },
                "rank": 0,
                "external_deps": skill["external_deps"],
                "status": skill["status"],
            })
        scored.sort(key=lambda x: x["score"], reverse=True)
        for i, s in enumerate(scored):
            s["rank"] = i + 1
        registry["clusters"].append({
            "id": "uncategorized",
            "name": "未分类",
            "description": "暂未归入明确聚类的技能",
            "skills": scored,
        })

    # 输出
    output_file = ROOT_DIR / "skills-registry.json"
    output_file.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n")

    # 统计
    total = sum(len(c["skills"]) for c in registry["clusters"])
    print(f"Registry generated: {len(registry['clusters'])} clusters, {total} skills")
    for c in registry["clusters"]:
        print(f"  {c['name']} ({len(c['skills'])} skills):")
        for s in c["skills"][:3]:
            label = "首选" if s["rank"] == 1 else ("备选" if s["rank"] == 2 else "")
            print(f"    #{s['rank']} {s['name']:35s} score={s['score']:5.1f}  {label}")
        if len(c["skills"]) > 3:
            print(f"    ... +{len(c['skills'])-3} more")


if __name__ == "__main__":
    main()
