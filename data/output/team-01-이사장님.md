# Team 01. 이사장님 심층인터뷰 준비서

## 1. 만들고자 하는 것

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

## 2. 사전 보충자료 요약

github 관련:
- all ok

본 프로젝트에 있어서 팀원별 R&R(Role & Responsibility):

- **설영은**
  - 총괄, 프롬프트 설계, 알고리즘 리드를 담당하며, 전체 프로젝트 기획 및 일정을 총괄하고 CLIP 프롬프트 전략 수립과 80개 템플릿 설계 방향을 결정한다.
  - 또한 MTA 알고리즘 설계 및 MeanShift 방법론을 검토하며, 연구 결과물의 최종 품질 확인 및 논문/보고서 핵심 파트를 정리한다.
- **신지민**
  - 모델 구현, 인프라, 알고리즘 구현을 맡아 CLIP 임베딩 파이프라인을 구축 및 구현하고, Stable Diffusion 기반 이미지 증강(DiffTPT 프로토콜, 총 128장)을 수행한다.
  - MeanShift 알고리즘 코드 구현과 outlier view 제거 및 mode m* 추출도 담당하며, 연구 방법론 설계에 참여하고 중간 보고서 자료를 정리한다.
- **윤희서**
  - 데이터, 실험 설계, 평가를 담당하며, 테스트 데이터셋 선정, 수집, 전처리를 수행하고 실험 설계 및 성능 지표(분류 정확도 등)를 측정한다.
  - Ablation study를 수행하고 결과를 분석하며, 결과 시각화와 문헌 조사, 보고서 자료 정리를 지원한다.

기말에 대략 어떤 것을 만들어 보여줄지의 개요, 그 의미:

- 기말까지 구현 범위는 CLIP 기반 이미지 임베딩 추출부터 RandomCrop 기반 Augmentation, MTA(MeanShift) 적용을 통한 robust mode m* 획득까지이다.
- 도메인 추정 이후 단계는 구현 없이 아이디어와 계획으로 발표에 포함한다.
- 개발 환경은 PyTorch와 OpenAI 공식 CLIP을 활용하며, GPU는 Colab을 사용한다.
- 기말 발표에서는 MTA 적용 전후 이미지 임베딩 품질 비교(outlier 제거 효과)를 결과로 제시한다.
- 도메인 추정 이후 전체 파이프라인에 대한 분류 정확도 향상은 예상 연구 결과로 포함하며, 향후 계획과 함께 발표를 마무리한다.
- 코드는 GitHub에 업로드하고 결과 테이블과 발표 자료를 함께 제출한다.
- 이 구현이 갖는 의미는, MTA가 전체 파이프라인에서 이미지 임베딩의 품질을 높이는 핵심 단계라는 점이다.
- 기존 CLIP이 단순 평균 임베딩을 사용하는 것과 달리, MTA는 outlier view를 제거하고 본질적인 특징만 남긴 robust한 임베딩을 만든다.
- 이는 이후 도메인 추정의 정확도를 좌우하는 기반이 되므로, 전체 연구의 성패를 결정하는 첫 번째 검증 단계로서 의미가 있다.

서비스를 지향하는 산학트랙의 경우, API Call을 통해 어떤 AI 서비스를, 어떤 목적으로, 어떤 파라미터를 주고, 그 결과를 어떻게 활용하는지 간단히 정리(어떻든 AI를 적극적으로 적용해보세요):
- 연구트랙입니다.

AI 투명성 리포트 (텍스트로 간단히 정리):

### 사용한 AI와 용도
- Claude AI- 연구 아이디어 구체화, 방법론 비교 및 예시 코드 생성
- Chat GPT - 논문 속 개념 정리,  실험/코드 아이디어 보조, 면담 내용 정리
- Lilys AI - 논문 분석 및 이해, 면담 내용 정리
- Gemini - Google Colab 코드 구조 설계 보조

### AI 제안을 수정하거나 기각한 사례
- Claude AI가 CLIP 템플릿 평균 방식을 제안했으나, 도메인 특성을 반영하지 못한다고 판단, 도메인 가중치 기반 prompt blending 방식으로 변경.
- Claude AI가 도메인 임베딩을 MLP를 통해 ViT에 삽입하는 방식을 제안했으나, MLP는 추가 학습이 필요해 training-free 원칙에 어긋난다고 판단. → CLIP 내부 projection을 재활용하는 방식으로 수정.

### AI가 틀렸거나 신뢰하기 어려웠던 순간
- Claude AI가 동일한 도메인 임베딩을 텍스트와 비전 브랜치에 함께 사용하는 방식을 제안했으나, 동일 정보의 중복 사용으로 효과가 제한적이라고 판단. → 텍스트 브랜치 결과를 비전 브랜치에 coupling하는 방식으로 수정.
- Claude AI가 텍스트 임베딩을 비전 브랜치에 직접 삽입하는 방식을 제안했으나, 이후 효과가 불확실하다고 번복함. → 효과가 있다고 가정하고 진행하기로 결정.
- Claude AI가 DA(Domain Adaptation) 연구라고 제안했으나, 실제로는 source 데이터 없이 테스트 단계에서만 동작하는 TTA(Test-Time Adaptation)에 가까운 오류. 연구 방향 포지셔닝은 팀이 직접 판단 및 수정.
- Chat GPT가 프롬프트 은행을 직접 제작하라 했으나, CLIP 원 논문에 80개 템플릿이 이미 존재함을 팀이 먼저 파악한 오류. AI가 기존 자원 활용 가능성을 간과, 팀이 직접 수정.
- Claude AI가 텍스트+비전 coupled 추론을 별도 단계로 추가했으나, 텍스트 브랜치 결과를 비전 브랜치에 넣는 구조 자체가 이미 coupled임을 팀이 먼저 파악한 오류. 구조적 중복을 스스로 인지하지 못해 팀이 직접 삭제.

### AI 없이 팀이 직접 한 것
- 지도 교수님 면담 및 연구 방향 설정, 연구 기획안 작성, 데이터셋 선정 검토, 실험 설계 및 최종 아이디어 도출 직접 진행. AI는 이해와 구현을 돕는 보조 수단으로만 활용하였으며, 연구의 방향성과 핵심 판단은 팀의 이해와 책임 하에 이루어져야 한다고 판단했기 때문.

## 3. 팀지도교수 면담보고서

<!-- page 1 -->

면담 보고서 
 
일시: 2026.03.24. 13 시 
참석자: 황의원 교수님, 2448052 설영은, 2466033 신지민, 2476199 윤희서 
면담 목적: 멀티모달 도메인 적응 연구과 관련하여 방향성 및 주제 설정 구체화를 위한 
교수님의 피드백을 받고, 최신 연구 동향 및 연구 진행 시 고려사항에 대한 조언을 구함 
연구 주제 개요 
1. 도메인 선정 배경 
멀티모달 도메인 적응(multimodal domain adaptation)을 기반으로, 기후·기상 
도메인에 대한 관심에서 출발함. 초기에는 cloud 데이터를 고려하였으나, 단순하거나 
기존 연구와 차별성이 부족할 수 있다는 판단 하에 열대저기압(Tropical Cyclone) 
도메인으로 방향을 설정 
2. 현재 진행 상황 
- 멀티모달 domain adaptation 관련 주제 탐색 단계 
- 기후/기상 도메인 중 tropical cyclone 으로 방향 설정 
- 관련 논문 및 방법론(TPT, CoOp 등) 조사 진행 중 
- 연구 난이도 및 도메인 적절성에 대한 검토 단계 
3. 예상 데이터 모달리티 
- 이미지 데이터 
- 시계열 데이터 
- 수치 데이터


<!-- page 2 -->

교수님 피드백 요약 
1. 연구 주제 및 도메인 관련 
- 해당 연구 주제(multimodal domain adaptation)는 연구실에서도 진행 중인 
분야로, 적절한 방향성임 
- 다만 초기 단계에서는 AI 기본 지식 및 선행 논문 학습이 선행되어야 함 
- 멀티모달 도메인 적응은 아직 연구가 많지 않아 탐색 가치가 있는 분야 
- 특정 도메인 연구의 경우, 데이터 확보가 가장 중요한 요소 
- 공개 데이터셋(가장 쉬운 방법) 또는 외부 협업을 통한 데이터 확보 
또한, 
- 특정 도메인보다 일반 벤치마크 기반 연구 후 확장하는 방식 고려 가능 
- 기존 모델을 적용한 뒤 개선하는 접근이 현실적인 전략임 
- 특정 도메인으로 시작한 뒤, 벤치마크 기반 연구로 바꾸는 것은 어려움 
2. 방법론(Prompt Tuning) 관련 
- TPT 는 시작하기 좋은 방법이지만, 최신 방법론(CoOp, CoCoOp 등)을 참고하는 
것이 중요 
- 연구 목표가 최신 모델보다 성능을 향상하는 것이 목적이라면, 최신 논문 기반 
접근이 더 적절 
- 성능이 기대에 미치지 못할 경우, 다른 분야 속 비슷한 아이디어 및 문제 차용                  
→ 샘플 필터링 등 엔지니어링 접근 고려 
특히, 
- 엔트로피 기반 필터링 
- Spurious correlation 문제 해결 등이 중요한 연구 방향으로 제시됨 
- 시나리오 기반으로 성능을 높이는 것도 좋지만, 3 학년 수준에서는 쉽지 않음


<!-- page 3 -->

3. 연구 방향 및 최신 트렌드 
- 도메인 적응 연구는 DA → SFDA → TTA(Test-Time Adaptation)로 발전 중 
- DA: 소스 데이터로 학습된 모델을 타겟 데이터에 맞춰 튜닝하는 방식 
- SFDA (Source-Free Domain Adaptation): 소스 데이터에 접근할 수 없는 
상황에서, 학습된 모델과 라벨 없는 타겟 데이터만으로 학습을 진행 
- TTA (Test-Time Adaptation): 소스 데이터에 접근할 수 없고, 학습된 
모델과 라벨 없는 타겟 데이터를 단 한 번만 볼 수 있는 조건에서 
실시간으로 적응하는 방식 
- 최근 연구는 TTA 중심으로 진행되는 추세 
- Spurious correlation 를 재언급해주심 
또한, 
- CLIP 기반 모델 활용 시 다른 모델에 비해 상대적으로 가볍게 연구 가능 
- 대규모 모델은 GPU 인프라 필요하지만, 도메인 적응은 비교적 경량화 가능 
4. 연구 수행 및 학습 방법 
- CLIP 논문, Tent 논문 찾아볼 것 
- 논문은 저널 논문이 아닌 학회 논문 위주로 탐색 
ML (Machine Learning) ICML, NeurIPS, ICLR 
CV (Computer Vision) CVPR, ICCV, ECCV 
NLP (Natural Language Processing) ACL, NAACL, EMNLP 
- 인용수 높은 논문부터 읽는 전략 권장 
- 연구 준비 방향: 메소드 이해가 최우선, 구현은 기존 코드를 이해한 후 수정하는 
방향 
추가적으로, 
- 메소드 완전 이해하는 것 가장 중요 
- 1 학기 후반까지 아이디어 도출 필요 및 여름방학 내 실험 완료 목표 설정 
- 2 학기 인공지능 수학 학습 필요

## 4. 팀원별 학기초 개인설문

### 설영은

최근에 AI 연구에 관심이 생겨 대학원 진학을 목표로, 현재 컴퓨터비전, 딥러닝을 중심으로 공부하고 있습니다.

지금까지 참여한 프로젝트는 다음과 같습니다.
1. YOLO 기반 객체 인식 파인튜닝: 도서관 좌석 이용 현황을 파악하기 위해 YOLO 모델을 활용한 객체 인식 시스템을 구현했습니다. 사람을 인식할 수 있도록 데이터셋을 구축하고 모델을 파인튜닝하여 좌석에 앉아 있는 인원을 자동으로 인식·집계하도록 했으며, AWS를 통한 배포를 담당해 서버의 전반적인 운영과 배포 과정을 관리했습니다.
2. 이화여대 대동제 웹사이트 개발: 백엔드 파트로 참여하여 행사 정보 제공을 위한 API를 개발했습니다.
3. 환율 자동 적용 가계부 서비스: 백엔드 파트로 참여하여 교환, 방문학생을 대상으로 환율을 자동 적용해 지출을 관리할 수 있도록 돕는 가계부 서비스를 개발했습니다. 또한 AWS를 통한 배포를 담당하여 서버의 전반적인 운영과 배포 과정을 관리했습니다.
4. 기분 기반 차(Tea) 추천 서비스: 백엔드 파트로 참여하여 사용자의 기분에 따라 어울리는 차를 추천하는 서비스를 구현했으며, 해당 프로젝트로 최우수상을 수상했습니다. 또한 pythonanywhere를 통한 배포를 담당하여 서버의 전반적인 운영과 배포 과정을 관리했습니다.
- **이번에 팀이 구성된 계기**: 세 명 모두 최근 AI 연구에 관심이 생겼고, 이전에 함께 프로젝트를 진행한 경험이 있어 자연스럽게 팀이 구성되었습니다.

### 신지민

참여한 프로젝트
1. 서대문구 독거노인을 위한 배달 서비스: 지역 상권을 되살리고 독거 노인의 식사 문제와 디지털 격차 문제를 해결하기 위한 서비스입니다. Whisper AI를 비롯한 OpenAI의 오픈소스 API를 연동하여 음성 채팅이 가능한 챗봇을 구현했고, 실시간 배달 서비스를 제작 및 배포했습니다. django 프레임워크 기반으로 개발을 진행했고, 배포 플랫폼은 pythonanywhere를 사용했습니다.
2. 맞벌이 부모와 아이를 위한 AI 동화 제작 서비스: OpenAI, MyShell OpenVoice, Stable Diffusion 등 오픈소스 API를 사용하여 아동이 스스로 동화를 제작하거나 동화의 결말을 확장할 수 있으며, 동화를 부모의 목소리로 직접 들을 수 있는 서비스를 제작 및 배포했습니다. django 프레임워크 기반으로 개발을 진행했고, AWS(EC2·S3·RDS·Redis), Nginx, Gunicorn, Docker 기반의 인프라를 통해 배포를 진행했습니다.
3. 축제준비위원회 주최 밴드제 공연팀 소개 웹사이트를 구현 및 배포하여 실제 유저의 서비스 사용을 경험한 바가 있습니다.
4. 이화여대 대동제 사이트 개발: 전체적인 검색, 정렬, 필터링을 담당하여 db 쿼리셋 연산 로직을 구현했습니다.

최근에는 인공지능 및 기후, 에너지 분야에 관심을 가지고 있어 기후에너지시스템공학과를 부전공하며 공부하고 있습니다. 외부 API를 연동하여 서비스에 적용시키는 영역에 자신이 있습니다. 현재는 딥러닝 공부를 중점적으로 하고 있어 pytorch 사용 경험을 쌓고 있습니다.
- **이번에 팀이 구성된 계기**: 비슷한 시기에 AI에 관심을 가지고 공부를 하게 되어 딥러닝 분야를 연구하며 같이 성장하고자 이번 캡스톤디자인프로젝트에서 팀을 결성하게 되었습니다.

### 윤희서

저는 AI, 머신러닝에 관심이 있습니다. 특히 다양한 형태의 데이터를 활용해 모델의 일반화 성능을 높이거나 실제 문제에 적용하는 과정에 흥미를 가지고 있습니다.
교내 프로젝트CoRise(이화 마켓)에서 대학생 간 중고거래를 위한 웹 서비스를 개발하며 프론트엔드 구현을 담당했고, HTML, CSS, JavaScript를 학습하며 실제로 동작하는 화면을 구현했습니다. 또한 Git/GitHub를 활용해 코드 버전 관리와 협업을 진행한 경험이 있습니다. 이러한 경험을 통해 데이터와 모델이 실제 서비스에 적용되는 과정에 흥미를 갖게 되었고, 멀티모달 도메인 적응 연구를 통해 다양한 데이터 간 일반화와 활용 가능성을 탐구하고 싶습니다.
- **이번에 팀이 구성된 계기**: 세 팀원 모두 AI 분야에 대한 공통된 관심을 가지고 있었고, 자연스럽게 연구 중심의 프로젝트를 진행해보고자 의견이 모였습니다. 특히 대규모 데이터가 존재하고 사회적 의미도 큰 기후 분야를 AI 연구와 연결하기에 적합하다는 의견이 모아져 팀을 구성하게 되었습니다.

## 5. 개인별 5 Questions

### 설영은

1. 멀티모달 도메인 적응을 통한 성능 개선을 달성하기 위해, 어떤 도메인이 가장 효과적인 타겟 도메인으로 간주될 수 있는가?
2. 특정 도메인에 대한 적응을 통해 성능을 향상시킬 경우, 기존에 잘 작동하던 일반 도메인에서의 성능이 저하되는 generalization degradation 문제는 어느 정도로 중요한가?
3. Prompt Tuning과 관련해서 train-time마다 학습하는 방식, test-time에서 샘플마다 적응하는 방식, 동적으로 관리하고 재사용하는 방식 등 다양한 방식이 있다. 이 중 어떤 방식이 성능, 안정성, 계산 비용 측면에서 가장 효과적이라고 생각하는가?
4. Prompt Tuning에서 효과적인 prompt는 어떻게 구성되어야 하는가?
5. 도메인 차이가 발생했을 때, CLIP 같은 모델의 내부에서 구체적으로 어떤 왜곡이 발생하여 성능 저하로 이어진다고 생각하는가?

### 신지민

1. Vision-Language Model의 zero-shot 성능은 왜 실제 환경에서의 domain shift 에 대해 구조적으로 취약한가?
2. 기존 멀티모달 도메인 적응 방법들은 왜 cross-domain 일반화 성능 향상에 있어 비효율적이며, 그 한계는 어디에서 발생하는가?
3. Test-time Prompt Tuning은 domain shift로 인한 성능 저하를 일반적으로 극복할 수 있는가, 아니면 특정 유형의 domain shift에서만 제한적으로 작동하는가?
4. Test-time Prompt Tuning의 효과를 검증하기 위해, domain shift를 체계적으로 반영하면서도 train과 test 간의 일반화 성능을 신뢰성 있게 평가할 수 있는 데이터셋은 어떻게 설계하고 수집할 수 있는가?
5. 멀티모달 도메인 적응 문제가 해당 도메인의 전문가 혹은 인공지능 엔지니어 뿐만 아니라 실제 사용자 또한 공감할 수 있을 만큼 중요한 문제인가?

### 윤희서

1. 서로 다른 modality(예: 이미지, 텍스트) 간 정보량과 신뢰도가 다를 때, 현재 모델들은 어떤 한계를 보이는가?
2. modality 간 alignment를 강화하는 과정이 오히려 새로운 도메인에서의 일반화 성능을 저해하는 경우가 있는가, 그 원인은 무엇인가?
3. early fusion, late fusion, hybrid fusion 방식 각각이 어떤 상황에서 성능 저하를 보이는가?
4. 멀티모달 학습에서 modality 간 데이터가 불완전하거나 missing된 경우, source 도메인에서 학습된 multimodal representation은 얼마나 견고하게 유지되는가?
5. 멀티모달 모델이 단일 모달 모델 대비 실제 환경에서 의미 있는 성능 향상을 보이는 조건은 무엇인가?

## 6. 기반 소프트웨어 리스트

env:
  - 1. Client 디바이스를: PC(Windows, Mac) 및 GPU 서버 기반 연구 환경
  - 2. 딥러닝 프레임워크: Python/PyTorch/CUDA/CuDNN 기반 GPU 환경
  - 3. 데이터셋: Himawari-8/9 TC Archive, TC PRIMED, IBTrACS, ERA5 등
  - 4. 활용 모델: CLIP 기반 Vision-Language Model
  - 5. 사전학습 모델: CLIP pretrained model
  - 6. 라이브러리: NumPy, Pandas, Matplotlib, TensorBoard, NetCDF 등
  - 7. 데이터 시각화 뷰어: Panoply

url:
  - https://www.python.org/downloads/ (Python)
  - https://developer.nvidia.com/cuda-downloads (CUDA)
  - https://developer.nvidia.com/cudnn (CuDNN)
  - https://www.anaconda.com/download (Anaconda)
  - https://pytorch.org/get-started/locally/ (Pytorch 설치에 필요한 명령어 생성)
  - https://www.giss.nasa.gov/tools/panoply/ (Panoply, NASA 제공 데이터 시각화)

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
