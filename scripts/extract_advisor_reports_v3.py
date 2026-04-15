from __future__ import annotations

import re
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError as exc:
    raise SystemExit("pypdf가 필요합니다. 실행: python -m pip install pypdf") from exc

from source_config import (
    ROOT,
    pdf_extension_for_source,
    resolve_github_pdf_folder_local_path,
    team_prefix_digits_for_source,
)

SOURCE_KEY = "advisor_interview_reports"
PDF_DIR = resolve_github_pdf_folder_local_path(SOURCE_KEY)
OUTPUT_DIR = ROOT / "data" / "normalized"
OUTPUT_PATH = OUTPUT_DIR / "advisor_interview_reports.md"
TEAM_PREFIX_DIGITS = team_prefix_digits_for_source(SOURCE_KEY)
PDF_EXTENSION = pdf_extension_for_source(SOURCE_KEY)


def normalize_team_no_from_filename(filename_stem: str) -> str:
    prefix_pattern = rf"^\s*(\d{{{TEAM_PREFIX_DIGITS}}})"
    m = re.match(prefix_pattern, filename_stem)
    if m:
        return m.group(1)

    fallback_patterns = [
        r"(?:Team|team|팀)\s*0?(\d{1,2})",
        r"0?(\d{1,2})\s*팀",
        r"^\s*0?(\d{1,2})\D",
    ]
    for pattern in fallback_patterns:
        m = re.search(pattern, filename_stem)
        if m:
            return m.group(1).zfill(2)
    return "unknown"


def extract_text_from_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    pages: list[str] = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        pages.append(f"\n\n<!-- page {i} -->\n\n{text.strip()}")
    return "\n".join(pages).strip()


def main() -> None:
    if not PDF_DIR.exists():
        raise SystemExit(
            f"PDF 폴더가 없습니다: {PDF_DIR}\n"
            f"sources.yaml의 {SOURCE_KEY}.base_url과 로컬 repo 경로를 확인하세요."
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pdf_files = sorted(PDF_DIR.glob(f"*{PDF_EXTENSION}"))
    if not pdf_files:
        raise SystemExit(f"PDF 파일이 없습니다: {PDF_DIR}")

    blocks: list[str] = ["# 팀지도교수 면담보고서 추출본\n"]
    unknown_files: list[str] = []

    for pdf_path in pdf_files:
        team_no = normalize_team_no_from_filename(pdf_path.stem)
        if team_no == "unknown":
            unknown_files.append(pdf_path.name)
        text = extract_text_from_pdf(pdf_path)
        blocks.append(f"## Team {team_no}: {pdf_path.name}\n")
        blocks.append(text if text else "_텍스트 추출 실패 또는 스캔 PDF입니다._")
        blocks.append("\n---\n")

    if unknown_files:
        blocks.append("## 팀번호 추출 실패 파일\n")
        blocks.extend(f"- {name}" for name in unknown_files)

    OUTPUT_PATH.write_text("\n\n".join(blocks), encoding="utf-8")
    print(f"Source key: {SOURCE_KEY}")
    print(f"PDF dir: {PDF_DIR}")
    print(f"Extracted {len(pdf_files)} PDF files")
    print(f"Wrote {OUTPUT_PATH}")
    if unknown_files:
        print("Warning: some files did not match team number rule from sources.yaml")


if __name__ == "__main__":
    main()
