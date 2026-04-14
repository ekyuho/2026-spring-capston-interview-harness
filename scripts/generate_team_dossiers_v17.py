from __future__ import annotations

import re

import generate_team_dossiers_v16 as v16

SURVEY_GUIDE_PATTERNS = [
    re.compile(r"^\s*본인의\s*기술적\s*관심영역,\s*실제로\s*만들어서\s*작동시켜본\s*산출물,\s*남보다\s*잘한다고\s*생각되는\s*영역\s*등\s*소개\s*:\s*", flags=re.IGNORECASE),
    re.compile(r"^\s*-\s*\*\*본인의\s*기술적\s*관심영역,\s*실제로\s*만들어서\s*작동시켜본\s*산출물,\s*남보다\s*잘한다고\s*생각되는\s*영역\s*등\s*소개\*\*\s*:\s*", flags=re.IGNORECASE),
    re.compile(r"\n\s*본인의\s*기술적\s*관심영역,\s*실제로\s*만들어서\s*작동시켜본\s*산출물,\s*남보다\s*잘한다고\s*생각되는\s*영역\s*등\s*소개\s*:\s*", flags=re.IGNORECASE),
    re.compile(r"\n\s*-\s*\*\*본인의\s*기술적\s*관심영역,\s*실제로\s*만들어서\s*작동시켜본\s*산출물,\s*남보다\s*잘한다고\s*생각되는\s*영역\s*등\s*소개\*\*\s*:\s*", flags=re.IGNORECASE),
]


def clean_survey_prefix(content: str) -> str:
    content = content.strip()
    for pattern in SURVEY_GUIDE_PATTERNS:
        content = pattern.sub("\n" if pattern.pattern.startswith("\\n") else "", content)
    return content.strip()


def normalize_member_surveys(items: list[dict[str, str]]) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    for item in items:
        content = clean_survey_prefix(item.get("content", ""))
        normalized.append({**item, "content": content})
    return normalized


def render_member_section_clean(items: list[dict[str, str]], empty_message: str) -> str:
    if not items:
        return empty_message
    blocks = []
    for item in items:
        content = item.get("content", "").strip()
        blocks.append(f"### {item['name']}\n\n{content}")
    return "\n\n".join(blocks)


def render_team_dossier(context: dict) -> str:
    context = {
        **context,
        "member_surveys": normalize_member_surveys(context.get("member_surveys", [])),
        "five_questions": v16.normalize_five_questions(context.get("five_questions", [])),
    }

    supplement_summary = v16.v15.v14.v8.format_supplement_text_v8(context.get("supplement_summary", ""))
    supplement_summary = __import__("generate_team_dossiers_v7").tune_github_section(supplement_summary)
    advisor_report = context.get("advisor_report", "") or "자료 없음 또는 PDF 추출 필요"
    base_software = v16.v15.v14.format_base_software(context.get("base_software", ""))

    return f"""# Team {context['team_no']}. {context['team_name']} 심층인터뷰 준비서

## 1. 만들고자 하는 것

{context.get('project_summary', '정리 필요')}

## 2. 사전 보충자료 요약

{supplement_summary}

## 3. 팀지도교수 면담보고서

{advisor_report}

## 4. 팀원별 학기초 개인설문

{render_member_section_clean(context.get('member_surveys', []), '자료 없음 또는 column_map.yaml 보정 필요')}

## 5. 개인별 5 Questions

{v16.v15.render_member_section_clean(context.get('five_questions', []), '자료 없음 또는 column_map.yaml 보정 필요')}

## 6. 기반 소프트웨어 리스트

{base_software}

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


if __name__ == "__main__":
    from generate_team_dossiers_v6 import load_advisor_reports

    advisor_reports = load_advisor_reports()
    v16.v15.v14.v8.split_sentences_korean = v16.v15.v14.split_sentences_korean_fixed
    v16.v15.v14.v8.format_field_block_v8 = v16.v15.v14.format_field_block_v14

    def render_with_advisor(context: dict) -> str:
        team_no = str(context.get("team_no", "")).zfill(2)
        context = {**context, "advisor_report": advisor_reports.get(team_no, "")}
        return render_team_dossier(context)

    v16.v15.v14.v8.base.render_team_dossier = render_with_advisor
    v16.v15.v14.v8.base.main()
