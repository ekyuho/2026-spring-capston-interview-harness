# Team 16. 퓨터 심층인터뷰 준비서

## 1. 만들고자 하는 것

## Team 16 퓨터

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 성향 변화형 AI 캐릭터 기반 영어 회화 학습 서비스  |
| 서비스명(브랜드) | |
| 트랙 | 산학 |
| 팀명 | 퓨터 |
| 팀구성 | 김민주, 백은혜, 이찬희, 최윤서  |
| 팀지도교수 | 심재형 |
| 무엇을 만들고자 하는가 | 사용자와 대화할수록 성격이 변화하는 AI 캐릭터 기반 영어 회화 학습 서비스 |
| 고객 (누구를 위해) | 영어 회화를 재미있게 꾸준히 학습하고 싶은 10~20대 사용자 |
| Pain Point (해결할 문제) | 기존 영어 학습 앱은 고정된 응답으로 흥미가 금방 떨어지고 지속 사용이 어려움 |
| 사용 기술 | LLM API, RAG (벡터 DB), Reddit/YouTube API, Rive 애니메이션, Next.js, FastAPI |
| 개발환경 | 1. PC (Windows, Mac) 및 Mobile 웹 브라우저<br>2. FE-Next.js 14, Tailwind CSS<br>3. BE-Spring Boot 3 (Java), FastAPI (Python)<br>4. DB-PostgreSQL, Pinecone, Supabase<br>5. Rive, Zustand, JPA / Hibernate, LangChain, PRAW (Reddit), YouTube Data API<br>6. LLM: OpenAI (GPT-4o) / Embedding: OpenAI (text-embedding-3-small)
| 사용하는 소프트웨어 URL | 1. PC (Windows, Mac) 및 Mobile 웹 브라우저<br>2. FE-Next.js 14, Tailwind CSS<br>3. BE-Spring Boot 3 (Java), FastAPI (Python)<br>4. DB-PostgreSQL, Pinecone, Supabase<br>5. Rive, Zustand, JPA / Hibernate, LangChain, PRAW (Reddit), YouTube Data API<br>6. LLM: OpenAI (GPT-4o) / Embedding: OpenAI (text-embedding-3-small)
| 기대 효과 | 캐릭터와의 정서적 유대감 형성으로 학습 지속률 향상, 최신 슬랭 기반 실용 영어 습득 |
| GitHub Repo | [https://github.com/puter8/capstone](https://github.com/puter8/capstone) |
| Team Ground Rule | https://github.com/puter8/capstone/blob/main/Team_Ground_Rule.md |
| 최종수정일 | 2026.03.13 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-17"></a>

## 2. 사전 보충자료 요약

- **github 관련**: Class Repo의 Project Description의 내용은 최신상태로 PR되어있습니까?, 팀 Project Repo는 제3자가 검색해서 들어오게되었을때, 구조 이해에 도움이 되도록 Readme.MD 에 내용 정리해 두었습니까?, 팀 Project Repo의 폴더 구성은 통상 오픈소스 구성처럼 잘 구조화 되어있습니까?, 팀 Project Repo에 PR해가면서 공동작업을 github 활용하고 있습니까?, 데모한 모든 코드/데이타 등은 팀 Project Repo에 다 올라가 있습니까?
- **본 프로젝트에 있어서 팀원별 R&R(Role & Responsibility)**: 최윤서- PM/기획 총괄. 프로젝트 목표·범위 설정, 일정/마일스톤 관리, 요구사항 정의(PRD), 기능 우선순위 결정, 회의 운영, 교수님 커뮤니케이션, 리스크 관리, 최종 발표자료 통합 및 발표 리딩 담당.

이찬희- 프론트엔드 총괄. Next.js 기반 UI(Auth/채팅) 구현, SSE 스트리밍 응답 렌더링, Zustand 상태관리, Canvas2D 캐릭터 시각화 구현, 반응형/UX 개선, 프론트 테스트 및 백엔드 API 연동 담당.

김민주- 백엔드 총괄. FastAPI /api/chat 포함 핵심 API 설계·구현, Supabase(Auth/RLS/DB) 연동, 데이터 스키마 관리, 에러 핸들링·로깅, 서버 테스트/성능 점검, 배포 환경 구성 및 운영 담당.

백은혜- AI 총괄. 발화 분석기(5축 점수) 설계·개선, MATRIX/EMA 로직 구현, 프롬프트 빌더 설계, 슬랭 파이프라인(Reddit 수집·pgvector 검색) 구축, 모델 성능 평가 및 개선, AI 품질 관리 담당.
- **기말에 대략 어떤 것을 만들어 보여줄지의 개요, 그 의미**: 기말에는 사용자가 영어 문장을 입력하면 시스템이 이를 5개 축(Formality, Energy, Intimacy, Humor, Curiosity)으로 분석하고, 그 결과를 CHARACTER MATRIX에 반영하여 AI 캐릭터의 반응 성향과 시각적 상태가 달라지는 웹 기반 프로토타입을 보여줄 계획입니다. 

여기에 더해, 사용자가 부자연스럽거나 잘못된 영어 표현을 말했을 때 캐릭터가 이를 즉시 코렉팅하고, 올바른 표현이나 대체 문장을 제시하면서 자연스럽게 대화를 이어가는 기능까지 구현하고자 합니다. 
즉, 단순히 문장에 답하는 챗봇이 아니라, 사용자의 말투와 대화 성향을 반영해 반응이 달라지고 동시에 학습 보조 역할까지 수행하는 AI 캐릭터를 시연하는 것이 목표입니다. 

이를 통해 저희 프로젝트의 핵심기술이 아이디어 수준이 아니라 실제 사용자 입력, 발화 분석, CHARACTER MATRIX 연산, 교정형 응답 생성까지 연결되는 작동 가능한 MVP라는 점을 보여주고, 기존 영어 회화 서비스보다 더 개인화되고 몰입감 있는 학습 경험을 제공할 수 있음을 증명하고자 합니다.
- **서비스를 지향하는 산학트랙의 경우, API Call을 통해 어떤 AI 서비스를, 어떤 목적으로, 어떤 파라미터를 주고, 그 결과를 어떻게 활용하는지 간단히 정리(어떻든 AI를 적극적으로 적용해보세요)**: API Call 기반으로 AI를 기능 단위에 분리 적용함.

OpenAI GPT-4o (Chat Completions)
목적: 사용자 입력과 MATRIX 상태(5축 점수)를 반영한 맞춤형 영어 회화 답변 생성
생성된 답변을 채팅 UI에 출력하고, 다음 턴 학습 프롬프트의 컨텍스트로 누적

OpenAI Embeddings (text-embedding-3-small)
목적: 슬랭/표현 예문 검색용 벡터 인덱싱(RAG)
임베딩 벡터를 Supabase pgvector에 저장하고, 질의 시 유사도 검색 결과를 GPT-4o 프롬프트에 첨부해 답변 품질 향상

OpenAI Moderation API
목적: 욕설·혐오·유해발화 필터링(안전한 학습 환경)
위험도 높은 입력은 즉시 차단/완화 응답으로 대체하고, 정상 입력만 대화 생성 파이프라인으로 전달
- **AI 투명성 리포트 (텍스트로 간단히 정리)**: https://github.com/puter8/capstone/blob/main/AI%20transparency%20report.md

## 3. 팀원별 학기초 개인설문

### 최윤서

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: AX, AI 프롬프팅 및 리서치에 관심이 있습니다. 전통적 CS보다 HCI에 관심이 많습니다. / API를 사용한 AI 영어 회화 앱, XR을 이용한 가상 환경 사용 팝업 소프트웨어 등을 제작해본 경험이 있습니다. / 개발도 가능하나 PM, 리서치 영역에 더 강한 편이며 발표에 자신이 있습니다.
- **이번에 팀이 구성된 계기**: ICT 한마음 드림업을 신청하여 이를 기반으로 함께할 팀원을 구하면서 팀을 구성함

### 김민주

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: 클라우드, 인프라 영역에 관심 있습니다. 프론트엔드로 참여하여 앱을 배포해본 경험이 있으며, 이슈나 에러를 고치는 트러블 슈팅을 잘한다고 생각합니다.
- **이번에 팀이 구성된 계기**: ai agent와 클라우드에 관심있는 팀원들이 모여 의미있는 결과물을 만들어보자는 뜻이 맞아 팀을 구성하게 되었습니다.

### 이찬희

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: AI agent 분야에 관심이 있습니다.
- **이번에 팀이 구성된 계기**: 에이전트, 클라우드 관심사 기반

### BAI xinhui(백은혜)

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: AI와 데이터 분석을 활용한 서비스 개발에 관심이 있습니다. Python을 활용해 이커머스 리뷰 데이터를 수집·분석하고 감성 분석 기반 추천 시스템을 구현한 경험이 있습니다. 또한 React와 Spring Boot를 활용한 웹 서비스 개발을 진행했으며, STT 기능을 적용해 음성을 텍스트로 변환하는 기능도 구현해 보았습니다.
- **이번에 팀이 구성된 계기**: 추구하는 바와 관심사 일치

## 4. 개인별 5 Questions

### 이찬희

- **질문당 한줄씩 5개의 질문**: 마지막으로 영어 회화 연습한 게 언제이신가요?? 그때 어떻게 하셨나요?
영어 회화 앱 쓰다가 그만두신 적 있으신가요? 왜 그만두셨나요?
영어로 대화할 때 제일 답답하거나 어색했던 순간이 있으셨나요?
영어 회화 연습의 불편함을 문제를 해결하려고 지금까지 뭘 해보셨나요?
지금 쓰는 영어 학습 방법에서 ‘이것만 바뀌면 계속 쓸 텐데’라고 느낀 적 있으신가요? 그것이 무엇인가요?

### 최윤서

- **질문당 한줄씩 5개의 질문**: 1. 영어 회화를 하고싶다고 생각했던 적이 있나요?
2. 언어 공부에 가장 중요하다고 생각하는 것은 무엇인가요?
3. 영어로 말할 때 가장 막히는 부분이 있다면 무엇인가요?
4. 영어 말하기에 한 달에 어느정도 금전을 투자할 의향이 있나요?
5. 기존 영어 말하기 서비스에 대한 불만은 무엇이 있나요?

### 백은혜(BAI XINHUI)

- **질문당 한줄씩 5개의 질문**: - 영어 회화 공부를 위해 현재 어떤 앱이나 방법을 사용하고 있나요? 그 방법의 어떤 점이 마음에 들지 않나요?

- 영어 학습 앱을 쓰다가 그만둔 적이 있나요? 있다면 그만둔 이유가 무엇이었나요?

- 대화할수록 나의 말투와 성격을 닮아가는 AI 캐릭터와 영어로 대화한다면 실제로 더 오래 사용할 것 같나요?

- 유튜브, 넷플릭스 등?에서 나오는 최신 슬랭이나 밈 표현을 영어로 배우고 싶다고 느낀 적이 있나요?

- 영어 공부를 꾸준히 하게 만드는 가장 큰 동기가 무엇인가요? 재미, 성취감, 실용성 중 어떤 게 가장 중요한가요?

### 김민주

- **질문당 한줄씩 5개의 질문**: 1. 영어 회화 연습을 할 때 가장 불편하거나 꾸준히 못 하게 되는 이유는 무엇인가요?
2. AI 캐릭터와 대화하며 영어를 연습하는 서비스가 있다면, 어떤 점이 가장 기대되거나 걱정되나요?
3. 캐릭터가 대화할수록 말투나 성격이 변하는 기능이 있다면 얼마나 흥미롭게 느껴지나요? 왜 그렇게 생각하시나요?
4. 이 서비스를 사용한다면 가장 자주 쓰고 싶은 상황은 언제인가요? (예: 혼자 회화 연습할 때, 심심할 때, 시험 준비할 때)
5. 무료 기능과 유료 기능이 나뉜다면, 어떤 기능까지는 돈을 내고 사용할 의향이 있나요? (예: 무제한 대화, 음성 대화, 프리미엄 캐릭터, 맞춤 피드백)

## 5. 기반 소프트웨어 리스트

- **env**: 1. PC (Windows, Mac) 및 Mobile 웹 브라우저
2. FE-Next.js 14, Tailwind CSS
3. BE-Spring Boot 3 (Java), FastAPI (Python)
4. DB-PostgreSQL, Pinecone, Supabase
5. Rive, Zustand, JPA / Hibernate, LangChain, PRAW (Reddit), YouTube Data API
6. LLM: OpenAI (GPT-4o) / Embedding: OpenAI (text-embedding-3-small)
- **url**: VS Code (프론트엔드/AI 서버 개발용): https://code.visualstudio.com/download
IntelliJ IDEA (Spring Boot 개발용): https://www.jetbrains.com/idea/download/
Node.js (Next.js 14 실행용 ): https://nodejs.org/en/download/
JDK 17 or 21 (Spring Boot 3 실행용): https://www.oracle.com/java/technologies/downloads/
Python (FastAPI 및 AI 파이프라인용): https://www.python.org/downloads/
Docker Desktop (컨테이너 관리 및 배포 테스트용): https://www.docker.com/products/docker-desktop/
PostgreSQL (로컬 DB 테스트용): https://www.postgresql.org/download/
Postman (API 엔드포인트 테스트용): https://www.postman.com/downloads/
Git (버전 관리용): https://git-scm.com/downloads
DBeaver (DB 관리 GUI 도구): https://dbeaver.io/download/

## 6. 인터뷰에서 확인할 핵심 쟁점

- 문제 정의가 충분히 좁혀졌는가?
- 학기말 산출물이 실제 구현 가능한 형태로 정의되어 있는가?
- 핵심 기술 검증 계획이 있는가?
- 팀원별 역할과 책임이 명확한가?
- GitHub repo와 실제 개발 진도가 일치하는가?

## 7. 교수자용 질문 초안

1. 이 프로젝트에서 학기말에 반드시 보여줄 수 있어야 하는 최소 산출물은 무엇인가?
2. 현재 가장 불확실한 기술 요소는 무엇이며, 언제까지 검증할 계획인가?
3. 팀원별 구현 책임은 어떻게 나뉘어 있는가?
4. 기존 서비스나 연구와 비교했을 때 차별점은 무엇인가?
5. 실패 가능성이 가장 높은 지점은 어디이며, 대안은 무엇인가?
