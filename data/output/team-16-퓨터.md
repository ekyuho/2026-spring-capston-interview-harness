# Team 16. 퓨터 심층인터뷰 준비서

## 1. 프로젝트 개요

- 트랙: 
- 프로젝트명: 
- 팀원: 
- 지도교수: 
- GitHub Repo: https://github.com/puter8/capstone](https://github.com/puter8/capstone

## 2. 만들고자 하는 것

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

## 3. 사전 보충자료 요약

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

## 4. 팀원별 학기초 개인설문

### 이찬희

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 최윤서

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### BAI xinhui(백은혜)

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 김민주

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 최윤서

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 김민주

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 이찬희

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### BAI xinhui(백은혜)

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 최윤서

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 김민주

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 이찬희

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### BAI xinhui(백은혜)

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 최윤서

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 김민주

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 이찬희

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### BAI xinhui(백은혜)

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 최윤서

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 김민주

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 이찬희

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### BAI xinhui(백은혜)

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 최윤서

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 김민주

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 이찬희

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### BAI xinhui(백은혜)

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 


## 5. 개인별 5 Questions

### 이찬희



### 최윤서



### 백은혜(BAI XINHUI)



### 김민주




## 6. 기반 소프트웨어 리스트

자료 없음 또는 정리 필요

## 7. 인터뷰에서 확인할 핵심 쟁점

- 문제 정의가 충분히 좁혀졌는가?
- 학기말 산출물이 실제 구현 가능한 형태로 정의되어 있는가?
- 핵심 기술 검증 계획이 있는가?
- 팀원별 역할과 책임이 명확한가?
- GitHub repo와 실제 개발 진도가 일치하는가?

## 8. 교수자용 질문 초안

1. 이 프로젝트에서 학기말에 반드시 보여줄 수 있어야 하는 최소 산출물은 무엇인가?
2. 현재 가장 불확실한 기술 요소는 무엇이며, 언제까지 검증할 계획인가?
3. 팀원별 구현 책임은 어떻게 나뉘어 있는가?
4. 기존 서비스나 연구와 비교했을 때 차별점은 무엇인가?
5. 실패 가능성이 가장 높은 지점은 어디이며, 대안은 무엇인가?