from __future__ import annotations

import re

import generate_team_dossiers_v2 as base


def format_supplement_text(text: str) -> str:
    if not text:
        return "자료 없음 또는 정리 필요"

    # v2의 row_to_bullets 결과에서 '- **컬럼명**: 값' 형태를
    # '컬럼명:\n- 값1\n- 값2' 형태로 바꾼다.
    pattern = re.compile(r"^- \*\*(.+?)\*\*: (.*)$", flags=re.MULTILINE | re.DOTALL)

    blocks: list[str] = []
    current_title: str | None = None
    current_body: list[str] = []

    for line in text.splitlines():
        m = re.match(r"^- \*\*(.+?)\*\*: (.*)$", line)
        if m:
            if current_title is not None:
                blocks.append(format_field_block(current_title, "\n".join(current_body)))
            current_title = m.group(1).strip()
            current_body = [m.group(2).strip()]
        else:
            current_body.append(line.rstrip())

    if current_title is not None:
        blocks.append(format_field_block(current_title, "\n".join(current_body)))

    return "\n\n".join(blocks) if blocks else text


def format_field_block(title: str, body: str) -> str:
    body = body.strip()
    if not body:
        return f"{title}:"

    items = split_to_items(body)
    if not items:
        return f"{title}:\n{body}"

    return f"{title}:\n" + "\n".join(f"- {item}" for item in items)


def split_to_items(body: str) -> list[str]:
    # 이미 bullet이 섞여 있으면 bullet 단위 우선 처리
    normalized = body.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.strip() for line in normalized.split("\n") if line.strip()]

    bullet_items: list[str] = []
    non_bullet_lines: list[str] = []
    for line in lines:
        if line.startswith("- "):
            bullet_items.append(line[2:].strip())
        else:
            non_bullet_lines.append(line)

    # 이름: 역할 문장들이 줄 단위로 들어온 경우
    if len(non_bullet_lines) > 1 and all(looks_like_named_item(line) for line in non_bullet_lines):
        return non_bullet_lines + bullet_items

    joined = " ".join(non_bullet_lines).strip()
    items: list[str] = []

    if joined:
        # GitHub 점검 문항처럼 '?,'로 이어지는 목록 처리
        if "?," in joined:
            parts = re.split(r"\?,\s*", joined)
            items.extend([p.strip() + "?" for p in parts if p.strip()])
        # 이름: 역할이 여러 명 이어진 경우 처리
        elif has_multiple_named_items(joined):
            items.extend(split_named_items(joined))
        else:
            items.append(joined)

    items.extend(bullet_items)
    return [item.strip() for item in items if item.strip()]


def looks_like_named_item(text: str) -> bool:
    return bool(re.match(r"^[가-힣A-Za-z0-9_. -]{2,20}\s*[:：]", text))


def has_multiple_named_items(text: str) -> bool:
    return len(re.findall(r"[가-힣]{2,4}\s*[:：]", text)) >= 2


def split_named_items(text: str) -> list[str]:
    # '설영은: ... 신지민: ... 윤희서: ...' 형태를 사람별로 분리
    matches = list(re.finditer(r"([가-힣]{2,4}\s*[:：])", text))
    if not matches:
        return [text]

    items: list[str] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        item = text[start:end].strip()
        if item:
            items.append(item)
    return items


def render_team_dossier(context: dict) -> str:
    supplement_summary = format_supplement_text(context.get("supplement_summary", ""))

    return f"""# Team {context['team_no']}. {context['team_name']} 심층인터뷰 준비서

## 1. 만들고자 하는 것

{context.get('project_summary', '정리 필요')}

## 2. 사전 보충자료 요약

{supplement_summary}

## 3. 팀원별 학기초 개인설문

{base.render_member_section(context.get('member_surveys', []), '자료 없음 또는 column_map.yaml 보정 필요')}

## 4. 개인별 5 Questions

{base.render_member_section(context.get('five_questions', []), '자료 없음 또는 column_map.yaml 보정 필요')}

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
    base.render_team_dossier = render_team_dossier
    base.main()
