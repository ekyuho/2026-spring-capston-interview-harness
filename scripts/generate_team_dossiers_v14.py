from __future__ import annotations

import re

import generate_team_dossiers_v8 as v8

ORIGINAL_FORMAT_FIELD_BLOCK = v8.format_field_block_v8

SENTENCE_BULLET_TITLES = {
    "기말에 대략 어떤 것을 만들어 보여줄지의 개요, 그 의미:",
}
AI_REPORT_TITLE = "AI 투명성 리포트 (텍스트로 간단히 정리):"
AI_GUIDE_PHRASES = [
    "어떤 AI를, 어떤 작업에 썼나",
    "AI 제안을 수정하거나 기각한 사례",
    "AI가 틀렸거나 못 믿었던 순간",
    "AI 없이 우리가 직접 한 것",
]


def split_sentences_korean_fixed(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    split_mark = "<SPLIT_SENTENCE>"
    text = re.sub(r"(다\.|요\.|임\.|함\.|[.!?])\s+", rf"\1{split_mark}", text)
    return [part.strip() for part in text.split(split_mark) if part.strip()]


def is_guide_fragment(line: str) -> bool:
    clean = re.sub(r"^[\-•\d\.\s]+", "", line).strip()
    if not clean:
        return True
    return any(phrase in clean for phrase in AI_GUIDE_PHRASES)


def summarize_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    for old, new in [
        ("이에 따라", "→"),
        ("그러나", "→"),
        ("하지만", "→"),
        ("판단하여", "판단,"),
        ("판단함.", "판단."),
    ]:
        text = text.replace(old, new)
    return text


def format_ai_transparency_report(body: str) -> str:
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    lines = [line for line in lines if not is_guide_fragment(line)]

    ai_usage: list[str] = []
    modified: list[str] = []
    unreliable: list[str] = []
    direct_work: list[str] = []

    for line in lines:
        clean = line.strip("-• ").strip()
        if not clean or is_guide_fragment(clean):
            continue
        if re.match(r"^(Claude AI|Chat GPT|ChatGPT|Lilys AI|Gemini)\s*[-–]", clean, flags=re.IGNORECASE):
            ai_usage.append(clean)
        elif any(word in clean for word in ["오류", "간과", "중복", "못 믿", "불확실", "번복"]):
            unreliable.append(summarize_sentence(clean))
        elif "제안" in clean and any(word in clean for word in ["변경", "수정", "기각", "판단"]):
            modified.append(summarize_sentence(clean))
        else:
            direct_work.append(summarize_sentence(clean))

    modified = [x for x in modified if not is_guide_fragment(x)]
    unreliable = [x for x in unreliable if x not in modified and not is_guide_fragment(x)]
    direct_work = [x for x in direct_work if not is_guide_fragment(x)]

    blocks: list[str] = []
    if ai_usage:
        blocks.append("### 사용한 AI와 용도\n" + "\n".join(f"- {x}" for x in ai_usage))
    if modified:
        blocks.append("### AI 제안을 수정하거나 기각한 사례\n" + "\n".join(f"- {x}" for x in modified))
    if unreliable:
        blocks.append("### AI가 틀렸거나 신뢰하기 어려웠던 순간\n" + "\n".join(f"- {x}" for x in unreliable))
    if direct_work:
        blocks.append("### AI 없이 팀이 직접 한 것\n" + "\n".join(f"- {x}" for x in direct_work))
    return "\n\n".join(blocks) if blocks else "자료 없음 또는 정리 필요"


def format_base_software(text: str) -> str:
    if not text:
        return "자료 없음 또는 정리 필요"

    # v2 output: '- **env**: ...\n- **url**: ...' 등
    lines = text.replace("\r\n", "\n").replace("\r", "\n").splitlines()
    blocks: list[str] = []
    current_title: str | None = None
    current_body: list[str] = []

    def flush() -> None:
        nonlocal current_title, current_body
        if current_title is None:
            return
        body = "\n".join(current_body).strip()
        blocks.append(format_base_field(current_title, body))
        current_title = None
        current_body = []

    for line in lines:
        m = re.match(r"^- \*\*(.+?)\*\*: ?(.*)$", line)
        if m:
            flush()
            current_title = m.group(1).strip()
            current_body = [m.group(2).strip()]
        else:
            current_body.append(line.rstrip())
    flush()

    return "\n\n".join(blocks) if blocks else text


def format_base_field(title: str, body: str) -> str:
    title_lower = title.lower().strip()
    if title_lower in {"env", "url"}:
        items = split_base_items(body, is_url=(title_lower == "url"))
        if not items:
            return f"{title}:"
        return f"{title}:\n" + "\n".join(f"  - {item}" for item in items)
    return f"{title}: {body}" if body else f"{title}:"


def split_base_items(body: str, is_url: bool = False) -> list[str]:
    body = body.strip()
    if not body:
        return []
    if is_url:
        urls = re.findall(r"https?://\S+(?:\s*\([^\n)]*\))?", body)
        if urls:
            return [u.strip() for u in urls]
    # env는 빈 줄/줄바꿈 기준 우선, 없으면 ' 항목명:' 앞에서 분리
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    if len(lines) > 1:
        return lines
    parts = re.split(r"\s+(?=[가-힣A-Za-z0-9 /]+:)", body)
    return [p.strip() for p in parts if p.strip()]


def format_field_block_v14(title: str, body: str) -> str:
    title_line = f"{title}:"
    body = body.strip()
    if not body:
        return title_line

    if title_line == v8.RR_TITLE:
        return f"{title_line}\n\n{v8.format_rr_items(body)}"
    if title_line in SENTENCE_BULLET_TITLES:
        sentences = split_sentences_korean_fixed(body)
        if sentences:
            return f"{title_line}\n\n" + "\n".join(f"- {sentence}" for sentence in sentences)
    if title_line == AI_REPORT_TITLE:
        return f"{title_line}\n\n{format_ai_transparency_report(body)}"
    return ORIGINAL_FORMAT_FIELD_BLOCK(title, body)


def render_team_dossier(context: dict) -> str:
    supplement_summary = v8.format_supplement_text_v8(context.get("supplement_summary", ""))
    # v8의 내부 format_field_block_v8을 아래 main에서 v14로 교체하므로 위 호출도 v14 규칙 적용됨
    supplement_summary = __import__("generate_team_dossiers_v7").tune_github_section(supplement_summary)
    advisor_report = context.get("advisor_report", "") or "자료 없음 또는 PDF 추출 필요"
    base_software = format_base_software(context.get("base_software", ""))

    return f"""# Team {context['team_no']}. {context['team_name']} 심층인터뷰 준비서

## 1. 만들고자 하는 것

{context.get('project_summary', '정리 필요')}

## 2. 사전 보충자료 요약

{supplement_summary}

## 3. 팀지도교수 면담보고서

{advisor_report}

## 4. 팀원별 학기초 개인설문

{v8.base.render_member_section(context.get('member_surveys', []), '자료 없음 또는 column_map.yaml 보정 필요')}

## 5. 개인별 5 Questions

{v8.base.render_member_section(context.get('five_questions', []), '자료 없음 또는 column_map.yaml 보정 필요')}

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
    v8.split_sentences_korean = split_sentences_korean_fixed
    v8.format_field_block_v8 = format_field_block_v14

    def render_with_advisor(context: dict) -> str:
        team_no = str(context.get("team_no", "")).zfill(2)
        context = {**context, "advisor_report": advisor_reports.get(team_no, "")}
        return render_team_dossier(context)

    v8.base.render_team_dossier = render_with_advisor
    v8.base.main()
