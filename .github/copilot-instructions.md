# GitHub Copilot Instructions

GitHub Copilot을 위한 프로젝트 지침입니다.

## 1. 언어 및 문체

| 항목 | 규칙 |
|------|------|
| **출력 언어** | 한국어 (명시적 요청 시에만 영어) |
| **문체** | 간결하고 전문적인 매뉴얼 톤 |
| **경어** | '하십시오' 또는 '해요' 체 |
| **이모지** | 사용하지 않음 |

## 2. 서식 규칙

| 항목 | 형식 | 예시 |
|------|------|------|
| 날짜 | `YYYY. MM. DD.` | 2025. 11. 25. |
| 금액 | 천 단위 쉼표 + '원' | 10,000,000원 |
| 목록 | 글머리 기호 또는 표 사용 | - |
| 다국어 병기 | 한국어 먼저, 줄바꿈 후 영어 | `## 제목\n## (Title)` |

## 3. 개인정보 보호

- 주민등록번호, 전화번호, 학번 등 개인정보 출력 금지
- 민감 정보는 마스킹 처리: `010-****-5678`

## 4. 용어 및 맥락

| 항목 | 규칙 |
|------|------|
| **대상 독자** | 비기술직 행정직원 (IT 전문용어 지양) |
| **대학 용어** | 정확한 용어 사용 ('수강신청', '단과대학', '품의서' 등) |
| **문서 스타일** | 표 중심 정보 전달, 불필요한 설명 최소화 |

## 5. MCP 도구 (Byterover)

### byterover-store-knowledge
다음 상황에서 반드시 사용:
- 코드베이스에서 새로운 패턴/API/아키텍처 학습 시
- 오류 해결 방법 발견 시
- 재사용 가능한 코드 패턴 발견 시

### byterover-retrieve-knowledge
다음 상황에서 반드시 사용:
- 새 작업 시작 전 관련 컨텍스트 수집
- 아키텍처 결정 전 기존 패턴 확인
- 디버깅 시 이전 해결책 조회

[byterover-mcp]

[byterover-mcp]

You are given two tools from Byterover MCP server, including
## 1. `byterover-store-knowledge`
You `MUST` always use this tool when:

+ Learning new patterns, APIs, or architectural decisions from the codebase
+ Encountering error solutions or debugging techniques
+ Finding reusable code patterns or utility functions
+ Completing any significant task or plan implementation

## 2. `byterover-retrieve-knowledge`
You `MUST` always use this tool when:

+ Starting any new task or implementation to gather relevant context
+ Before making architectural decisions to understand existing patterns
+ When debugging issues to check for previous solutions
+ Working with unfamiliar parts of the codebase
