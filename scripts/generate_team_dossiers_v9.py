from __future__ import annotations

import re

import generate_team_dossiers_v8 as v8


def split_sentences_korean_fixed(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []

    # Python re는 variable-width look-behind를 지원하지 않으므로
    # 문장 종결 표현 뒤에 SPLIT_MARK를 삽입한 뒤 분리한다.
    split_mark = "<SPLIT_SENTENCE>"
    text = re.sub(r"(다\.|요\.|임\.|함\.|[.!?])\s+", rf"\1{split_mark}", text)
    return [part.strip() for part in text.split(split_mark) if part.strip()]


if __name__ == "__main__":
    v8.split_sentences_korean = split_sentences_korean_fixed
    v8.main()
