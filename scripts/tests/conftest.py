"""Shared fixtures: load the hyphenated script files as Python modules."""

import importlib.util
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent.parent


def _load(filename: str, module_name: str):
    spec = importlib.util.spec_from_file_location(
        module_name, SCRIPTS_DIR / filename
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="session")
def scan_mod():
    return _load("scan-all-skills.py", "scan_all_skills")


@pytest.fixture(scope="session")
def build_mod():
    return _load("build-registry.py", "build_registry")
