from __future__ import annotations

import re
from pathlib import Path

import generate_team_dossiers_v2 as base
from generate_team_dossiers_v5 import format_supplement_text
from generate_team_dossiers_v6 import load_advisor_reports

GITHUB_CHECK_ITEMS = [
    "Class Repo의 Project Description의 내용은 최신상태로 PR되어있습니까?",
    "팀 Project Repo는 제3자가 검색해서 들어오게되었을때, 구조 이해에 도움이 되도록 Readme.MD 에 내용 정리해 두었습니까?",
    "팀 Project Repo의 폴더 구성은 통상 오픈소스 구성처럼 잘 구조화 되어있습니까?",
    "팀 Project Repo에 PR해가면서 공동작업을 github 활용하고 있습니까?",
    "데모한 모든 코드/데이타 등은 팀 Project Repo에 다 올라가 있습니까?",
]


def normalize_check_text(text: str) -> str:
    text = re.sub(r"\s+", "", text)
    text = text.replace("??", "?")
    return text


def tune_github_section(markdown: str) -> str:
    heading = "github 관련:"
    if heading not in markdown:
        return markdown

    pattern = re.compile(
        r"github 관련:\n(?P<body>.*?)(?=\n\n[^\n]+:\n|\Z)",
        flags=re.DOTALL,
    )
    match = pattern.search(markdown)
    if not match:
        return markdown

    body = match.group("body")
    normalized_body = normalize_check_text(body)

    missing: list[str] = []
    for item in GITHUB_CHECK_ITEMS:
        if normalize_check_text(item) not in normalized_body:
            missing.append(item)

    if not missing:
        replacement = "github 관련:\n- all ok"
    else:
        replacement = "github 관련:\n" + "\n".join(f"- {item} -- 누락" for item in missing)

    return markdown[: match.start()] + replacement + markdown[match.end() :]


def render_team_dossier(context: dict) -> str:
    supplement_summary = format_supplement_text(context.get("supplement_summary", ""))
    supplement_summary = tune_github_section(supplement_summary)
    advisor_report = context.get("advisor_report", "") or "자료 없음 또는 PDF 추출 필요"

    return f"""# Team {context['team_no']}. {context['team_name']} 심층인터뷰 준비서

## 1. 만들고자 하는 것

{context.get('project_summary', '정리 필요')}

## 2. 사전 보충자료 요약

{supplement_summary}

## 3. 팀지도교수 면담보고서

{advisor_report}

## 4. 팀원별 학기초 개인설문

{base.render_member_section(context.get('member_surveys', []), '자료 없음 또는 column_map.yaml 보정 필요')}

## 5. 개인별 5 Questions

{base.render_member_section(context.get('five_questions', []), '자료 없음 또는 column_map.yaml 보정 필요')}

## 6. 기반 소프트웨어 리스트

{context.get('base_software') or '자료 없음 또는 정리 필요'}

## 7. 인터뷰에서 확인할 핵심 쟁점

- 문제 정의가 충분히 좁혀졌는가?
- 학기말 산출물이 실제 구현 가능한 형태로 정의되어 있는가?
- 핵심 기술 검증 계획이 있는가?
- 팀원별 역할과 책임이 명확한가?
- GitHub repo와 실제 개발 진도가 일치하는가?
- 지도교수 면담 내용과 현재 프로젝트 방향이 일치하는가?

## 8. 교수자용 질문 초안

1. 이 프로젝트에서 학기말에 반드시 보여줄 수 있어야 하는 최소 산출물은 무엇인가?
2. 현재 가장 불확실한 기술 요소는 무엇이며, 언제까지 검증할 계획인가?
3. 팀원별 구현 책임은 어떻게 나뉘어 있는가?
4. 기존 서비스나 연구와 비교했을 때 차별점은 무엇인가?
5. 지도교수 면담 이후 프로젝트 방향이 어떻게 수정되었는가?
6. 실패 가능성이 가장 높은 지점은 어디이며, 대안은 무엇인가?
"""


def main() -> None:
    advisor_reports = load_advisor_reports()

    def render_with_advisor(context: dict) -> str:
        team_no = str(context.get("team_no", "")).zfill(2)
        context = {**context, "advisor_report": advisor_reports.get(team_no, "")}
        return render_team_dossier(context)

    base.render_team_dossier = render_with_advisor
    base.main()


if __name__ == "__main__":
    main()
