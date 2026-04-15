# Team 19. Logue 심층인터뷰 준비서

## 1. 프로젝트 개요

- 트랙: 
- 프로젝트명: 
- 팀원: 
- 지도교수: 
- GitHub Repo: https://github.com/26-ewha-capstone-logue](https://github.com/26-ewha-capstone-logue/logue

## 2. 만들고자 하는 것

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

## 3. 사전 보충자료 요약

자료 없음 또는 정리 필요

## 4. 팀원별 학기초 개인설문

### 김겨레

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 손하늘

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 민지인

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 

### 김예원

- 관심 기술: 
- 강점: 
- 걱정/어려움: 
- 희망 역할: 


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

- **env**: Device : PC(Window)
FE
- Next.js
- Typescript
- Vite
- yarn
- Axios
- Tailwindcss v4.2
- StoryBook
- Zustand
- Tanstack Query
- React Hook form + Zod
- shadcn/ui (ui  컴포넌트)
- ECharts
- Monaco Editor(필요시)
- Vercel or Jenkins

BE
- Java 21, Spring Boot 3
- Spring AOP
- PostgreSQL
- AWS RDS
- AWS S3
- Redis
- Flyway
- Github Actions
- Docker
- Kubernetes
- AWS ec2, Route53, ALB
- AWS CloudWatch
- Sentry
- Slf4j, Logback
- Spring Security
- OAuth2.0
- JWT
- Swagger
- k6, p6spy

AI
- Python
- FastAPI
- Pydantic v2
- pandas
- sentence-transformers
- OpenAI API
- Uvicorn
- pytest
- Render
- GitHub Actions
- **url**: 1. FE
[Next.js by Vercel - The React Framework](https://nextjs.org/)
[Enable JavaScript to use search](https://www.google.com/search?q=vite&oq=vite&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg7MgYIAhBFGDsyBggDEEUYOzIGCAQQRRg9MgYIBRBFGEEyBggGEEUYQTIGCAcQRRhB0gEIMTAwN2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8)
[Home page | Yarn](https://yarnpkg.com/)
[시작하기 | Axios Docs](https://axios-http.com/kr/docs/intro)
[Tailwind CSS - Rapidly build modern websites without ever leaving your HTML.](https://tailwindcss.com/)
[Storybook: Frontend workshop for UI development](https://storybook.js.org/)
[Zustand](https://zustand-demo.pmnd.rs/)
[TanStack Query](https://tanstack.com/query/latest)
[Vercel: Build and deploy the best web experiences with the Frontend Cloud](https://vercel.com/)
[Jenkins](https://www.jenkins.io/)

2. BE
https://spring.io/projects/spring-boot
https://www.postgresql.org/download/
https://redis.io/download/
https://flywaydb.org/download
https://docs.docker.com/get-docker/
https://kubernetes.io/docs/tasks/tools/
https://aws.amazon.com/cli/
https://docs.sentry.io/product/sentry-basics/integrate-backend/
http://www.slf4j.org/download.html
https://logback.qos.ch/download.html
https://spring.io/projects/spring-security
https://swagger.io/tools/swagger-ui/download/
https://grafana.com/docs/k6/latest/set-up/install-k6/
https://github.com/p6spy/p6spy

3. AI
https://www.python.org/downloads/
https://fastapi.tiangolo.com/
https://docs.pydantic.dev/latest/
https://pandas.pydata.org/docs/
https://www.sbert.net/
https://platform.openai.com/docs/api-reference
https://www.uvicorn.org/
https://docs.pytest.org/
https://render.com/
https://docs.github.com/actions

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