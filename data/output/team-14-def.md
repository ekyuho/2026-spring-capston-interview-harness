# Team 14. def 심층인터뷰 준비서

## 1. 만들고자 하는 것

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

## 2. 사전 보충자료 요약

자료 없음 또는 정리 필요

## 3. 팀지도교수 면담보고서

<!-- page 1 -->

14(def)  
def (team 14)
  Agentic AI     : Apple silicon  
 
, , 
(Mac mini, Mac studio  Apple Silicon ) Agent AI  , 
bottleneck          ,  
.
  
  ‘Q)’ ,   ‘  )’  .
Q) benchmark          .
Q)   device      ,   
  KV Cache (SideQuest     ) KV
cache       Bottleneck     
.
Q) Apple silicon          .
 )  system sw stack  benchmark    
 .
 ) KV-Cache compression  agentic AI  .  KV-
Cache         .  cache
 bottleneck    , agent  , context   
      .
 )  Agent AI(open claw)  ,   bottleneck 
    .


<!-- page 2 -->

Agentic AI       :      
     .
<     >
SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic
Reasoning
ReAct: Synergizing Reasoning and Acting in Language Models
Agentic AI: Autonomous Intelligence for Complex Goals—A Comprehensive Survey
Mac Studio  Open claw     bottleneck

## 4. 팀원별 학기초 개인설문

### 신은서

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: NLP 분야에서 ontology와 hallucination, LLM 분야에서 RAG와 연산 효율, On-device AI의 시스템 최적화 및 경량화에 관심이 있습니다.
Grokking 현상에 호기심을 가지고 구현 및 보고서 작성을 해본 적이 있고, 생성형 AI 프로젝트로 depth&motion conditioned 효과음 생성 프로젝트, 간단한 이진 및 다중 분류 프로젝트를 해본 경험이 있습니다.
크고 작은 프로젝트 경험들을 통해, open cv나 transformer 등 다양한 모델들을 접해본 경험이 많습니다. ML, DL 프로젝트 및 논문 스터디 하면서 모델의 구조에 대한 높은 이해도를 쌓아왔다고 생각합니다.
- **이번에 팀이 구성된 계기**: 심재형 교수님 랩실에서 학부인턴을 하면서, 관심분야가 비슷한 친구를 찾았습니다. 그 친구와 관심분야들과 주제들에 대해 이야기하다가 공통적으로 agent ai가 최근 이슈로 대두되면서 관련된 연구를 해보고싶다는 생각을 하였고, 학교 커뮤니티를 통해 비슷한 관심사를 가진 학생을 한 명 더 구할 수 있게 되었습니다.

### 이재린

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: 관심 영역: 온디바이스 AI, LLM 및 시스템 최적화(System Optimization)
AI 모델의 다양한 활용 및 구조 연구, 제한된 하드웨어 자원(CPU, GPU, RAM) 내에서 AI 모델이 어떻게 하면 가장 효율적으로 작동할 수 있는지 연구하는 데 관심이 많습니다. 특히 에이전트(Agentic AI)가 스스로 시스템 상태를 분석하고 병목 현상을 해결하는 '자율형 자원 관리' 메커니즘에 관심을 갖고 있습니다.

산출물 : Jetson Nano 기반 실시간 객체 인식 최적화 및 LLM RAG 시스템 효율 분석
1. MobileNetV2 경량화: 리소스가 제한된 Jetson Nano 보드에서 추론 속도를 높이기 위해 MobileNetV2 모델의 경량화 및 최적화(TensorRT 활용 등)를 진행하여 실시간 구동 환경을 구축했습니다.
2. RAG 시스템 구축 및 최적화: 대규모 언어 모델(LLM)에 검색 증강 생성(RAG) 기술을 접목하고, 데이터 임베딩부터 답변 생성까지의 전 과정에서 발생하는 지연 시간(Latency)과 메모리 사용량을 분석했습니다. 특히 로컬 환경에서 검색 효율을 높이기 위한 인덱싱 최적화 과정을 직접 수행하며 시스템의 한계를 경험했습니다.

남보다 잘한다고 생각되는 영역 : CV 및 LLM 모델 구조에 대한 깊은 이해와 다각적 최적화 역량
다양한 모델 아키텍처 이해: 가벼운 CV 모델인 MobileNetV2의 Depthwise Separable Convolution 구조부터, 최신 LLM의 Transformer 기반 Attention 메커니즘까지 폭넓은 모델 구조를 이해하고 직접 다루어 본 경험이 있습니다.
하드웨어 맞춤형 최적화 경험: 단순히 모델을 돌리는 것에 그치지 않고, Jetson Nano와 같은 저사양 보드의 자원 한계를 극복하기 위해 모델을 경량화하거나 가속화(TensorRT 등)하여 실제 성능을 끌어올린 실전 감각을 보유하고 있습니다.
- **이번에 팀이 구성된 계기**: 졸업 프로젝트 주제인 'Agentic AI를 통한 로컬 워크로드 최적화'는 AI 모델에 대한 이해 및 최적화에 대한 이해 동시에 요구되는 난이도 높은 과제입니다. 이에 따라 모델 성능 분석에 강점이 있는 본인과, AI 프레임워크 구현 및 모델 튜닝에 경험이 있는 팀원들이 각자의 전문성을 결합하여 시너지를 내기 위해 팀을 구성하게 되었습니다.

### 서혜원

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: 제 관심영역은 agent ai, on-device ai, 지능형네트워크입니다. 
프로젝트로는 open cv를 활용하여 자동악보넘김 서비스를 구현한 경험이 있고, 2023 서초구 AIoT 메이커톤에 나가서 YOLOv8 모델로 차량과 보행자를 실시간으로 인식하고, 아두이노를 통해 신호제어를 구현한 스마트 신호등으로 특별상을 수상한 경험이 있습니다.
남들보다 잘한다고 생각하는 영역은 비판적으로 사고하기, 실현가능성에 대해 깊게 탐구하고 판단하기 입니다.
- **이번에 팀이 구성된 계기**: 먼저 팀이 구성되고 주제도 agent ai쪽으로 잡혀있었고 팀원을 모집하고 계셔서 제 경력과 능력을 어필하여 팀에 합류하게 되었습니다.

## 5. 개인별 5 Questions

### 이재린

- 에이전트가 직접 코드를 작성해 데이터를 가공하는 Programmatic Tool Calling 방식이 에이전트의 내부 작업 메모리(KV Cache) 점유율을 얼마나 효율적으로 방어하며 추론의 정확도를 유지시키는가?
- 사고(Reasoning)의 깊이와 하드웨어 자원 소모 사이의 상관관계는 어떠한가?
- 에이전트가 복잡한 task를 해결하기 위해 여러 번 도구를 호출할 때, 누적되는 실행 이력이 KV Cache 대역폭 병목에 미치는 영향은 어느 정도인가?
- 원본 데이터 전체를 모델에 넘기는 방식과 에이전트가 직접 짠 코드로 필요한 요약본만 가져오는 방식 간의 데이터 전송 오버헤드(I/O Overhead) 차이는 시스템 성능에 어떤 영향을 주는가?
- 에이전트가 Chain-of-Thought할 때 소모되는 추가적인 자원 대비 결과물 향상이 로컬 기기 환경에서 정당화될 수 있는 수준인가?

### 신은서

1. KV Cache 외에, Agentic AI 워크로드(ReAct 등)가 로컬 디바이스에서 실행될 때 실제로 어떤 자원(메모리 대역폭, CPU/GPU 스케줄링, I/O 등)이 주된 병목이 되는가?
2. OpenClaw 같은 오픈소스 agentic 프레임워크를 Apple Silicon(Mac Mini/Mac Studio) 위에서 30B~70B 모델로 돌렸을 때, 현재 구현의 어떤 부분이 실질적인 성능 저하를 유발하는가?
3. 메모리가 상대적으로 풍부한 온디바이스 환경(Mac Studio 등)에서도 Agentic AI 실행 시 병목이 생긴다면, 그 원인은 메모리 용량이 아닌 어떤 요인(대역폭, 스케줄링, 컨텍스트 스위칭 등)인가?
4. ReAct 같은 agent 루프(Observe → Think → Act)에서 각 단계별로 LLM 추론이 반복 호출될 때, 호출 간 상태 유지 및 컨텍스트 누적이 리소스 효율에 미치는 영향은 얼마나 큰가?
5. 기존 LLM 추론 최적화 벤치마크(throughput, latency 중심)는 Agentic 워크로드의 특성(반복 호출, 가변 길이 컨텍스트, 툴 호출 지연 등)을 제대로 반영하지 못하는 것 아닌가?

### 서혜원

1. 어떤 병목현상을 개선시킬 것 인가?
2. 남들이 찾지 못한 병목현상을 찾을 수 있는가?
3. agentic ai의 동작방식에서 비효율적인 부분이 있는가?
4. 성능이 개선됐다는 평가지표로 어떤 지표를 선택할 것인가?
5. 기존 논문에서의 LLM추론 최적화 벤치마크가 Agentic ai 추론 최적화 벤치마크와 동일시 될 수 있는가?

## 6. 기반 소프트웨어 리스트

env:
  - 1. Client 디바이스
  - - PC (macOS): 연구 대상이 Mac mini이므로 실험과 구동 모두 Mac 환경에서 진행
  - 2. FE
  - - Streamlit : 파이썬 기반으로 대시보드를 빠르게 만들 수 있어, 실시간 자원 사용량 그래프(CPU, GPU, RAM)를 시각화
  - 3. 특별한 라이브러리
  - - MLX : Apple Silicon GPU/NPU를 최대한 활용하기 위한 애플의 공식 딥러닝 프레임워크
  - - LangChain : Agent의 의사결정 루프를 설계
  - 6. API Call 서비스
  - - 해당 없음
  - - Local LLM (Llama 3, Ollama)의 활용. 외부 API(OpenAI 등)를 쓰면 '로컬 워크로드 최적화'라는 연구 취지에 어긋남. 로컬에 모델을 띄우고 호출함.

url:
  - https://www.python.org/downloads/ (Python 환경 구축)
  - https://ollama.com/download (로컬 LLM 구동 엔진)
  - https://code.visualstudio.com/ (메인 IDE)
  - https://www.docker.com/products/docker-desktop/ (DB 및 모니터링 툴 설치용)
  - https://developer.apple.com/xcode/ (Apple Silicon 성능 분석 도구 포함)
  - https://github.com/ml-explore/mlx (Apple ML 프레임워크 라이브러리)

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
