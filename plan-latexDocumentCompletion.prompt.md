# LaTeX 문서 전체 완성 계획

기존 `01_GitHub_Copilot_웹서비스_가이드.tex`의 프리앰블과 스타일을 재사용하여, `docs/` 및 `archive/` 폴더의 콘텐츠를 기반으로 5개의 LaTeX 문서를 순차적으로 완성합니다. 콘텐츠가 충분한 3개 문서(02, 03-1, 03-4)를 우선 작업하고, 신규 작성이 필요한 2개(03-2, 03-3)는 기존 자료를 재구성하여 작성합니다.

---

## 문서 목록 (latex file name guide.md 기준)

| 번호 | 파일명 | 문서 제목 | 콘텐츠 상태 |
|------|--------|----------|------------|
| 01 | `01_GitHub_Copilot_웹서비스_가이드.tex` | GitHub Copilot 웹서비스 활용 가이드 | ✅ 완료 |
| 02 | `02_GitHub_Copilot_VSCode_가이드.tex` | GitHub Copilot VS Code 확장 활용 가이드 | ⚠️ 콘텐츠 있음, LaTeX 변환 필요 |
| 03-1 | `03-1_GitHub_Copilot_교수용_가이드.tex` | GitHub Copilot 교수용 활용 가이드 | ⚠️ 콘텐츠 있음, LaTeX 변환 필요 |
| 03-2 | `03-2_GitHub_Copilot_학생용_가이드.tex` | GitHub Copilot 학생용 활용 가이드 | ❌ 신규 작성 필요 |
| 03-3 | `03-3_GitHub_Copilot_연구원용_가이드.tex` | GitHub Copilot 연구원용 활용 가이드 | ❌ 신규 작성 필요 |
| 03-4 | `03-4_GitHub_Copilot_행정직원용_가이드.tex` | GitHub Copilot 행정직원용 활용 가이드 | ⚠️ 콘텐츠 있음, LaTeX 변환 필요 |

---

## Phase 1: 공통 프리앰블 템플릿 분리

### 목표
`01_GitHub_Copilot_웹서비스_가이드.tex`에서 버전 관리, 폰트, 스타일 코드를 `_preamble.tex`로 분리하여 5개 문서에서 `\input{}` 재사용

### 작업 내용
1. `latex/_preamble.tex` 파일 생성
2. 다음 섹션 포함:
   - 문서 버전 관리 (KST 자동 반영)
   - 지오메트리 및 폰트 설정
   - 필수 패키지 로드
   - 색상 정의 (`eduNavy`)
   - 섹션 스타일링
   - 목록 설정
   - 헤더/푸터 설정

### 프리앰블 재사용 구조
```latex
% 각 문서에서:
\documentclass[11pt, a4paper]{article}
\input{_preamble}
\newcommand{\doctitle}{문서 제목}
\newcommand{\docsubtitle}{부제목}
\begin{document}
...
\end{document}
```

---

## Phase 2: 02_VSCode_가이드.tex 작성

### 소스 자료
- `docs/admin/ko/index.md` Level 1~3 섹션
- `archive/ko/level-1-basics/01-setup.md`
- `archive/ko/level-2-practical/05-copilot-edits.md`
- `archive/ko/level-3-expert/07-agents-instructions.md`

### 권장 구조
```
1. 개요
   1.1 VS Code란?
   1.2 왜 VS Code + Copilot인가?
   
2. 설치 및 설정
   2.1 VS Code 설치
   2.2 GitHub Copilot 확장 설치
   2.3 로그인 및 인증
   
3. 핵심 기능
   3.1 채팅 모드 (Ctrl+Alt+I)
   3.2 자동완성 (Ghost Text)
   3.3 Copilot Edits (다중 파일 수정)
   
4. 고급 기능
   4.1 @workspace 에이전트
   4.2 .github/copilot-instructions.md
   4.3 Mermaid 다이어그램
   
5. 실전 활용
   5.1 문서 작성 워크플로우
   5.2 데이터 분석 예시
```

---

## Phase 3: 03-4_행정직원용_가이드.tex 작성

### 소스 자료
- `docs/admin/ko/index.md` (1,467줄) 전체 활용

### 권장 구조
```
1. 개요 및 보안
   1.1 GitHub Copilot 소개
   1.2 보안 FAQ (정보 유출 걱정 해소)
   1.3 생성형 AI 활용 3대 원칙
   
2. 설치 및 기초
   2.1 VS Code 설치
   2.2 채팅 vs 자동완성
   
3. 프롬프트 작성법
   3.1 R.C.O 공식 (역할, 맥락, 출력)
   3.2 톤앤매너 조절
   
4. 핵심 기능
   4.1 Copilot Edits (다중 파일 수정)
   4.2 @workspace 에이전트
   4.3 Mermaid 다이어그램
   
5. 실전 워크북
   5.1 영문 이메일 3분 작성
   5.2 연례 보고서 데이터 정리
   5.3 작년 보고서 리모델링
   5.4 회의록 자동화
   
6. 부록
   6.1 실전 시나리오 라이브러리
   6.2 프롬프트 사전
   6.3 좋은 프롬프트 vs 나쁜 프롬프트
```

---

## Phase 4: 03-1_교수용_가이드.tex 작성

### 소스 자료
- `docs/professor/ko/index.md` (1,412줄) 전체 활용

### 권장 구조
```
1. 개요 및 연구윤리
   1.1 보안 (기업용 vs 무료 버전)
   1.2 AI 생성 콘텐츠와 학술적 정직성
   1.3 학생 데이터 프라이버시 (FERPA, 개인정보보호법)
   
2. 기본 사용법
   2.1 설치 및 설정
   2.2 채팅 vs 자동완성
   
3. 학문 분야별 활용
   3.1 인문학: 문학 분석 루브릭
   3.2 사회과학: 질적 연구 데이터 코딩
   3.3 자연과학: 실험 보고서 구조화
   3.4 공학: 설계 문서 검토
   3.5 예술: 작품 평가 기준
   
4. 교육학 프레임워크 적용
   4.1 Bloom's Taxonomy 기반 학습목표
   4.2 Backward Design 강의 설계
   4.3 Constructive Alignment 체크리스트
   4.4 학술 인용 자동화 (APA/MLA)
   
5. LMS 연계
   5.1 Canvas SpeedGrader 워크플로우
   5.2 Blackboard 루브릭 변환
   5.3 Moodle XML 퀴즈 생성
   
6. 부록
   6.1 학문 분야별 Instructions 템플릿
   6.2 교육용 프롬프트 사전
```

### 고유 고려사항
| 항목 | 고려사항 |
|------|---------|
| **연구윤리** | AI 생성 콘텐츠 표절 문제, 학생 AI 사용 감지 FAQ |
| **학생 개인정보** | FERPA, 개인정보보호법 준수 필수 |
| **학문 분야 특화** | 5개 분야별 맞춤 예시 (인문/사회/자연/공학/예술) |
| **LMS 연계** | Canvas, Blackboard, Moodle 워크플로우 |

---

## Phase 5: 03-2_학생용_가이드.tex 신규 작성

### 소스 자료
- 교수용 가이드의 "윤리" 섹션 역참조
- `docs/common/ko/copilot_web.md` 신청 절차 재활용
- 웹 검색으로 최신 Best Practice 보강

### 권장 구조
```
1. 시작하기
   1.1 GitHub Education 무료 신청
   1.2 VS Code 설치 및 로그인
   
2. 학업 활용
   2.1 과제 아이디어 브레인스토밍
   2.2 글쓰기 도우미 (문법, 표현 개선)
   2.3 코딩 과제 지원
   
3. 윤리적 사용
   3.1 절대 금지사항 (표절, 대리 제출)
   3.2 허용되는 활용 (초안 보조, 교정)
   3.3 인용 표기 방법
   
4. 실전 예시
   4.1 레포트 초안 작성
   4.2 발표 자료 구조화
   4.3 시험 준비 (개념 설명 요청)
   
5. 팁 & 트릭
   5.1 효과적인 프롬프트 작성 (R.C.O)
   5.2 AI 답변 검증하기
```

### 고유 고려사항
| 항목 | 고려사항 |
|------|---------|
| **윤리적 사용** | 표절 금지, 허용 범위 명확화 |
| **인용 표기** | AI 보조 도구 사용 시 명시 방법 |
| **무료 접근** | GitHub Education 신청 절차 강조 |
| **실용 예시** | 과제, 발표, 시험 준비 중심 |

---

## Phase 6: 03-3_연구원용_가이드.tex 신규 작성

### 소스 자료
- 교수용 가이드의 자연과학/공학 섹션 참조
- `archive/ko/level-2~3/` 데이터 분석 콘텐츠
- 웹 검색으로 최신 Best Practice 보강

### 권장 구조
```
1. 연구 환경 설정
   1.1 GitHub Education 자격 요건 (학생/교수 신분 필요)
   1.2 VS Code + Copilot 설치
   
2. 연구 단계별 활용
   2.1 문헌 검토 보조 (요약, 비교)
   2.2 연구 계획서 구조화
   2.3 실험 프로토콜 정리
   
3. 데이터 분석
   3.1 코드 생성 (Python, R)
   3.2 통계 분석 지원
   3.3 결과 시각화 (Mermaid, matplotlib)
   
4. 논문 작성
   4.1 초록/서론 초안
   4.2 IMRaD 구조 점검
   4.3 참고문헌 형식화 (APA, MLA)
   
5. 연구윤리
   5.1 데이터 보안 주의사항
   5.2 AI 사용 공개 가이드라인
```

### 고유 고려사항
| 항목 | 고려사항 |
|------|---------|
| **자격 요건** | 학생/교수 신분 필요 (순수 연구원은 무료 불가) |
| **논문 작성** | IMRaD 구조, 참고문헌 자동화 |
| **데이터 분석** | 코드 생성, 통계 분석 지원 |
| **연구윤리** | 데이터 보안, AI 사용 공개 |

---

## 작업 우선순위

| 순위 | 문서 | 이유 |
|------|------|------|
| 1 | `02_VSCode_가이드.tex` | 콘텐츠 풍부, 공통 활용 |
| 2 | `03-4_행정직원용_가이드.tex` | 콘텐츠 완전, 1,467줄 |
| 3 | `03-1_교수용_가이드.tex` | 콘텐츠 완전, 1,412줄 |
| 4 | `03-2_학생용_가이드.tex` | 신규 작성 필요 |
| 5 | `03-3_연구원용_가이드.tex` | 신규 작성 필요 |

---

## LaTeX 작업 시 주의사항

1. **프리앰블 재사용**: `01_*.tex`의 프리앰블 블록 그대로 복사 또는 `\input{_preamble}` 사용
2. **표 스타일 통일**: `tabularx` + `booktabs` 조합 유지
3. **한글 폰트**: `Noto Serif CJK KR` / `Noto Sans CJK KR` 유지
4. **색상 코드**: `eduNavy` (RGB 0, 43, 91) 일관 적용
5. **버전 관리**: `\docversion` 매크로 활용
6. **긴 표 처리**: `xltabular` 사용하여 페이지 넘김 지원

---

## Further Considerations (결정 필요)

1. **콘텐츠 부족 문서 처리**: 학생용(03-2), 연구원용(03-3)은 기존 콘텐츠 재조합으로 진행 vs 웹 검색으로 최신 Best Practice 보강?
2. **이미지 처리 방식**: `docs/images/copilot_web/` 폴더가 비어있는데, 스크린샷을 새로 추가할지 vs 텍스트 설명만으로 진행할지 결정 필요
3. **프리앰블 분리 여부**: `_preamble.tex`로 분리할지 vs 각 문서에 전체 프리앰블 복사할지 (Overleaf 호환성 고려)
