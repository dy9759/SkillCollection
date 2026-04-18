#!/usr/bin/env python3
"""扫描所有子仓库的 SKILL.md，提取元数据输出 JSON"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent

EXCLUDE_DIRS = {"node_modules", ".git", "vendor", "__tests__", "test", ".claude", ".gemini", "dist", "build"}

# 顶层 SKILL.md（不在任何带 .git 子仓库里的）被归属给哪个 source
# 历史上根目录 skills/ 来自 wpsnote-skills；如果未来根目录内容来自不同仓库，改此常量即可。
ROOT_SOURCE_NAME = "wpsnote-skills"


def find_skill_files(root: Path) -> list[Path]:
    results = []
    for path in sorted(root.rglob("SKILL.md")):
        if any(exc in path.parts for exc in EXCLUDE_DIRS):
            continue
        results.append(path)
    return results


def parse_frontmatter(filepath: Path) -> dict:
    text = filepath.read_text(encoding="utf-8", errors="replace")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    fm_text = match.group(1)
    result = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip("\"'")
        if key in ("name", "description", "version"):
            result[key] = val
        elif key == "user_invocable":
            result[key] = val.lower() == "true"
    return result


def detect_source(rel_path: str, root: Path) -> str:
    top_dir = rel_path.split("/")[0]
    if (root / top_dir / ".git").is_dir():
        return top_dir
    return ROOT_SOURCE_NAME


def detect_deps(skill_dir: Path, skill_file: Path) -> list[str]:
    deps = []
    if (skill_dir / "package.json").exists():
        deps.append("node")
    scripts_dir = skill_dir / "scripts"
    if scripts_dir.is_dir() and any(scripts_dir.glob("*.ts")):
        deps.append("bun")
    if (skill_dir / "references").is_dir():
        deps.append("references")
    content = skill_file.read_text(encoding="utf-8", errors="replace").lower()
    if any(kw in content for kw in ("chrome", "cdp", "playwright", "chromium")):
        deps.append("chrome")
    if any(kw in content for kw in ("api_key", "api key", "openai", "dashscope", "minimax")):
        deps.append("api-keys")
    return deps


def get_last_commit(repo_dir: Path) -> str:
    if not (repo_dir / ".git").is_dir():
        return "unknown"
    try:
        out = subprocess.check_output(
            ["git", "-C", str(repo_dir), "log", "-1", "--format=%Y-%m-%dT%H:%M:%S"],
            stderr=subprocess.DEVNULL, text=True
        )
        return out.strip()
    except Exception:
        return "unknown"


def main():
    skill_files = find_skill_files(ROOT_DIR)
    skills = []

    for sf in skill_files:
        fm = parse_frontmatter(sf)
        name = fm.get("name", "")
        if not name:
            continue

        rel_path = str(sf.relative_to(ROOT_DIR))
        skill_dir = sf.parent
        rel_dir = str(skill_dir.relative_to(ROOT_DIR))
        source = detect_source(rel_path, ROOT_DIR)
        deps = detect_deps(skill_dir, sf)
        line_count = len(sf.read_text(encoding="utf-8", errors="replace").splitlines())

        desc = fm.get("description", "")
        if len(desc) > 200:
            desc = desc[:200] + "..."

        status = "experimental" if "danger" in name else "active"
        last_commit = get_last_commit(ROOT_DIR / source)

        skills.append({
            "name": name,
            "source": source,
            "path": rel_dir,
            "description": desc,
            "version": fm.get("version"),
            "user_invocable": fm.get("user_invocable", False),
            "external_deps": deps,
            "status": status,
            "skill_md_lines": line_count,
            "last_repo_commit": last_commit,
        })

    json.dump(skills, sys.stdout, ensure_ascii=False, indent=2)
    print()
    print(f"// Total: {len(skills)} skills scanned", file=sys.stderr)


if __name__ == "__main__":
    main()
