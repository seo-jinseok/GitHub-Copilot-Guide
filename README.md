# 대학 행정직원을 위한 GitHub Copilot 완전 정복

이 프로젝트는 대학 행정 환경에 특화된 GitHub Copilot 활용법을 다루는 종합 가이드입니다. 단순한 기능 소개를 넘어, 실제 행정 업무(기획, 성과관리, 보고서 작성 등)에 Copilot을 통합하여 업무 효율을 극대화하는 실용적인 방법을 제시합니다.

## 📚 완성된 가이드 (최종 버전)

이 프로젝트의 모든 학습 콘텐츠는 단일 파일로 통합되어 제공됩니다:

- **[🇰🇷 한국어 완전판](./dist/University_Copilot_Guide_Complete_KO.md)** (51KB)
  - Level 1~3 학습 과정 + 실습 워크북 + 부록
  - 13개의 Mermaid 다이어그램 포함
  - 대학 행정직원을 위한 맞춤형 한국어 가이드

- **[🇬🇧 English Complete Guide](./dist/University_Copilot_Guide_Complete_EN.md)** (47KB)
  - Level 1~3 learning paths + workbooks + appendices
  - 13 Mermaid diagrams included
  - Full English translation with parallel structure

## 🗂️ 프로젝트 구조

```
Github_Copilot_Guide/
├── dist/                    # 📦 최종 배포 파일
│   ├── University_Copilot_Guide_Complete_KO.md  # 한국어 통합본
│   ├── University_Copilot_Guide_Complete_EN.md  # English integrated guide
│   └── images/              # 이미지 디렉토리 (향후 사용 예정)
│
├── archive/                 # 📁 원본 소스 백업
│   ├── ko/                  # 한국어 원본 (14 files)
│   ├── en/                  # English sources (13 files)
│   ├── exercises/           # 실습 템플릿 (7 files)
│   └── legacy/              # 이전 버전 문서
│
├── .taskmaster/             # 🤖 Task Master AI 프로젝트 관리
├── .github/                 # CI/CD 및 프로젝트 지침
│
└── (문서 및 설정 파일)
    ├── README.md            # 이 파일
    ├── CONTRIBUTING.md      # 기여 가이드
    ├── STYLE_GUIDE.md       # 마크다운 스타일 규칙
    ├── AGENTS.md            # Task Master 프로젝트 지침
    └── GEMINI.md            # AI 모델 설정 정보
```

## 🤝 기여하기

이 프로젝트는 여러분의 기여를 환영합니다. 버그 수정, 오탈자 교정, 내용 추가, 번역 등 어떤 형태의 기여도 가능합니다.

**기여 전 확인사항:**
- 최종 가이드 파일(`dist/*.md`)에 대한 수정은 원본 소스(`archive/`)를 기반으로 재생성이 필요합니다
- 원본 소스 파일은 `archive/` 디렉토리에서 확인할 수 있습니다

자세한 내용은 아래 문서를 참고해주세요:

- **[기여 가이드](./CONTRIBUTING.md):** Issue, PR, 커밋 메시지 등 기여에 필요한 모든 규칙
- **[스타일 가이드](./STYLE_GUIDE.md):** 문서 작성의 일관성을 유지하기 위한 스타일 규칙
- **[프로젝트 지침](./AGENTS.md):** Task Master AI를 활용한 프로젝트 관리 방법

## 📋 원본 소스 구조

통합 가이드 생성에 사용된 원본 파일들은 `archive/` 디렉토리에 보관되어 있습니다:

```
archive/
├── ko/                      # 한국어 원본 소스
│   ├── level-1-basics/      # 기초 (3 files)
│   ├── level-2-practical/   # 실전 (3 files)
│   ├── level-3-expert/      # 고급 (3 files)
│   ├── appendix/            # 부록 (2 files)
│   └── README.md            # 학습 가이드
│
├── en/                      # English source files
│   └── (동일한 구조)
│
└── exercises/               # 실습 템플릿 파일
    ├── level-1/             # Level 1 실습
    ├── level-2/             # Level 2 실습
    └── level-3/             # Level 3 실습
```
