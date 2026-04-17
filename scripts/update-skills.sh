#!/usr/bin/env bash
# update-skills.sh — 一键更新所有子仓库 + 重新扫描 + 重新生成
# 用法: bash scripts/update-skills.sh

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

echo "=========================================="
echo "  SkillCollection 更新工具"
echo "  $(date '+%Y-%m-%d %H:%M:%S')"
echo "=========================================="
echo ""

# ---- Step 1: 拉取所有 git 子仓库 ----
echo "▶ Step 1: 更新所有 Git 子仓库..."
UPDATED=()
FAILED=()
UPTODATE=()

for dir in */; do
    if [ -d "$dir/.git" ]; then
        repo_name="${dir%/}"
        printf "  %-35s " "$repo_name"
        output=$(git -C "$dir" pull --ff-only 2>&1) || {
            echo "✗ FAILED"
            FAILED+=("$repo_name: $output")
            continue
        }
        if echo "$output" | grep -q "Already up to date"; then
            echo "✓ up to date"
            UPTODATE+=("$repo_name")
        else
            echo "⬆ UPDATED"
            UPDATED+=("$repo_name")
        fi
    fi
done

echo ""
echo "  更新: ${#UPDATED[@]} | 已最新: ${#UPTODATE[@]} | 失败: ${#FAILED[@]}"
if [ ${#FAILED[@]} -gt 0 ]; then
    echo "  失败详情:"
    for f in "${FAILED[@]}"; do
        echo "    - $f"
    done
fi
echo ""

# ---- Step 2: 扫描所有 SKILL.md ----
echo "▶ Step 2: 扫描所有 SKILL.md..."
python3 scripts/scan-all-skills.py > scripts/scan-output.json 2>/dev/null
SKILL_COUNT=$(python3 -c "import json; print(len(json.load(open('scripts/scan-output.json'))))")
echo "  扫描到 $SKILL_COUNT 个技能"
echo ""

# ---- Step 3: 保存旧 registry 用于对比 ----
OLD_REGISTRY=""
if [ -f skills-registry.json ]; then
    OLD_REGISTRY=$(python3 -c "
import json
data = json.load(open('skills-registry.json'))
skills = {}
for c in data['clusters']:
    for s in c['skills']:
        skills[s['name']] = {'cluster': c['id'], 'score': s['score'], 'rank': s['rank']}
print(json.dumps(skills))
" 2>/dev/null || echo "{}")
fi

# ---- Step 4: 构建新 registry ----
echo "▶ Step 3: 构建 skills-registry.json..."
python3 scripts/build-registry.py
echo ""

# ---- Step 5: 生成 SKILLS_INDEX.md ----
echo "▶ Step 4: 生成 SKILLS_INDEX.md..."
python3 scripts/generate-index.py
echo ""

# ---- Step 6: 对比变更 ----
if [ -n "$OLD_REGISTRY" ] && [ "$OLD_REGISTRY" != "{}" ]; then
    echo "▶ Step 5: 变更对比..."
    python3 -c "
import json

old = json.loads('$OLD_REGISTRY')
new_data = json.load(open('skills-registry.json'))

new_skills = {}
for c in new_data['clusters']:
    for s in c['skills']:
        new_skills[s['name']] = {'cluster': c['id'], 'score': s['score'], 'rank': s['rank']}

# 新增
added = set(new_skills.keys()) - set(old.keys())
removed = set(old.keys()) - set(new_skills.keys())

# 排名变化
rank_changes = []
for name in set(new_skills.keys()) & set(old.keys()):
    o, n = old[name], new_skills[name]
    if o['rank'] != n['rank'] or o['cluster'] != n['cluster']:
        rank_changes.append((name, o, n))

if added:
    print(f'  新增 {len(added)} 个技能: {', '.join(sorted(added))}')
if removed:
    print(f'  移除 {len(removed)} 个技能: {', '.join(sorted(removed))}')
if rank_changes:
    print(f'  排名/聚类变化 {len(rank_changes)} 个:')
    for name, o, n in rank_changes[:10]:
        print(f'    {name}: #{o[\"rank\"]}({o[\"cluster\"]}) → #{n[\"rank\"]}({n[\"cluster\"]})')
if not added and not removed and not rank_changes:
    print('  无变更')
" 2>/dev/null || echo "  (对比跳过)"
    echo ""
fi

echo "=========================================="
echo "  更新完成！"
echo "=========================================="
