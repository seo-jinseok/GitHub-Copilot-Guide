# Gemini CLI 지침

Gemini CLI 전용 설정입니다. 범용 AI 에이전트 지침은 `AGENTS.md`를 참조하십시오.

## 1. 언어 설정

| 항목 | 규칙 |
|------|------|
| **출력 언어** | 한국어 (명시적 요청 시에만 영어) |
| **문체** | 간결하고 전문적인 매뉴얼 톤 |

## 2. MCP 설정

`~/.gemini/settings.json` 또는 `.gemini/settings.json`에 설정합니다.

```json
{
  "mcpServers": {
    "task-master-ai": {
      "command": "npx",
      "args": ["-y", "task-master-ai"]
    }
  }
}
```

API 키는 `task-master models --setup`으로 별도 설정합니다.

## 3. 세션 관리 명령어

| 명령어 | 기능 |
|--------|------|
| `/chat` | 새 대화 시작 (컨텍스트 유지) |
| `/checkpoint save <name>` | 세션 상태 저장 |
| `/checkpoint load <name>` | 저장된 세션 복원 |
| `/memory show` | 로드된 컨텍스트 조회 |
| `/stats` | 토큰 사용량 및 API 비용 확인 |

## 4. 헤드리스 모드

스크립트 자동화용 비대화형 모드입니다.

```bash
# 텍스트 응답
gemini -p "다음 작업은?"

# JSON 출력
gemini -p "대기 중인 작업 목록" --output-format json

# 스트림 출력
gemini -p "모든 작업 확장" --output-format stream-json
```

## 5. 모델 설정

```bash
# 메인 모델 설정
task-master models --set-main gemini-2.0-flash-exp
task-master models --set-fallback gemini-1.5-flash

# 리서치 모델 (선택)
task-master models --set-research perplexity-llama-3.1-sonar-large-128k-online
```

## 6. 다른 에이전트와의 차이점

| 항목 | Gemini CLI | 기타 (Claude Code 등) |
|------|------------|----------------------|
| 슬래시 명령어 | 자연어 사용 | 커스텀 명령어 지원 |
| 보안 관리 | MCP 레벨 | 에이전트 설정 |
| 세션 관리 | `/checkpoint` | Git worktree |
| 설정 파일 | `.gemini/settings.json` | `.mcp.json` |

## 7. Google 검색 활용

Gemini CLI의 내장 Google 검색을 활용합니다:
- 라이브러리 문서 조회
- 보안 취약점 확인
- 구현 패턴 검색
