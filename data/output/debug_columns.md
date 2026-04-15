# 데이터 소스 컬럼 진단

이 파일은 병합 전 자료 구조를 확인하기 위한 1차 진단 결과입니다.

## project_brief: Class Project Brief

- type: `github_markdown`

- 전체 문자 수: 40,624
- 비어 있지 않은 줄 수: 415

```md
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
| [14](#team-14) | def | 연구 | 로컬 LLM 기반 Coding Agent에서 Frequently Accessed Code 블록의 KV Cache 재사용을 통한 Token 소비 최적화 |
| [15](#team-15) | 햄부기 | 연구 | 엣지 디바이스 배포를 위한 Vision Foundation Model의 2:4 구조적 희소성 성능 분석 및 추론 파이프라인 구축 |
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
```


## supplement: 심층인터뷰 보충자료

- type: `google_sheet_csv`

⚠️ 로딩 실패: `SSLError: HTTPSConnectionPool(host='docs.google.com', port=443): Max retries exceeded with url: /spreadsheets/d/1w9N8jzw_S6Ay6RjPSoaurxu3vx9ZHa1f8EEnmcmQ5SY/export?format=csv&gid=603194317 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))`

## initial_survey: 학기초 개인설문

- type: `google_sheet_csv`

⚠️ 로딩 실패: `SSLError: HTTPSConnectionPool(host='docs.google.com', port=443): Max retries exceeded with url: /spreadsheets/d/1-f0Rw55PWrTvnYjbyoJsvyymihgyUMAXzoGYuYuLSPk/export?format=csv&gid=1166981779 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))`

## five_questions: 개인별 5 Questions

- type: `google_sheet_csv`

⚠️ 로딩 실패: `SSLError: HTTPSConnectionPool(host='docs.google.com', port=443): Max retries exceeded with url: /spreadsheets/d/1XU4Vks1vNhAJWYG7x55kDFagnzfxQD-0MgNyu4NdEig/export?format=csv&gid=542184958 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))`

## base_software: 기반 소프트웨어 리스트

- type: `google_sheet_csv`

⚠️ 로딩 실패: `SSLError: HTTPSConnectionPool(host='docs.google.com', port=443): Max retries exceeded with url: /spreadsheets/d/1aN2rfWu1M7mHkhOW76gXTAjjGyb1yMzN5kOgyLlMjaE/export?format=csv&gid=9030440 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))`
