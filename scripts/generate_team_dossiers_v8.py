from __future__ import annotations

import re

import generate_team_dossiers_v2 as base
from generate_team_dossiers_v6 import load_advisor_reports
from generate_team_dossiers_v7 import GITHUB_CHECK_ITEMS, normalize_check_text, tune_github_section

RR_TITLE = "본 프로젝트에 있어서 팀원별 R&R(Role & Responsibility):"


def split_sentences_korean(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    # 문장 종결 어미 뒤 공백 기준으로 분리. 괄호/영문 약어는 건드리지 않음.
    parts = re.split(r"(?<=[.!?]|다\.|요\.|임\.|함\.)\s+", text)
    return [p.strip() for p in parts if p.strip()]


def format_rr_items(body: str) -> str:
    # '- 설영은: ...' 또는 '설영은: ... 신지민: ...' 모두 처리
    compact = body.replace("\r\n", "\n").replace("\r", "\n")
    compact = re.sub(r"\n+-\s*", "\n", compact)
    compact = re.sub(r"^[-\s]+", "", compact.strip())

    matches = list(re.finditer(r"([가-힣]{2,4})\s*[:：]", compact))
    if not matches:
        return body.strip()

    blocks: list[str] = []
    for idx, match in enumerate(matches):
        name = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(compact)
        role_text = compact[start:end].strip(" \n-:")
        sentences = split_sentences_korean(role_text)
        if sentences:
            blocks.append(f"- **{name}**")
            blocks.extend(f"  - {sentence}" for sentence in sentences)
        else:
            blocks.append(f"- **{name}**")
    return "\n".join(blocks)


def format_supplement_text_v8(text: str) -> str:
    if not text:
        return "자료 없음 또는 정리 필요"

    blocks: list[str] = []
    current_title: str | None = None
    current_body: list[str] = []

    for line in text.splitlines():
        m = re.match(r"^- \*\*(.+?)\*\*: (.*)$", line)
        if m:
            if current_title is not None:
                blocks.append(format_field_block_v8(current_title, "\n".join(current_body)))
            current_title = m.group(1).strip()
            current_body = [m.group(2).strip()]
        else:
            current_body.append(line.rstrip())

    if current_title is not None:
        blocks.append(format_field_block_v8(current_title, "\n".join(current_body)))

    return "\n\n".join(blocks) if blocks else text


def format_field_block_v8(title: str, body: str) -> str:
    title_line = f"{title}:"
    body = body.strip()
    if not body:
        return title_line

    if title_line == RR_TITLE:
        return f"{title_line}\n\n{format_rr_items(body)}"

    items = split_to_items_v8(body)
    if not items:
        return f"{title_line}\n{body}"
    return f"{title_line}\n" + "\n".join(f"- {item}" for item in items)


def split_to_items_v8(body: str) -> list[str]:
    normalized = body.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.strip() for line in normalized.split("\n") if line.strip()]

    bullet_items: list[str] = []
    non_bullet_lines: list[str] = []
    for line in lines:
        if line.startswith("- "):
            bullet_items.append(line[2:].strip())
        else:
            non_bullet_lines.append(line)

    joined = " ".join(non_bullet_lines).strip()
    items: list[str] = []
    if joined:
        if "?," in joined:
            parts = re.split(r"\?,\s*", joined)
            items.extend([p.strip() + "?" for p in parts if p.strip()])
        else:
            items.append(joined)
    items.extend(bullet_items)
    return [item.strip() for item in items if item.strip()]


def render_team_dossier(context: dict) -> str:
    supplement_summary = format_supplement_text_v8(context.get("supplement_summary", ""))
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
