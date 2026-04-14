from __future__ import annotations

import io
import re
from pathlib import Path
from typing import Any

import pandas as pd
import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "sources.yaml"
RAW_DIR = ROOT / "data" / "raw"
OUTPUT_DIR = ROOT / "data" / "output"


def ensure_dirs() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_config() -> dict[str, Any]:
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def google_sheet_csv_url(spreadsheet_id: str, gid: str) -> str:
    return f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid={gid}"


def fetch_text(url: str) -> str:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.text


def safe_filename(name: str) -> str:
    name = re.sub(r"[^0-9A-Za-z가-힣._-]+", "_", name.strip())
    return name.strip("_") or "source"


def fetch_google_sheet_as_dataframe(source_key: str, source: dict[str, Any]) -> pd.DataFrame:
    url = google_sheet_csv_url(source["spreadsheet_id"], str(source["gid"]))
    csv_text = fetch_text(url)

    raw_path = RAW_DIR / f"{safe_filename(source_key)}.csv"
    raw_path.write_text(csv_text, encoding="utf-8")

    return pd.read_csv(io.StringIO(csv_text))


def fetch_github_markdown(source_key: str, source: dict[str, Any]) -> str:
    text = fetch_text(source["url"])
    raw_path = RAW_DIR / f"{safe_filename(source_key)}.md"
    raw_path.write_text(text, encoding="utf-8")
    return text


def dataframe_sample_markdown(df: pd.DataFrame, max_rows: int = 3) -> str:
    if df.empty:
        return "_빈 데이터프레임입니다._\n"
    sample = df.head(max_rows).fillna("")
    return sample.to_markdown(index=False)


def markdown_brief_summary(text: str) -> str:
    lines = [line for line in text.splitlines() if line.strip()]
    preview = "\n".join(lines[:40])
    return f"- 전체 문자 수: {len(text):,}\n- 비어 있지 않은 줄 수: {len(lines):,}\n\n```md\n{preview}\n```"


def main() -> None:
    ensure_dirs()
    config = load_config()
    sources = config.get("sources", {})

    report: list[str] = []
    report.append("# 데이터 소스 컬럼 진단\n")
    report.append("이 파일은 병합 전 자료 구조를 확인하기 위한 1차 진단 결과입니다.\n")

    for source_key, source in sources.items():
        name = source.get("name", source_key)
        source_type = source.get("type")
        report.append(f"## {source_key}: {name}\n")
        report.append(f"- type: `{source_type}`\n")

        try:
            if source_type == "google_sheet_csv":
                df = fetch_google_sheet_as_dataframe(source_key, source)
                report.append(f"- rows: {len(df):,}")
                report.append(f"- columns: {len(df.columns):,}\n")
                report.append("### 컬럼명\n")
                for col in df.columns:
                    report.append(f"- `{col}`")
                report.append("\n### 샘플 3행\n")
                report.append(dataframe_sample_markdown(df))
                report.append("\n")

            elif source_type == "github_markdown":
                text = fetch_github_markdown(source_key, source)
                report.append(markdown_brief_summary(text))
                report.append("\n")

            else:
                report.append(f"지원하지 않는 source type입니다: `{source_type}`\n")

        except Exception as exc:  # noqa: BLE001
            report.append(f"⚠️ 로딩 실패: `{type(exc).__name__}: {exc}`\n")

    output_path = OUTPUT_DIR / "debug_columns.md"
    output_path.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
