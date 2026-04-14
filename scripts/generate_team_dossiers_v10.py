from __future__ import annotations

import re

import generate_team_dossiers_v8 as v8

SENTENCE_BULLET_TITLES = {
    "기말에 대략 어떤 것을 만들어 보여줄지의 개요, 그 의미:",
}


def split_sentences_korean_fixed(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    split_mark = "<SPLIT_SENTENCE>"
    text = re.sub(r"(다\.|요\.|임\.|함\.|[.!?])\s+", rf"\1{split_mark}", text)
    return [part.strip() for part in text.split(split_mark) if part.strip()]


def format_field_block_v10(title: str, body: str) -> str:
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

    return v8.format_field_block_v8(title, body)


if __name__ == "__main__":
    v8.split_sentences_korean = split_sentences_korean_fixed
    v8.format_field_block_v8 = format_field_block_v10
    v8.main()
