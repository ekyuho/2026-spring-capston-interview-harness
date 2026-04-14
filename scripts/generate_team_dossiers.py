from __future__ import annotations

import io
import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any

import pandas as pd
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"
RAW_DIR = ROOT / "data" / "raw"
OUTPUT_DIR = ROOT / "data" / "output"
TEMPLATE_DIR = ROOT / "templates"

SOURCES_PATH = CONFIG_DIR / "sources.yaml"
COLUMN_MAP_PATH = CONFIG_DIR / "column_map.yaml"


def ensure_dirs() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def normalize_team_no(value: Any, zero_pad: int = 2) -> str:
    if pd.isna(value):
        return ""
    text = str(value).strip()
    text = re.sub(r"^(Team|team|팀)\s*", "", text).strip()
    match = re.search(r"\d+", text)
    if not match:
        return ""
    return match.group(0).zfill(zero_pad)


def normalize_name(value: Any) -> str:
    if pd.isna(value):
        return ""
    text = unicodedata.normalize("NFC", str(value).strip())
    text = re.sub(r"\s+", "", text)
    return text


def safe_filename(value: str) -> str:
    value = re.sub(r"[^0-9A-Za-z가-힣._-]+", "_", value.strip())
    return value.strip("_") or "team"


def read_csv_raw(source_key: str) -> pd.DataFrame:
    path = RAW_DIR / f"{source_key}.csv"
    if not path.exists():
        raise FileNotFoundError(f"Missing raw CSV: {path}. 먼저 scripts/fetch_debug_columns.py를 실행하세요.")
    return pd.read_csv(path, encoding="utf-8-sig")


def read_markdown_raw(source_key: str) -> str:
    path = RAW_DIR / f"{source_key}.md"
    if not path.exists():
        raise FileNotFoundError(f"Missing raw markdown: {path}. 먼저 scripts/fetch_debug_columns.py를 실행하세요.")
    return path.read_text(encoding="utf-8")


def existing_columns(df: pd.DataFrame, columns: list[str]) -> tuple[list[str], list[str]]:
    existing = [col for col in columns if col in df.columns]
    missing = [col for col in columns if col not in df.columns]
    return existing, missing


def row_to_bullets(row: pd.Series, columns: list[str]) -> str:
    lines: list[str] = []
    for col in columns:
        value = row.get(col, "")
        if pd.isna(value) or str(value).strip() == "":
            continue
        lines.append(f"- **{col}**: {str(value).strip()}")
    return "\n".join(lines) if lines else ""


def parse_project_briefs(markdown: str) -> dict[str, dict[str, Any]]:
    """Best-effort parser for Team sections in project briefs markdown."""
    teams: dict[str, dict[str, Any]] = {}

    # Split at headings containing Team N. Supports '# Team 1', '## Team 1', etc.
    pattern = re.compile(r"(?m)^(#{1,6}\s*)?(Team\s+\d+[^\n]*)")
    matches = list(pattern.finditer(markdown))

    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(markdown)
        section = markdown[start:end].strip()
        title_line = match.group(2).strip()
        team_no = normalize_team_no(title_line)
        if not team_no:
            continue

        info: dict[str, Any] = {
            "team_no": team_no,
            "team_name": "",
            "track": "",
            "project_title": "",
            "members": "",
            "advisor": "",
            "github_repo": "",
            "project_summary": section,
        }

        # Extract common bullet/table-like fields. This is intentionally permissive.
        field_patterns = {
            "team_name": [r"팀명\s*[:：]\s*(.+)", r"Team\s+\d+\s*[-–:]\s*(.+)"],
            "track": [r"트랙\s*[:：]\s*(.+)", r"Track\s*[:：]\s*(.+)"],
            "project_title": [r"프로젝트명\s*[:：]\s*(.+)", r"Project\s*Name\s*[:：]\s*(.+)", r"주제\s*[:：]\s*(.+)"],
            "members": [r"팀구성\s*[:：]\s*(.+)", r"팀원\s*[:：]\s*(.+)", r"Members\s*[:：]\s*(.+)"],
            "advisor": [r"지도교수\s*[:：]\s*(.+)", r"Advisor\s*[:：]\s*(.+)"],
            "github_repo": [r"GitHub\s*Repo\s*[:：]\s*(.+)", r"GitHub\s*[:：]\s*(.+)", r"https://github\.com/[^\s)]+"],
        }

        for field, patterns in field_patterns.items():
            for p in patterns:
                m = re.search(p, section, flags=re.IGNORECASE)
                if m:
                    info[field] = m.group(1).strip() if m.lastindex else m.group(0).strip()
                    break

        if not info["team_name"]:
            # Use heading tail as fallback if available.
            heading_tail = re.sub(r"^Team\s+\d+\s*[-–:]?\s*", "", title_line, flags=re.IGNORECASE).strip()
            if heading_tail and heading_tail != title_line:
                info["team_name"] = heading_tail

        teams[team_no] = info

    return teams


def collect_team_rows(
    df: pd.DataFrame,
    mapping: dict[str, Any],
    unresolved: list[str],
    source_label: str,
) -> dict[str, list[str]]:
    team_col = mapping.get("team_no", "")
    columns = mapping.get("content_columns", []) or []
    found_cols, missing_cols = existing_columns(df, columns)

    if missing_cols:
        unresolved.append(f"## {source_label}: 누락 컬럼\n" + "\n".join(f"- `{c}`" for c in missing_cols) + "\n")

    if not team_col or team_col not in df.columns:
        unresolved.append(f"## {source_label}: 팀번호 컬럼 없음\n- 지정값: `{team_col}`\n")
        return {}

    result: dict[str, list[str]] = defaultdict(list)
    for idx, row in df.iterrows():
        team_no = normalize_team_no(row.get(team_col, ""))
        if not team_no:
            unresolved.append(f"## {source_label}: 팀번호 없음\n- row: {idx + 2}\n")
            continue
        body = row_to_bullets(row, found_cols)
        if body:
            result[team_no].append(body)
    return result


def collect_member_rows(
    df: pd.DataFrame,
    mapping: dict[str, Any],
    member_team_lookup: dict[str, str],
    unresolved: list[str],
    source_label: str,
) -> dict[str, list[dict[str, str]]]:
    name_col = mapping.get("student_name", "")
    team_col = mapping.get("team_no", "")
    columns = mapping.get("content_columns", []) or []
    found_cols, missing_cols = existing_columns(df, columns)

    if missing_cols:
        unresolved.append(f"## {source_label}: 누락 컬럼\n" + "\n".join(f"- `{c}`" for c in missing_cols) + "\n")

    if not name_col or name_col not in df.columns:
        unresolved.append(f"## {source_label}: 학생 이름 컬럼 없음\n- 지정값: `{name_col}`\n")
        return {}

    result: dict[str, list[dict[str, str]]] = defaultdict(list)

    for idx, row in df.iterrows():
        display_name = str(row.get(name_col, "")).strip()
        name_key = normalize_name(display_name)
        if not name_key:
            unresolved.append(f"## {source_label}: 학생 이름 없음\n- row: {idx + 2}\n")
            continue

        team_no = ""
        if team_col and team_col in df.columns:
            team_no = normalize_team_no(row.get(team_col, ""))
        if not team_no:
            team_no = member_team_lookup.get(name_key, "")

        if not team_no:
            unresolved.append(f"## {source_label}: 팀 매핑 실패\n- row: {idx + 2}\n- name: `{display_name}`\n")
            continue

        item = {
            "name": display_name,
            "content": row_to_bullets(row, found_cols),
            "questions": row_to_bullets(row, found_cols),
            "interests": str(row.get("관심 기술", "")).strip() if "관심 기술" in df.columns else "",
            "strengths": str(row.get("잘하는 것", "")).strip() if "잘하는 것" in df.columns else "",
            "concerns": str(row.get("걱정되는 것", "")).strip() if "걱정되는 것" in df.columns else "",
            "preferred_role": str(row.get("희망 역할", "")).strip() if "희망 역할" in df.columns else "",
        }
        result[team_no].append(item)

    return result


def build_member_team_lookup(teams: dict[str, dict[str, Any]]) -> dict[str, str]:
    lookup: dict[str, str] = {}
    for team_no, info in teams.items():
        members = str(info.get("members", ""))
        # Split common separators. Korean names are usually 2-4 chars; this is best-effort.
        tokens = re.split(r"[,/·\n]|\s{2,}", members)
        for token in tokens:
            token = token.strip()
            if not token:
                continue
            # Remove labels or parenthesized roles.
            token = re.sub(r"\([^)]*\)", "", token).strip()
            key = normalize_name(token)
            if len(key) >= 2:
                lookup[key] = team_no
    return lookup


def join_blocks(blocks: list[str]) -> str:
    return "\n\n".join(blocks).strip()


def main() -> None:
    ensure_dirs()
    column_map = load_yaml(COLUMN_MAP_PATH)
    unresolved: list[str] = ["# 병합 실패 및 확인 필요 항목\n"]

    project_text = read_markdown_raw("project_brief")
    teams = parse_project_briefs(project_text)

    if not teams:
        unresolved.append("## project_brief: 팀 섹션 파싱 실패\n- `data/raw/project_brief.md`의 Team heading 형식을 확인하세요.\n")

    member_team_lookup = build_member_team_lookup(teams)

    # Team-level sources
    supplement_by_team: dict[str, list[str]] = {}
    base_software_by_team: dict[str, list[str]] = {}

    if "supplement" in column_map:
        supplement_df = read_csv_raw("supplement")
        supplement_by_team = collect_team_rows(supplement_df, column_map["supplement"], unresolved, "supplement")

    if "base_software" in column_map:
        base_df = read_csv_raw("base_software")
        base_software_by_team = collect_team_rows(base_df, column_map["base_software"], unresolved, "base_software")

    # Member-level sources
    survey_by_team: dict[str, list[dict[str, str]]] = {}
    questions_by_team: dict[str, list[dict[str, str]]] = {}

    if "initial_survey" in column_map:
        survey_df = read_csv_raw("initial_survey")
        survey_by_team = collect_member_rows(
            survey_df,
            column_map["initial_survey"],
            member_team_lookup,
            unresolved,
            "initial_survey",
        )

    if "five_questions" in column_map:
        questions_df = read_csv_raw("five_questions")
        questions_by_team = collect_member_rows(
            questions_df,
            column_map["five_questions"],
            member_team_lookup,
            unresolved,
            "five_questions",
        )

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=False,
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("team_dossier.md.j2")

    generated = 0
    for team_no in sorted(teams.keys()):
        info = teams[team_no]
        team_name = info.get("team_name") or f"Team {team_no}"
        context = {
            **info,
            "team_no": team_no,
            "team_name": team_name,
            "supplement_summary": join_blocks(supplement_by_team.get(team_no, [])),
            "base_software": join_blocks(base_software_by_team.get(team_no, [])),
            "member_surveys": survey_by_team.get(team_no, []),
            "five_questions": questions_by_team.get(team_no, []),
        }
        rendered = template.render(**context)
        output_name = f"team-{team_no}-{safe_filename(team_name)}.md"
        (OUTPUT_DIR / output_name).write_text(rendered, encoding="utf-8")
        generated += 1

    unresolved.append(f"\n## 생성 결과\n- team dossier files: {generated}\n")
    (OUTPUT_DIR / "unresolved.md").write_text("\n".join(unresolved), encoding="utf-8")

    print(f"Generated {generated} team dossier files in {OUTPUT_DIR}")
    print(f"Wrote {OUTPUT_DIR / 'unresolved.md'}")


if __name__ == "__main__":
    main()
