from __future__ import annotations

import time
from pathlib import Path
from typing import Any

import requests

from source_config import ROOT, load_sources

RAW_CSV_DIR = ROOT / "data" / "raw" / "csv"
TIMEOUT_SECONDS = 60
RETRY_COUNT = 3
RETRY_SLEEP_SECONDS = 2


class FetchError(RuntimeError):
    pass


def ensure_dirs() -> None:
    RAW_CSV_DIR.mkdir(parents=True, exist_ok=True)


def google_sheet_csv_url(spreadsheet_id: str, gid: str) -> str:
    return f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&gid={gid}"


def fetch_text(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/csv,text/plain,*/*",
        "Connection": "close",
    }

    last_error: Exception | None = None
    for attempt in range(1, RETRY_COUNT + 1):
        try:
            response = requests.get(url, headers=headers, timeout=TIMEOUT_SECONDS)
            response.raise_for_status()
            return response.content.decode("utf-8-sig")
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt < RETRY_COUNT:
                time.sleep(RETRY_SLEEP_SECONDS)

    raise FetchError(f"failed to fetch after {RETRY_COUNT} attempts: {url}\n{last_error}")


def fetch_google_sheet_csv(source_key: str, source: dict[str, Any]) -> Path:
    url = google_sheet_csv_url(source["spreadsheet_id"], str(source["gid"]))
    csv_text = fetch_text(url)

    output_path = RAW_CSV_DIR / f"{source_key}.csv"
    output_path.write_text(csv_text, encoding="utf-8")
    return output_path


def main() -> None:
    ensure_dirs()
    sources = load_sources()

    csv_sources = {
        key: value
        for key, value in sources.items()
        if value.get("type") == "google_sheet_csv"
    }

    if not csv_sources:
        raise SystemExit("sources.yaml에 google_sheet_csv 소스가 없습니다.")

    print(f"Found {len(csv_sources)} CSV sources")

    success_count = 0
    failed: list[tuple[str, str]] = []

    for source_key, source in csv_sources.items():
        name = source.get("name", source_key)
        try:
            output_path = fetch_google_sheet_csv(source_key, source)
            print(f"[OK] {source_key} ({name}) -> {output_path}")
            success_count += 1
        except Exception as exc:  # noqa: BLE001
            failed.append((source_key, str(exc)))
            print(f"[FAIL] {source_key} ({name}) -> {exc}")

    print(f"\nFetched {success_count}/{len(csv_sources)} CSV sources")

    if failed:
        print("\nFailed sources:")
        for source_key, message in failed:
            print(f"- {source_key}: {message}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
