# 2026 Spring 전체 프로젝트 리스트 

| 팀번호 | 팀명 | 트랙 | 프로젝트명 |
|:------:|------|:----:|------------|
| [1](#team-1) | 이사장님 | 연구 | 테스트 이미지의 도메인을 자동으로 파악해 텍스트와 이미지 임베딩을 동적으로 재조합함으로써 도메인 변화에도 정확한 CLIP 기반 Zero-Shot 이미지 분류 연구 |
| [2](#team-2) | Sudo | 산학 | HealthMate AI: 만성질환 위험군 대상 식단 인식·코칭 통합 헬스케어 플랫폼 |
| [3](#team-3) | Alltology | 연구 | 일반 벤치마크를 활용한 LLM 내부 파라미터 확장과 온톨로지 기반 지식 증강 기법의 실증적 성능 비교 및 융합 방법론 연구 |
| [5](#team-5) | 규교굥 | 산학 | 생성형 AI NPC와 흥정하는 골동품 가게 운영 시뮬레이션 게임 |
| [6](#team-6) | Greenfield | 산학 | 	AI 역사 인물 인터랙션과 다국어 스토리 콘텐츠 기반 역사 관광 활성화 웹 플랫폼 |
| [7](#team-7) | reverdir | 산학 | 익명 매칭부터 미션, 쪽지, 힌트, 랭킹, 정체 공개까지 마니또 활동 전 과정을 지원하는 마니또 소셜 플랫폼 |
| [8](#team-8) | 하면된다 | 산학 | AI 기반 가격 검증과 정시 경매 시스템으로 정보 비대칭과 탐색 피로를 해결하는 빈티지 거래 플랫폼 |
| [9](#team-9) | Cloud9 | 산학 | 퀀트 전략 실시간 상태 모니터링 및 이상 징후 탐지 시스템 |
| [10](#team-10) | 212223 | 산학 | 프롬프트 자동 최적화 기반 LLM API 비용 실시간 비교 웹 서비스 |
| [11](#team-11) | 알고리듬 | 산학 |  SpeedSchedule: 인력 운영 최적화를 위한 AI 스케줄링 및 시간표 관리 웹 플랫폼 |
| [12](#team-12) | 404 | 산학 | 여성 1인 여행자를 위한 DB 기반 가이드맵 및 안전 동행 매칭 서비스 |
| [13](#team-13) | Semicolone; | 산학 | AI 질문을 ‘기억되는 인사이트’로 바꿔주는 개인 지식 관리 플랫폼 |
| [14](#team-14) | def | 연구 | 로컬 환경에서의 Agentic AI 병목 분석 및 성능 최적화: Apple silicon 온디바이스를 중심으로 |
| [15](#team-15) | 햄부기 | 연구 | 엣지 환경 배포를 위한 Vision Transformer 구조적 가지치기 및 경량화 파이프라인 구축과 성능 분석 |
| [16](#team-16) | 퓨터 | 산학| 성향 변화형 AI 캐릭터 기반 영어 회화 학습 서비스 |
| [17](#team-17) | SPY | 산학 | Moni: AI 기반 소비 예측과 맞춤형 챌린지를 결합한 개인화 소비 코칭 서비스 |
| [18](#team-18) | 디바트(deep-art) | 연구 | 멀티모달 AI 기반 배리어프리 오디오 도슨트 자동 생성 서비스 |
| [19](#team-19) | Logue | 산학 | 자연어 기반 데이터 분석 질의를 통해 조직의 데이터 접근성과 의사결정 속도를 향상시키는 AI 기반 데이터 분석 웹 인터페이스, Logue |

---

<a id="team-1"></a>
## Team 1 이사장님

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 테스트 이미지의 도메인을 자동으로 파악해 텍스트와 이미지 임베딩을 동적으로 재조합함으로써 도메인 변화에도 정확한 CLIP 기반 Zero-Shot 이미지 분류 연구 |
| 서비스명(브랜드) | DoFit |
| 트랙 | 연구 |
| 팀명 | 이사장님 |
| 팀구성 | 설영은, 신지민, 윤희서 |
| 팀지도교수 | 황의원 교수님 |
| 무엇을 만들고자 하는가 | CLIP(Contrastive Language–Image Pre-training)은 이미지와 텍스트를 함께 이해하는 멀티모달 AI 모델인데, 기존 방식은 스케치든 실사(이를 domain shift라고 봄) 사진이든 똑같은 클래스 대표 벡터로 판단해서 domain shift 상황에서 성능이 떨어지는 경우가 많다. 따라서 테스트 이미지가 들어오는 순간 "아 이건 ~~한 도메인이네"를 자동으로 파악하고, 그 도메인에 맞게 텍스트·이미지 임베딩을 동적으로 재조합하는 test-time domain adaptation 시스템을 만들고자 한다. |
| 고객 (누구를 위해) | 스케치, 회화, 위성사진, 의료 이미지처럼 학습 데이터와 도메인이 다른(domain shift가 발생하는) 이미지를 분류해야 하는데, 매번 새로 fine-tuning하기엔 데이터도 없고 비용도 부담스러운 연구자 및 ML 엔지니어 |
| Pain Point (해결할 문제) | 멀티모달 데이터는 도메인 차이(domain shift)가 발생하면 테스트 성능이 크게 저하된다. 특히 CLIP과 같은 Vision-Language Model(VLM)은 Zero-Shot downstream task 환경에서 학습 도메인과 테스트 도메인이 달라지는 순간 이미지-텍스트 간 정렬이 어긋나 분류 성능이 떨어진다. 기존의 멀티모달 도메인 적응(domain adaptation) 방식은 추가 학습 데이터나 fine-tuning이 필요해 비효율적이고 성능 향상도 제한적이다. 이를 해결하기 위해 별도의 재학습 없이 테스트 시점에서만 도메인을 자동으로 감지하고 적응하는 Test-Time Domain Adaptation 방식이 필요하다. |
| 사용 기술 | 본 연구에서는 다음과 같은 기술을 활용한다. <br><br>- Vision-Language Model (CLIP 기반): 이미지와 텍스트 정보를 함께 이해하는 멀티모달 모델<br>- MeanShift 기반 MTA (MeanShift for Test-Time Augmentation): 테스트 단계에서 augmented view들의 outlier를 자동 제거하고 robust한 이미지 임베딩을 획득하는 기법<br>- Test-Time Domain Adaptation: 테스트 단계에서 이미지의 도메인을 자동 추정하여 텍스트·이미지 임베딩을 동적으로 재조합하는 기법<br>- Stable Diffusion V2: 테스트 이미지로부터 다양한 augmented view를 생성하는 이미지 증강 모델<br>- Deep Learning Framework (PyTorch): 모델 학습 및 실험 환경 구축<br><br>또한 기존 CLIP의 고정 평균 프롬프트 앙상블을 베이스라인으로 설정하고, 도메인 가중 동적 임베딩 재조합 방식과의 성능을 비교하여 domain shift 환경에서의 성능 개선 여부를 분석한다. |
| 개발환경 | 1. Client 디바이스: PC(Windows, Mac) 및 GPU 서버 기반 연구 환경<br>2. 딥러닝 프레임워크: Python/PyTorch/CUDA 기반 GPU 환경<br>3. 데이터셋: ImageNet 계열 5종(ImageNet, ImageNet-A, ImageNet-V2, ImageNet-R, ImageNet-Sketch) + 특정 도메인 10종(SUN397, Aircraft, EuroSAT, StanfordCars, Food101, OxfordPets, Flower102, Caltech101, DTD, UCF101)<br>4. 활용 모델: CLIP 기반 Vision-Language Model<br>5. 사전학습 모델: CLIP pretrained model (ViT 기반)<br>6. 라이브러리: NumPy, Pandas, Matplotlib, TensorBoard 등<br>7. 이미지 증강: Stable Diffusion V2, RandomCrop |
| 사용하는 소프트웨어 URL | 1. CLIP 공식 코드베이스: https://github.com/openai/CLIP<br>2. DiffTPT 코드베이스: https://github.com/chunmeifeng/DiffTPT<br>3. MTA 코드베이스: https://github.com/MaxZanella/MTA<br>4. ImageNet 데이터셋: [https://www.image-net.org](https://www.image-net.org/)<br>5. HuggingFace (사전학습 모델 허브): [https://huggingface.co](https://huggingface.co/) |
| 기대 효과 | 본 연구를 통해 domain shift 환경에서도 강건한 이미지 분류 모델 개발, Zero-Shot 분류 정확도 향상, 새로운 도메인 환경에서도 추가 fine-tuning 없이 활용 가능한 모델 제안과 같은 효과를 기대할 수 있다. 또한 본 연구에서 제안하는 test-time domain adaptation 방법론은 멀티모달 모델의 domain shift 문제를 다루는 다양한 downstream task로 확장될 수 있으며, 데이터 확보가 어려운 특수 도메인 분야에서 멀티모달 AI 연구의 활용 가능성을 확대할 것으로 기대된다. |
| GitHub Repo | [https://github.com/chairwomans/chairwomans-capstone](https://github.com/chairwomans/chairwomans-capstone) |
| Team Ground Rule | [Team Ground Rule](https://github.com/chairwomans/chairwomans-capstone/blob/main/Team_Ground_Rule.md) |
| 최종수정일 | 2026-04-14 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-2"></a>
## Team 2 Sudo

| 항목 | 내용 |
|------|------|
| 프로젝트명 | HealthMate AI: 만성질환 위험군 대상 식단 인식·코칭 통합 헬스케어 플랫폼 |
| 서비스명(브랜드) | 온케어 (On-Care) |
| 트랙 | 산학 |
| 팀명 | Sudo |
| 팀구성 | 최지수, 박서연, 신수빈 |
| 팀지도교수 | 황의원 교수님 |
| 무엇을 만들고자 하는가 | 만성질환(고혈압·당뇨·이상지질혈증) 위험군을 대상으로, 식단 사진 한 장으로 영양소를 자동 분석하고 개인 건강 이력 기반의 AI 코칭을 제공하는 통합 헬스케어 모바일 플랫폼 On-Care. 식단 인식, 운동 코칭, AI 챗봇 상담, 헬스장 검색·예약, 건강 일정 관리, 포인트 보상을 하나의 앱에서 제공한다. |
| 고객 (누구를 위해) | -**1차 타겟**: 고혈압·당뇨·이상지질혈증 등 만성질환 위험군에 해당하는 2030세대. 건강 관리의 필요성은 인식하지만 복잡한 기록·관리 방식에 진입 장벽을 느끼는 사용자.<br> -**2차 타겟**: 담당 트레이너와 연동해 고객 데이터를 효율적으로 파악하고자 하는 헬스 트레이너 및 헬스장 운영자. |
| Pain Point (해결할 문제) | **① 파편화된 건강 관리**: 식단, 운동, 병원 일정을 별도 앱에서 따로 관리해야 해 지속성이 낮음<br> **② 식단 기록의 높은 진입 장벽**: 기존 앱은 텍스트 수동 입력·바코드 스캔에 의존해 번거롭고 기록 이탈률이 높음<br> **③ 획일적 AI 조언**: 개인 건강 이력·식단 로그·질환 정보를 반영하지 못하는 일반적 정보만 제공<br> **④ 트레이너 연동 부재**: 이용자의 건강 데이터를 트레이너에게 전달하는 인앱 채널이 없어 맞춤 지도가 어려움<br> **⑤ 동기부여 지속성 부족**: 단기 목표 달성 후 앱 이탈이 빈번하고 장기 습관 형성을 유도하는 보상 메커니즘이 없음 |
| 사용 기술 | **AI/ML**: YOLOv8 (음식 이미지 1차 필터링으로 불필요한 API 호출 차단), Gemini Vision API (음식 종류·섭취량·영양소 세부 분석), GPT-4o (RAG 파이프라인 최종 답변 생성), LangChain (RAG 오케스트레이션), Pinecone (사용자 건강 이력 Vector DB), text-embedding-3-small (질문 임베딩)<br> **모바일**: Flutter 3.x (iOS/Android 크로스플랫폼), Riverpod (상태 관리), Dart<br> **백엔드**: FastAPI (REST API 서버), MySQL on AWS RDS (사용자·식단·운동·포인트 데이터), JWT 인증<br> **인프라**: Docker (컨테이너화), AWS EC2 (서버 배포), GitHub Actions (CI/CD 자동화), FCM (실시간 푸시 알림)<br> **외부 API**: 카카오맵 API (위치 기반 헬스장 검색), 공공데이터포털 식품영양성분 DB (칼로리·탄수화물·단백질·지방·나트륨 매핑) |
| 개발환경 | **OS**: macOS / Linux (Docker 기반 통일 환경)<br> **모바일 개발**: Flutter 3.x, Dart SDK, Android Studio / VS Code<br> **백엔드 개발**: Python 3.11+, FastAPI, SQLAlchemy, Uvicorn<br> **AI 모델 서빙**: PyTorch (YOLOv8 inference), Ultralytics 라이브러리<br> **클라우드**: AWS EC2 (백엔드 서버), AWS RDS MySQL (데이터베이스)<br> **컨테이너**: Docker, Docker Compose<br> **버전 관리 및 협업**: Git / GitHub, GitHub Actions (CI/CD), GitHub Projects (태스크 관리) |
| 사용하는 소프트웨어 URL | -Flutter: https://flutter.dev<br> -FastAPI: https://fastapi.tiangolo.com<br> -YOLOv8 (Ultralytics): https://github.com/ultralytics/ultralytics<br> -Google Gemini API: https://ai.google.dev<br> -OpenAI GPT-4o: https://openai.com<br> -LangChain: https://www.langchain.com<br> -Pinecone: https://www.pinecone.io<br> -Firebase FCM: https://firebase.google.com<br> -카카오맵 API: https://apis.map.kakao.com<br> -공공데이터포털 식품영양성분 DB: https://www.data.go.kr<br> -AWS (EC2 · RDS): https://aws.amazon.com<br> -Docker: https://www.docker.com |
| 기대 효과 | **① 식단 기록 자동화**: 사진 1장으로 칼로리·영양소 자동 분석, 기록 부담을 획기적으로 줄여 지속적 식단 관리 가능<br> **② 개인 맞춤 AI 코칭 실현**: RAG 파이프라인으로 인바디·식단 로그·운동 이력·질환 정보를 LLM에 주입, '내 데이터를 아는 AI 코치'로 일반 앱과 차별화<br> **③ 건강 관리 통합화**: 식단·운동·헬스장·병원 일정을 단일 플랫폼에서 관리해 앱 전환 비용 제거 및 데이터 연속성 확보<br> **④ 트레이너-이용자 연결**: AI가 이용자 데이터를 자동 요약해 트레이너에게 전달, 전문 지도의 질과 효율 향상<br> **⑤ 만성질환 예방 기여**: 2030세대의 조기 식습관·운동 습관 개선을 통해 고혈압·당뇨·이상지질혈증 발병 위험 감소에 기여<br> **⑥ 장기 지속성 확보**: 포인트·Streak 보상 시스템으로 사용자의 내재적 동기를 강화하고 장기적 건강 습관 형성 유도 |
| GitHub Repo | [https://github.com/CSE-Sudo-26/sudo-capstone-project](https://github.com/CSE-Sudo-26/sudo-capstone-project) |
| Team Ground Rule | [Team Ground Rule](https://github.com/CSE-Sudo-26/sudo-capstone-project/blob/main/Team_Ground_Rule.md) |
| 최종수정일 | 2026-04-13 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-3"></a>
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
## Team 5 규교굥

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 생성형 AI NPC와 흥정하는 골동품 가게 운영 시뮬레이션 게임 |
| 서비스명(브랜드) | Do Not Open This Box. |
| 트랙 | 산학 |
| 팀명 | 규교굥 |
| 팀구성 | 정혜교, 윤민주, 박남규 |
| 팀지도교수 | 윤명국 교수님 |
| 무엇을 만들고자 하는가 | 골동품 가게를 운영하는 3D 1인칭 시뮬레이션 게임. Ollama를 기반으로 한 손님과의 흥정으로 최대한 낮은 가격에 물건을 사고, 도구를 이용해 물건을 관리해야 하며, 적절한 가격을 매겨 손님에게 팔아야 한다. 돈을 많이 벌 수록 물건을 더 많이 사고 가게를 확장할 수 있다. 동시에 어떤 사건과 연관된 물건을 찾아 상자 안에 넣어야 한다. |
| 고객 (누구를 위해) | 평소 PC를 이용해 시뮬레이션 등의 게임을 즐겨하는 사람들과 영상 플랫폼을 이용해 이러한 게임들과 관련된 콘텐츠를 즐기는 사람들. |
| Pain Point (해결할 문제) | 기존의 'Supermarket Simulator'와 같은 경영 시뮬레이션 게임의 재미를 유지하되, 플레이어가 NPC와 선택지로만 대화하는 것이 아닌, AI NPC인 손님과 텍스트로 대화하며 플레이어가 실제 그 상황에 몰입하고 더 극대화된 재미를 느낄 수 있도록 하는 것이 목표이다. |
| 사용 기술 | 유니티 3D, Ollama |
| 개발환경 | 1. Client 디바이스: PC (Windows, Mac)<br>2. FE: Unity, Blender, Clip studio<br>3. BE: 초기에는 Standalone 형태로 개발 후, 필요 시 FastAPI 기반 서버 연동 예정<br>4. DB: 초기에는 로컬 데이터 저장 방식을 고려하고 있으며, 필요 시 MySQL 도입 예정<br>5. 특별한 라이브러리: Unity URP/2D Light, TextMeshPro, JsonUtility, Custom Render Feature, Shader Graph, Post Processing, Cinemachine<br>6. API Call 서비스:  로컬 LLM 또는 자체 호스팅 모델 검토 중
| 사용하는 소프트웨어 URL | 1. Client 디바이스: PC (Windows, Mac)<br>2. FE: Unity, Blender, Clip studio<br>3. BE: 초기에는 Standalone 형태로 개발 후, 필요 시 FastAPI 기반 서버 연동 예정<br>4. DB: 초기에는 로컬 데이터 저장 방식을 고려하고 있으며, 필요 시 MySQL 도입 예정<br>5. 특별한 라이브러리: Unity URP/2D Light, TextMeshPro, JsonUtility, Custom Render Feature, Shader Graph, Post Processing, Cinemachine<br>6. API Call 서비스:  로컬 LLM 또는 자체 호스팅 모델 검토 중
| 기대 효과 | 플레이어는 AI NPC 손님과 대화하며 흥정하는 재미를 느낄 수 있고 동시에 다양한 물건과 상호작용하여 직접 가게를 운영하는 듯한 몰입감을 느낄 수 있다. |
| GitHub Repo | [https://github.com/muffinhead03/Start2026_1](https://github.com/muffinhead03/Start2026_1) |
| Team Ground Rule | https://github.com/muffinhead03/Start2026_1/blob/main/Team_Ground_Rule.md |
| 최종수정일 | 2026.03.10 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-6"></a>
## Team 6 Greenfield

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 역사 스토리 콘텐츠와 역사 인물 챗봇을 활용한 관광 탐색 웹 플랫폼 |
| 서비스명(브랜드) | Histour |
| 트랙 | 산학 |
| 팀명 | Greenfield |
| 팀구성 | 최준희, 권은재, 김재희 |
| 팀지도교수 | 박현석 |
| 무엇을 만들고자 하는가 | 사용자에게 AI 기반 역사 스토리 콘텐츠(텍스트, 영상)와 역사 인물 챗봇과의 대화 기능을 제공하여 역사에 흥미를 느낄 수 있도록 유도한 후, 위 콘텐츠들과 관련한 관광지를 추천하여 대한민국 관광을 활성화할 수 있는 웹 플랫폼을 만들고자 한다. |
| 고객 (누구를 위해) | 역사에 큰 관심은 없지만 재미있는 콘텐츠에는 반응하는 20~30대 사용자<br>여행을 계획 중이거나, 새로운 여행지를 찾고 싶은 사용자<br>한국 문화를 경험해 보고 싶은 외국인<br>기존 관광 정보 서비스에 흥미를 느끼지 못한 사용자 |
| Pain Point (해결할 문제) | - 역사 정보를 흥미롭게 전달하는 매체 부족<br>- 외국인 관광객의 한국 역사 이해 및 관광 접근성 부족<br>- 학생들이 실제 역사 장소를 체험하며 학습할 기회 부족<br><br>스토리를 중심으로 역사 장소를 연결하여 외국인과 학생 모두가 한국 역사를 쉽게 이해하고 직접 체험할 수 있는 몰입형 문화관광 경험을 제공하는 것을 목표 |
| 사용 기술 | **프론트엔드**<br><br>- Next.js, React, TypeScript, Tailwind CSS, Kakao Maps API<br><br>**백엔드**<br><br>- Node.js , MySQL, FastAPI<br><br>**데이터 수집**<br><br>- 관광지 위치, 관광지 관련 이미지 및 텍스트 데이터 분석<br><br>**AI 및 추천 시스템**<br><br>- 스토리 기반 관광 코스 추천 알고리즘, LLM 기반 역사 요약 및 다국어 번역 |
| 개발환경 | 1. Client 디바이스를 PC로 제공<br>2. FE는 Next.js(React), TypeScript 사용<br>3. BE는 FastAPI 사용<br>4. DB는 PostgreSQL 사용<br>5. 사용하는 특별한 라이브러리는 FE ( Tailwind CSS, TanStack Query, Leaflet) / BE ( SQLAlchemy, Pydantic, Uvicorn) 사용<br>6. API Call로 사용할 서비스는 OpenAI 사용
| 사용하는 소프트웨어 URL | 1. Client 디바이스를 PC로 제공<br>2. FE는 Next.js(React), TypeScript 사용<br>3. BE는 FastAPI 사용<br>4. DB는 PostgreSQL 사용<br>5. 사용하는 특별한 라이브러리는 FE ( Tailwind CSS, TanStack Query, Leaflet) / BE ( SQLAlchemy, Pydantic, Uvicorn) 사용<br>6. API Call로 사용할 서비스는 OpenAI 사용
| 기대 효과 | 모두가 쉽게 이해하고 직접 체험할 수 있는 몰입형 문화 관광 경험을 제공하여 한국 역사에 대한 사람들의 관심과 흥미를 유도한다. 또한 이에 따른 한국 관광지 활성화를 목표로 한다. |
| GitHub Repo | [https://github.com/greenfield-2026-capstone/greenfield-project](https://github.com/greenfield-2026-capstone/greenfield-project) |
| Team Ground Rule | https://github.com/greenfield-2026-capstone/greenfield-project/blob/main/Team_Ground_Rule.md |
| 최종수정일 | 2026.4.12 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-7"></a>
## Team 7 reverdir

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 익명 매칭부터 모임 맞춤형 미션 및 힌트, 쪽지, 랭킹, 개인 맞춤형 결과 리포트까지 마니또 활동 전 과정을 지원하여 지인 간 구성된 소모임의 마니또 경험을 개선하는 마니또 소셜 앱 서비스 |
| 서비스명(브랜드) | 또마니또(ToManito) |
| 트랙 | 산학 |
| 팀명 | reverdir |
| 팀구성 | 전채연, Lyu Dongying, 이은효 |
| 팀지도교수 | 이미정 교수님 |
| 무엇을 만들고자 하는가 | ‘또마니또(ToManito)’는 기존 마니또 이벤트의 한계를 개선하기 위해, 익명성과 상호작용을 강화한 게임화된 소셜 플랫폼을 구축하는 것을 목표로 한다. 이 서비스는 초대 코드 및 초대 링크를 통한 소모임 방 구성을 지원하며, 자동 매칭을 통해 게임 진행의 편의성을 높인다. 이후에는 비밀 쪽지와 실시간 채팅 등 다양한 인터랙션 기능을 통해 이벤트 과정에서의 지속적인 참여와 몰입을 유도한다. 또한 AI를 활용하여 모임의 성격에 맞는 맞춤형 미션을 제공함으로써 단순한 선물 교환을 넘어선 능동적인 게임 경험을 설계한다. 나아가 이벤트 종료 후에는 사용자 행동 데이터를 분석해 개인화된 결과 리포트를 제공함으로써, 참여 경험을 하나의 기록이자 콘텐츠로 축적하고 공유할 수 있도록 한다. 이를 통해 ‘또마니또’는 일회성 이벤트를 반복 가능한 소셜 경험으로 확장하는 앱 서비스를 지향한다. |
| 고객 (누구를 위해) | 이 프로젝트의 주요 고객은 마니또 이벤트를 기획하고자 하는 사람들로, 학교, 직장, 동아리 등 소규모 그룹의 구성원들이다. 특히 기존 오프라인 마니또의 번거로움이나 재미 부족을 경험한 사용자들을 주 타겟으로 한다. 이들은 마니또 이벤트를 더 재미있고 효율적인 방식으로 진행하고 싶어하며, 기존 방식에서 겪었던 문제들을 해결할 수 있는 더 나은 방법을 찾는다. |
| Pain Point (해결할 문제) | 수작업 관리의 번거로움: 기존 오프라인 마니또 이벤트는 모든 과정을 수작업으로 관리해야 하며, 이로 인해 관리가 복잡하고 시간이 많이 소요될 뿐 아니라 진행자는 마니또 이벤트 참여에 어려움을 겪게 된다.<br>익명성 부족: 참여자 간 익명성이 보장되지 않아 이벤트의 핵심인 비밀성과 재미가 쉽게 훼손되며 이로 인해 이벤트 몰입도가 낮다.<br>빈약한 콘텐츠와 참여 동기 저하: 제공되는 콘텐츠가 제한적이어서 지속적인 흥미 유도가 어렵고, 결과적으로 참여자의 몰입도가 낮아진다. |
| 사용 기술 | FE: Flutter (Dart) — 실시간 상호작용 기반 모바일 UI/UX 구현<br>BE: Spring Boot (Java) — API 서버 및 비즈니스 로직 처리<br>DB: PostgreSQL — 사용자 및 이벤트 데이터 관리<br>Library: OAuth (카카오/구글) — 간편 로그인 및 사용자 인증 처리<br>API Call: FCM(Firebase Cloud Messaging) — 실시간 푸시 알림 (미션, 이벤트, 결과 안내)<br>Kakao Link API — 초대 링크 기반 사용자 유입 및 공유 기능<br>OpenAI GPT-40 API — 맞춤형 미션 생성 및 사용자 행동 기반 리포트 생성 |
| 개발환경 | Client Device: Mobile (Android)<br>FE: Flutter (Dart)<br>BE: Spring Boot (Java)<br>DB: PostgreSQL<br>Auth: OAuth<br>API Call: FCM(Firebase Cloud Messaging), Kakao Link API, OpenAI GPT-40 API |
| 사용하는 소프트웨어 URL | Device: Mobile(Android)<br>FE: Flutter (Dart)<br>BE: Spring Boot (Java)<br>DB: PostgreSQL<br>Auth: OAuth<br>API Call: FCM(Firebase Cloud Messaging), Kakao Link API
| 기대 효과 | '또마니또'를 통해 얻을 수 있는 주요 효과는 참여자들이 마니또 이벤트를 보다 재미있고 몰입감 있게 경험할 수 있다는 것이다. 게임화된 시스템과 AI 기반의 맞춤형 미션은 사용자들의 흥미를 유지하며, 플랫폼에서 제공하는 익명성을 통해 사용자들의 마니또 경험을 개선한다. 또한, 게임 종료 후에는 AI가 참여자들의 활동을 분석하여 캐릭터화된 결과 리포트를 각 사용자에게 제공한다. 이를 통해 사용자들이 마니또 이벤트를 단발적 이벤트가 아닌, 즐거웠던 경험으로 기억 속에 남길 수 있게 한다. 이와 같은 기능의 흐름은 마니또 이벤트가 단순히 선물 교환에 그치지 않고, 지속적인 상호작용을 통해 사용자들 간 관계 증진을 촉발할 수 있게 한다. 이러한 경험은 동일하거나 다른 소모임에서의 반복 사용으로 이어져 서비스의 자연스러운 확산과 사용자 리텐션 향상 또한 기대할 수 있다. |
| GitHub Repo | [https://github.com/team-capstone-reverdir-2026/reverdir_repo](https://github.com/team-capstone-reverdir-2026/reverdir_repo) |
| Team Ground Rule | https://github.com/team-capstone-reverdir-2026/reverdir_repo/blob/main/Team_Ground_Rule.md |
| 최종수정일 | 2026.04.12 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-8"></a>
## Team 8 하면된다

| 항목 | 내용 |
|------|------|
| 프로젝트명 | AI 기반 가격 검증과 정시 경매 시스템으로 정보 비대칭과 탐색 피로를 해결하는 빈티지 거래 플랫폼 |
| 서비스명(브랜드) | Vintic |
| 트랙 | 산학 |
| 팀명 | 하면된다 |
| 팀구성 | 김수연, 이예주, 조채윤 |
| 팀지도교수 | 오세은 교수님 |
| 무엇을 만들고자 하는가 | 판매자가 제시한 가격이 적절한지 AI가 함께 검증하고, 구매자는 정해진 시간에 열리는 경매를 통해 상품을 효율적으로 탐색할 수 있도록 하여, 빈티지 거래 과정에서 발생하는 가격 판단의 어려움과 무한 탐색의 피로를 줄이는 플랫폼을 구현합니다. |
| 고객 (누구를 위해) | 빈티지 거래 플랫폼 이용자 |
| Pain Point (해결할 문제) | (1) 가격 정보의 불균형: 판매자가 상품 가격을 임의로 책정하는 경우가 많아, 구매자가 적정 가격을 판단하기 어려운 구조</br>(2) 구매자의 탐색 피로: 원하는 매물의 업로드 시점을 알기 어려워, 사용자가 플랫폼에 반복적으로 접속하며 무한 스크롤링을 지속하는 문제</br>(3) 판매글 노출의 비효율: 게시글이 업로드 시점에 따라 쉽게 묻혀, 판매자가 동일한 글을 반복 업로드해야 하는 비효율 |
| 사용 기술 | Vision AI(FastAPI+상용 API), Spring, React 등 |
| 개발환경 | 1.Client Device: Wep App<br>2.FE(Web)<br>Core: React, TypeScript, Next.js<br>State Management: TanStack Query, Zustand<br>Styling: Emotion<br>CI/CD: GitHub Actions<br>3.BE:SpringBoot,docker<br>4.DB:MySQL<br>5.BE:Spring Data JPA,Spring WebSockets FE:Emotion,TanStack Query,Zustand<br>6.API Call 서비스:OpenAI API(GPT-4o Vision)
| 사용하는 소프트웨어 URL | 1.Client Device: Wep App<br>2.FE(Web)<br>Core: React, TypeScript, Next.js<br>State Management: TanStack Query, Zustand<br>Styling: Emotion<br>CI/CD: GitHub Actions<br>3.BE:SpringBoot,docker<br>4.DB:MySQL<br>5.BE:Spring Data JPA,Spring WebSockets FE:Emotion,TanStack Query,Zustand<br>6.API Call 서비스:OpenAI API(GPT-4o Vision)
| 기대 효과 | (1) 상품별 AI 측정가와 판매자 희망가 병기를 통한 가격 판단 기준 제공</br>(2) AI 측정가와 희망가 차이 제한을 통한 가격 신뢰도 향상</br>(3) 특정 시각 일괄 경매 방식을 통한 구매자 탐색 피로 완화 및 판매자 노출 기회의 공정성 확보 |
| GitHub Repo | [https://github.com/hamyeon/Team-Hamyeon](https://github.com/hamyeon/Team-Hamyeon) |
| Team Ground Rule | [Team Grouond Rule](https://github.com/hamyeon/Team-Hamyeon/blob/main/Team_Ground_Rule.md) |
| 최종수정일 | 2026.03.16 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-9"></a>
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
## Team 10 212223

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 프롬프트 자동 최적화 기반 LLM API 비용 실시간 비교 웹 서비스 |
| 서비스명(브랜드) | |
| 트랙 | 산학 |
| 팀명 | 212223 |
| 팀구성 | 고윤진(2176018), 김나현(2276040), 이유진(2376218) |
| 팀지도교수 | 심재형 교수님 |
| 무엇을 만들고자 하는가 | 사용자가 프롬프트를 입력하면 각 AI 모델(GPT-4, Gemini, Claude 등)의 최적화된 프롬프트를 추천 후 그에 따른 예상 비용을 실시간으로 계산하고 비교하는 웹 서비스 |
| 고객 (누구를 위해) | Ai api를 사용하는 학생 및 개발자, 스타트업 등 비용에 민감한 사용자 |
| Pain Point (해결할 문제) | AI 프롬프트 작성 미숙으로 인한 과다한 비용 청구 |
| 사용 기술 | Tailwind, Next.js, FastAPI, tiktoken,LangChain,LLMLingua,Firebase Firestore |
| 개발환경 | 1. Client 디바이스: PC(Windows, Mac)<br>2. FE:React.js ,TailwindCSS<br>3. BE:FastAPI (Python)<br>4. DB: Firebase Firestore<br>5. AI/LLM: tiktoken<br>6. 외부 API: OpenAI / Anthropic / Google AI SDK<br>7.크롤러: BeautifulSoup<br>8. 배포: Vercel (프론트) + Railway or Render (백엔드)<br>9. FE또는 BE에 사용하는 특별한 라이브러리:LiteLLM(백엔드),TanStack Query(프론트엔드)
| 사용하는 소프트웨어 URL | 1. Client 디바이스: PC(Windows, Mac)<br>2. FE:React.js ,TailwindCSS<br>3. BE:FastAPI (Python)<br>4. DB: Firebase Firestore<br>5. AI/LLM: tiktoken<br>6. 외부 API: OpenAI / Anthropic / Google AI SDK<br>7.크롤러: BeautifulSoup<br>8. 배포: Vercel (프론트) + Railway or Render (백엔드)<br>9. FE또는 BE에 사용하는 특별한 라이브러리:LiteLLM(백엔드),TanStack Query(프론트엔드)
| 기대 효과 | AI 사용성 계선 및 비용 감소 |
| GitHub Repo | [https://github.com/0727n1122-beep/graduationproject/tree/main](https://github.com/0727n1122-beep/graduationproject/tree/main) |
| Team Ground Rule | [Team Ground Rule](https://github.com/0727n1122-beep/graduationproject/blob/main/Team_Ground_Rule.md) |
| 최종수정일 | 03.16 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-11"></a>
## Team 11 알고리듬

| 항목 | 내용 |
|------|------|
| 프로젝트명 | SpeedSchedule: 인력 운영 최적화를 위한 AI 스케줄링 및 시간표 관리 웹 플랫폼 |
| 서비스명(브랜드) | 우리학교시간표 |
| 트랙 | 산학 |
| 팀명 | 알고리듬 |
| 팀구성 | PM / 조상은 / 컴퓨터공학과 / 2376273 <br> FE&Design / 정지유 / 국제사무학과 / 2416023 <br> BE&AI / 이시은 / 컴퓨터공학과 / 2466044 |
| 팀지도교수 | 오세은 교수님  |
| 무엇을 만들고자 하는가 | 인력 운영 최적화를 위한 AI 스케줄링 및 시간표 관리 웹 플랫폼.<br>교내의 복잡한 수업 시간표와 감독 배정 업무를 데이터 기반으로 자동화하며, 실시간 수정이 가능한 인터렉티브 캘린더와 결원 발생기 대리 근무자를 매칭해주는 기능까지 통합된 관리 솔루션. |
| 고객 (누구를 위해) | 학교 현장의 행정 관리자와 교사 |
| Pain Point (해결할 문제) | 기존 시스템은 AI 최적화가 없는 단순 알고리즘이라 교사 개개인의 선호도나 숙련도 반영이 불가능함. 이로 인해 관리자가 엑셀로 2차 수동 수정을 거치는 등 행정력이 낭비됨. <br> 또한 가나다순/ 고정 순번제 배정은 특정 인원에게 업무가 쏠리는 불균형을 초래하여 조직 내 공정성 시비와 만족도 저하를 일으킴. |
| 사용 기술 | AI : 딥러닝 기반 스케줄 최적화 알고리즘 (PyTorch / TensorFlow) <br> FE : React, Vite, Axios, Vercel, ESLint <br> BE : SpringBoot 3, MySQL, Hibernate(JPA), Docker, Gradle <br> DevOps : Docker, GitHub Action <br> Infra : AWS EC2 (Amazon Linux), AWS RDS
| 개발환경 | 1. Web -> PC 권장<br>2. javaScript<br>3. spring<br>4. MySQL 인데 PostgreSQL로 이전 고려중<br>5. Redis 캐싱<br>6. OpenAI
| 사용하는 소프트웨어 URL | 1. Web -> PC 권장<br>2. javaScript<br>3. spring<br>4. MySQL 인데 PostgreSQL로 이전 고려중<br>5. Redis 캐싱<br>6. OpenAI
| 기대 효과 | 스케줄링 업무 자동화를 통한 행정 비용 절감 및 운영 효율성 극대화. <br> 데이터 기반의 객관적 배정 시스템을 통한 운영의 투명성 확보. <br> 교사 업무 만족도 향상 및 조직 내 인력 운영 효율성 극대화.  |
| GitHub Repo | [https://github.com/speedSchedule/AlgoRhythm](https://github.com/speedSchedule/AlgoRhythm) |
| Team Ground Rule | [Team_Ground_Rule.md](https://github.com/speedSchedule/AlgoRhythm/blob/main/Team_Ground_Rule.md) |
| 최종수정일 | 2025/04/09 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-12"></a>
## Team 12 404

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 여성 1인 여행자를 위한 DB 기반 가이드맵 및 안전 동행 매칭 서비스 |
| 서비스명(브랜드) | 여기지! (여성 기행 지켜!) |
| 트랙 | 산학 |
| 팀명 | 404 |
| 팀구성 | 이아림, 노유나, 이채원  |
| 팀지도교수 |  |
| 무엇을 만들고자 하는가 | 여성 혼자 여행하는 사람들을 위한 안전 중심 여행 플랫폼을 개발하고자 한다. 여성 사용자들이 직접 작성한 안전 리뷰 데이터를 기반으로 여행지의 안전도를 지도에 표시하고, 이를 활용해 안전한 여행 경로와 맛집 및 관광 코스를 추천한다. 또한 같은 지역을 여행하는 여성들 간 동행 매칭 기능을 제공하여 안전하고 편안한 여행 환경을 만드는 것을 목표로 한다. |
| 고객 (누구를 위해) | 20대 초반 여성교환 학생, 사회초년생 여성 직장인(20대 중후반) |
| Pain Point (해결할 문제) | 여성의 안전 정보 부족과 혼자 여행할 때의 불안감 |
| 사용 기술 | [AI] OpenAI API <br> [Frontend] React, Google Maps Platform, HTML / CSS / JavaScript <br> [Backend] Node.js, Express.js<br> [Database] MySQL |
| 개발환경 | 1. Client 디바이스는 Windows를 기반으로 한 PC로 한다.<br>2. FE는  React를 사용한다.<br>3. BE는 FastAPI를 기반으로 구현한다.<br>4. DB는 MySQL를 사용한다.<br>5. FE또는 BE에 사용하는 특별한 라이브러리는 Google Maps JavaScript API를 활용하여 지도 기반 기능을 구현한다.<br>6. API Call을 위해 OpenAI 서비스를 사용한다.
| 사용하는 소프트웨어 URL | 1. Client 디바이스는 Windows를 기반으로 한 PC로 한다.<br>2. FE는  React를 사용한다.<br>3. BE는 FastAPI를 기반으로 구현한다.<br>4. DB는 MySQL를 사용한다.<br>5. FE또는 BE에 사용하는 특별한 라이브러리는 Google Maps JavaScript API를 활용하여 지도 기반 기능을 구현한다.<br>6. API Call을 위해 OpenAI 서비스를 사용한다.
| 기대 효과 | 여성 1인 여행자가 안전하고 효율적으로 여행을 계획할 수 있고, 여성의 이동권과 안전권을 기술적으로 보장한다. |
| GitHub Repo | [https://github.com/capstone-team404](https://github.com/capstone-team404) |
| Team Ground Rule | (https://github.com/capstone-team404/Spring404/blob/main/Team_Ground_Rule.md) |
| 최종수정일 | 26.03.16 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---
<a id="team-13"></a>
## Team 13 Semicolone;

| 항목 | 내용 |
|------|------|
| 프로젝트명 | AI 질문을 ‘기억되는 인사이트’로 바꿔주는 개인 지식 관리 플랫폼 |
| 서비스명(브랜드) | Flow(플로우) |
| 트랙 | 산학 |
| 팀명 | Semicolone; |
| 팀구성 | 신지원, 이채원, 윤현진 |
| 팀지도교수 | 이미정 |
| 무엇을 만들고자 하는가 | AI 기반 질문 기록 및 인사이트 내재화 플랫폼을 만들고자 한다. 최근 많은 사람들이 ChatGPT와 같은 생성형 AI를 통해 다양한 질문을 하고 정보를 얻고 있지만, 대부분의 대화 내용은 일회성으로 소비되고 이후에는 다시 활용되지 않는 경우가 많다. 본 서비스는 사용자가 AI에게 질문했던 내용과 답변을 기록하고, 이를 AI가 자동으로 정리하고 연결하며, 시간이 지나 다시 노출하여 장기 기억으로 내재화하도록 돕는 개인 지식 관리 시스템이다. 단순히 AI 대화를 저장하는 것이 아니라 사용자가 얻은 인사이트를 정리하고 필요할 때 다시 활용할 수 있도록 돕는 것을 목표로 한다. |
| 고객 (누구를 위해) | 본 서비스의 주요 고객은 생성형 AI를 자주 활용하는 사용자들이다. 특히 학습이나 과제, 프로젝트, 창업 아이디어 탐색 등을 위해 AI에게 질문을 자주 하는 대학생과 지식 노동자를 주요 타겟으로 한다. 또한 업무나 공부 과정에서 AI를 활용해 정보를 탐색하지만 대화 내용을 체계적으로 정리하거나 다시 활용하지 못하는 사용자들에게도 유용한 서비스가 될 수 있다. |
| Pain Point (해결할 문제) | 최근 생성형 AI 사용이 증가하면서 사용자들은 다양한 질문을 통해 많은 정보를 얻고 있다. 그러나 대부분의 AI 대화는 일회성으로 끝나고 시간이 지나면 어떤 질문을 했는지, 어떤 답변을 받았는지 기억하기 어렵다. 또한 AI 대화 기록은 길고 복잡한 경우가 많아 필요한 정보를 다시 찾기 어렵고, 중요한 인사이트가 묻히는 문제가 발생한다. 이로 인해 사용자는 많은 질문을 통해 정보를 얻지만 실제로 자신의 지식으로 축적되거나 활용되는 경우는 제한적이라는 문제가 발생한다. |
| 사용 기술 | 프론트엔드 <br> React.js <br> 사용자 입력 중심 UI/UX 설계 (질문·답변 입력, 인사이트 탐색) <br> 상태 관리 (Zustand 또는 Context API) <br> 반응형 웹 UI 구현 <br>  <br> 🔹 백엔드 <br> Spring Boot (Java) <br> RESTful API 설계 및 데이터 처리 <br> 사용자 인증 및 권한 관리 (Spring Security + JWT) <br> 스케줄링 기반 리마인드 기능 구현 <br>  <br> 🔹 데이터베이스 <br> MySQL / PostgreSQL <br> 사용자 질문, 답변, 인사이트 데이터 저장 <br> 카테고리 및 태그 기반 데이터 구조 관리 <br>  <br> 🔹 AI 및 데이터 처리 <br> OpenAI API (LLM) <br> 질문·답변 기반 핵심 요약 생성 <br> 키워드 추출 및 인사이트 도출 <br> 텍스트 임베딩 (Embedding) 기반 유사도 분석 <br> 인사이트 간 의미적 유사성 계산 <br> 관련 인사이트 추천 기능 구현 |
| 개발환경 | Client 디바이스:Pc(windows)<br>프론트엔드<br>React.js<br>사용자 입력 중심 UI/UX 설계 (질문·답변 입력, 인사이트 탐색)<br>상태 관리 (Zustand 또는 Context API)<br>반응형 웹 UI 구현<br>🔹백엔드<br>Spring Boot (Java)<br>RESTful API 설계 및 데이터 처리<br>사용자 인증 및 권한 관리 (Spring Security + JWT)<br>스케줄링 기반 리마인드 기능 구현<br>🔹 데이터베이스<br>MySQL / PostgreSQL<br>사용자 질문, 답변, 인사이트 데이터 저장<br>카테고리 및 태그 기반 데이터 구조 관리<br>🔹 AI 및 데이터 처리<br>OpenAI API (LLM)<br>질문·답변 기반 핵심 요약 생성<br>키워드 추출 및 인사이트 도출<br>텍스트 임베딩 (Embedding) 기반 유사도 분석<br>인사이트 간 의미적 유사성 계산<br>관련 인사이트 추천 기능 구현
| 사용하는 소프트웨어 URL | Client 디바이스:Pc(windows)<br>프론트엔드<br>React.js<br>사용자 입력 중심 UI/UX 설계 (질문·답변 입력, 인사이트 탐색)<br>상태 관리 (Zustand 또는 Context API)<br>반응형 웹 UI 구현<br>🔹백엔드<br>Spring Boot (Java)<br>RESTful API 설계 및 데이터 처리<br>사용자 인증 및 권한 관리 (Spring Security + JWT)<br>스케줄링 기반 리마인드 기능 구현<br>🔹 데이터베이스<br>MySQL / PostgreSQL<br>사용자 질문, 답변, 인사이트 데이터 저장<br>카테고리 및 태그 기반 데이터 구조 관리<br>🔹 AI 및 데이터 처리<br>OpenAI API (LLM)<br>질문·답변 기반 핵심 요약 생성<br>키워드 추출 및 인사이트 도출<br>텍스트 임베딩 (Embedding) 기반 유사도 분석<br>인사이트 간 의미적 유사성 계산<br>관련 인사이트 추천 기능 구현
| 기대 효과 | 본 서비스를 통해 사용자는 AI와의 대화에서 얻은 정보를 체계적으로 관리할 수 있다. 저장된 인사이트는 시간이 지나 다시 노출되기 때문에 기억에 오래 남게 되며 학습이나 프로젝트 과정에서 다시 활용될 가능성이 높아진다. 또한 관련 인사이트가 자동으로 연결되기 때문에 사용자는 자신의 질문과 생각이 구조적으로 확장되는 경험을 할 수 있다. 결과적으로 AI 사용이 단순한 질문과 답변에서 끝나는 것이 아니라 개인의 지식 축적과 사고 확장으로 이어지는 효과를 기대할 수 있다. |
| GitHub Repo | [https://github.com/Semicolone](https://github.com/Semicolone) |
| Team Ground Rule | [https://github.com/Semicolone/start/blob/main/Team_Ground_Rule.md](https://github.com/Semicolone/start/blob/main/Team_Ground_Rule.md) |
| 최종수정일 | 2026.03.19. |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---



<a id="team-14"></a>
## Team 14 def

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 로컬 환경에서의 Agentic AI 병목 분석 및 성능 최적화: Apple silicon 온디바이스를 중심으로 |
| 서비스명(브랜드) | |
| 트랙 | 연구 |
| 팀명 | def |
| 팀구성 | 서혜원, 신은서, 이재린 |
| 팀지도교수 | 심재형 교수님 |
| 무엇을 만들고자 하는가 | - 로컬 워크로드를 분석하고 병목을 스스로 해결하는 에이전트 기반 최적화 프레임워크 설계 및 구현<br>- Experimental Evaluation (논문 핵심): 최적화 적용 전/후의 성능(TPS, Latency, Energy Efficiency) 비교 데이터와 다양한 워크로드 시나리오(단일 추론 vs 멀티태스킹)에서의 자원 효율성 검증 보고서 |
| 고객 (누구를 위해) | - Agent AI 시스템 설계자 및 연구자: 클라우드 의존도를 낮추고 로컬 기기(Edge Device)의 하드웨어 잠재력을 끝까지 끌어올려야 하는 엔지니어<br>- Agent AI 사용자: 외부 클라우드 서버에 데이터를 보내지 않고, Mac mini 같은 로컬 기기에서 개인화된 AI 모델을 안전하게 돌리고 싶은 개인 및 기업 |
| Pain Point (해결할 문제) | - 리소스 고갈:LLM(거대언어모델) 실행 시 메모리 점유율이 급증하여 시스템이 멈추거나 느려지는 현상<br>- 예측 불가능한 병목(Dynamic Bottleneck):워크로드의 성격(연산 중심 vs 메모리 중심)에 따라 시스템의 어느 부분에서 병목이 생길지 실시간으로 파악하기 어려움<br>- 메모리 고갈(Memory Issue):특히 LLM 구동 시 제한된 통합 메모리(Unified Memory) 용량을 초과할 때 생기는 다양한 문제점 |
| 사용 기술 | - Agentic Monitoring Loop : 에이전트가 시스템 API를 통해 CPU/GPU 등 점유율 및 전력 소모량을 실시간 관찰하고 대응 전략을 결정<br>- 현재 실행 중인 워크로드에 대한 실시간으로 분류하는 분석 알고리즘 |
| 개발환경 | 1. Client 디바이스<br><br>- PC (macOS): 연구 대상이 Mac mini이므로 실험과 구동 모두 Mac 환경에서 진행<br><br>2. FE <br><br>- Streamlit : 파이썬 기반으로 대시보드를 빠르게 만들 수 있어, 실시간 자원 사용량 그래프(CPU, GPU, RAM)를 시각화<br><br>3. 특별한 라이브러리<br><br>- MLX : Apple Silicon GPU/NPU를 최대한 활용하기 위한 애플의 공식 딥러닝 프레임워크<br><br>- LangChain : Agent의 의사결정 루프를 설계<br><br>6. API Call 서비스<br>- 해당 없음<br>- Local LLM (Llama 3, Ollama)의 활용. 외부 API(OpenAI 등)를 쓰면 '로컬 워크로드 최적화'라는 연구 취지에 어긋남. 로컬에 모델을 띄우고 호출함.
| 사용하는 소프트웨어 URL | 1. Client 디바이스<br><br>- PC (macOS): 연구 대상이 Mac mini이므로 실험과 구동 모두 Mac 환경에서 진행<br><br>2. FE <br><br>- Streamlit : 파이썬 기반으로 대시보드를 빠르게 만들 수 있어, 실시간 자원 사용량 그래프(CPU, GPU, RAM)를 시각화<br><br>3. 특별한 라이브러리<br><br>- MLX : Apple Silicon GPU/NPU를 최대한 활용하기 위한 애플의 공식 딥러닝 프레임워크<br><br>- LangChain : Agent의 의사결정 루프를 설계<br><br>6. API Call 서비스<br>- 해당 없음<br>- Local LLM (Llama 3, Ollama)의 활용. 외부 API(OpenAI 등)를 쓰면 '로컬 워크로드 최적화'라는 연구 취지에 어긋남. 로컬에 모델을 띄우고 호출함.
| 기대 효과 | - 효율성 극대화:동일 하드웨어 대비 AI 추론 성능(Throughput) 및 응답 속도(Latency)의 유의미한 향상.<br>- 시스템 안정성:메모리 이슈로 인한 시스템 다운 방지 및 멀티태스킹 환경에서의 부드러운 사용자 경험 유지.<br>- 에너지 효율: 불필요한 연산 낭비를 줄여 전력 소모 최적화 및 발열 제어 |
| GitHub Repo | [https://github.com/capstone-2026-ewha/def](https://github.com/capstone-2026-ewha/def) |
| Team Ground Rule | [https://github.com/capstone-2026-ewha/def/blob/main/Team_Ground_Rule.md](https://github.com/capstone-2026-ewha/def/blob/main/Team_Ground_Rule.md) |
| 최종수정일 | 2026-3-12 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-15"></a>
## Team 15 햄부기

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 엣지 환경 배포를 위한 Vision Transformer 구조적 가지치기 및 경량화 파이프라인 구축과 성능 분석 |
| 서비스명(브랜드) | |
| 트랙 | 연구 |
| 팀명 | 햄부기 |
| 팀구성 | 신성현, 송영채, 장수연 |
| 팀지도교수 | 심재형 |
| 무엇을 만들고자 하는가 | 엣지 장치와 클라우드 서버가 협력하여 이미지를 빠르게 분석하는 분산 AI 추론 시스템 |
| 고객 (누구를 위해) | AI 기반 서비스를 개발하는 학생 팀 및 연구 프로젝트 수행자를 위해 |
| Pain Point (해결할 문제) | 엣지 장치에서 AI 모델을 실행할 때 발생하는 높은 연산 부담과 네트워크 지연 문제를 해결하기 위해 |
| 사용 기술 | Computer Vision 모델과 Edge–Cloud Split Inference 기술을 사용하여 일부 연산은 엣지에서, 나머지는 클라우드에서 처리하는 방식 사용 |
| 개발환경 | 1. Client 디바이스 — PC (Windows) + Jetson AGX Orin (엣지 디바이스)<br>2. FE — 없음<br>3. BE — 없음<br>4. DB — 없음 (실험 결과는 TensorBoard로 시각화)<br>5. 특별한 라이브러리<br>- PyTorch (모델 학습 및 가지치기)<br>- Hugging Face Transformers (ViT 모델 로드)<br>- torch.ao (2:4 Sparsity 적용)<br>- TensorRT (Jetson 추론 최적화)<br>- ONNX (모델 변환)<br>- TensorBoard (실험 결과 시각화)<br>6. API Call 서비스 — 없음
| 사용하는 소프트웨어 URL | 1. Client 디바이스 — PC (Windows) + Jetson AGX Orin (엣지 디바이스)<br>2. FE — 없음<br>3. BE — 없음<br>4. DB — 없음 (실험 결과는 TensorBoard로 시각화)<br>5. 특별한 라이브러리<br>- PyTorch (모델 학습 및 가지치기)<br>- Hugging Face Transformers (ViT 모델 로드)<br>- torch.ao (2:4 Sparsity 적용)<br>- TensorRT (Jetson 추론 최적화)<br>- ONNX (모델 변환)<br>- TensorBoard (실험 결과 시각화)<br>6. API Call 서비스 — 없음
| 기대 효과 | AI 추론 속도를 개선하고 네트워크 사용량을 줄이며, 제한된 연산 자원을 가진 장치에서도 효율적인 AI 서비스가 가능해진다 |
| GitHub Repo | [https://github.com/Ewha-Capstone-Project/Hambugy.git](https://github.com/Ewha-Capstone-Project/Hambugy.git) |
| Team Ground Rule | [https://github.com/Ewha-Capstone-Project/Hambugy/blob/main/Team_Ground_Rule.md](https://github.com/Ewha-Capstone-Project/Hambugy/blob/main/Team_Ground_Rule.md) |
| 최종수정일 | 26/03/14 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-16"></a>
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
## Team 17 SPY

| 항목 | 내용 |
|------|------|
| 프로젝트명 | Moni: AI 기반 소비 예측과 맞춤형 챌린지를 결합한 개인화 소비 코칭 서비스 |
| 서비스명(브랜드) | Moni(모니) |
| 트랙 | 산학 |
| 팀명 | SPY |
| 팀구성 | 신희조, 윤수연, 박은수 |
| 팀지도교수 | 오세은 |
| 무엇을 만들고자 하는가 | 본 프로젝트는 사용자의 과거 소비 패턴을 AI가 분석·예측하고, 바로 실천할 수 있는 개인화 챌린지를 제공하는 소비 습관 코칭 앱을 목표로 한다. 카테고리별 지출 예측을 바탕으로 사용자의 소비 목표와 당일 소비 현황을 반영한 데일리 챌린지를 자동 생성하며, 챌린지 달성 시 캐릭터가 성장하는 게임형 보상 구조를 통해 지속적인 행동 변화를 유도한다. |
| 고객 (누구를 위해) | 예산은 있지만 계획적으로 소비하기 어려운 사용자, 소비 습관 개선 필요성을 느끼거나 감정적·충동적 소비를 줄이고 싶은 사용자 |
| Pain Point (해결할 문제) | 많은 사용자는 예산을 설정해도 이를 실제 행동으로 이어가지 못하고, 자신의 소비 패턴을 직관적으로 파악하는 데 어려움을 겪는다. 기존 소비 관리 서비스는 기록과 통계 제공에 머무르는 경우가 많아 지속적인 행동 변화 유도가 부족하다. 소비 습관은 월간 통계가 아니라 오늘의 행동으로 결정되지만, 오늘 어떻게 행동해야 할지 알려주는 도구가 없다. |
| 사용 기술 | FE: Kotlin, BE: FastAPI , DB: MySQL, AI: Python 기반 Prophet / ARIMA / LSTM 모델 비교 실험, 챌린지 생성: OpenAI GPT API |
| 개발환경 | 1. AI/ML: 소비 패턴 분석 및 예측 모델 (Prophet / ARIMA / LSTM)<br>2. Data Analysis: Pandas, NumPy 기반 소비 데이터 처리 및 시계열 분석<br>3. LLM: 개인화 챌린지 문장 및 주간 리포트 생성 (OpenAI API)<br>4. FE: Kotlin (Android Native), Retrofit<br>5. BE: FastAPI<br>6. DB: MySQL
| 사용하는 소프트웨어 URL | 1. AI/ML: 소비 패턴 분석 및 예측 모델 (Prophet / ARIMA / LSTM)<br>2. Data Analysis: Pandas, NumPy 기반 소비 데이터 처리 및 시계열 분석<br>3. LLM: 개인화 챌린지 문장 및 주간 리포트 생성 (OpenAI API)<br>4. FE: Kotlin (Android Native), Retrofit<br>5. BE: FastAPI<br>6. DB: MySQL
| 기대 효과 | 본 서비스는 소비가 발생하기 전에 개입하는 예측 기반 구조를 통해 사용자의 실제 소비 행동 변화를 유도하고, 예산 준수율 및 소비 습관 개선에 기여할 것으로 기대된다. 하루 단위의 챌린지와 보상 시스템으로 단기 실천을, 주간 리포트로 중기 점검을 함께 제공함으로써 사용자 참여도와 지속 사용성을 높인다. |
| GitHub Repo | [https://github.com/SPY-capstone-2026/SPY-capstoneREPO](https://github.com/SPY-capstone-2026/SPY-capstoneREPO) |
| Team Ground Rule | https://github.com/SPY-capstone-2026/SPY-capstoneREPO/blob/main/Team_Ground_Rule.md |
| 최종수정일 | 2026.04.06 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-18"></a>
## Team 18 디바트(deep-art)

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 멀티모달 AI 기반 배리어프리 오디오 도슨트 자동 생성 서비스 |
| 서비스명(브랜드) | |
| 트랙 | 연구 |
| 팀명 | 디바트(deep-art) |
| 팀구성 | 최현서, 이나겸, 김나경 |
| 팀지도교수 | 박현석 |
| 무엇을 만들고자 하는가 | 전시 정보를 입력하면 AI가 도슨트 설명을 생성하고 음성으로 변환해주는 AI 기반 오디오 도슨트 자동 제작 서비스. 시각장애인을 위한 배리어프리 모드를 함께 제공한다. |
| 고객 (누구를 위해) | 전시 기획자 및 전시 콘텐츠 제작자 |
| Pain Point (해결할 문제) | 기존 오디오 도슨트는 전문 도슨트의 해설 작성과 녹음 과정을 통해 제작되기 때문에 시간과 비용이 많이 소요되며, 소규모 전시나 개인 전시에서는 도입이 어려운 경우가 많다. 이에 전시 기획자가 작품 이미지와 작품 정보를 입력하면 AI가 도슨트 해설을 자동으로 생성하고 이를 음성으로 변환하여 오디오 도슨트 콘텐츠를 제작할 수 있는 서비스를 구축하고자 한다. 추가적으로 배리어프리 모드를 통해, 시각장애인의 전시 해설 서비스 접근성을 높이고, 작품의 시각적 요소를 보다 자세히 설명하는 해설 기능을 제공하고자 한다. |
| 사용 기술 | LMM을 통한 이미지 분석, LLM 및 RAG 기반 콘텐츠 생성, 음성 합성(TTS) 기술 |
| 개발환경 | <대략의 개발환경 구성요소><br><br>1. client 디바이스<br>- 전시 기획자용: PC 웹 (Windows)<br>- 관람객용: 모바일 웹 (Android)<br><br>2. FE: React + TypeScript<br><br>3. BE: FastAPI<br><br>4. DB: PostgreSQL<br><br>5. FE또는 BE에 사용하는 특별한 라이브러리<br>- Axios<br>- Howler.js<br>- Pillow(이미지 전처리)<br><br>6. API Call로 사용할 서비스<br>- OpenAI<br>- Google Cloud TTS
| 사용하는 소프트웨어 URL | <대략의 개발환경 구성요소><br><br>1. client 디바이스<br>- 전시 기획자용: PC 웹 (Windows)<br>- 관람객용: 모바일 웹 (Android)<br><br>2. FE: React + TypeScript<br><br>3. BE: FastAPI<br><br>4. DB: PostgreSQL<br><br>5. FE또는 BE에 사용하는 특별한 라이브러리<br>- Axios<br>- Howler.js<br>- Pillow(이미지 전처리)<br><br>6. API Call로 사용할 서비스<br>- OpenAI<br>- Google Cloud TTS
| 기대 효과 | 소규모 전시에서도 활용 가능한 전시 해설 환경을 제공하며, 배리어프리 해설 기능을 통해 시각장애인을 포함한 다양한 관람객의 문화 접근성 확대에 기여할 수 있다. |
| GitHub Repo | [https://github.com/ewha-deep-art/deep-art](https://github.com/ewha-deep-art/deep-art) |
| Team Ground Rule | [https://github.com/ewha-deep-art/deep-art/blob/main/Team_Ground_Rule.md](https://github.com/ewha-deep-art/deep-art/blob/main/Team_Ground_Rule.md) |
| 최종수정일 | 2026.03.14 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-19"></a>
## Team 19 Logue

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 자연어 기반 데이터 분석 질의를 통해 조직의 데이터 접근성과 의사결정 속도를 향상시키는 AI 기반 데이터 분석 웹 인터페이스, Logue |
| 서비스명(브랜드) | Logue |
| 트랙 | 산학 |
| 팀명 | Logue |
| 팀구성 | 손하늘, 김겨레, 김예원, 민지인 |
| 팀지도교수 | 하진용 |
| 무엇을 만들고자 하는가 | 자연어 질문만으로 데이터베이스에서 필요한 정보를 조회할 수 있는 데이터 분석 인터페이스 |
| 고객 (누구를 위해) | 데이터 기반 의사결정을 해야 하지만 SQL이나 데이터 조회가 어려운 기획자·마케터 |
| Pain Point (해결할 문제) | 비즈니스 데이터를 확인할 때 개발자에게 쿼리를 요청해야 하는 의존성과 분석 지연 문제를 해결 |
| 사용 기술 | LLM 기반 Text-to-SQL, 데이터베이스 스키마 이해, 자연어 질의 처리 기술을 사용 |
| 개발환경 | Device : PC(Window)<br>FE<br>- Next.js<br>- Typescript<br>- Vite<br>- yarn<br>- Axios<br>- Tailwindcss v4.2<br>- StoryBook<br>- Zustand<br>- Tanstack Query<br>- React Hook form + Zod<br>- shadcn/ui (ui  컴포넌트)<br>- ECharts<br>- Monaco Editor(필요시)<br>- Vercel or Jenkins<br><br>BE<br>- Java 21, Spring Boot 3<br>- Spring AOP<br>- PostgreSQL<br>- AWS RDS<br>- AWS S3<br>- Redis<br>- Flyway<br>- Github Actions<br>- Docker<br>- Kubernetes<br>- AWS ec2, Route53, ALB<br>- AWS CloudWatch<br>- Sentry<br>- Slf4j, Logback<br>- Spring Security<br>- OAuth2.0<br>- JWT<br>- Swagger<br>- k6, p6spy<br><br>AI<br>- Python<br>- FastAPI<br>- Pydantic v2<br>- pandas<br>- sentence-transformers<br>- OpenAI API<br>- Uvicorn<br>- pytest<br>- Render<br>- GitHub Actions
| 사용하는 소프트웨어 URL | Device : PC(Window)<br>FE<br>- Next.js<br>- Typescript<br>- Vite<br>- yarn<br>- Axios<br>- Tailwindcss v4.2<br>- StoryBook<br>- Zustand<br>- Tanstack Query<br>- React Hook form + Zod<br>- shadcn/ui (ui  컴포넌트)<br>- ECharts<br>- Monaco Editor(필요시)<br>- Vercel or Jenkins<br><br>BE<br>- Java 21, Spring Boot 3<br>- Spring AOP<br>- PostgreSQL<br>- AWS RDS<br>- AWS S3<br>- Redis<br>- Flyway<br>- Github Actions<br>- Docker<br>- Kubernetes<br>- AWS ec2, Route53, ALB<br>- AWS CloudWatch<br>- Sentry<br>- Slf4j, Logback<br>- Spring Security<br>- OAuth2.0<br>- JWT<br>- Swagger<br>- k6, p6spy<br><br>AI<br>- Python<br>- FastAPI<br>- Pydantic v2<br>- pandas<br>- sentence-transformers<br>- OpenAI API<br>- Uvicorn<br>- pytest<br>- Render<br>- GitHub Actions
| 기대 효과 | 비개발자도 즉시 데이터를 탐색하고 빠르게 의사결정을 내릴 수 있게 됨. |
| GitHub Repo | [https://github.com/26-ewha-capstone-logue](https://github.com/26-ewha-capstone-logue/logue) |
| Team Ground Rule | [Team_Ground_Rule](https://github.com/26-ewha-capstone-logue/docs/blob/main/Team_Ground_Rule.md) |
| 최종수정일 | 2026.03.16 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

