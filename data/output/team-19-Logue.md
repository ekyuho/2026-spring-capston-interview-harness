# Team 19. Logue 심층인터뷰 준비서

## 1. 만들고자 하는 것

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

## 2. 사전 보충자료 요약

자료 없음 또는 정리 필요

## 3. 팀지도교수 면담보고서

<!-- page 1 -->

캡스톤 
프로젝트 
면담 
결과 
보고서 
캡
스
톤
디
자
인
과
창
업
프
로
젝
트
B 
캡스톤 
면담 
결과 
보고서 
team 
 19 
Logue  
| 
손
하
늘
, 
김
겨
레
, 
김
예
원
, 
민
지
인 
 
1. 
면담 
개요 
본 
면담은 
Logue
의 
주제 
적절성
, 
기술적 
구현 
방향
, 
학기 
내 
실현 
가능한 
MVP 
범위
, 
그리고 
최종 
평가 
시 
설득력 
있는 
시연 
구조를 
점검하기 
위해 
진행되었다
. 
사전자료에서 
Logue
는 
비개발자
·
현업 
사용자가 
자연어 
질문으로 
조직 
데이터를 
조회하되
, 
결과와 
함께 
지표 
정의
, 
계산 
기준
, 
근거를 
확인할 
수 
있게 
하는 
웹 
인터페이스로 
정의되었으며
, 
현재 
구현 
방향은 
단일 
CSV 
업로드
, 
고정 
metric 
registry, 
제한적 
ambiguity clarification, 
결과
·
차트
·
계산근거 
노출 
중심의 
MVP
 로 
설정되어 
있었다
. 
면담에서는 
서비스 
소개 
자체보다
, 
실제로 
무엇을 
직접 
구현하고 
무엇을 
기존 
도구
·
오픈소스로 
대체할지
, 
그리고 
어떤 
데모 
시나리오가 
프로젝트의 
차별점을 
가장 
명확하게 
보여줄지를 
중심으로 
논의가 
진행되었다
. 
 
2. 
면담에서 
설명한 
주요 
내용 
2
-
1. 
서비스 
및 
프로토타입 
설명 
• 
기존 
BI 
환경은 
정해진 
지표를 
조회하는 
데에는 
강하지만
, 
비정형 
질문이나 
후속 
탐색으로 
넘어가는 
순간 
해석과 
검증의 
병목이 
다시 
데이터팀으로 
돌아가는 
문제가 
있다는 
점을 
설명하였다
. 
면
담 
일
시 
/ 
장
소 
 2026.03.27 15
:30 
진
선
미
관 
226
 호 
담
당 
교
수
님 
 하
진
용 
교
수
님 
참
여 
팀
원 
 손
하
늘
, 
김
겨
레
, 
김
예
원
, 
민
지
인


<!-- page 2 -->

캡스톤 
프로젝트 
면담 
결과 
보고서 
캡
스
톤
디
자
인
과
창
업
프
로
젝
트
B 
• 
Logue
는 
자연어 
질문을 
그대로 
받아 
자유롭게 
SQL
을 
생성하는 
방식이 
아니라
, 
반복적으로 
사용되는 
비즈니스 
질문을 
검증된 
metric template
와 
연결하고 
결과와 
함께 
지표 
정의
·
계산 
기준
·
필터 
조건을 
보여주는 
구조라는 
점을 
강조하였다
. 
• 
또한 
Google Looker
와 
같은 
기존 
BI 
서비스와의 
차별점으로
, 
질문을 
먼저 
받고 
필요한 
데이터 
구조를 
역으로 
안내하는 
Question
-
first Flow, 
자연어의 
모호성을 
짧은 
재질문으로 
고정하는 
Ambiguity Clarification, 
계산 
근거를 
함께 
노출하는 
Calculation Transparency
를 
설명하였다
. 
2
-
2. 
구현 
방식 
및 
기술 
플로우 
설명 
• 
자연어 
질문은 
AI 
서버에서 
intent, semantic role, ambiguity 
여부
, 
출력 
형식 
등을 
구조화된 
JSON
으로 
변환하고
, 
API 
서버는 
이를 
바탕으로 
업로드 
데이터의 
충족 
여부를 
판단한 
뒤 
준비가 
되었을 
때만 
실행 
단계로 
넘기는 
구조로 
설명하였다
. 
• 
핵심 
원칙은 
자유 
생성 
LLM SQL
을 
직접 
실행하지 
않는다는 
점이며
, 
실제 
실행은 
metric registry
에 
등록된 
검증된 
SQL template 
혹은 
사전 
정의된 
집계 
로직만 
사용하도록 
제한하는 
방식으로 
제시하였다
. 
• 
이 
과정에서 
질문 
파싱
, ambiguity 
처리
, 
질문 
구조화
, 
컬럼 
매핑
, 
실행 
준비
, 
결과 
및 
설명 
레이어 
제공까지가 
이번 
프로젝트의 
실질적 
구현 
범위로 
논의되었다
. 
 
3. 
교수님 
주요 
피드백 
교수님 
피드백은 
크게 
네 
가지 
축으로 
정리된다
. 
핵심은 
‘
무엇을 
만들 
수 
있는가
’
보다 
‘
무엇을 
비교 
기준으로 
삼아 
어떤 
실패 
케이스를 
이길 
것인가
’
를 
먼저 
고정해야 
한다는 
점이었다
. 
피드백 
항목 
 교수님 
조언 
 우리에게 
의미하는 
바 
비교 
대상 
명확화 
기존 
BI, ChatGPT, 
내부 
데이터팀 
등 
여러 
비교축을 
동시에 
잡지 
말고 
Julia AI 
같은 
단일 
서비스로 
명확히 
좁힐 
것
. 
경쟁 
구도가 
흐리면 
데모 
메시지가 
약해진다
. 
한 
서비스의 
실패 
지점을 
먼저 
고정해야 
차별점이 
선명해진다
.


<!-- page 3 -->

캡스톤 
프로젝트 
면담 
결과 
보고서 
캡
스
톤
디
자
인
과
창
업
프
로
젝
트
B 
실패 
케이스 
선확보 
경쟁 
서비스가 
반복적으로 
해결하지 
못하는 
질문
·
상황을 
먼저 
확보하고
, 
같은 
시나리오에서 
우리 
서비스가 
되는 
것을 
보여줄 
것
. 
개발 
전에 
비교 
기준이 
없으면 
‘
이미 
남들도 
되는 
기능
’
을 
뒤늦게 
구현할 
위험이 
크다
. 
MVP 
범위 
축소 
FE, API, AI, 
액션 
엔진을 
모두 
완성하려 
하기보다 
인프라는 
최대한 
기존 
도구를 
활용하고 
핵심 
로직과 
UI
 에 
집중할 
것
. 
프로젝트 
성패는 
전 
범위 
구현이 
아니라 
핵심 
기능을 
끝까지 
보여주는 
데 
달려 
있다
. 
Plan B/C 
준비 
시스템 
연결이 
불안정하면 
차트나 
일부 
결과는 
스태틱
·
임의 
데이터로 
대체하는 
플랜을 
미리 
준비할 
것
. 
최종 
데모는 
완전성보다 
실패하지 
않는 
시연 
구조가 
더 
중요하다
. 
 
4. 
성과 
측정
(KPI) 
관련 
논의 
• 
프로젝트의 
핵심 
가치로 
설정한 
‘
유연성
’
은 
직관적으로는 
중요한 
차별점이지만
, 
독자적으로 
정의해서 
수치화하기에는 
기준이 
모호하고 
방어가 
어렵다는 
문제가 
지적되었다
. 
• 
이에 
따라 
교수님은 
기존 
인터뷰 
대상자 
혹은 
데이터 
분석 
경험이 
있는 
사용자에게 
경쟁 
서비스와 
Logue
를 
모두 
사용하게 
한 
뒤
, 
사용성
·
이해도
·
신뢰도
·
질문 
확장 
용이성 
등에 
대해 
점수화하는 
비교 
평가 
방식을 
제안하였다
. 
• 
또한 
LLM 
또는 
AI 
제품 
평가 
분야에서 
functionality, usability, helpfulness
와 
관련된 
기존 
벤치마크나 
평가 
프레임워크가 
있는지 
조사해
, 
가능하면 
자체 
정의 
지표보다 
외부 
프레임워크를 
차용하는 
방향이 
바람직하다는 
의견이 
제시되었다
. 
따
라
서
, KPI
는 
‘
우리가 
생각한 
멋진 
개념
’
을 
새로 
만드는 
문제가 
아니라
, 
비교 
가능한 
평가 
구조
를 
설계하는 
문제로 
접근해야 
한다
.


<!-- page 4 -->

캡스톤 
프로젝트 
면담 
결과 
보고서 
캡
스
톤
디
자
인
과
창
업
프
로
젝
트
B 
5. 
면담 
이후 
재정리된 
개발 
방향 
5
-
1. 
첫째
, 
경쟁 
서비스 
1
종을 
우선 
타깃으로 
고정해야 
한다
. 
현재 
단계에서 
비교 
축이 
많으면 
기능 
우선순위가 
흔들린다
. 
따라서 
Julia AI
와 
같이 
BI+AI 
에이전트 
성격이 
분명한 
서비스를 
기준점으로 
잡고
, 
그 
서비스에서 
반복적으로 
발생하는 
실패 
케이스를 
먼저 
문서화할 
필요가 
있다
. 
5
-
2. 
둘째
, 
개발 
출발점을 
‘
기능 
목록
’
이 
아니라 
‘
데모 
시나리오
’
로 
바꿔야 
한다
. 
어떤 
질문에서 
경쟁 
서비스는 
실패하고 
Logue
는 
성공하는지
, 
그 
과정에서 
어떤 
재질문과 
설명 
레이어가 
필요한지를 
먼저 
확정해야 
실제 
구현 
범위도 
자연스럽게 
정리된다
. 
5
-
3. 
셋째
, 
이번 
학기에는 
인프라 
완성도보다 
핵심 
로직의 
설득력이 
더 
중요하다
. 
즉
, 
질문 
구조화
, ambiguity clarification, metric definition layer, calculation transparency, 
제한된 
결과 
시각화가 
핵심이며
, 
나머지 
연결이나 
자동화는 
오픈소스
·API·
스태틱 
데이터로 
대체하는 
것이 
현실적이다
. 
5
-
4. 
넷째
, 
최종 
시연은 
반드시 
실패하지 
않는 
구조로 
설계해야 
한다
. 
차트
, 
일부 
데이터 
연결
, 
부가 
기능은 
Plan B
와 
Plan C
를 
준비하고
, 
데모에서 
반드시 
보여줘야 
할 
장면은 
‘
경쟁 
서비스는 
답이 
흐려지는 
질문에서 
Logue
는 
의미를 
명확히 
하고 
근거까지 
제시하는 
장면
’
으로 
좁혀야 
한다
. 
 
6. 
후속 
액션 
아이템 
No. 
 항목 
 실행 
내용 
 우선순위 
1 
경쟁 
서비스 
실패 
케이스 
확보 
Julia AI 
등 
비교 
대상 
1
종을 
선정하고
, 
동일 
데이터
·
동일 
질문 
기준으로 
반복 
재현 
가능한 
실패 
사례를 
수집
·
문서화한다
. 
상 
2 
 기능 
우선순위 
재정리 
3/31 
스펙 
제출 
전 
필수 
기능과 
후순위 
기능을 
재구분하고
, 
데모에 
필요한 
최소 
시나리오를 
상


<!-- page 5 -->

캡스톤 
프로젝트 
면담 
결과 
보고서 
캡
스
톤
디
자
인
과
창
업
프
로
젝
트
B 
기준으로 
목록을 
다시 
정리한다
. 
3 
 MVP 
범위 
재조정 
인프라
·
연동
·
자동화 
요소는 
축소하고
, 
핵심 
로직 
레이어와 
UI 
중심으로 
구현 
계획을 
다시 
짠다
. 
상 
4 
 성과 
측정 
방법 
리서치 
LLM/AI 
제품 
평가 
프레임워크 
및 
usability 
비교 
평가 
방식을 
조사해 
측정 
체계를 
정리한다
. 
중 
5 
서베이 
및 
테스트 
대상자 
확보 
기존 
인터뷰 
대상자 
또는 
데이터 
분석 
경험자를 
대상으로 
비교 
평가 
실험 
설계를 
준비한다
. 
중 
 
7. 
면담 
후 
내부 
판단 
이번 
면담을 
통해 
현재 
팀이 
가장 
경계해야 
할 
것은 
범위를 
넓히는 
일 
자체가 
아니라
, 
비교 
기준 
없이 
기능을 
늘려 
차별점이 
흐려지는 
상황이라는 
점이 
분명해졌다
. 
특히 
use case 1
을 
바로 
삭제하기보다는 
우선순위를 
낮추고
, 
먼저 
경쟁 
서비스가 
해결하지 
못하는 
질문 
시나리오를 
확보한 
뒤 
그에 
맞춰 
핵심 
기능을 
정렬하는 
방식이 
더 
합리적이라고 
판단된다
. 
또한 
설문과 
사용자 
테스트는 
선택 
사항이 
아니라 
프로젝트 
설득력을 
뒷받침하는 
검증 
장치로 
보아야 
하므로
, 
가능한 
범위 
안에서 
반드시 
추진할 
필요가 
있다
. 
8. 
결론 
교수님 
조언의 
핵심은 
명확했다
. 
지금 
단계에서 
중요한 
것은 
서비스 
설명을 
더 
화려하게 
만드는 
것이 
아니라
, 
경쟁 
서비스의 
구체적 
한계를 
먼저 
붙잡고
, 
그 
한계를 
분명히 
넘는 
최소 
기능 
조합을 
설계하는 
일이다
. 
따라서 
이후 
작업은 
‘
많이 
만드는 
방향
’
이 
아니라 
‘
반드시 
이기는 
장면을 
만드는 
방향
’
으로 
재정렬되어야 
한다
.

## 4. 팀원별 학기초 개인설문

### 김겨레

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: Spring / FastAPI / AI / Infra에 관심이 있고, Spring 위주 백엔드 개발 경험이 많습니다. 기본 협업 플로우 설계부터 배포까지 전 과정 경험이 있고, 개발 리드 경험이 많아 타 파트와의 소통을 잘 한다고 생각합니다. AI 활용에 익숙해 빠르게 코딩하고 성능/안정성/운영 문제 훑는 일에 익숙합니다.
- **이번에 팀이 구성된 계기**: 팀장이랑 아는 사이인데, 팀장이 기획안을 들고 와서 먼저 제안해주었습니다.

### 손하늘

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: 데이터 기반 의사결정에 관심이 있는데, AI 활용하면 훨씬 질 좋은 결과물을 얻을 것이라 생각했다. 특히 개발을 잘 모를 때 it학회에서 PM을 맡으며 기획자나 비개발 직군이 데이터에 쉽게 접근할 수 있도록 하는 툴이 있으면 좋겠다고 생각했다.
- **이번에 팀이 구성된 계기**: BE는 AI에 관심이 있고, 기존에 BE를 잘 하고 있는 것을 알고 있는 친구라 영입하였고, FE의 경우 FE 경험은 많지 않지만 열정 있게 팀 활동에 임해주실 것 같아 모시게 되었다.

### 민지인

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: 기술적 관심 영역: 네트워크 및 무선 시스템, 데이터베이스(SQL), AI를 활용한 데이터 처리 및 분석

산출물: 교내 동아리 사이드 프로젝트로 ‘스크랩 아카이빙 플랫폼’을 개발하여 배포한 경험이 있습니다. Spring Boot 기반으로 개발한 서비스로 흩어져 있는 웹 스크랩을 한 곳에 저장하고, 스크랩을 저장한 맥락과 정보를 함께 관리할 수 있도록 하는 것을 목표로 한 서비스였습니다.

남보다 잘한다고 생각되는 영역: 특정 기술에서 뛰어나다고 생각하기보다는 협업 과정에서의 기본적인 원칙을 중요하게 생각합니다. 시간 약속을 지키고 맡은 역할을 책임감 있게 수행하며, 문제 상황이 생겼을 때 팀원들과 충분히 소통하며 해결하려고 노력하는 점은 저의 강점이라고 생각합니다.
- **이번에 팀이 구성된 계기**: 원래는 백엔드 개발을 중심으로 프로젝트에 참여해 왔습니다. 그러나 본 팀이 데이터베이스와 AI 관련 주제로 프론트엔드 파트를 모집하는 것을 보고 평소 관심 있던 분야와 맞닿아 있다고 생각했습니다.
새로운 역할인 프론트엔드에도 도전하면서 기술적으로 성장해 보고 싶다는 생각에 팀장에게 지원하게 되었습니다.

### 김예원

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: 프론트엔드 개발에 관심이 많고, React/Next.js + TypeScript 기반 웹 개발을 주로 합니다.
만들어본 것들:

여기어때 인턴십에서 JSP→React 마이그레이션, 디자인 시스템 컴포넌트 개발, 스크린샷→코드 변환 AI 툴(Screencraft) 개발
소셜미디어 관리 플랫폼(ClipEdu) - TikTok/Instagram/YouTube 등 멀티플랫폼 OAuth 연동, 예약 포스팅
골프장 매매 중개 플랫폼, 쇼핑몰 등 다수 프리랜스 프로젝트
Cafe24/Imweb 기반 커스텀 웹사이트 다수 제작

강점:

빠른 프로토타이핑과 UI/UX 구현
AI API(Claude, Gemini) 활용한 개발 도구 제작 경험
실제 서비스 배포 및 운영 경험(AWS, Vercel)
- **이번에 팀이 구성된 계기**: 데이터 분석 툴을 제작하기 위해 직접 팀원을 모집했습니다. 각자 담당 파트에 열정과 실무 경험이 있는 팀원들끼리 모여 구성하게 되었습니다.

## 5. 개인별 5 Questions

### 김겨레

- **질문당 한줄씩 5개의 질문**: 데이터 조회 과정에서 가장 번거로운 단계는 무엇인가요?
원하는 데이터를 바로 얻지 못한 경험이 있나요?
SQL을 잘 모르는 사람이 데이터를 확인하려 할 때 어떤 문제가 생기나요?
이런 문제가 얼마나 자주 발생하나요?
SQL을 작성하기 어려울 때 보통 어떻게 해결하시나요?

### 민지인

- **질문당 한줄씩 5개의 질문**: 1. 최근 이 문제를 겪었던 구체적인 상황을 하나만 떠올려 설명해 주실 수 있나요? 그때 어떤 행동을 하셨나요?
2. 그 상황에서 문제를 해결하기 위해 선택한 방법은 무엇이었고, 그 이유는 무엇이었나요?
3. 그 과정에서 시간, 비용, 노력 중 어떤 부분이 가장 크게 부담되었나요? (가능하다면 대략적인 수준도 함께)
4. 현재 방식이 완전히 만족스럽지 않다면, 어떤 점이 가장 먼저 개선되길 바라시나요? (우선순위 1개만)
5. 만약 새로운 해결 방법이 있다면, 지금 사용 중인 방식에서 바꾸기 위해 반드시 충족되어야 할 조건은 무엇인가요?

### 손하늘

- **질문당 한줄씩 5개의 질문**: 1.최근 3개월 동안 업무에서 데이터를 조회한 경험이 있으신가요? 있다면 어떻게 조회하셨나요?
2. 현재 어떤 직무를 맡고 계신지 간단히 소개 부탁드립니다.
3. 업무 중 데이터 확인이 필요한 상황은 보통 어떤 경우인가요?
4. 중간에 수정 요청이나 재작업이 발생했나요?
5. 데이터를 확인하는 과정에서 개선되었으면 하는 점이 있다면 무엇인가요?

## 6. 기반 소프트웨어 리스트

env:
  - Device : PC(Window)
  - FE
  - - Next.js
  - - Typescript
  - - Vite
  - - yarn
  - - Axios
  - - Tailwindcss v4.2
  - - StoryBook
  - - Zustand
  - - Tanstack Query
  - - React Hook form + Zod
  - - shadcn/ui (ui  컴포넌트)
  - - ECharts
  - - Monaco Editor(필요시)
  - - Vercel or Jenkins
  - BE
  - - Java 21, Spring Boot 3
  - - Spring AOP
  - - PostgreSQL
  - - AWS RDS
  - - AWS S3
  - - Redis
  - - Flyway
  - - Github Actions
  - - Docker
  - - Kubernetes
  - - AWS ec2, Route53, ALB
  - - AWS CloudWatch
  - - Sentry
  - - Slf4j, Logback
  - - Spring Security
  - - OAuth2.0
  - - JWT
  - - Swagger
  - - k6, p6spy
  - AI
  - - Python
  - - FastAPI
  - - Pydantic v2
  - - pandas
  - - sentence-transformers
  - - OpenAI API
  - - Uvicorn
  - - pytest
  - - Render
  - - GitHub Actions

url:
  - https://nextjs.org/)
  - https://www.google.com/search?q=vite&oq=vite&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg7MgYIAhBFGDsyBggDEEUYOzIGCAQQRRg9MgYIBRBFGEEyBggGEEUYQTIGCAcQRRhB0gEIMTAwN2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8)
  - https://yarnpkg.com/)
  - https://axios-http.com/kr/docs/intro)
  - https://tailwindcss.com/)
  - https://storybook.js.org/)
  - https://zustand-demo.pmnd.rs/)
  - https://tanstack.com/query/latest)
  - https://vercel.com/)
  - https://www.jenkins.io/)
  - https://spring.io/projects/spring-boot
  - https://www.postgresql.org/download/
  - https://redis.io/download/
  - https://flywaydb.org/download
  - https://docs.docker.com/get-docker/
  - https://kubernetes.io/docs/tasks/tools/
  - https://aws.amazon.com/cli/
  - https://docs.sentry.io/product/sentry-basics/integrate-backend/
  - http://www.slf4j.org/download.html
  - https://logback.qos.ch/download.html
  - https://spring.io/projects/spring-security
  - https://swagger.io/tools/swagger-ui/download/
  - https://grafana.com/docs/k6/latest/set-up/install-k6/
  - https://github.com/p6spy/p6spy
  - https://www.python.org/downloads/
  - https://fastapi.tiangolo.com/
  - https://docs.pydantic.dev/latest/
  - https://pandas.pydata.org/docs/
  - https://www.sbert.net/
  - https://platform.openai.com/docs/api-reference
  - https://www.uvicorn.org/
  - https://docs.pytest.org/
  - https://render.com/
  - https://docs.github.com/actions

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
