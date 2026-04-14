from __future__ import annotations

import re

import generate_team_dossiers_v15 as v15

QUESTION_GUIDE_PATTERNS = [
    re.compile(r"^\s*질문당\s*한줄씩\s*5개의\s*질문\s*:\s*", flags=re.IGNORECASE),
    re.compile(r"^\s*-\s*\*\*질문당\s*한줄씩\s*5개의\s*질문\*\*\s*:\s*", flags=re.IGNORECASE),
    re.compile(r"\n\s*질문당\s*한줄씩\s*5개의\s*질문\s*:\s*", flags=re.IGNORECASE),
    re.compile(r"\n\s*-\s*\*\*질문당\s*한줄씩\s*5개의\s*질문\*\*\s*:\s*", flags=re.IGNORECASE),
]


def clean_question_prefix(content: str) -> str:
    content = content.strip()
    for pattern in QUESTION_GUIDE_PATTERNS:
        content = pattern.sub("\n" if pattern.pattern.startswith("\\n") else "", content)
    return content.strip()


def normalize_five_questions(items: list[dict[str, str]]) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    for item in items:
        content = clean_question_prefix(item.get("content", ""))
        normalized.append({**item, "content": content})
    return normalized


if __name__ == "__main__":
    v15.normalize_five_questions = normalize_five_questions
    v15.QUESTION_GUIDE_PATTERN = re.compile(r"a^")  # disable old single-pattern cleaner
    v15.__dict__["normalize_five_questions"] = normalize_five_questions

    from generate_team_dossiers_v6 import load_advisor_reports

    advisor_reports = load_advisor_reports()
    v15.v14.v8.split_sentences_korean = v15.v14.split_sentences_korean_fixed
    v15.v14.v8.format_field_block_v8 = v15.v14.format_field_block_v14

    def render_with_advisor(context: dict) -> str:
        team_no = str(context.get("team_no", "")).zfill(2)
        context = {**context, "advisor_report": advisor_reports.get(team_no, "")}
        return v15.render_team_dossier(context)

    v15.v14.v8.base.render_team_dossier = render_with_advisor
    v15.v14.v8.base.main()
