# Team 03. Alltology 심층인터뷰 준비서

## 1. 만들고자 하는 것

## Team 3 Alltology

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 일반 벤치마크를 활용한 LLM 내부 파라미터 확장과 온톨로지 기반 지식 증강 기법의 실증적 성능 비교 및 융합 방법론 연구 |
| 서비스명(브랜드) | |
| 트랙 | 연구 |
| 팀명 | Alltology |
| 팀구성 | 박세령, 이다영, 손현경 |
| 팀지도교수 | 황의원 교수님 |
| 무엇을 만들고자 하는가 | 기존 모델과 온톨로지가 탑재된 모델의 성능(정확도) 비교한 연구논문 |
| 고객 (누구를 위해) | LLM 모델의 답변 정확도 향상 |
| Pain Point (해결할 문제) | 할루시네이션을 비롯한 정확도 문제를 개선하기 위해서 |
| 사용 기술 | 온톨로지 |
| 개발환경 | 1. 클라이언트 및 플랫폼 (Client & Platform)<br>Target: 웹 브라우저 기반 (Multi-Device 지원)<br>환경: 데스크톱/노트북(Windows, Mac, Linux) 및 모바일 브라우저 최적화<br>특이사항: 별도의 네이티브 앱(iOS/Android)이나 엔진(Unity/Unreal)을 사용하지 않는 Web-Standard 방식 채택<br><br>2. 프론트엔드 (Front-end)<br>Framework: Vue 3 (Composition API)<br>Build Tool: Vite (고속 번들링 및 개발 서버)<br>Key Libraries:<br>1. UI/Design: Vuestic UI, Element Plus, Tailwind CSS<br>2. Visualization: vis-network (온톨로지 그래프 시각화 핵심)<br>3. Content: marked, github-markdown-css (문서 렌더링)<br>4. Communication: axios, vue-router<br><br>3. 백엔드 (Back-end)<br>Language: Python 3.x<br>Framework: FastAPI (고성능 비동기 API 프레임워크)<br>Server: Uvicorn (ASGI)<br>Key Libraries: <br>1. Core: Pydantic (데이터 검증), python-dotenv (환경 변수 관리) <br>2. Async: FastAPI CORS Middleware, Threading (LLM 작업 병렬 처리)<br><br>4. 데이터 관리 (Data Management)<br>Storage Strategy: File System Based Storage (No-DB Architecture)<br><br>5. 외부 서비스 및 AI 모델 (External API & AI)<br>Main LLM: OpenAI API (GPT-5 계열 모델)<br>
| 사용하는 소프트웨어 URL | 1. 클라이언트 및 플랫폼 (Client & Platform)<br>Target: 웹 브라우저 기반 (Multi-Device 지원)<br>환경: 데스크톱/노트북(Windows, Mac, Linux) 및 모바일 브라우저 최적화<br>특이사항: 별도의 네이티브 앱(iOS/Android)이나 엔진(Unity/Unreal)을 사용하지 않는 Web-Standard 방식 채택<br><br>2. 프론트엔드 (Front-end)<br>Framework: Vue 3 (Composition API)<br>Build Tool: Vite (고속 번들링 및 개발 서버)<br>Key Libraries:<br>1. UI/Design: Vuestic UI, Element Plus, Tailwind CSS<br>2. Visualization: vis-network (온톨로지 그래프 시각화 핵심)<br>3. Content: marked, github-markdown-css (문서 렌더링)<br>4. Communication: axios, vue-router<br><br>3. 백엔드 (Back-end)<br>Language: Python 3.x<br>Framework: FastAPI (고성능 비동기 API 프레임워크)<br>Server: Uvicorn (ASGI)<br>Key Libraries: <br>1. Core: Pydantic (데이터 검증), python-dotenv (환경 변수 관리) <br>2. Async: FastAPI CORS Middleware, Threading (LLM 작업 병렬 처리)<br><br>4. 데이터 관리 (Data Management)<br>Storage Strategy: File System Based Storage (No-DB Architecture)<br><br>5. 외부 서비스 및 AI 모델 (External API & AI)<br>Main LLM: OpenAI API (GPT-5 계열 모델)<br>
| 기대 효과 | 미디어 분야의 LLM 모델의 답변 정확도 향상 (헐루시네이션 감소 효과) |
| GitHub Repo | [https://github.com/Ontology0/Graduation-Project](https://github.com/Ontology0/Graduation-Project) |
| Team Ground Rule |  [Team Ground Rule](https://github.com/ontology0/Graduation-Project/blob/main/Team_Ground_Rule.md) |
| 최종수정일 | 2026/03/11 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-5"></a>

## 2. 사전 보충자료 요약

자료 없음 또는 정리 필요

## 3. 팀지도교수 면담보고서

자료 없음 또는 PDF 추출 필요

## 4. 팀원별 학기초 개인설문

### 이다영

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: 데이터베이스 관련 기술, 온톨로지, AI 모델등에 관심있다. 겨울방학동안 이공계 학생들을 위한 LLM 및 노트관리 서비스 프로젝트에 참여하여 배포까지 하고 데모데이를 열어서 박람회에 참가한 경험이 있다.
- **이번에 팀이 구성된 계기**: 개인적으로 관심이 매우 있었던 주제인 온톨로지에 대해 연구하고 이를 활용하여 생산성을 높이는 것에 대해 비교하고 분석하는 논무을 쓰는 팀이어서 같이 구성하게 되었다.

### 박세령

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: [기술적 관심영역]
저의 가장 큰 기술적 관심사는 자연어 처리(NLP), 대형 언어 모델(LLM), 그리고 강화학습(RL) 등 최신 AI 기술을 활용해 실제 비즈니스 문제를 해결하는 것입니다. 단순히 모델의 성능 지표를 높이는 연구 수준에 그치지 않고, 완성된 AI 기술이 어떻게 실제 서비스 구조에 녹아들어 사용자에게 실질적인 효용을 제공할 수 있는지에 깊은 흥미를 느끼고 있습니다. 최근에는 검색 증강 생성(RAG)을 통한 Ontology 등 도메인 특화 데이터 최적화부터, LLM 기반의 가상 환경 시뮬레이션 구축까지 다양한 방법론을 탐구하고 있습니다. 장기적으로는 최첨단 AI 기술과 비즈니스 니즈 사이의 간극을 완벽하게 메우는 FDE(Forward Deployed Engineer) 역할을 지향하며, 기술이 실제 서비스로 구현되고 가치를 창출하는 전체 사이클을 조망하는 능력을 기르고 있습니다. 이론적 학습을 넘어, 데이터를 다루는 AI 모델을 직접 구현하고 이를 실제 작동하는 시스템과 연동하는 산출물들을 꾸준히 만들어 왔습니다.

[실제로 만들어서 작동시켜본 산출물]
강화학습 기반 추천 시스템 'MOARD' : LLM과 강화학습을 결합한 추천 시스템 파이프라인을 설계하고 구현했습니다. 특히 LLM을 활용해 가상 사용자의 반응을 생성하고, 이를 강화학습 환경과 연동하는 핵심 시뮬레이션 환경 구축을 주도했습니다. 페르소나 정보 관리와 데이터 흐름을 제어하는 데이터베이스 구조까지 직접 설계하며 AI 모델과 시스템 아키텍처의 통합을 이뤄냈고, 그 완성도를 인정받아 최우수상을 수상했습니다.

법률 도메인 특화 RAG 시스템 최적화: AI 플랫폼 기업 인턴십 과정에서 법률 도메인 온톨로지 구축 프로젝트에 참여했습니다. RAG 튜닝과 정교한 프롬프트 엔지니어링을 수행하여, 복잡한 법률 데이터 환경에서도 AI가 환각(Hallucination) 현상 없이 정확한 답변을 도출해 내도록 파이프라인을 고도화했습니다.

얼굴 비식별화 및 개인화 API 서비스 배포: MTCNN과 ArcFace를 활용한 얼굴 비식별화(Anonymizer) 모델 구축을 비롯해, Python과 FastAPI를 활용하여 일상에 필요한 정보를 맞춤형으로 제공하는 'Morning Assistant'의 백엔드를 설계하고 배포하는 등 실무적인 서비스 개발 경험을 쌓았습니다.

[남보다 잘한다고 생각되는 영역]
저는 개발 과정에서 마주하는 한계를 단순히 단일 모델의 관점에서만 접근하지 않습니다. MOARD 프로젝트에서 가상 유저 시뮬레이션과 강화학습 루프를 데이터베이스로 매끄럽게 연결했듯, 복잡한 AI 기술들이 하나의 서비스 로직 안에서 병목 없이 톱니바퀴처럼 맞물려 돌아가도록 전체 구조를 설계하는 데 강점이 있습니다. 법률 데이터와 같은 낯선 도메인에서도 특성을 집요하게 분석하여 RAG 검색 효율을 비약적으로 끌어올리는 등, 저는 코드를 작성할 때부터 이것이 최종적인 비즈니스 임팩트로 어떻게 이어질지 치열하게 고민하는 목적 지향적인 엔지니어입니다.
- **이번에 팀이 구성된 계기**: 온톨로지(Ontology)를 활용한 AI 연구를 주도적으로 진행해 보고자 하는 명확한 목표가 있었습니다. 이를 실현하기 위해 기획안을 작성하여 교내 커뮤니티에 오픈 공고를 올렸고, 감사하게도 11명의 학우분들께서 지원해 주셨습니다. 팀을 구성하는 과정에서 단순히 기술적 스택만을 보지 않고, 프로젝트의 비전에 깊이 공감하며 시너지를 낼 수 있는 팀원을 찾는 데 집중했습니다. 이 과정에서 최적의 팀 빌딩을 위해 다양한 현업 선배 및 지인들에게 조언을 구하며 객관적인 시각을 유지하고자 노력했습니다. 그 결과, 저와 가장 결이 맞고 같은 목표를 향해 몰입할 수 있는 두 분을 최종 팀원으로 모시게 되면서 현재의 탄탄한 팀을 구성하게 되었습니다.

### 손현경

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: 프론트엔드, 백엔드보다는 통계학 지식을 베이스로 한 AI 자체에 더 관심이 많았기 때문에 AI 모델을 만드는 경험이 많습니다. 다수의 공모전에 참여했고, 예측 모델을 만드는 공모전에서 시계열 지식 기반의 모델을 만들어 본 경험이 있습니다. 그 외에도 Computer Vision 수업에서 사람 이미지에 옷 이미지를 합성해주는 서비스를 개발해 발표한 경험이 있습니다.

다수의 운영진 경험, 과대표 경험이 있기 때문에 여러 의견을 듣고 방향을 결정하는데 익숙한 편입니다. 이런 지점이 저희 팀이 프로젝트를 진행함에 있어 방향성을 잡는데 도움될 거라고 생각합니다. 그 이외에도 1년 간 프로젝트를 진행하다보니 성실함, 연락의 빈도가 중요하다고 생각합니다. 이미 약 2년 간 운영진, 팀프로젝트 경험을 통해 협업의 중요성을 체감할 수 있었고, 이를 위해 깃허브, 슬랙, 지라, 노션, 디스코드 등 다수의 협업 툴 또한 익혀본 경험이 있습니다. 저희 팀의 협업에 큰 도움이 될 거라고 생각합니다.
- **이번에 팀이 구성된 계기**: 현재 서울대학교 NLP 랩실에서 인턴 생활 중에 있습니다. 관심 연구 주제가 knowledge injection이라서 해당 분야로 팀원을 모집하다가 온톨로지에 관심이 많은 팀원을 만나게 됐고, 연구 트랙으로 함께 졸업 프로젝트를 진행하게 됐습니다.

## 5. 개인별 5 Questions

### 박세령

- **질문당 한줄씩 5개의 질문**: 1. 대형 언어모델의 성능 향상을 위해, 모델 내부 구조를 변경하는 접근(예: 파인튜닝, LoRA 등)과 외부 구조를 활용하는 접근(예: RAG, Knowledge Augmentation)은 각각 어떤 특성과 한계를 가지는가?
2. 내부 구조 변경 방식과 외부 구조 활용 방식은 일반적인 벤치마크(예: MMLU, TruthfulQA 등)에서 어떤 성능 차이를 보이며, 각 접근 방식의 강점은 어떤 상황에서 더 두드러지는가?
3. 두 접근 방식은 학습 비용, 추론 비용, 데이터 요구사항 측면에서 어떤 trade-off를 가지며, 실제 산업 환경에서는 어떤 방식이 더 현실적인가?
4. 하이브리드 접근 가능성 질문 - 모델 내부 구조 변경과 외부 지식 주입 방식을 결합한 하이브리드 접근은 단일 접근 방식 대비 어떤 성능 향상을 기대할 수 있는가?
5. 일반화 가능성 질문  - 특정 도메인에 의존하지 않고, 다양한 태스크 및 벤치마크에서 일관되게 성능을 향상시키는 AI 시스템 설계 방법론은 어떻게 정의될 수 있는가?

### 이다영

- **질문당 한줄씩 5개의 질문**: 1. 현재 LLM 모델들의 발전 방향성은 어떻게 되는가?
2. 온톨로지라는 것이 어떠한 경쟁적 요소를 가할것인가?
3.  지식 그래프의 복잡도가 RAG 시스템의 성능(Latency)에 미치는 영향은 무엇일까
4. 그래프 구조를 활용한 멀티홉(Multi-hop) 추론의 신뢰성 검증은 무엇이 있을까?
5. 새로운 지식이 유입될 때마다 사람이 직접 온톨로지를 설계하는 대신, LLM이 비정형 텍스트에서 새로운 엔티티와 관계를 추출하여 기존 온톨로지 스키마에 모순 없이 자동 병합하게 할 수 있는 알고리즘은 무엇인가?

### 손현경

- **질문당 한줄씩 5개의 질문**: 1. 지식 충돌 문제: 모델이 미리 배운 내용(FT)과 새로 검색해온 내용(RAG)이 다를 때, 어떤 정보를 우선하도록 설계해야 하는가?

2. 구조적 이해 문제: 온톨로지의 복잡한 관계 정보를 LLM이 단순 텍스트가 아닌 '논리적 연결 고리'로 이해하게 하려면 어떻게 학습시켜야 하는가? 

3. 효율성 문제: 모든 지식을 모델에 넣기엔 비용이 크고 검색만 하기엔 속도가 느린데, '암기할 지식'과 '찾아볼 지식'의 최적의 비율은 무엇인가? 

4. 평가 지표 문제: 단순히 정답을 맞히는 것 외에, '두 방식을 섞어서 실제로 더 똑똑해졌다'는 것을 입증할 수 있는 객관적인 지표는 무엇인가? 

5. 범용성 유지 문제: 특정 전문 분야에 특화시키면서도(Domain-specific), 모델이 가진 원래의 일반적인 추론 능력을 잃지 않게 하는 방법은 무엇인가?

## 6. 기반 소프트웨어 리스트

- **env**: 1. 클라이언트 및 플랫폼 (Client & Platform)
Target: 웹 브라우저 기반 (Multi-Device 지원)
환경: 데스크톱/노트북(Windows, Mac, Linux) 및 모바일 브라우저 최적화
특이사항: 별도의 네이티브 앱(iOS/Android)이나 엔진(Unity/Unreal)을 사용하지 않는 Web-Standard 방식 채택

2. 프론트엔드 (Front-end)
Framework: Vue 3 (Composition API)
Build Tool: Vite (고속 번들링 및 개발 서버)
Key Libraries:
1. UI/Design: Vuestic UI, Element Plus, Tailwind CSS
2. Visualization: vis-network (온톨로지 그래프 시각화 핵심)
3. Content: marked, github-markdown-css (문서 렌더링)
4. Communication: axios, vue-router

3. 백엔드 (Back-end)
Language: Python 3.x
Framework: FastAPI (고성능 비동기 API 프레임워크)
Server: Uvicorn (ASGI)
Key Libraries: 
1. Core: Pydantic (데이터 검증), python-dotenv (환경 변수 관리) 
2. Async: FastAPI CORS Middleware, Threading (LLM 작업 병렬 처리)

4. 데이터 관리 (Data Management)
Storage Strategy: File System Based Storage (No-DB Architecture)

5. 외부 서비스 및 AI 모델 (External API & AI)
Main LLM: OpenAI API (GPT-5 계열 모델)
- **url**: https://www.python.org/downloads/ (Python 3.10+ 언어 환경)
https://code.visualstudio.com/ (VS Code 코드 에디터)
https://www.docker.com/products/docker-desktop/ (Neo4j 및 DB 컨테이너 관리)
https://neo4j.com/deployment-center/ (Neo4j Desktop - 온톨로지 시각화 및 관리)
https://protege.stanford.edu/ (Protégé - 온톨로지 설계 및 편집 표준 도구)
https://www.postman.com/downloads/ (API 테스트 및 디버깅)
https://git-scm.com/downloads (버전 관리 시스템)

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
