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
            "copywriter", "copywriting", "copy-editing", "draft", "writes",
            "创作", "comic", "漫画", "style-profiler", "topic", "outline",
            "title-generator", "content-production", "content-strategy",
            "content-humanizer", "content-strategist",
            "humanizer", "domain-name-brainstormer", "brainstormer",
            "writing-clearly-and-concisely", "crafting-effective-readmes",
            "naming-analyzer",
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
            "logo", "brand mark", "icon design", "SVG", "ui-design-system",
            "brand-guidelines", "design-system-starter", "design tokens",
            "draw-io", "drawio", "mermaid-diagrams", "excalidraw",
            "marp-slide",
        ],
    },
    {
        "id": "social-publish",
        "name": "社交媒体与营销投放",
        "description": "微信/微博/X/小红书发布、付费广告、SEO、邮件营销、着陆页、转化优化",
        "keywords": [
            "post-to", "publish", "wechat-publisher", "weibo", "twitter",
            "x-twitter-growth", "发布", "排版", "formatter",
            "draft-publisher", "markdown-to-html",
            "paid-ads", "ad-creative", "ads", "seo", "seo-audit", "ai-seo",
            "programmatic-seo", "app-store-optimization", "schema-markup",
            "site-architecture", "social-content", "social-media",
            "email-sequence", "email-template", "cold-email",
            "landing-page", "popup-cro", "form-cro", "signup-flow-cro",
            "onboarding-cro", "page-cro", "paywall-upgrade-cro",
            "campaign-analytics", "demo-video", "marketing-psychology",
            "marketing-strategy", "marketing-ops", "marketing-context",
            "marketing-demand-acquisition", "marketing-ideas",
            "marketing-skills", "referral-program", "churn-prevention",
            "free-tool-strategy", "launch-strategy", "behuman",
            "video-content-strategist",
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
            "fetch", "research-summarizer", "autoresearch",
            "meeting-analyzer",
        ],
    },
    {
        "id": "note-knowledge",
        "name": "笔记管理与知识整理",
        "description": "笔记美化、标签整理、知识关联、灵感发现、记忆系统、内部 wiki",
        "keywords": [
            "note", "笔记", "tag", "beautif", "insight", "memory",
            "calendar", "search", "知识", "clawiser", "recall",
            "connect-dot", "save-game", "load-game", "deposit", "noise",
            "wiki-ingest", "wiki-init", "wiki-lint", "wiki-log",
            "wiki-query", "cs-wiki", "llm-wiki", "context-engine",
            "codebase-onboarding", "code-tour", "decision-logger",
            "remember", "ljg-think", "追本", "纵向深钻", "思维工具",
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
        "description": "前端/移动端/全栈开发、代码审查、测试、调试、Office自动化、子代理编排",
        "keywords": [
            "frontend", "fullstack", "mobile", "android", "ios", "flutter",
            "react", "coding", "skill-map", "skill-creator", "subagent",
            "office", "ppt", "excel", "docx", "pdf",
            "multimodal", "design-style", "color-font",
            "senior-architect", "senior-backend", "senior-frontend",
            "senior-fullstack", "senior-ml-engineer", "senior-data",
            "senior-computer-vision", "senior-prompt-engineer", "senior-qa",
            "senior-engineer", "engineering-skills", "engineering-team",
            "prompt-engineer", "prompt-governance", "code-reviewer",
            "code-to-prd", "pr-review", "api-design-reviewer",
            "api-test-suite-builder", "tdd", "tdd-guide", "testing",
            "testrail", "playwright", "browserstack", "coverage",
            "dependency-auditor", "stress-test", "self-eval", "eval",
            "adversarial-reviewer", "debug", "focused-fix", "fix",
            "karpathy", "performance-profiler", "monorepo", "migrate",
            "migration-architect", "spec-driven-workflow", "spec-to-repo",
            "saas-scaffolder", "mcp-server-builder", "rag-architect",
            "llm-cost-optimizer", "self-improving-agent",
            "agent-designer", "agent-workflow-designer", "agent-protocol",
            "agenthub", "orchestration", "git-worktree-manager",
            "browser-automation", "interview-system-designer",
            "changelog", "changelog-generator", "runbook-generator",
            "tech-debt", "tech-debt-tracker", "tech-stack-evaluator",
            "release-manager", "plugin-audit", "skill-tester",
            "database-designer", "database-schema-designer",
            "sql-database", "snowflake-development", "docker-development",
            "shipping-products", "vibe-coding", "fullstack-dev",
            "android-native-dev",
            "code-review-and-quality", "code-simplification",
            "api-and-interface-design", "documentation-and-adrs",
            "incremental-implementation", "performance-optimization",
            "qa-test-planner", "deprecation-and-migration",
            "git-workflow-and-versioning", "commit-work",
            "agent-md-refactor", "command-creator", "mui",
            "reducing-entropy", "merge", "session-handoff",
            "skill-judge", "using-agent-skills",
            "spec-driven-development", "source-driven-development",
            "lesson-learned", "ship-learn-next", "shipping-and-launch",
            "frontend-ui-engineering", "frontend-to-backend-requirements",
            "backend-to-frontend-handoff-docs", "c4-architecture",
            "browser-testing-with-devtools", "openapi-to-typescript",
            "react-dev", "react-useeffect", "datadog-cli",
            "dependency-updater", "debugging-and-error-recovery",
            "ci-cd-and-automation", "plugin-forge", "gepetto",
        ],
    },
    {
        "id": "devops-cloud",
        "name": "DevOps 与云基础设施",
        "description": "DevOps、SRE、Docker/K8s、Terraform、AWS/Azure/GCP、CI/CD、监控与密钥",
        "keywords": [
            "devops", "senior-devops", "sre", "helm-chart", "kubernetes",
            "terraform-patterns", "aws-solution-architect",
            "azure-cloud-architect", "gcp-cloud-architect", "cloud-architect",
            "ci-cd-pipeline", "ci-cd", "pipeline-builder", "observability",
            "env-secrets-manager", "secrets-vault-manager",
            "incident-response", "incident-commander", "postmortem",
            "post-mortems", "analytics-tracking", "stripe-integration",
            "atlassian-admin", "atlassian-templates", "confluence-expert",
            "jira-expert", "google-workspace", "ms365-tenant-manager",
            "workspace-admin",
        ],
    },
    {
        "id": "security-compliance",
        "name": "安全与合规",
        "description": "安全架构、渗透测试、威胁建模、代码/依赖审计、合规（SOC2/GDPR/ISO27001/HIPAA）",
        "keywords": [
            "senior-security", "senior-secops", "ai-security",
            "cloud-security", "security-pen-testing", "threat-detection",
            "red-team", "skill-security-auditor", "soc2-compliance",
            "gdpr-dsgvo-expert", "information-security-manager-iso27001",
            "isms-audit", "qms-audit", "iso13485", "mdr-745-specialist",
            "fda-consultant-specialist", "risk-management-specialist",
            "quality-documentation-manager", "quality-manager-qmr",
            "quality-manager-qms", "capa-officer",
            "regulatory-affairs-head", "ra-qm-skills",
            "security-and-hardening",
        ],
    },
    {
        "id": "product-agile",
        "name": "产品管理与敏捷开发",
        "description": "产品管理、敏捷/Scrum、Sprint 规划、OKR、路线图、用户研究、实验设计",
        "keywords": [
            "product-manager", "product-skills", "product-analytics",
            "product-discovery", "product-strategist", "product-team",
            "product-manager-toolkit", "pm-skills", "senior-pm",
            "agile-product-owner", "scrum-master", "sprint-plan",
            "sprint-health", "sprint-planning", "project-health",
            "project-management", "release-manager", "okr",
            "roadmap", "roadmap-communicator", "prd", "epic-design",
            "user-story", "rice", "retro", "retrospective",
            "ux-researcher-designer", "experiment-designer",
            "ab-test-setup", "persona", "apple-hig-expert",
            "saas-health", "saas-metrics-coach", "cs-product",
            "cs-agile-product-owner", "roadmap-update",
            "requirements-clarity", "daily-meeting-update",
            "planning-and-task-breakdown", "idea-refine",
            "game-changing-features", "feedback-mastery",
            "difficult-workplace-conversations", "professional-communication",
        ],
    },
    {
        "id": "business-analysis",
        "name": "商业诊断与分析",
        "description": "商业模式诊断、市场调研、投资分析、产品创新、竞品情报、增长策略",
        "keywords": [
            "diagnos", "诊断", "benchmark", "标杆", "invest", "投资",
            "rank", "降秩", "roundtable", "圆桌", "relationship", "关系",
            "action", "执行", "概念解构", "dbs", "chatroom", "austrian",
            "短视频", "content-diagnos",
            "market-sizing", "TAM", "SAM", "SOM", "market",
            "consultant", "framework", "JTBD", "KANO", "McKinsey",
            "user-interview", "focus group", "atypica",
            "product-rnd", "innovation", "NPD",
            "competitive-intel", "competitive-matrix", "competitive-teardown",
            "competitor-alternatives", "business-growth", "growth-strategist",
            "saas-metrics", "revenue-operations", "financial-analyst",
            "financial-health", "business-investment-advisor",
            "ma-playbook", "intl-expansion", "scenario-war-room",
            "strategic-alignment", "internal-narrative",
            "statistical-analyst", "data-quality-auditor",
            "finance-skills",
        ],
    },
    {
        "id": "c-level-advisor",
        "name": "高管顾问与领导力",
        "description": "CEO/CTO/CFO/CMO/CIO/COO/CISO/CRO/CPO/CHRO 顾问、董事会、创始人辅导、组织健康",
        "keywords": [
            "ceo-advisor", "cto-advisor", "cfo-advisor", "cmo-advisor",
            "coo-advisor", "ciso-advisor", "cro-advisor", "chro-advisor",
            "cpo-advisor", "c-level-advisor", "chief-of-staff",
            "board", "board-deck-builder", "board-meeting", "board-prep",
            "founder-coach", "executive-mentor", "culture-architect",
            "org-health-diagnostic", "change-management",
            "hard-call", "challenge", "company-os",
            "team-communications",
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
