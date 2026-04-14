from __future__ import annotations

import re

import generate_team_dossiers_v8 as v8

ORIGINAL_FORMAT_FIELD_BLOCK = v8.format_field_block_v8

SENTENCE_BULLET_TITLES = {
    "기말에 대략 어떤 것을 만들어 보여줄지의 개요, 그 의미:",
}
AI_REPORT_TITLE = "AI 투명성 리포트 (텍스트로 간단히 정리):"
AI_REPORT_GUIDE_PATTERN = re.compile(
    r"어떤 AI를, 어떤 작업에 썼나\s*2\.\s*AI 제안을 수정하거나 기각한 사례\s*3\.\s*AI가 틀렸거나 못 믿었던 순간\s*4\.\s*AI 없이 우리가 직접 한 것\s*",
    flags=re.DOTALL,
)


def split_sentences_korean_fixed(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    split_mark = "<SPLIT_SENTENCE>"
    text = re.sub(r"(다\.|요\.|임\.|함\.|[.!?])\s+", rf"\1{split_mark}", text)
    return [part.strip() for part in text.split(split_mark) if part.strip()]


def format_ai_transparency_report(body: str) -> str:
    body = AI_REPORT_GUIDE_PATTERN.sub("", body).strip()
    lines = [line.strip() for line in body.splitlines() if line.strip()]

    ai_usage: list[str] = []
    modified: list[str] = []
    unreliable: list[str] = []
    direct_work: list[str] = []

    for line in lines:
        clean = line.strip("- ").strip()
        if not clean:
            continue

        if re.match(r"^(Claude AI|Chat GPT|ChatGPT|Lilys AI|Gemini)\s*[-–]", clean, flags=re.IGNORECASE):
            ai_usage.append(clean)
        elif "제안" in clean and any(word in clean for word in ["변경", "수정", "기각", "판단"]):
            modified.append(summarize_sentence(clean))
        elif any(word in clean for word in ["오류", "간과", "중복", "못 믿", "불확실", "번복"]):
            unreliable.append(summarize_sentence(clean))
        else:
            direct_work.append(summarize_sentence(clean))

    # 일부 항목은 modified와 unreliable 양쪽 성격이 있지만, 가독성을 위해 중복 제거
    unreliable = [x for x in unreliable if x not in modified]

    blocks: list[str] = []
    if ai_usage:
        blocks.append("### 사용한 AI와 용도\n" + "\n".join(f"- {x}" for x in ai_usage))
    if modified:
        blocks.append("### AI 제안을 수정하거나 기각한 사례\n" + "\n".join(f"- {x}" for x in modified))
    if unreliable:
        blocks.append("### AI가 틀렸거나 신뢰하기 어려웠던 순간\n" + "\n".join(f"- {x}" for x in unreliable))
    if direct_work:
        blocks.append("### AI 없이 팀이 직접 한 것\n" + "\n".join(f"- {x}" for x in direct_work))

    return "\n\n".join(blocks) if blocks else body


def summarize_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    replacements = [
        ("이에 따라", "→"),
        ("그러나", "→"),
        ("하지만", "→"),
        ("판단하여", "판단,"),
        ("판단함.", "판단."),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def format_field_block_v12(title: str, body: str) -> str:
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
    v8.format_field_block_v8 = format_field_block_v12
    v8.main()
