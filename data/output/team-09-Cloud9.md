# Team 09. Cloud9 심층인터뷰 준비서

## 1. 만들고자 하는 것

## Team 9 Cloud9

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 다중 퀀트 전략 실시간 상태 모니터링 및 이상 징후 탐지 서비스 |
| 서비스명(브랜드) | Canary |
| 트랙 | 산학 |
| 팀명 | Cloud9 |
| 팀구성 | 박나림, 임도경, 최은우 |
| 팀지도교수 | 이민수 |
| 무엇을 만들고자 하는가 | 퀀트 전략 실시간 상태 모니터링 및 이상 징후 탐지 시스템 |
| 고객 (누구를 위해) | 개인 자동매매 투자자 |
| Pain Point (해결할 문제) | 여러 퀀트 전략을 동시에 운용할 경우, 이상 상황이 발생했을 때 어떤 전략에서 문제가 생겼는지 빠르게 확인하기 어렵다는 문제가 있다. 본 프로젝트는 전략별 상태를 실시간으로 모니터링하고 이상 징후를 탐지하여, 이를 대시보드로 시각화해 효율적인 대응을 가능하게 한다. |
| 사용 기술 | Front(React, Recharts, WebSocket client), Back(Python, FastAPI, SQLAlchemy, WebSocket), AI(Pandas, NumPy)  |
| 개발환경 | 1. Client 디바이스 - PC<br>2. FE - React(javascript), websocket client, recharts<br>3. BE - FastAPI<br>4. DB - PostgreSQL<br>5. (BE) - pandas/numpy, scikit-learn, pytorch, statsmodels (Streaming) - websocket (알람) - SMTP/Slack API/Firebase <br>6. Binance API, OpenAI
| 사용하는 소프트웨어 URL | 1. Client 디바이스 - PC<br>2. FE - React(javascript), websocket client, recharts<br>3. BE - FastAPI<br>4. DB - PostgreSQL<br>5. (BE) - pandas/numpy, scikit-learn, pytorch, statsmodels (Streaming) - websocket (알람) - SMTP/Slack API/Firebase <br>6. Binance API, OpenAI
| 기대 효과 | 손실 최소화 |
| GitHub Repo | https://github.com/Cloud9-capstone-2026/cloud9 |
| Team Ground Rule | [Team Ground Rule](https://github.com/Cloud9-capstone-2026/cloud9/blob/main/Team_Ground_Rule.md) |
| 최종수정일 | 2026.04.09 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-10"></a>

## 2. 사전 보충자료 요약

자료 없음 또는 정리 필요

## 3. 팀지도교수 면담보고서

<!-- page 1 -->

지도교수님  면담  보고서
기본  정보
면담  일시 :
면담  장소  / 방식 :
지도교수명 : 이민수  교수님
팀명 : 9 조  Cloud9
팀원 : 박나림 , 임도경 , 최은우
프로젝트  주제 :
면담  목적
프로젝트  진행  현황
현재까지의  문제점  또는  고민사항
주요  논의  내용
지도  교수님  피드백
향후  일정  계획
기타  사항
지 도 교 수 님  면 담  보 고 서
1

## 4. 팀원별 학기초 개인설문

### 최은우

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: AI, Langgraph 사용한 AI 에이전트(to-do 리스트 최적화 프로그램)
- **이번에 팀이 구성된 계기**: 경제/금융 관련 소재로 프로젝트를 하고 싶은 팀원들이 모여서 구성

### 박나림

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: 저는 데이터 기반 서비스와 백엔드 시스템 개발에 관심이 있습니다.
파이썬을 활용해서 중소기업의 금융건강지수를 예측하는 프로젝트를 해보았고, 개인적으로는 FastAPI를 활용한 todo api 서버를 구축해본 경험이 있습니다.
저는 새로운 기술을 빠르고 꾸준하게 학습하고 직접 구현해보는 과정을 두려워하지 않는다는 강점이 있다고 생각합니다.
- **이번에 팀이 구성된 계기**: 금융과 관련하여 비슷한 관심사를 가지고 있는 벗들과 팀을 구성하였습니다.

### 임도경

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: UI/UX 설계
- **이번에 팀이 구성된 계기**: 비슷한 관심사와 성향을 계기로 구성됨

## 5. 개인별 5 Questions

### 박나림

- **질문당 한줄씩 5개의 질문**: 지금 투자 전략 성과를 어떻게 확인하고 계신가요?
전략이 잘못되었다고 느끼는 순간은 언제인가요?
이상 상황이 발생했을 때 어떤 방식의 알람을 원하시나요?
전략 상태를 판단할 때 가장 중요하게 보는 지표는 무엇인가요?
손실이 발생했을 때 시장 문제인지 전략 문제인지 구분이 필요하다고 느끼시나요?

### 최은우

- **질문당 한줄씩 5개의 질문**: 1. 현재 퀀트 전략을 운용할 때 이상 징후를 어떻게 파악하고 있나요? (직접 차트를 보는지, 별도 도구를 쓰는지 등)
2. 전략 성과가 나빠졌을 때 그 원인이 시장 전체 문제인지 내 전략 문제인지 구분하는 데 어려움을 느낀 적이 있나요?
3. 이상 징후 알림을 받는다면 어떤 정보가 포함되어 있을 때 가장 유용할 것 같나요? (수치, 원인 분석, 관련 뉴스 등)
4. 여러 전략을 동시에 운용할 때 전략 간 상태를 비교하고 싶었던 경험이 있나요? 있다면 어떤 방식으로 비교하셨나요?
5. 실시간 모니터링 도구를 사용한다면 어느 정도의 탐지 지연(예: 수 분 이내)까지 허용 가능한가요?

### 임도경

- **질문당 한줄씩 5개의 질문**: 1. 현재 여러 개의 퀀트 전략을 동시에 운용하실 때, 특정 전략에서 수익률 저하나 이상 징후가 발생하면 그 원인을 즉각적으로 판단하는 데 얼마나 시간이 걸리시나요?
2. 기존에 수동으로 모니터링하시면서 가장 아찔했던 순간은 언제였으며, 그때 실시간 알림 기능이 있었다면 리스크를 얼마나 줄일 수 있었을까요?
3. PnL, Drawdown, Win rate 외에 실시간으로 꼭 확인하고 싶은 본인만의 핵심 메트릭이나 보조 지표가 따로 있으신가요?
4. 이상 징후가 포착되었을 때, 단순 알림을 넘어 시스템이 자동으로 거래를 일시 중지하거나 특정 비중을 조절하는 기능에 대해서는 어떻게 생각하시나요?
5. 모바일 앱이나 웹 대시보드를 통해 24시간 자산을 확인할 때, 가장 중요하게 생각하는 시각화 요소는 무엇인가요?

## 6. 기반 소프트웨어 리스트

env:
  - 1. Client 디바이스 - PC
  - 2. FE - React(javascript), websocket client, recharts
  - 3. BE - FastAPI
  - 4. DB - PostgreSQL
  - 5. (BE) - pandas/numpy, scikit-learn, pytorch, statsmodels (Streaming) - websocket (알람) - SMTP/Slack API/Firebase
  - 6. Binance API, OpenAI

url:
  - https://nodejs.org/
  - https://react.dev/
  - https://code.visualstudio.com/
  - https://www.python.org/
  - https://fastapi.tiangolo.com/
  - https://www.postgresql.org/download/
  - https://www.docker.com/products/docker-desktop/
  - https://git-scm.com/
  - https://pytorch.org/get-started/locally/
  - https://scikit-learn.org/stable/install.html
  - https://numpy.org/install/
  - https://pandas.pydata.org/docs/getting_started/install.html
  - https://www.statsmodels.org/stable/install.html
  - https://www.tensorflow.org/install (optional)

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
