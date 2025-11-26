# GitHub Copilot 지침 파일 활용 가이드 (대학 구성원용)

> **대상 독자**: 대학교 교수, 학생, 연구원, 행정직원  
> **필요 조건**: VS Code 설치 및 GitHub Copilot 구독  
> **최종 수정일**: 2025년 11월 26일

---

## 목차

1. [개요](#1-개요)
2. [주요 파일 유형 설명](#2-주요-파일-유형-설명)
3. [지침 설정 방법](#3-지침-설정-방법)
4. [대학 구성원별 활용 예시](#4-대학-구성원별-활용-예시)
5. [권장 폴더 구조](#5-권장-폴더-구조)
6. [applyTo 패턴 활용법](#6-applyto-패턴-활용법)
7. [시작하기 (단계별 가이드)](#7-시작하기-단계별-가이드)
8. [자주 묻는 질문 (FAQ)](#8-자주-묻는-질문-faq)

---

## 1. 개요

### 1.1 Copilot 지침 파일이란?

GitHub Copilot 지침 파일은 AI 어시스턴트인 Copilot에게 **"이 프로젝트에서는 이렇게 답변해줘"**라고 미리 알려주는 설정 파일입니다.

**비유로 설명하면:**
- 새로 채용한 조교에게 "우리 연구실에서는 보고서를 이런 형식으로 작성해"라고 알려주는 매뉴얼
- 학생에게 "이 과목 리포트는 APA 형식으로 작성하세요"라고 알려주는 가이드라인
- 공문 작성 시 참고하는 기관 내부 양식집

### 1.2 왜 필요한가? (대학 업무 관점)

| 문제 상황 | 지침 파일 없이 | 지침 파일 있으면 |
|-----------|----------------|------------------|
| 연구 제안서 작성 | 매번 형식 설명 필요 | 자동으로 형식 준수 |
| 논문 작성 | 학술 용어 번역 불일관 | 일관된 전문용어 사용 |
| 강의자료 제작 | 학과별 스타일 무시 | 학과 맞춤형 콘텐츠 |
| 행정 문서 | 공문서 형식 오류 | 기관 양식 자동 적용 |

### 1.3 주요 이점

✅ **일관성**: 동일한 프로젝트에서 항상 같은 스타일로 응답  
✅ **효율성**: 매번 같은 설명을 반복할 필요 없음  
✅ **협업**: 연구실/학과 단위로 설정 공유 가능  
✅ **맥락 이해**: 프로젝트별 특수 용어나 요구사항 자동 적용

---

## 2. 주요 파일 유형 설명

GitHub Copilot은 네 가지 유형의 지침 파일을 지원합니다.

### 2.1 copilot-instructions.md (프로젝트 기본 지침)

**용도**: 프로젝트 전체에 적용되는 기본 규칙

**위치**: 프로젝트 폴더 내 `.github/copilot-instructions.md`

**특징**:
- 프로젝트 폴더를 열면 자동으로 적용
- 모든 대화에 기본으로 포함
- 팀원과 Git으로 공유 가능

**예시 (연구 프로젝트용)**:
```markdown
# 연구 프로젝트 기본 지침

## 프로젝트 개요
이 프로젝트는 2026년도 NRF 기초연구사업 신청을 위한 연구 제안서 작성 프로젝트입니다.

## 문서 작성 원칙
- 모든 문서는 한국어로 작성
- 학술 용어는 영문 병기 (예: 인공지능(Artificial Intelligence))
- 참고문헌은 APA 7th Edition 형식 사용

## 핵심 용어
- LLM: Large Language Model (대규모 언어 모델)
- RAG: Retrieval-Augmented Generation (검색 증강 생성)
```

### 2.2 Instruction Files (.instructions.md)

**용도**: 특정 파일 유형이나 폴더에만 적용되는 세부 규칙

**위치**: 
- 프로젝트 내: `.github/instructions/*.instructions.md`
- 개인 설정: VS Code 설정의 프롬프트 폴더

**특징**:
- `applyTo` 패턴으로 적용 범위 지정
- 여러 파일 생성하여 상황별 규칙 관리
- 자동 첨부 또는 수동 선택 가능

**예시 (논문 작성용)**:
```markdown
---
applyTo: "**/paper/**/*.md"
---
# 논문 작성 지침

## 구조
1. 초록 (Abstract) - 200단어 이내
2. 서론 (Introduction)
3. 방법 (Methods)
4. 결과 (Results)
5. 논의 (Discussion)
6. 결론 (Conclusion)

## 인용 형식
- 본문 내 인용: (저자, 연도)
- 참고문헌: APA 7th Edition
```

### 2.3 Prompt Files (.prompt.md)

**용도**: 재사용 가능한 프롬프트 템플릿

**위치**:
- 프로젝트 내: `.github/prompts/*.prompt.md`
- 개인 설정: VS Code 설정의 프롬프트 폴더

**특징**:
- 채팅창에서 `/` 명령으로 호출
- 변수 사용 가능 (`$SELECTION`, `$FILE` 등)
- 반복 작업 자동화에 적합

**예시 (문헌 요약용)**:
```markdown
---
description: "학술 논문을 구조화된 형식으로 요약"
mode: "ask"
---
# 논문 요약 프롬프트

다음 논문을 아래 형식으로 요약해주세요:

## 요약 대상
${selection}

## 요약 형식
### 연구 목적
(1-2문장)

### 연구 방법
(3-4문장)

### 주요 결과
- 결과 1
- 결과 2
- 결과 3

### 한계점 및 시사점
(2-3문장)

### 인용 정보
(APA 형식)
```

### 2.4 AGENTS.md (에이전트 모드용)

**용도**: Copilot 에이전트 모드에서 자율적 작업 수행 시 참조

**위치**: 프로젝트 루트 또는 하위 폴더의 `AGENTS.md`

**특징**:
- 에이전트가 코드 수정, 명령 실행 시 참조
- 해당 폴더와 하위 폴더에 적용
- 기술적 프로젝트에서 주로 사용

---

## 3. 지침 설정 방법

### 3.1 프로젝트 레벨 설정 (팀 공유용)

**장점**: Git으로 공유, 팀원 모두 동일 설정 사용

**설정 방법**:
1. 프로젝트 폴더에 `.github` 폴더 생성
2. `copilot-instructions.md` 파일 생성
3. 지침 내용 작성
4. Git commit하여 팀과 공유

```
프로젝트폴더/
├── .github/
│   ├── copilot-instructions.md    # 기본 지침
│   ├── instructions/              # 세부 지침
│   │   ├── paper.instructions.md
│   │   └── proposal.instructions.md
│   └── prompts/                   # 프롬프트 템플릿
│       ├── summarize.prompt.md
│       └── translate.prompt.md
└── (프로젝트 파일들...)
```

### 3.2 개인 설정 (모든 프로젝트 적용)

**장점**: 한 번 설정으로 모든 프로젝트에서 사용

**설정 방법**:
1. VS Code 설정 열기 (`Cmd+,` 또는 `Ctrl+,`)
2. "copilot chat prompts" 검색
3. "Chat: Prompts Folders" 설정에 폴더 경로 추가
4. 해당 폴더에 `.instructions.md` 또는 `.prompt.md` 파일 생성

**추천 개인 폴더 구조**:
```
~/my-copilot-prompts/
├── academic-writing.instructions.md     # 학술 글쓰기 규칙
├── korean-formal.instructions.md        # 한국어 공식 문서 규칙
├── summarize-paper.prompt.md            # 논문 요약 템플릿
└── translate-abstract.prompt.md         # 초록 번역 템플릿
```

### 3.3 VS Code 설정 상세

#### 기본 지침 활성화
```json
{
  "github.copilot.chat.codeGeneration.useInstructionFiles": true
}
```

#### 개인 프롬프트 폴더 지정
```json
{
  "chat.promptFiles.locations": [
    {
      "path": "/Users/username/my-copilot-prompts"
    }
  ]
}
```

---

## 4. 대학 구성원별 활용 예시

### 4.1 교수용

#### 4.1.1 연구 제안서 작성

**파일**: `.github/instructions/proposal.instructions.md`

```markdown
---
applyTo: "**/proposal/**"
---
# 연구 제안서 작성 지침

## 작성 원칙
1. **간결하고 명확한 문장**: 한 문장에 하나의 아이디어만
2. **객관적 근거 제시**: 주장마다 참고문헌 인용
3. **정량적 표현 선호**: "많은" 대신 "약 70%의"

## 필수 포함 요소
- [ ] 연구 목적 및 필요성
- [ ] 국내외 연구 동향
- [ ] 연구 내용 및 방법
- [ ] 기대 효과 및 활용 방안
- [ ] 추진 일정

## 용어 사용 규칙
- 전문용어 첫 등장 시 영문 병기
- 약어 첫 등장 시 풀이 후 사용
- 예시: 대규모 언어 모델(Large Language Model, LLM)

## 페이지 제한
- 연구 목적: 1페이지
- 연구 내용: 5페이지 이내
- 참고문헌: 별도
```

#### 4.1.2 논문 작성

**파일**: `.github/instructions/paper.instructions.md`

```markdown
---
applyTo: "**/papers/**/*.md"
---
# 학술 논문 작성 지침

## 문체
- 수동태보다 능동태 선호 (단, 방법론 섹션 제외)
- 1인칭 복수 사용 (We propose, Our approach)
- 현재 시제 (일반적 사실), 과거 시제 (실험 결과)

## 논문 구조
### Abstract (250단어 이내)
- 연구 배경 (1-2문장)
- 연구 목적 (1문장)
- 방법 (2-3문장)
- 결과 (2-3문장)
- 의의 (1-2문장)

### Introduction
- 연구 배경 및 동기
- 문제 정의
- 연구 기여점 (contributions)
- 논문 구성

### Related Work
- 선행 연구 분류별 정리
- 본 연구와의 차별점 명시

## 인용 형식
- IEEE 형식: [1], [2], [3-5]
- 저자 언급 시: Kim et al. [1] proposed...

## Figure/Table 규칙
- 본문에서 반드시 언급: "Figure 1 shows..."
- 캡션은 독립적으로 이해 가능하게
```

#### 4.1.3 강의자료 제작

**파일**: `.github/instructions/lecture.instructions.md`

```markdown
---
applyTo: "**/lectures/**"
---
# 강의자료 제작 지침

## 대상 학생
- 학부 3-4학년
- 선수과목: 프로그래밍 기초, 자료구조

## 슬라이드 원칙
1. **한 슬라이드 = 한 개념**: 핵심 메시지는 하나만
2. **시각적 요소 활용**: 다이어그램, 플로우차트 포함
3. **글머리 기호 사용**: 긴 문단 지양, 6줄 이내

## 설명 방식
- 개념 → 예시 → 연습문제 순서
- 일상적 비유로 시작
- 코드 예제는 단계별로 분리

## 예시 형식
```python
# 좋은 예시: 단계별 주석 포함
def example():
    # Step 1: 데이터 준비
    data = load_data()
    
    # Step 2: 전처리
    processed = preprocess(data)
    
    # Step 3: 결과 반환
    return processed
```

## 연습문제 형식
- 난이도 표시: ⭐ (기초), ⭐⭐ (중급), ⭐⭐⭐ (심화)
- 힌트 제공
- 예상 소요시간 명시
```

#### 4.1.4 학생 피드백 작성

**파일**: `.github/prompts/feedback.prompt.md`

```markdown
---
description: "학생 과제/논문에 대한 건설적 피드백 작성"
mode: "ask"
---
# 과제 피드백 프롬프트

## 피드백 대상
${selection}

## 피드백 형식

### 1. 전체 평가 (Overall Assessment)
- 잘한 점 2-3가지 먼저 언급
- 전체적인 완성도 평가

### 2. 구체적 개선점 (Specific Improvements)
각 항목에 대해:
- **현재 상태**: 무엇이 부족한지
- **개선 방향**: 어떻게 고치면 좋을지
- **참고 자료**: 관련 문헌이나 예시

### 3. 우선순위 (Priority)
- 🔴 필수 수정: 제출 전 반드시
- 🟡 권장 수정: 가능하면
- 🟢 선택 수정: 시간 여유 시

### 4. 격려 메시지
노력을 인정하고 발전 가능성 언급

## 톤앤매너
- 건설적이고 구체적
- 비판이 아닌 제안 형식
- 학생의 자존감 고려
```

---

### 4.2 학생용

#### 4.2.1 과제 및 리포트 작성

**파일**: `.github/instructions/assignment.instructions.md`

```markdown
---
applyTo: "**/assignments/**"
---
# 과제 작성 지침

## 기본 형식
- 글꼴: 맑은 고딕 11pt
- 줄간격: 1.5줄
- 여백: 상하좌우 2.5cm
- 분량: 교수님 지정 분량 ±10%

## 과제 구조
1. **표지**
   - 과목명, 과제명
   - 학번, 이름
   - 제출일

2. **목차** (5페이지 이상 시)

3. **본문**
   - 서론: 주제 소개, 작성 목적
   - 본론: 핵심 내용, 논리적 전개
   - 결론: 요약, 의견

4. **참고문헌**
   - 인용한 모든 자료 명시
   - 형식 통일 (APA, MLA 등)

## 금지 사항
❌ 위키피디아 직접 인용
❌ 출처 없는 이미지 사용
❌ 다른 학생 과제 참고
❌ AI 생성 내용 무검증 사용

## AI 활용 시 주의사항
✅ AI는 아이디어 브레인스토밍에 활용
✅ 생성된 내용 반드시 검증
✅ AI 활용 사실 명시 (교수님 지침 따름)
✅ 최종 내용은 본인이 이해하고 수정
```

#### 4.2.2 졸업논문 작성

**파일**: `.github/instructions/thesis.instructions.md`

```markdown
---
applyTo: "**/thesis/**"
---
# 졸업논문 작성 지침

## 논문 구조
1. **표지**: 학교 양식 준수
2. **인준서**: 지도교수 서명란
3. **초록**: 국문/영문 각 1페이지
4. **목차**: 그림/표 목차 포함
5. **본문**
   - 제1장: 서론
   - 제2장: 이론적 배경
   - 제3장: 연구 방법
   - 제4장: 연구 결과
   - 제5장: 결론 및 제언
6. **참고문헌**
7. **부록** (필요시)

## 장/절 번호 체계
- 장: 제1장, 제2장...
- 절: 1.1, 1.2, 1.3...
- 항: 1.1.1, 1.1.2...

## 그림 및 표
- 그림: [그림 1-1] 설명
- 표: <표 1-1> 설명
- 본문 언급 후 배치

## 참고문헌 형식 (학과 지정)
- 국내문헌: 저자(연도). 제목. 출판사.
- 영문문헌: Author, A. A. (Year). Title. Publisher.
- 웹자료: URL (접속일: 2025.11.26)
```

#### 4.2.3 발표 준비

**파일**: `.github/prompts/presentation-prep.prompt.md`

```markdown
---
description: "발표 자료 구조화 및 스크립트 작성"
mode: "ask"
---
# 발표 준비 프롬프트

## 발표 정보
- 주제: ${input:발표 주제}
- 시간: ${input:발표 시간(분)}
- 청중: ${input:청중 유형(교수/학생/일반)}

## 요청사항
위 정보를 바탕으로 다음을 작성해주세요:

### 1. 슬라이드 구성안
- 각 슬라이드 제목과 핵심 내용
- 슬라이드당 예상 시간
- 시각 자료 제안

### 2. 발표 스크립트
- 도입부 (청중 주의 끌기)
- 전환 문구
- 핵심 강조 부분
- 마무리 멘트

### 3. 예상 질문 및 답변
- Q1:
- A1:
- Q2:
- A2:
```

---

### 4.3 연구원용

#### 4.3.1 실험 보고서 작성

**파일**: `.github/instructions/experiment.instructions.md`

```markdown
---
applyTo: "**/experiments/**"
---
# 실험 보고서 작성 지침

## 보고서 구조
1. **실험 개요**
   - 실험명
   - 실험 일시
   - 실험자
   - 실험 목적

2. **실험 환경**
   - 하드웨어 사양
   - 소프트웨어 버전
   - 데이터셋 정보

3. **실험 방법**
   - 실험 설계
   - 파라미터 설정
   - 평가 지표

4. **실험 결과**
   - 정량적 결과 (표/그래프)
   - 정성적 분석
   - 오류 분석

5. **결론 및 향후 계획**

## 재현성 보장
- [ ] 랜덤 시드 기록
- [ ] 코드 버전 (commit hash)
- [ ] 데이터셋 버전
- [ ] 환경 설정 파일 첨부

## 표기 규칙
- 수치: 소수점 둘째자리 (예: 0.95)
- 백분율: 소수점 첫째자리 (예: 95.3%)
- 통계적 유의성: p < 0.05 명시
```

#### 4.3.2 연구 노트 작성

**파일**: `.github/instructions/research-notes.instructions.md`

```markdown
---
applyTo: "**/notes/**/*.md"
---
# 연구 노트 작성 지침

## 일일 노트 형식
```
# 연구 노트: YYYY-MM-DD

## 오늘의 목표
- [ ] 목표 1
- [ ] 목표 2

## 수행 내용
### 실험/분석 1
- 내용:
- 결과:
- 문제점:

## 발견/인사이트
- 

## 내일 할 일
- 

## 참고 자료
- 논문:
- 코드:
```

## 주간 요약 형식
- 주요 진행 상황
- 달성 목표 vs 미달성 목표
- 주요 발견점
- 다음 주 계획

## 태그 시스템
- #experiment: 실험 관련
- #reading: 논문 읽기
- #idea: 아이디어
- #bug: 문제/버그
- #meeting: 미팅 내용
```

#### 4.3.3 코드 문서화

**파일**: `.github/instructions/code-docs.instructions.md`

```markdown
---
applyTo: "**/*.py"
---
# Python 코드 문서화 지침

## Docstring 형식 (Google Style)
```python
def function_name(param1: str, param2: int) -> dict:
    """함수에 대한 간단한 설명.
    
    더 자세한 설명이 필요한 경우 여기에 작성.
    여러 줄로 작성 가능.
    
    Args:
        param1: 첫 번째 파라미터 설명
        param2: 두 번째 파라미터 설명
    
    Returns:
        반환값에 대한 설명
        
    Raises:
        ValueError: 어떤 조건에서 발생하는지
        
    Example:
        >>> result = function_name("test", 42)
        >>> print(result)
        {'status': 'success'}
    """
```

## 클래스 문서화
```python
class ModelTrainer:
    """모델 학습을 관리하는 클래스.
    
    Attributes:
        model: 학습할 모델
        config: 학습 설정
        
    Example:
        trainer = ModelTrainer(model, config)
        trainer.train()
    """
```

## 모듈 상단 주석
```python
"""모듈명: data_loader.py

데이터 로딩 및 전처리 기능 제공.

주요 기능:
    - 데이터셋 로딩
    - 배치 생성
    - 데이터 증강

Author: 홍길동
Created: 2025-11-01
"""
```
```

---

### 4.4 행정직원용

#### 4.4.1 공문서 작성

**파일**: `.github/instructions/official-document.instructions.md`

```markdown
---
applyTo: "**/documents/**"
---
# 공문서 작성 지침

## 문서 형식
- 용지: A4 세로
- 글꼴: 휴먼명조 또는 바탕체
- 본문: 13pt, 줄간격 160%
- 여백: 위 15mm, 아래 15mm, 좌우 20mm

## 공문서 구성요소
1. **두문**
   - 기관명
   - 수신자
   - (경유)

2. **본문**
   - 제목
   - 내용 (1., 가., 1), 가))
   - 붙임

3. **결문**
   - 끝. 표시
   - 발신기관명
   - 직인

## 문체 규칙
- 경어체 사용 (~습니다, ~합니다)
- 간결하고 명확한 표현
- 불필요한 수식어 지양
- 전문용어 최소화

## 날짜 표기
- 연월일: 2025. 11. 26.
- 기간: 2025. 11. 26. ~ 2025. 12. 31.

## 금액 표기
- 한글과 숫자 병기: 금 1,000,000원(일백만 원)
```

#### 4.4.2 회의록 작성

**파일**: `.github/prompts/meeting-minutes.prompt.md`

```markdown
---
description: "회의 내용을 체계적인 회의록으로 정리"
mode: "ask"
---
# 회의록 작성 프롬프트

## 회의 정보
다음 회의 내용을 회의록으로 정리해주세요:

${selection}

## 회의록 형식

### 회의 개요
| 항목 | 내용 |
|------|------|
| 회의명 | |
| 일시 | |
| 장소 | |
| 참석자 | |
| 불참자 | |
| 작성자 | |

### 회의 안건
1. 안건 1
2. 안건 2

### 회의 내용
#### 안건 1: [제목]
- 논의 내용:
- 결정 사항:
- 담당자 및 기한:

### 향후 일정
| 할 일 | 담당자 | 기한 |
|-------|--------|------|
| | | |

### 다음 회의
- 일시:
- 안건:
```

#### 4.4.3 보고서 작성

**파일**: `.github/instructions/report.instructions.md`

```markdown
---
applyTo: "**/reports/**"
---
# 행정 보고서 작성 지침

## 보고서 종류별 형식

### 업무 보고서
1. 보고 개요
2. 추진 현황
3. 주요 성과
4. 향후 계획
5. 건의 사항

### 사업 결과 보고서
1. 사업 개요
2. 추진 경과
3. 추진 실적
4. 예산 집행 현황
5. 성과 분석
6. 문제점 및 개선방안
7. 향후 계획

### 출장 보고서
1. 출장 개요 (일시, 장소, 목적)
2. 주요 활동 내용
3. 결과 및 성과
4. 건의 사항

## 작성 원칙
- 두괄식 작성 (결론 먼저)
- 객관적 사실 기반
- 수치화된 성과 제시
- 명확한 후속 조치 제안

## 표/차트 활용
- 수치 데이터는 표로 정리
- 추이는 그래프로 시각화
- 출처 명시
```

---

## 5. 권장 폴더 구조

### 5.1 연구 프로젝트용

```
연구프로젝트/
├── .github/
│   ├── copilot-instructions.md      # 프로젝트 기본 지침
│   ├── instructions/
│   │   ├── paper.instructions.md    # 논문 작성 규칙
│   │   ├── proposal.instructions.md # 제안서 작성 규칙
│   │   └── code.instructions.md     # 코드 작성 규칙
│   └── prompts/
│       ├── summarize.prompt.md      # 논문 요약 템플릿
│       ├── translate.prompt.md      # 번역 템플릿
│       └── review.prompt.md         # 리뷰 템플릿
├── papers/                           # 논문 파일
├── proposal/                         # 제안서 파일
├── experiments/                      # 실험 코드 및 결과
├── data/                             # 데이터
└── notes/                            # 연구 노트
```

### 5.2 강의용

```
강의자료/
├── .github/
│   ├── copilot-instructions.md
│   └── instructions/
│       ├── slides.instructions.md   # 슬라이드 규칙
│       └── exercise.instructions.md # 연습문제 규칙
├── week01/
│   ├── slides/
│   ├── exercises/
│   └── solutions/
├── week02/
│   └── ...
└── exams/
```

### 5.3 개인 프롬프트 폴더 (모든 프로젝트 공통)

```
~/copilot-prompts/
├── academic/
│   ├── paper-writing.instructions.md
│   ├── citation-apa.instructions.md
│   └── academic-korean.instructions.md
├── templates/
│   ├── summarize-paper.prompt.md
│   ├── translate-formal.prompt.md
│   └── brainstorm.prompt.md
└── my-preferences.instructions.md    # 개인 선호 설정
```

---

## 6. applyTo 패턴 활용법

### 6.1 기본 패턴

| 패턴 | 설명 | 적용 대상 |
|------|------|-----------|
| `**/*.md` | 모든 Markdown 파일 | 프로젝트 내 모든 .md 파일 |
| `**/paper/**` | paper 폴더 내 모든 파일 | paper 폴더 하위 전체 |
| `src/**/*.py` | src 폴더의 Python 파일 | src 하위 모든 .py 파일 |
| `*.{md,txt}` | 루트의 md 또는 txt | 최상위 폴더만 |

### 6.2 실용 예시

```markdown
---
# 모든 마크다운 파일에 적용
applyTo: "**/*.md"
---

---
# 논문 폴더에만 적용
applyTo: "**/papers/**"
---

---
# 여러 확장자에 적용
applyTo: "**/*.{py,ipynb}"
---

---
# 특정 파일 제외하고 적용 (패턴 조합)
applyTo: 
  - "**/src/**"
  - "!**/test/**"
---
```

### 6.3 주의사항

- 패턴은 프로젝트 루트 기준
- 대소문자 구분 (OS에 따라 다름)
- 여러 instructions 파일이 같은 파일에 적용될 수 있음
- 충돌 시 더 구체적인 패턴 우선

---

## 7. 시작하기 (단계별 가이드)

### Step 1: VS Code 및 Copilot 준비

1. **VS Code 설치 확인**
   - [code.visualstudio.com](https://code.visualstudio.com)에서 다운로드
   
2. **GitHub Copilot 확장 설치**
   - VS Code 좌측 Extensions 탭 클릭
   - "GitHub Copilot" 검색 후 설치
   - "GitHub Copilot Chat" 도 함께 설치

3. **GitHub 계정 연결**
   - 좌측 하단 계정 아이콘 클릭
   - "Sign in to use GitHub Copilot"

### Step 2: 첫 지침 파일 만들기

1. **프로젝트 폴더 열기**
   - File > Open Folder

2. **`.github` 폴더 생성**
   - 탐색기에서 우클릭 > New Folder
   - `.github` 입력 (점으로 시작)

3. **`copilot-instructions.md` 생성**
   - `.github` 폴더 우클릭 > New File
   - 아래 내용 복사하여 붙여넣기:

```markdown
# 프로젝트 지침

## 기본 정보
이 프로젝트는 [프로젝트 설명]을 위한 것입니다.

## 작성 규칙
- 한국어로 작성
- 존댓말 사용
- 간결한 문장 선호

## 용어집
- [용어1]: [설명]
- [용어2]: [설명]
```

### Step 3: 동작 확인

1. **Copilot Chat 열기**
   - `Cmd+Shift+I` (Mac) 또는 `Ctrl+Shift+I` (Windows)
   
2. **테스트 질문**
   - "이 프로젝트에 대해 알려줘"
   - 지침 파일 내용이 반영되었는지 확인

### Step 4: 활용 확장

1. **상황별 지침 추가**
   - `.github/instructions/` 폴더 생성
   - 용도별 `.instructions.md` 파일 추가

2. **프롬프트 템플릿 추가**
   - `.github/prompts/` 폴더 생성
   - 자주 쓰는 작업용 `.prompt.md` 파일 추가

3. **개인 설정 폴더 지정** (선택)
   - VS Code 설정에서 프롬프트 폴더 경로 추가

---

## 8. 자주 묻는 질문 (FAQ)

### Q1: 지침 파일이 적용되었는지 어떻게 확인하나요?

**A**: Copilot Chat에서 "현재 적용된 지침을 알려줘"라고 물어보면 됩니다. 또는 채팅창 상단의 컨텍스트 영역에서 첨부된 파일을 확인할 수 있습니다.

### Q2: 여러 지침 파일이 충돌하면 어떻게 되나요?

**A**: 모든 해당 지침이 합쳐져서 적용됩니다. 내용이 충돌하는 경우, Copilot이 가장 관련성 높은 규칙을 선택하거나 두 규칙을 조합합니다.

### Q3: 지침 파일을 팀원과 공유하려면?

**A**: `.github` 폴더를 Git에 커밋하면 됩니다. 팀원이 저장소를 clone하면 자동으로 같은 지침이 적용됩니다.

### Q4: 개인 지침을 Git에서 제외하려면?

**A**: `.gitignore` 파일에 해당 경로를 추가합니다:
```
.github/instructions/my-personal.instructions.md
```

### Q5: 지침이 너무 길면 문제가 있나요?

**A**: Copilot은 컨텍스트 길이에 제한이 있으므로, 핵심 내용 위주로 간결하게 작성하는 것이 좋습니다. 긴 지침보다는 여러 개의 짧은 지침 파일로 분리하세요.

### Q6: 지침을 임시로 비활성화하려면?

**A**: 파일 이름을 변경하거나 (예: `paper.instructions.md.bak`), VS Code 설정에서 해당 기능을 끌 수 있습니다:
```json
{
  "github.copilot.chat.codeGeneration.useInstructionFiles": false
}
```

### Q7: `.prompt.md` 파일은 어떻게 사용하나요?

**A**: Copilot Chat에서 `/` 를 입력하면 사용 가능한 프롬프트 목록이 나타납니다. 원하는 프롬프트를 선택하면 해당 템플릿이 적용됩니다.

### Q8: 영문 응답을 한글로 바꾸고 싶어요.

**A**: `copilot-instructions.md`에 다음을 추가하세요:
```markdown
## 언어 설정
- 모든 응답은 한국어로 작성
- 전문용어는 영문 병기 가능
```

---

## 부록: 빠른 참조 카드

### 파일 유형 요약

| 파일 유형 | 확장자 | 위치 | 용도 |
|-----------|--------|------|------|
| 기본 지침 | `copilot-instructions.md` | `.github/` | 프로젝트 전체 규칙 |
| 세부 지침 | `*.instructions.md` | `.github/instructions/` | 특정 파일/폴더 규칙 |
| 프롬프트 | `*.prompt.md` | `.github/prompts/` | 재사용 템플릿 |
| 에이전트 | `AGENTS.md` | 루트 또는 하위 폴더 | 에이전트 모드 지침 |

### 유용한 VS Code 단축키

| 동작 | Mac | Windows |
|------|-----|---------|
| Copilot Chat 열기 | `Cmd+Shift+I` | `Ctrl+Shift+I` |
| 인라인 제안 수락 | `Tab` | `Tab` |
| 다음 제안 | `Alt+]` | `Alt+]` |
| 이전 제안 | `Alt+[` | `Alt+[` |
| 제안 거부 | `Esc` | `Esc` |

### 체크리스트

#### 프로젝트 설정 완료 체크
- [ ] `.github/copilot-instructions.md` 생성
- [ ] 프로젝트 기본 정보 작성
- [ ] 작성 규칙 정의
- [ ] 용어집 추가

#### 팀 공유 준비 체크
- [ ] 지침 파일 Git 커밋
- [ ] README에 지침 파일 설명 추가
- [ ] 팀원에게 사용법 공유

---

> **문서 버전**: 1.0  
> **작성자**: GitHub Copilot 가이드  
> **피드백**: 이 가이드에 대한 의견이나 추가 요청사항이 있으시면 알려주세요.
