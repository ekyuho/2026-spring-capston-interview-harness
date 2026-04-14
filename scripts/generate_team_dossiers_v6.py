from __future__ import annotations

import re
from pathlib import Path

import generate_team_dossiers_v2 as base
from generate_team_dossiers_v5 import format_supplement_text

ROOT = Path(__file__).resolve().parents[1]
ADVISOR_REPORT_PATH = ROOT / "data" / "normalized" / "advisor_interview_reports.md"


def load_advisor_reports() -> dict[str, str]:
    if not ADVISOR_REPORT_PATH.exists():
        return {}

    text = ADVISOR_REPORT_PATH.read_text(encoding="utf-8")
    pattern = re.compile(r"^## Team\s+(\d{1,2})[:：].*$", flags=re.MULTILINE)
    matches = list(pattern.finditer(text))

    reports: dict[str, str] = {}
    for idx, match in enumerate(matches):
        team_no = match.group(1).zfill(2)
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        body = re.sub(r"\n?---\n?$", "", body).strip()
        reports[team_no] = body or "_면담보고서 내용 없음_"

    return reports


def render_team_dossier(context: dict) -> str:
    supplement_summary = format_supplement_text(context.get("supplement_summary", ""))
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
    original_render = render_team_dossier

    def render_with_advisor(context: dict) -> str:
        team_no = str(context.get("team_no", "")).zfill(2)
        context = {**context, "advisor_report": advisor_reports.get(team_no, "")}
        return original_render(context)

    base.render_team_dossier = render_with_advisor
    base.main()


if __name__ == "__main__":
    main()
