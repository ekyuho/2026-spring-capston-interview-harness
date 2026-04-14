from __future__ import annotations

import re
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError as exc:
    raise SystemExit("pypdf가 필요합니다. 실행: python -m pip install pypdf") from exc

ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "data" / "raw" / "advisor_interview_reports"
OUTPUT_DIR = ROOT / "data" / "normalized"
OUTPUT_PATH = OUTPUT_DIR / "advisor_interview_reports.md"


def normalize_team_no(text: str) -> str:
    patterns = [
        r"(?:Team|team|팀)\s*0?(\d{1,2})",
        r"0?(\d{1,2})\s*팀",
    ]
    for pattern in patterns:
        m = re.search(pattern, text)
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
        raise SystemExit(f"PDF 폴더가 없습니다: {PDF_DIR}\nDrive 폴더의 PDF들을 이 위치에 저장하세요.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pdf_files = sorted(PDF_DIR.glob("*.pdf"))
    if not pdf_files:
        raise SystemExit(f"PDF 파일이 없습니다: {PDF_DIR}")

    blocks: list[str] = ["# 팀지도교수 면담보고서 추출본\n"]
    for pdf_path in pdf_files:
        team_no = normalize_team_no(pdf_path.stem)
        text = extract_text_from_pdf(pdf_path)
        blocks.append(f"## Team {team_no}: {pdf_path.name}\n")
        blocks.append(text if text else "_텍스트 추출 실패 또는 스캔 PDF입니다._")
        blocks.append("\n---\n")

    OUTPUT_PATH.write_text("\n\n".join(blocks), encoding="utf-8")
    print(f"Extracted {len(pdf_files)} PDF files")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
