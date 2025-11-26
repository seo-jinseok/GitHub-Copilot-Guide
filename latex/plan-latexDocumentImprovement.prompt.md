# 피드백 분석 및 개선 방안

피드백을 분석한 결과, 주요 개선 영역은 다음과 같습니다.

---

## 1. 시각적 설명 보강 (피드백 1, 6)

**문제**: 등록절차가 텍스트만으로 설명되어 이해하기 어려움

**개선 방안**:
- LaTeX 문서 내에 스크린샷 이미지를 삽입할 수 있도록 `\includegraphics` 명령어 활용
- 또는 별도의 이미지 첨부 PDF 가이드를 제작하여 함께 배포
- 각 단계별 캡처 화면 예시:
  - GitHub 회원가입 화면
  - 프로필 설정 화면
  - 2FA 설정 QR 코드 화면
  - GitHub Education 신청 페이지
- latex 폴더 내에 figs 폴더 생성
- tex 코드 내에는 어떤 이미지를 넣어야 하는지 주석으로 명시(이미지 파일명도 제안), tex 커맨드 및 태그는 미리 작성

---

## 2. 2단계 인증(2FA) 설명 강화 (피드백 2)

**현재 문서**:
```latex
\item \textit{주의: 복구 코드는 반드시 별도 저장 (USB, 클라우드, 인쇄물)}
```

**개선안**:
```latex
\item \textbf{복구 코드 저장 (필수)}:
\begin{itemize}
    \item 6자리 인증 코드 입력 후 \textbf{복구 코드 다운로드} 화면이 표시됨
    \item 반드시 \textbf{Download} 버튼을 클릭하여 파일로 저장
    \item \textit{주의: 복구 코드를 분실하면 계정 접근이 불가능해질 수 있음}
    \item \textit{권장: 복구 코드 화면을 캡처하여 별도 보관}
\end{itemize}
```

---

## 3. 스캔 및 파일 업로드 안내 강화 (피드백 3, 4)

**현재 문서의 해당 부분을 다음과 같이 확장**:

```latex
\subsection{증명서 스캔 시 주의사항}
\begin{itemize}
    \item \textbf{파일 형식}: \textbf{JPG 형식 필수} (PDF 업로드 불가)
    \item \textbf{스캔 모드}: \textbf{컬러 모드}로 스캔 (흑백/그레이스케일 금지)
    \item \textbf{자동 보정 기능 비활성화}: 
    \begin{itemize}
        \item 스캐너 소프트웨어에서 "자동 문서 보정", "배경 제거", "화이트 밸런스" 등의 기능을 \textbf{끄기}
        \item 이 기능이 켜져 있으면 학교 로고(워터마크)가 흰색으로 처리되어 사라짐
        \item 로고가 없으면 위조 문서로 의심받아 \textbf{승인 거절} 가능
    \end{itemize}
    \item \textbf{해상도}: 150-300 DPI 권장
    \item \textbf{파일 크기}: 10MB 이하
\end{itemize}

\textbf{스캔이 어려운 경우}: 
스마트폰 카메라로 촬영 가능 (평평한 곳에 증명서를 놓고 그림자 없이 촬영)
```

---

## 4. 영문 사이트 탐색 가이드 추가 (피드백 5)

**새 섹션 추가 권장**:

```latex
\subsection{GitHub 영문 인터페이스 안내}
GitHub은 영문으로 제공됩니다. 주요 메뉴 번역을 참고하세요:

\begin{table}[H]
    \centering
    \begin{tabularx}{\textwidth}{@{}l l X@{}}
        \toprule
        \textbf{영문} & \textbf{한국어} & \textbf{위치/용도} \\
        \midrule
        Sign up & 회원가입 & 첫 화면 우측 상단 \\
        Sign in & 로그인 & 첫 화면 우측 상단 \\
        Settings & 설정 & 프로필 아이콘 클릭 후 메뉴 \\
        Profile & 프로필 & 개인정보 설정 \\
        Billing & 결제 & 결제 정보 설정 \\
        Password and authentication & 비밀번호 및 인증 & 2단계 인증 설정 \\
        Submit & 제출 & 신청서 제출 버튼 \\
        \bottomrule
    \end{tabularx}
\end{table}
```

---

## 5. 학교 검색 절차 상세화 (피드백 8)

**현재 6번 단계를 다음과 같이 확장**:

```latex
\item \textbf{학교 선택}:
\begin{itemize}
    \item 신분(Student/Teacher) 선택 후 학교 검색 화면이 표시됨
    \item \textbf{자동 검색되는 경우}: 목록에서 학교를 찾아 \textbf{Select this school} 클릭
    \item \textbf{검색되지 않는 경우}: 
    \begin{enumerate}
        \item 검색창에 \textbf{Dong-eui University} 직접 입력
        \item 여전히 없으면 \textbf{I don't see my school} 또는 수동 입력 옵션 선택
        \item "How would you describe your school?"에서 \textbf{Higher-education: university college} 선택
        \item City란에 \textbf{Busan} 입력
        \item Country란에 \textbf{Korea, South} 선택
        \item \textbf{Submit} 버튼 클릭
    \end{enumerate}
\end{itemize}
```

---

## 6. 지원 자격 상세화 (피드백 7)

**현재 표를 다음과 같이 확장**:

```latex
\begin{table}[H]
    \centering
    \renewcommand{\arraystretch}{1.1}
    \begin{tabularx}{\textwidth}{@{}l l X@{}}
        \toprule
        \textbf{구분} & \textbf{신청 가능 여부} & \textbf{필요 서류 및 비고} \\
        \midrule
        학부생 & \textbf{가능} & 영문 재학증명서 \\
        대학원생 (석사/박사) & \textbf{가능} & 영문 재학증명서 \\
        전임교원 & \textbf{가능} & 영문 재직증명서 \\
        비전임교원 (강사, 겸임) & 직접 확인 필요 & 승인 사례 불일치 \\
        연구원 & 직접 확인 필요 & 고용 형태에 따라 다름 \\
        행정 직원 & \textbf{불가} & 유료 라이선스 구매 필요 \\
        휴학생 & \textbf{불가} & 복학 후 재학증명서로 신청 \\
        졸업생 & \textbf{불가} & 재학 중에만 사용 가능 \\
        \bottomrule
    \end{tabularx}
\end{table}
```

---

## 요약: 우선순위별 개선 항목

| 우선순위 | 개선 항목 | 난이도 |
|---------|----------|--------|
| **높음** | 스캔 주의사항 (JPG 필수, 자동보정 끄기) 강조 | 쉬움 |
| **높음** | 학교 검색 절차 상세화 | 쉬움 |
| **높음** | 복구 코드 저장 절차 강화 | 쉬움 |
| **중간** | 영문 메뉴 번역표 추가 | 쉬움 |
| **중간** | 지원 자격 표 확장 | 쉬움 |
| **낮음** | 스크린샷 이미지 추가 | 시간 소요 |
