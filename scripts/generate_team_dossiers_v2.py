from __future__ import annotations

import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"
RAW_DIR = ROOT / "data" / "raw"
OUTPUT_DIR = ROOT / "data" / "output"
COLUMN_MAP_PATH = CONFIG_DIR / "column_map.yaml"


def ensure_dirs() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def normalize_team_no(value: Any) -> str:
    if pd.isna(value):
        return ""
    text = str(value).strip()
    text = re.sub(r"^(Team|team|팀)\s*", "", text).strip()
    m = re.search(r"\d+", text)
    return m.group(0).zfill(2) if m else ""


def normalize_name(value: Any) -> str:
    if pd.isna(value):
        return ""
    text = unicodedata.normalize("NFC", str(value).strip())
    return re.sub(r"\s+", "", text)


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


def row_to_bullets(row: pd.Series, columns: list[str]) -> str:
    lines: list[str] = []
    for col in columns:
        if col not in row.index:
            continue
        value = row.get(col, "")
        if pd.isna(value) or str(value).strip() == "":
            continue
        lines.append(f"- **{col}**: {str(value).strip()}")
    return "\n".join(lines)


def parse_project_briefs(markdown: str) -> dict[str, dict[str, Any]]:
    teams: dict[str, dict[str, Any]] = {}
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

        heading_tail = re.sub(r"^Team\s+\d+\s*[-–:]?\s*", "", title_line, flags=re.IGNORECASE).strip()
        teams[team_no] = {
            "team_no": team_no,
            "team_name": heading_tail if heading_tail != title_line else f"Team {team_no}",
            "track": extract_first(section, [r"트랙\s*[:：]\s*(.+)", r"Track\s*[:：]\s*(.+)"]),
            "project_title": extract_first(section, [r"프로젝트명\s*[:：]\s*(.+)", r"주제\s*[:：]\s*(.+)"]),
            "members": extract_first(section, [r"팀구성\s*[:：]\s*(.+)", r"팀원\s*[:：]\s*(.+)", r"Members\s*[:：]\s*(.+)"]),
            "advisor": extract_first(section, [r"지도교수\s*[:：]\s*(.+)"]),
            "github_repo": extract_first(section, [r"https://github\.com/[^\s)]+", r"GitHub\s*[:：]\s*(.+)"]),
            "project_summary": section,
        }
    return teams


def extract_first(text: str, patterns: list[str]) -> str:
    for pattern in patterns:
        m = re.search(pattern, text, flags=re.IGNORECASE)
        if m:
            return m.group(1).strip() if m.lastindex else m.group(0).strip()
    return ""


def build_member_team_lookup(teams: dict[str, dict[str, Any]]) -> dict[str, str]:
    lookup: dict[str, str] = {}
    for team_no, info in teams.items():
        members = str(info.get("members", ""))
        for token in re.split(r"[,/·\n]|\s{2,}", members):
            token = re.sub(r"\([^)]*\)", "", token).strip()
            key = normalize_name(token)
            if len(key) >= 2:
                lookup[key] = team_no
    return lookup


def collect_team_rows(df: pd.DataFrame, mapping: dict[str, Any], unresolved: list[str], label: str) -> dict[str, list[str]]:
    team_col = mapping.get("team_no", "")
    columns = mapping.get("content_columns", []) or []
    found_cols = [c for c in columns if c in df.columns]
    missing_cols = [c for c in columns if c not in df.columns]
    if missing_cols:
        unresolved.append(f"## {label}: 누락 컬럼\n" + "\n".join(f"- `{c}`" for c in missing_cols) + "\n")
    if team_col not in df.columns:
        unresolved.append(f"## {label}: 팀번호 컬럼 없음\n- 지정값: `{team_col}`\n")
        return {}

    result: dict[str, list[str]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    for idx, row in df.iterrows():
        team_no = normalize_team_no(row.get(team_col, ""))
        body = row_to_bullets(row, found_cols)
        if not team_no:
            unresolved.append(f"## {label}: 팀번호 없음\n- row: {idx + 2}\n")
            continue
        if not body:
            continue
        key = (team_no, body)
        if key in seen:
            continue
        seen.add(key)
        result[team_no].append(body)
    return result


def collect_member_rows(df: pd.DataFrame, mapping: dict[str, Any], member_team_lookup: dict[str, str], unresolved: list[str], label: str) -> dict[str, list[dict[str, str]]]:
    name_col = mapping.get("student_name", "")
    team_col = mapping.get("team_no", "")
    columns = mapping.get("content_columns", []) or []
    found_cols = [c for c in columns if c in df.columns]
    missing_cols = [c for c in columns if c not in df.columns]

    if missing_cols:
        unresolved.append(f"## {label}: 누락 컬럼\n" + "\n".join(f"- `{c}`" for c in missing_cols) + "\n")
    if name_col not in df.columns:
        unresolved.append(f"## {label}: 학생 이름 컬럼 없음\n- 지정값: `{name_col}`\n")
        return {}

    result: dict[str, list[dict[str, str]]] = defaultdict(list)
    seen: set[tuple[str, str, str]] = set()

    for idx, row in df.iterrows():
        display_name = str(row.get(name_col, "")).strip()
        name_key = normalize_name(display_name)
        if not name_key:
            unresolved.append(f"## {label}: 학생 이름 없음\n- row: {idx + 2}\n")
            continue

        team_no = normalize_team_no(row.get(team_col, "")) if team_col in df.columns else ""
        if not team_no:
            team_no = member_team_lookup.get(name_key, "")
        if not team_no:
            unresolved.append(f"## {label}: 팀 매핑 실패\n- row: {idx + 2}\n- name: `{display_name}`\n")
            continue

        body = row_to_bullets(row, found_cols)
        if not body:
            unresolved.append(f"## {label}: 출력할 내용 없음\n- row: {idx + 2}\n- name: `{display_name}`\n- 원인: column_map.yaml의 content_columns가 실제 컬럼명과 다를 가능성이 큼\n")
            continue

        key = (team_no, name_key, body)
        if key in seen:
            continue
        seen.add(key)
        result[team_no].append({"name": display_name, "content": body})

    return result


def join_blocks(blocks: list[str]) -> str:
    return "\n\n".join(b for b in blocks if b).strip()


def render_member_section(items: list[dict[str, str]], empty_message: str) -> str:
    if not items:
        return empty_message
    blocks = []
    for item in items:
        blocks.append(f"### {item['name']}\n\n{item['content']}")
    return "\n\n".join(blocks)


def render_team_dossier(context: dict[str, Any]) -> str:
    return f"""# Team {context['team_no']}. {context['team_name']} 심층인터뷰 준비서

## 1. 프로젝트 개요

- 트랙: {context.get('track', '')}
- 프로젝트명: {context.get('project_title', '')}
- 팀원: {context.get('members', '')}
- 지도교수: {context.get('advisor', '')}
- GitHub Repo: {context.get('github_repo', '')}

## 2. 만들고자 하는 것

{context.get('project_summary', '정리 필요')}

## 3. 사전 보충자료 요약

{context.get('supplement_summary') or '자료 없음 또는 정리 필요'}

## 4. 팀원별 학기초 개인설문

{render_member_section(context.get('member_surveys', []), '자료 없음 또는 column_map.yaml 보정 필요')}

## 5. 개인별 5 Questions

{render_member_section(context.get('five_questions', []), '자료 없음 또는 column_map.yaml 보정 필요')}

## 6. 기반 소프트웨어 리스트

{context.get('base_software') or '자료 없음 또는 정리 필요'}

## 7. 인터뷰에서 확인할 핵심 쟁점

- 문제 정의가 충분히 좁혀졌는가?
- 학기말 산출물이 실제 구현 가능한 형태로 정의되어 있는가?
- 핵심 기술 검증 계획이 있는가?
- 팀원별 역할과 책임이 명확한가?
- GitHub repo와 실제 개발 진도가 일치하는가?

## 8. 교수자용 질문 초안

1. 이 프로젝트에서 학기말에 반드시 보여줄 수 있어야 하는 최소 산출물은 무엇인가?
2. 현재 가장 불확실한 기술 요소는 무엇이며, 언제까지 검증할 계획인가?
3. 팀원별 구현 책임은 어떻게 나뉘어 있는가?
4. 기존 서비스나 연구와 비교했을 때 차별점은 무엇인가?
5. 실패 가능성이 가장 높은 지점은 어디이며, 대안은 무엇인가?
"""


def main() -> None:
    ensure_dirs()
    column_map = load_yaml(COLUMN_MAP_PATH)
    unresolved: list[str] = ["# 병합 실패 및 확인 필요 항목\n"]

    teams = parse_project_briefs(read_markdown_raw("project_brief"))
    if not teams:
        unresolved.append("## project_brief: 팀 섹션 파싱 실패\n")
    member_team_lookup = build_member_team_lookup(teams)

    supplement_by_team = collect_team_rows(read_csv_raw("supplement"), column_map.get("supplement", {}), unresolved, "supplement")
    base_software_by_team = collect_team_rows(read_csv_raw("base_software"), column_map.get("base_software", {}), unresolved, "base_software")
    survey_by_team = collect_member_rows(read_csv_raw("initial_survey"), column_map.get("initial_survey", {}), member_team_lookup, unresolved, "initial_survey")
    questions_by_team = collect_member_rows(read_csv_raw("five_questions"), column_map.get("five_questions", {}), member_team_lookup, unresolved, "five_questions")

    generated = 0
    for team_no in sorted(teams):
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
        output_name = f"team-{team_no}-{safe_filename(team_name)}.md"
        (OUTPUT_DIR / output_name).write_text(render_team_dossier(context), encoding="utf-8")
        generated += 1

    unresolved.append(f"\n## 생성 결과\n- team dossier files: {generated}\n")
    (OUTPUT_DIR / "unresolved.md").write_text("\n".join(unresolved), encoding="utf-8")
    print(f"Generated {generated} team dossier files in {OUTPUT_DIR}")
    print(f"Wrote {OUTPUT_DIR / 'unresolved.md'}")


if __name__ == "__main__":
    main()
