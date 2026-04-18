"""Tests for build-registry.py :: classify_skill, compute_score, dedupe_by_source_name"""


def _s(**overrides):
    """Build a skill dict with sensible defaults for scoring tests."""
    base = {
        "name": "test-skill",
        "description": "a test skill",
        "version": "1.0.0",
        "external_deps": [],
        "status": "active",
        "user_invocable": False,
        "skill_md_lines": 150,
        "last_repo_commit": "unknown",
    }
    base.update(overrides)
    return base


# --- classify_skill ---

def test_classify_name_match_wins(build_mod):
    """Name match scores 3, description match scores 1 — name should dominate."""
    s = {"name": "my-writer", "description": "unrelated topic"}
    assert build_mod.classify_skill(s) == "content-writing"


def test_classify_chinese_keyword(build_mod):
    s = {"name": "xxx", "description": "整理笔记的工具"}
    assert build_mod.classify_skill(s) == "note-knowledge"


def test_classify_c_level_advisor(build_mod):
    s = {"name": "cto-advisor", "description": "CTO guidance"}
    assert build_mod.classify_skill(s) == "c-level-advisor"


def test_classify_no_match_is_uncategorized(build_mod):
    s = {"name": "xyz123", "description": "totally unrelated text"}
    assert build_mod.classify_skill(s) == "uncategorized"


def test_classify_best_score_wins(build_mod):
    """When multiple clusters get hits, the one with most keyword hits wins."""
    # "code-reviewer" hits dev-engineering, "笔记" hits note-knowledge.
    # dev-engineering has "code-reviewer" as a name keyword (score 3).
    s = {"name": "code-reviewer", "description": "reviews code quality"}
    assert build_mod.classify_skill(s) == "dev-engineering"


# --- compute_score ---

def test_score_complete_skill_high(build_mod):
    """A skill with all metadata filled should score well."""
    s = _s(description="a" * 200, skill_md_lines=400,
           external_deps=["references"], user_invocable=True)
    scores = build_mod.compute_score(s)
    assert scores["total"] >= 75
    assert 0 <= scores["total"] <= 100


def test_score_experimental_drops_stability(build_mod):
    s = _s(status="experimental")
    scores = build_mod.compute_score(s)
    assert scores["stability"] == 30


def test_score_user_invocable_bonus(build_mod):
    plain = build_mod.compute_score(_s(user_invocable=False))
    ui = build_mod.compute_score(_s(user_invocable=True))
    assert ui["stability"] > plain["stability"]


def test_score_many_deps_lowers_simplicity(build_mod):
    """Each dep beyond 'references' costs 25 simplicity points."""
    no_dep = build_mod.compute_score(_s(external_deps=[]))
    many_dep = build_mod.compute_score(_s(external_deps=["node", "bun", "chrome"]))
    assert no_dep["dependency_simplicity"] > many_dep["dependency_simplicity"]
    assert many_dep["dependency_simplicity"] >= 0


def test_score_no_version(build_mod):
    """Missing version drops version_activity."""
    with_v = build_mod.compute_score(_s(version="1.0.0"))
    no_v = build_mod.compute_score(_s(version=None))
    assert with_v["version_activity"] > no_v["version_activity"]


def test_score_bounded_0_to_100(build_mod):
    """Even pathological inputs stay in [0, 100]."""
    s = _s(description="x" * 5000, skill_md_lines=99999,
           external_deps=["a", "b", "c", "d", "e", "f"],
           version="999.999.999", status="experimental")
    scores = build_mod.compute_score(s)
    for k in ("completeness", "dependency_simplicity", "version_activity", "stability"):
        assert 0 <= scores[k] <= 100, f"{k}={scores[k]}"
    assert 0 <= scores["total"] <= 100


# --- dedupe_by_source_name ---

def test_dedupe_unique_unchanged(build_mod):
    skills = [
        {"source": "a", "name": "x", "skill_md_lines": 10, "description": "d1"},
        {"source": "a", "name": "y", "skill_md_lines": 10, "description": "d2"},
        {"source": "b", "name": "x", "skill_md_lines": 10, "description": "d3"},
    ]
    out = build_mod.dedupe_by_source_name(skills)
    assert len(out) == 3


def test_dedupe_same_source_name_keeps_longer(build_mod):
    """Same (source, name) — keeper has more SKILL.md lines."""
    skills = [
        {"source": "a", "name": "x", "skill_md_lines": 10, "description": "short"},
        {"source": "a", "name": "x", "skill_md_lines": 100, "description": "also short"},
    ]
    out = build_mod.dedupe_by_source_name(skills)
    assert len(out) == 1
    assert out[0]["skill_md_lines"] == 100


def test_dedupe_tiebreak_on_description_length(build_mod):
    skills = [
        {"source": "a", "name": "x", "skill_md_lines": 50, "description": "short"},
        {"source": "a", "name": "x", "skill_md_lines": 50, "description": "a much longer description"},
    ]
    out = build_mod.dedupe_by_source_name(skills)
    assert len(out) == 1
    assert "longer" in out[0]["description"]


def test_dedupe_different_sources_preserved(build_mod):
    """Same name in different sources should both survive."""
    skills = [
        {"source": "a", "name": "x", "skill_md_lines": 10, "description": "d1"},
        {"source": "b", "name": "x", "skill_md_lines": 10, "description": "d2"},
    ]
    out = build_mod.dedupe_by_source_name(skills)
    assert len(out) == 2
