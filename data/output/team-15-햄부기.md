# Team 15. 햄부기 심층인터뷰 준비서

## 1. 프로젝트 개요

- 트랙: 
- 프로젝트명: 
- 팀원: 
- 지도교수: 
- GitHub Repo: https://github.com/Ewha-Capstone-Project/Hambugy.git](https://github.com/Ewha-Capstone-Project/Hambugy.git

## 2. 만들고자 하는 것

## Team 15 햄부기

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 엣지 디바이스 배포를 위한 Vision Foundation Model의 2:4 구조적 희소성 성능 분석 및 추론 파이프라인 구축 |
| 서비스명(브랜드) | |
| 트랙 | 연구 |
| 팀명 | 햄부기 |
| 팀구성 | 신성현, 송영채, 장수연 |
| 팀지도교수 | 심재형 교수님 |
| 무엇을 만들고자 하는가 | NVIDIA Ampere 및 차세대 아키텍처에서 지원하는 2:4 Structured Sparsity 기법을 VFM에 적용하여 엣지 디바이스에서의 추론 성능을 극대화하는 파이프라인 구축 |
| 고객 (누구를 위해) | Edge AI 기반 서비스를 개발하는 학생 팀 및 연구 프로젝트 수행자를 위해 |
| Pain Point (해결할 문제) | 최근 Vision Foundation Model(VFM)은 강력한 성능을 보여주지만, 엣지 환경에 배포하기에는 다음과 같은 치명적인 한계가 있다.<br><br>- **VFM의 높은 연산 비용**: ViT 기반 모델은 파라미터 수가 방대하여 엣지 GPU에서도 실시간 추론이 어렵다.<br>- **메모리 대역폭 병목**: 대규모 가중치를 메모리에서 불러오는 과정에서 에너지가 소모되고 지연 시간이 발생한다.<br>- **하드웨어 최적화 미비**: 일반적인 Unstructured Sparsity(무작위 희소화)는 가중치를 줄여도 실제 하드웨어(GPU)에서 연산 가속으로 이어지지 않는 경우가 많다.<br><br>따라서 엣지 디바이스(NVIDIA Jetson AGX Orin 등)의 Sparse Tensor Core를 활용하여, 하드웨어 수준에서 성능을 끌어올릴 수 있는 구조적 최적화가 필요하다. |
| 사용 기술 | **모델 최적화 및 학습**<br>- 2:4 Structured Sparsity: 연속된 4개의 가중치 중 2개를 0으로 제한하는 구조적 희소화 기법으로, Sparse Tensor Core에서 0이 아닌 값만 선택적으로 연산하여 이론적으로 최대 2배의 처리량 향상을 달성할 수 있다.<br>- VFM Fine-tuning: DINOv2나 CLIP 같은 모델에 Sparse-refined 학습을 적용하여 정확도 손실을 최소화한다.<br><br>**추론 최적화**<br>- TensorRT 가속: 2:4 패턴을 인식하는 TensorRT 엔진을 빌드하여 Orin 디바이스에 최적화된 실행 파일을 생성한다.<br><br>**시스템 파이프라인**<br>- End-to-End 파이프라인: 이미지 입력부터 Sparse 연산을 거친 최종 추론까지의 전 과정을 자동화한다. |
| 개발환경 | 1. Client 디바이스 — PC (Windows) + Jetson AGX Orin (엣지 디바이스)<br>2. FE — 없음<br>3. BE — 없음<br>4. DB — 없음 (실험 결과는 TensorBoard로 시각화)<br>5. 특별한 라이브러리<br>- PyTorch (모델 학습 및 가지치기)<br>- torch.ao (2:4 Sparsity 적용)<br>- TensorRT (Jetson 추론 최적화)<br>- ONNX (모델 변환)<br>- TensorBoard (실험 결과 시각화)<br>6. API Call 서비스 — 없음 |
| 사용하는 소프트웨어 URL | - PyTorch(https://pytorch.org/)<br>- TensorRT(https://developer.nvidia.com/tensorrt)<br>- ONNX(https://onnx.ai/)<br>- NVIDIA Developer(https://developer.nvidia.com/) |
| 기대 효과 | 본 프로젝트를 통해 Vision Foundation Model을 엣지 환경에서도 실시간으로 활용할 수 있는 기반을 마련할 수 있으며, 기존 Dense 모델 대비 연산 속도와 처리량이 크게 개선된다. 특히 2:4 Structured Sparsity와 Sparse Tensor Core를 활용함으로써 단순한 모델 경량화를 넘어 실제 하드웨어 수준에서의 성능 향상을 달성할 수 있다. 또한 pruning 이후 fine-tuning 전략을 통해 정확도 손실을 최소화함으로써, 경량화와 성능 사이의 trade-off 문제를 효과적으로 해결할 수 있다. 결과적으로 본 파이프라인은 다양한 비전 및 멀티모달 모델에 재사용 가능하며, VFM을 실제 산업 현장에 적용 가능한 수준으로 끌어내리는 데 기여할 수 있다. |
| GitHub Repo | [https://github.com/Ewha-Capstone-Project/Hambugy.git](https://github.com/Ewha-Capstone-Project/Hambugy.git) |
| Team Ground Rule | [https://github.com/Ewha-Capstone-Project/Hambugy/blob/main/Team_Ground_Rule.md](https://github.com/Ewha-Capstone-Project/Hambugy/blob/main/Team_Ground_Rule.md) |
| 최종수정일 | 26/04/15 |

[↑ 목록으로](#2026-spring-전체-프로젝트-리스트)

---

<a id="team-16"></a>

## 3. 사전 보충자료 요약

- **github 관련**: Class Repo의 Project Description의 내용은 최신상태로 PR되어있습니까?, 팀 Project Repo는 제3자가 검색해서 들어오게되었을때, 구조 이해에 도움이 되도록 Readme.MD 에 내용 정리해 두었습니까?, 팀 Project Repo의 폴더 구성은 통상 오픈소스 구성처럼 잘 구조화 되어있습니까?, 팀 Project Repo에 PR해가면서 공동작업을 github 활용하고 있습니까?, 데모한 모든 코드/데이타 등은 팀 Project Repo에 다 올라가 있습니까?
- **본 프로젝트에 있어서 팀원별 R&R(Role & Responsibility)**: • 성현: 작업 문서화, 실험 실행
• 영채: AGX Orin 환경 세팅 및 실험 파이프라인 구축, 실험 실행
• 수연: 논문 서치 및 이론 정리, 실험 실행
- **기말에 대략 어떤 것을 만들어 보여줄지의 개요, 그 의미**: ViT에서의 2:4 sparsity 실험을 구체화하고 평가 지표를 다양화하는 것을 출발점으로, VLM 등 더 넓은 범위의 Vision Foundation Model로 대상을 확장하여 엣지 디바이스 환경에서의 성능 지표를 분석하고 개선 방안을 탐색하는 것을 기말 목표로 설정하였습니다. 또한 2:4 sparsity에서 메모리 접근 패턴 분석도 연구 공백인 점을 감안하여 이 부분에 대해 구체적인 조사를 하려고 합니다. 현재 VLM 도메인에서 AGX Orin 기반 실측 데이터가 거의 없다는 점에서, 본 연구가 엣지 환경에서의 대형 비전 모델 경량화 연구에 실질적인 기여를 할 수 있을 것으로 기대하고 있습니다.
- **서비스를 지향하는 산학트랙의 경우, API Call을 통해 어떤 AI 서비스를, 어떤 목적으로, 어떤 파라미터를 주고, 그 결과를 어떻게 활용하는지 간단히 정리(어떻든 AI를 적극적으로 적용해보세요)**: 연구트랙
- **AI 투명성 리포트 (텍스트로 간단히 정리)**: 1. 어떤 AI를, 어떤 작업에 썼나

- Claude — 연구 흐름 정리 및 보고서 문장 다듬기, 코드 구현
- ChatGPT — 논문 서치, 논문 내용 요약 및 개념 정리 (2:4 sparsity, coalescing 동작 원리 등)

2. AI 제안을 수정하거나 기각한 사례

- 사례 1: ChatGPT가 모델구축 및 다운로드를 AGXOrin에서 하는걸 제안했으나, AGXorin의 용량 제한 때문에 좋지 않은 선택임을 인지하고 PC에서 모델을 구축후 AGXOrin으로 보내는 형태를 선택함
- 사례 2: Claude가 기말 결과물로 "end-to-end 추론 파이프라인 완성"을 제안했으나, 현실적인 일정을 고려해 파이프라인 구축 대신 성능 지표 분석 및 비교 실험으로 범위를 조정함.

3. AI가 틀렸거나 못 믿었던 순간

Claude가 메모리 access실험에서 dense model과 sparse model의 측정 실험에서 둘다 같은 dense 모델을 측정하는 코드를 줌. 직접 수정하여, dense 와 sparse를 둘 다 측정하도록 설계함.

4. AI 없이 우리가 직접 한 것

- AGX Orin 환경 세팅 직접 수행. 디바이스 특성상 AI가 환경 오류를 진단할 수 없었기 때문.
- 연구 방향 결정(ViT → VLM 확장)은 팀 논의로 직접 결정. 실험 결과 해석과 방향 판단은 AI 제안을 참고하되 최종 결정은 팀이 직접 내림.

## 4. 팀원별 학기초 개인설문

### 신성현

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 장수연

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 송영채

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 


## 5. 개인별 5 Questions

### 송영채

- **질문당 한줄씩 5개의 질문**: 왜 기존의 Vision 모델(예: Vision Transformer)은 Edge 디바이스에서 실시간으로 동작하기 어려운가?
GPU에서 지원되는 2:4 structured sparsity가 실제 Vision 모델 성능과 효율에 어떤 한계를 가지는가?
기존 경량화 기법(양자화, pruning 등)이 Edge 환경에서 항상 효과적이지 않은 이유는 무엇인가?
고해상도 입력(이미지/영상)을 처리할 때 Edge 디바이스에서 발생하는 병목은 어디인가?
Vision 모델의 정확도(accuracy)와 지연 시간(latency) 사이의 trade-off를 어떻게 해결할 수 있는가?

### 신성현

- **질문당 한줄씩 5개의 질문**: 1. 2:4 Sparsity 적용 시 ViT의 어떤 레이어가 성능 손실에 가장 취약한가?
2. AGX Orin의 Sparse Tensor Core는 ViT 연산 패턴에서 실제로 이론적 2x 속도 향상을 달성하는가?
3.  AGX Orin에서 2:4 Sparsity의 실질적 전력 효율(Performance per Watt)은 Dense 모델 대비 얼마나 개선되는가?
4. 2:4 Sparsity로 경량화된 ViT 파이프라인은 TensorRT 변환 과정에서 sparsity 정보가 보존되는가?
5. 2:4 Sparsity 적용만으로 ViT의 엣지 배포가 가능한가, 아니면 추가적인 경량화 기법(양자화, Knowledge Distillation 등)과의 병행이 필수적인가?

### 장수연

- **질문당 한줄씩 5개의 질문**: 1. NVIDIA Jetson에서 Vision Transformer 모델에 2:4 Sparsity 기반의 구조적 가지치기를 적용했을 때, 이론적인 연산량 감소 수치 대비 실제 엣지 디바이스 환경에서 얻을 수 있는 Inference 지연시간 단축 효과는 어느 정도인가? 2. 엣지 디바이스에서 2:4 Sparsity가 적용된 경량화 ViT 모델로 앞단의 특징을 추출하고 클라우드로 넘겨 연산하는 분산 추론 구조를 채택할 경우, 가지치기로 인한 모델 압축이 엣지-클라우드 간의 데이터 전송량 및 통신 오버헤드 감소에 실질적인 기여를 할 수 있는가? 3. CNN 구조와 달리 병렬 연산의 비중이 높은 ViT의 Self-Attention 메커니즘에 2:4 Sparsity를 강제할 경우, 모델의 표현력과 정확도 손실폭은 어느 정도이며, 이를 Fine-tuning 과정을 통해 기존 수준으로 복구할 수 있는가? 4. 구조적 가지치기를 통해 희소 행렬 연산 속도를 높이더라도, Jetson과 같이 자원이 제한된 엣지 환경에서는 연산기보다 메모리 대역폭이 새로운 병목 지점이 될 수 있는데, 이를 해결하기 위한 TensorRT 수준의 메모리 접근 최적화 방안은 무엇인가? 5. 비전 모델을 실시간 영상 처리가 필요한 산업 현장에 배포한다고 가정할 때, 2:4 Sparsity가 적용된 경량화 모델이 요구되는 실시간 처리 속도를 방어함과 동시에, Jetson 디바이스의 제한된 전력 소모량과 발열 문제를 유의미하게 개선할 수 있는가?


## 6. 기반 소프트웨어 리스트

- **env**: 1. Client 디바이스 — PC (Windows) + Jetson AGX Orin (엣지 디바이스)
2. FE — 없음
3. BE — 없음
4. DB — 없음 (실험 결과는 TensorBoard로 시각화)
5. 특별한 라이브러리
- PyTorch (모델 학습 및 가지치기)
- Hugging Face Transformers (ViT 모델 로드)
- torch.ao (2:4 Sparsity 적용)
- TensorRT (Jetson 추론 최적화)
- ONNX (모델 변환)
- TensorBoard (실험 결과 시각화)
6. API Call 서비스 — 없음
- **url**: Python - https://www.python.org
PyTorch - https://pytorch.org
Hugging Face - https://huggingface.co
TensorRT - https://developer.nvidia.com/tensorrt
JetPack SDK - https://developer.nvidia.com/jetpack
ONNX - https://onnx.ai
Conda - https://docs.conda.io
VS Code - https://code.visualstudio.com

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