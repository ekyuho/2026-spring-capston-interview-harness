# Team 08. 하면된다 심층인터뷰 준비서

## 1. 만들고자 하는 것

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

## 2. 사전 보충자료 요약

자료 없음 또는 정리 필요

## 3. 팀지도교수 면담보고서

자료 없음 또는 PDF 추출 필요

## 4. 팀원별 학기초 개인설문

### 김수연

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: iOS 앱 개발, 프론트엔드, 디자인 등 시각적 요소를 산출하는 활동에 관심이 많습니다. 클라이언트 개발자로 여러 프로젝트에 참여했으며, 실제로 서비스를 출시해 본 경험이 있습니다.
- **이번에 팀이 구성된 계기**: 첫 강의 시간에 하고 싶은 파트가 맞는 인원끼리 팀을 구성하였습니다.

### 조채윤

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: 시스템 로우레벨,서버
C언어로 db,웹소켓,쉘 구현해본적 있음(튜토리얼 기반)
- **이번에 팀이 구성된 계기**: 수업시간에 짬

### 이예주

- **본인의 기술적 관심영역,  실제로 만들어서 작동시켜본 산출물, 남보다 잘한다고 생각되는 영역 등 소개**: 저는 인공지능과 데이터 기반 시스템에 관심을 가지고 있으며, 특히 실제 서비스에 적용할 수 있는 실용적인 AI 응용 분야에 흥미가 있습니다. 이미지나 텍스트 등 다양한 데이터를 활용하여 사용자에게 도움이 되는 기능을 만드는 것에 관심이 있습니다.

지금까지 수업과 프로젝트를 통해 몇 가지 소프트웨어를 직접 구현해 본 경험이 있습니다. 예를 들어 Java 기반 키오스크 주문 프로그램을 개발하여 메뉴 선택, 주문 처리, 사용자 인터페이스 흐름 등을 구현해 보았으며, 이를 통해 객체지향 프로그래밍과 애플리케이션 구조를 이해할 수 있었습니다. 또한 데이터베이스 시스템 프로젝트에서는 맞춤 케이크 주문 관리 시스템을 설계하고 SQL을 이용해 데이터베이스 구조를 설계하고 관리하는 경험을 했습니다.

동아리 활동에서는 냉장고 속 재료를 기반으로 레시피를 추천하는 AI 기반 모바일 애플리케이션 프로젝트에 참여하여, 데이터 처리와 애플리케이션 로직 구현 과정에 참여했습니다. 이 프로젝트를 통해 AI가 실제 서비스에서 어떻게 활용되는지에 대해 경험할 수 있었습니다.

저는 새로운 기술을 빠르게 배우고 실제 프로젝트에 적용하는 것을 좋아하며, 특히 AI 기술을 활용한 서비스 기획과 구현 과정에 관심이 있습니다.
- **이번에 팀이 구성된 계기**: 이번 팀은 AI 기술을 실제 서비스 문제 해결에 적용해 보고자 하는 공통된 관심사를 바탕으로 구성되었습니다. 평소 빈티지 거래 플랫폼이나 중고 거래 서비스를 이용하면서 가격이 적절한지 판단하기 어렵고 원하는 상품을 찾기 위해 계속 플랫폼을 확인해야 하는 불편함이 있다는 점을 느끼게 되었습니다.

이러한 문제를 해결하기 위해 팀원들과 함께 AI 기반 가격 검증 시스템과 정시 경매 방식을 결합한 빈티지 거래 플랫폼을 기획하게 되었습니다. AI를 활용해 상품의 적정 가격을 분석하고, 경매 방식으로 판매 노출을 공정하게 만들어 기존 중고 거래 플랫폼의 문제를 해결해 보고자 합니다.

또한 팀원들 대부분이 AI 및 소프트웨어 개발에 관심이 있는 전공자이기 때문에, 단순한 아이디어 수준을 넘어서 실제로 작동하는 프로토타입을 만들어 보는 것을 목표로 팀을 구성하게 되었습니다.

## 5. 개인별 5 Questions

### 김수연

- **질문당 한줄씩 5개의 질문**: 구매자 대상
1. 가격 불신 검증 질문: 빈티지 상품을 볼 때 가격이 적절한지 판단하기 어렵다고 느낀 적이 있나요? 구체적인 사례가 있다면 말씀해주세요.
2. 탐색 피로 검증 질문: 원하는 상품이 언제 올라올지 몰라서 반복적으로 앱이나 플랫폼을 확인했던 경험이 있나요?

판매자 대상
3. 가격 책정 검증 질문: 비슷한 상품들의 가격 차이가 클 때, 내 가격을 어떻게 정해야 할지 혼란스러웠던 적이 있나요?
4. 노출 비효율 검증 질문: 같은 상품이어도 업로드 시점에 따라 노출 차이가 크다고 느끼시나요?
5. 판매 지연 및 거래 실패 경험 질문: 판매가 잘 되지 않았던 경험이 있다면, 그때 가장 큰 원인은 무엇이었다고 생각하시나요?

### 이예주

- **질문당 한줄씩 5개의 질문**: 빈티지 상품을 살 때 지금 가격이 비싼지 적정한지 판단하기 어려웠던 경험이 있나요?

원하는 빈티지 매물을 찾기 위해 중고거래 앱이나 사이트를 자주 반복해서 확인한 적이 있나요?

판매자라면 내 상품이 제값보다 너무 싸게 팔리거나, 반대로 너무 비싸게 올려져 안 팔릴까 걱정된 적이 있나요?

모든 매물이 정해진 시간에 한꺼번에 공개되는 방식이 있다면, 지금보다 더 공정하고 편하다고 느끼실 것 같나요?

AI가 제시한 예상 가격과 판매자 희망가를 함께 보여준다면 구매하거나 판매할 때 더 신뢰가 갈 것 같나요?

### 조채윤

- **질문당 한줄씩 5개의 질문**: 1. 빈티지 의류를 구매할 때, 판매자가 제시한 가격이 상태 대비 적정한지 의심스러워 구매를 포기하거나 망설였던 경험이 있습니까?
2. 원하는 스타일의 빈티지 제품을 찾기 위해 여러 앱이나 오프라인 샵을 뒤지는 과정에서 느끼는 피로도는 1~10점 중 어느 정도입니까?
3. 만약 AI가 수천 건의 거래 데이터를 분석하여 해당 제품의 '객관적 적정가 범위'를 실시간으로 보여준다면, 구매 결정에 얼마나 도움이 될 것 같습니까?
4. 하루 중 정해진 시간(예: 매일 저녁 8시)에만 짧고 굵게 진행되는 '정시 경매' 방식이 기존의 무기한 리스팅 방식보다 더 빠르고 합리적인 구매를 유도한다고 생각하십니까?
5. '희귀성(빈티지 특성)'과 '객관적 시세(AI 분석)' 중, 귀하가 기꺼이 지갑을 열게 만드는 더 결정적인 요인은 무엇입니까?

## 6. 기반 소프트웨어 리스트

- **env**: 1.Client Device: Wep App
2.FE(Web)
Core: React, TypeScript, Next.js
State Management: TanStack Query, Zustand
Styling: Emotion
CI/CD: GitHub Actions
3.BE:SpringBoot,docker
4.DB:MySQL
5.BE:Spring Data JPA,Spring WebSockets FE:Emotion,TanStack Query,Zustand
6.API Call 서비스:OpenAI API(GPT-4o Vision)
- **url**: https://www.jetbrains.com/idea/download/ (IntelliJ IDEA Community - BE IDE)
https://www.docker.com/products/docker-desktop/ (Docker Desktop - 로컬 MySQL 및 Redis 컨테이너 구동용)
https://www.postman.com/downloads/ (Postman - REST API 엔드포인트 테스트용)
https://dev.mysql.com/downloads/ (MySQL)
https://openai.com/ko-KR/api/ (OpenAI API)
https://spring.io/ (SpringBoot)

FE 개발 머신 설치 소프트웨어
- Node.js: https://nodejs.org/en/download
- pnpm: https://pnpm.io/installation
- Git: https://git-scm.com/install
- Visual Studio Code: https://code.visualstudio.com/download

FE 주요 프레임워크 및 라이브러리 참고 URL
- React: https://react.dev/learn/installation
- Next.js: https://nextjs.org/docs/app/getting-started/installation
- TypeScript: https://www.typescriptlang.org/download/
- TanStack Query: https://tanstack.com/query/latest/docs/framework/react/installation
- Zustand: https://zustand.docs.pmnd.rs/
- Emotion: https://emotion.sh/docs/install
- GitHub Actions: https://docs.github.com/actions

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
