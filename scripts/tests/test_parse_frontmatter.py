"""Tests for scan-all-skills.py :: parse_frontmatter

Covers the YAML-based frontmatter parser: top-level fields, nested
metadata.version fallback, multi-line block scalars, quoting, malformed
input, and no-frontmatter input.
"""


def _write(tmp_path, body: str):
    p = tmp_path / "SKILL.md"
    p.write_text(body, encoding="utf-8")
    return p


def test_minimal_frontmatter(scan_mod, tmp_path):
    f = _write(tmp_path, "---\nname: foo\ndescription: bar\n---\nbody\n")
    assert scan_mod.parse_frontmatter(f) == {"name": "foo", "description": "bar"}


def test_top_level_version(scan_mod, tmp_path):
    f = _write(tmp_path, "---\nname: foo\ndescription: bar\nversion: 1.2.3\n---\n")
    assert scan_mod.parse_frontmatter(f)["version"] == "1.2.3"


def test_nested_metadata_version(scan_mod, tmp_path):
    body = (
        "---\n"
        "name: foo\n"
        "description: bar\n"
        "metadata:\n"
        "  version: 9.9.9\n"
        "  author: alice\n"
        "---\n"
    )
    fm = scan_mod.parse_frontmatter(_write(tmp_path, body))
    assert fm["version"] == "9.9.9"


def test_top_level_beats_nested(scan_mod, tmp_path):
    """When both are present, top-level version wins."""
    body = (
        "---\n"
        "name: foo\n"
        "description: bar\n"
        "version: 1.0.0\n"
        "metadata:\n"
        "  version: 9.9.9\n"
        "---\n"
    )
    fm = scan_mod.parse_frontmatter(_write(tmp_path, body))
    assert fm["version"] == "1.0.0"


def test_block_scalar_description(scan_mod, tmp_path):
    """Multi-line block-scalar description should collapse to one line."""
    body = (
        "---\n"
        "name: foo\n"
        "description: |\n"
        "  first line\n"
        "  second line\n"
        "---\n"
    )
    fm = scan_mod.parse_frontmatter(_write(tmp_path, body))
    assert "first line" in fm["description"]
    assert "second line" in fm["description"]
    assert "\n" not in fm["description"]


def test_user_invocable_bool_true(scan_mod, tmp_path):
    f = _write(tmp_path, "---\nname: foo\ndescription: bar\nuser_invocable: true\n---\n")
    assert scan_mod.parse_frontmatter(f)["user_invocable"] is True


def test_user_invocable_bool_false(scan_mod, tmp_path):
    f = _write(tmp_path, "---\nname: foo\ndescription: bar\nuser_invocable: false\n---\n")
    assert scan_mod.parse_frontmatter(f)["user_invocable"] is False


def test_quoted_values(scan_mod, tmp_path):
    f = _write(tmp_path, '---\nname: "foo-bar"\ndescription: \'hello world\'\n---\n')
    fm = scan_mod.parse_frontmatter(f)
    assert fm["name"] == "foo-bar"
    assert fm["description"] == "hello world"


def test_no_frontmatter(scan_mod, tmp_path):
    """File without `---` fence returns empty dict, doesn't raise."""
    f = _write(tmp_path, "# just a markdown heading\nno frontmatter here\n")
    assert scan_mod.parse_frontmatter(f) == {}


def test_empty_frontmatter(scan_mod, tmp_path):
    f = _write(tmp_path, "---\n---\nbody\n")
    assert scan_mod.parse_frontmatter(f) == {}


def test_malformed_yaml(scan_mod, tmp_path, capsys):
    """Broken YAML should log a warning and return empty dict, not crash."""
    body = "---\nname: foo\n  bad: indent\n :::\n---\n"
    fm = scan_mod.parse_frontmatter(_write(tmp_path, body))
    assert fm == {}
    # Warning goes to stderr (parse failed message) - just confirm no crash


def test_triggers_list_ignored(scan_mod, tmp_path):
    """Frontmatter with a triggers list (as in claude-skills0418) should parse
    cleanly without extracting the list itself."""
    body = (
        "---\n"
        "name: senior-security\n"
        "description: Security toolkit\n"
        "triggers:\n"
        "  - STRIDE analysis\n"
        "  - OWASP\n"
        "---\n"
    )
    fm = scan_mod.parse_frontmatter(_write(tmp_path, body))
    assert fm == {"name": "senior-security", "description": "Security toolkit"}
