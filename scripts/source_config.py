from __future__ import annotations

from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "sources.yaml"


def load_config() -> dict[str, Any]:
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_sources() -> dict[str, dict[str, Any]]:
    config = load_config()
    return config.get("sources", {})


def get_source(source_key: str) -> dict[str, Any]:
    sources = load_sources()
    try:
        return sources[source_key]
    except KeyError as exc:
        available = ", ".join(sorted(sources))
        raise KeyError(f"source '{source_key}' not found in sources.yaml. available: {available}") from exc


def github_raw_url_to_repo_relative_path(raw_url_or_base_url: str) -> Path:
    parsed = urlparse(raw_url_or_base_url)
    if parsed.netloc != "raw.githubusercontent.com":
        raise ValueError(f"raw.githubusercontent.com URL expected, got: {raw_url_or_base_url}")

    # /owner/repo/ref/path/to/file-or-dir
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 4:
        raise ValueError(f"unexpected GitHub raw URL shape: {raw_url_or_base_url}")

    repo_relative_parts = parts[3:]
    return Path(*repo_relative_parts)


def resolve_github_pdf_folder_local_path(source_key: str = "advisor_interview_reports") -> Path:
    source = get_source(source_key)
    if source.get("type") != "github_pdf_folder":
        raise ValueError(f"source '{source_key}' must have type github_pdf_folder")

    base_url = source["base_url"]
    repo_relative_path = github_raw_url_to_repo_relative_path(base_url)
    return ROOT / repo_relative_path


def pdf_extension_for_source(source_key: str = "advisor_interview_reports") -> str:
    source = get_source(source_key)
    match_rule = source.get("match_rule", {})
    return str(match_rule.get("file_extension", ".pdf"))


def team_prefix_digits_for_source(source_key: str = "advisor_interview_reports") -> int:
    source = get_source(source_key)
    match_rule = source.get("match_rule", {})
    return int(match_rule.get("team_no_from_filename_prefix", 2))
