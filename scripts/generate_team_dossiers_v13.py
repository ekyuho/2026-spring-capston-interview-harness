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


def format_field_block_v13(title: str, body: str) -> str:
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


if __name__ == "__main__":
    v8.split_sentences_korean = split_sentences_korean_fixed
    v8.format_field_block_v8 = format_field_block_v13
    v8.main()
