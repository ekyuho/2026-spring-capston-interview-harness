from __future__ import annotations

from generate_team_dossiers_v2 import *  # noqa: F403,F401


def render_team_dossier(context: dict) -> str:
    return f"""# Team {context['team_no']}. {context['team_name']} 심층인터뷰 준비서

## 1. 만들고자 하는 것

{context.get('project_summary', '정리 필요')}

## 2. 사전 보충자료 요약

{context.get('supplement_summary') or '자료 없음 또는 정리 필요'}

## 3. 팀원별 학기초 개인설문

{render_member_section(context.get('member_surveys', []), '자료 없음 또는 column_map.yaml 보정 필요')}

## 4. 개인별 5 Questions

{render_member_section(context.get('five_questions', []), '자료 없음 또는 column_map.yaml 보정 필요')}

## 5. 기반 소프트웨어 리스트

{context.get('base_software') or '자료 없음 또는 정리 필요'}

## 6. 인터뷰에서 확인할 핵심 쟁점

- 문제 정의가 충분히 좁혀졌는가?
- 학기말 산출물이 실제 구현 가능한 형태로 정의되어 있는가?
- 핵심 기술 검증 계획이 있는가?
- 팀원별 역할과 책임이 명확한가?
- GitHub repo와 실제 개발 진도가 일치하는가?

## 7. 교수자용 질문 초안

1. 이 프로젝트에서 학기말에 반드시 보여줄 수 있어야 하는 최소 산출물은 무엇인가?
2. 현재 가장 불확실한 기술 요소는 무엇이며, 언제까지 검증할 계획인가?
3. 팀원별 구현 책임은 어떻게 나뉘어 있는가?
4. 기존 서비스나 연구와 비교했을 때 차별점은 무엇인가?
5. 실패 가능성이 가장 높은 지점은 어디이며, 대안은 무엇인가?
"""


if __name__ == "__main__":
    main()
