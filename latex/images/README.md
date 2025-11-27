# 스크린샷 이미지 폴더 구조

## 폴더 구조

```
images/
├── 01-web/              # 01_GitHub_Copilot_웹_가이드.tex
├── 02-vscode/           # 02_GitHub_Copilot_VSCode_가이드.tex
├── 03-professor/        # 03-1_GitHub_Copilot_교수용_가이드.tex
├── 03-student/          # 03-2_GitHub_Copilot_학생용_가이드.tex
├── 03-researcher/       # 03-3_GitHub_Copilot_연구원용_가이드.tex
├── 03-admin/            # 03-4_GitHub_Copilot_행정직원용_가이드.tex
├── 04-instructions/     # 04_GitHub_Copilot_지침파일_가이드.tex
└── common/              # 여러 문서에서 공유하는 이미지
```

## 파일 네이밍 규칙

```
##-description.png
```

- `##`: 두 자리 순서 번호 (01, 02, 03...)
- `description`: 영문 소문자, 하이픈으로 구분
- 확장자: `.png` 또는 `.jpg`

## 01-web/ 폴더 필요 이미지 목록

| 파일명 | 설명 | 문서 내 위치 |
|--------|------|--------------|
| `01-github-signup.png` | GitHub 회원가입 화면 | 등록 절차 1단계 |
| `02-profile-settings.png` | 프로필 설정 화면 (Settings → Public profile) | 등록 절차 2단계 |
| `03-billing-info.png` | 결제 정보 입력 화면 | 등록 절차 3단계 |
| `04-2fa-setup.png` | 2단계 인증 설정 화면 (QR 코드) | 등록 절차 4단계 |
| `05-recovery-codes.png` | 복구 코드 다운로드 화면 | 등록 절차 4단계 |
| `06-education-apply.png` | GitHub Education 신청 페이지 | 등록 절차 5단계 |
| `07-school-select.png` | 학교 검색/선택 화면 | 등록 절차 6단계 |
| `08-document-upload.png` | 증명서 업로드 화면 | 등록 절차 7단계 |

## 이미지 권장 사양

- **해상도**: 1280×720 ~ 1920×1080 (화면 캡처 기준)
- **형식**: PNG (투명도 필요 시) 또는 JPG
- **파일 크기**: 500KB 이하 권장
- **내용**: 개인정보 마스킹 필수 (이메일, 이름 등)

## LaTeX 사용법

```latex
% 이미지가 있으면 표시, 없으면 플레이스홀더 표시
\inlineImage{01-github-signup.png}

% 너비 조절
\inlineImage[width=0.5\textwidth]{02-profile-settings.png}
```

## 주의사항

1. 파일명에 한글이나 공백 사용 금지
2. 이미지가 없어도 LaTeX 컴파일 오류 발생하지 않음 (플레이스홀더 표시)
3. 민감한 정보는 반드시 마스킹 처리 후 업로드
