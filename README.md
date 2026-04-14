# 2026 Spring Capstone Interview Harness

캡스톤디자인 팀별 심층인터뷰 준비를 위해 흩어진 자료를 팀 단위로 모으는 자동화 저장소입니다.

## 데이터 소스

- Class Project Brief: GitHub Markdown
- 심층인터뷰 보충자료: Google Spreadsheet
- 학기초 개인설문: Google Spreadsheet
- 개인별 5 Questions: Google Spreadsheet
- 기반 소프트웨어 리스트: Google Spreadsheet

## 1차 목표

아직 병합하지 않고, 각 자료가 정상적으로 읽히는지 확인합니다.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/fetch_debug_columns.py
```

실행 후 아래 파일을 확인합니다.

```text
data/raw/
data/output/debug_columns.md
```

## 2차 목표

컬럼명을 확인한 뒤, 팀번호와 학생 이름 기준으로 병합 규칙을 확정합니다.

예상 출력:

```text
data/output/team-01.md
data/output/team-02.md
...
data/output/unresolved.md
```

## 주의

개인설문은 민감할 수 있으므로, 생성 결과물을 공개 저장소에 그대로 올리지 않도록 주의합니다.
