# =============================================================================
# GitHub Copilot 가이드 LaTeX 빌드 Makefile
# =============================================================================
#
# 사용 가능한 명령어:
#   make list          - 빌드 가능한 문서 목록
#   make all           - 모든 문서 빌드
#   make web           - 웹 가이드만 빌드
#   make vscode        - VSCode 가이드만 빌드
#   make professor     - 교수용 가이드만 빌드
#   make student       - 학생용 가이드만 빌드
#   make researcher    - 연구원용 가이드만 빌드
#   make admin         - 행정직원용 가이드만 빌드
#   make instructions  - 지침파일 가이드만 빌드
#   make clean         - 임시 파일 정리 (PDF 유지)
#   make cleanall      - PDF 포함 모든 파일 삭제
#
# =============================================================================

# 컴파일러 설정
LATEX = xelatex
LATEXFLAGS = -interaction=nonstopmode -file-line-error -synctex=1

# 소스 파일 (한글 파일명 지원)
SOURCES = $(wildcard *.tex)
MAIN_DOCS = $(filter-out _preamble.tex,$(SOURCES))
PDFS = $(MAIN_DOCS:.tex=.pdf)

# 색상 출력
GREEN = \033[0;32m
YELLOW = \033[0;33m
RED = \033[0;31m
NC = \033[0m # No Color

# =============================================================================
# 기본 타겟
# =============================================================================

.PHONY: all clean cleanall help list watch

# 기본: 모든 문서 빌드
all: web vscode professor student researcher admin instructions
	@echo "$(GREEN)✓ 모든 문서 빌드 완료$(NC)"

# =============================================================================
# 빌드 함수 정의
# =============================================================================

define build_pdf
	@echo "$(YELLOW)▶ 빌드 중: $(1)$(NC)"
	@$(LATEX) $(LATEXFLAGS) $(1) > /dev/null 2>&1 || $(LATEX) $(LATEXFLAGS) $(1)
	@$(LATEX) $(LATEXFLAGS) $(1) > /dev/null 2>&1
	@echo "$(GREEN)✓ 완료: $(1:.tex=.pdf)$(NC)"
endef

# =============================================================================
# 개별 문서 타겟
# =============================================================================

.PHONY: web vscode professor student researcher admin instructions

web: _preamble.tex
	$(call build_pdf,01_GitHub_Copilot_웹_가이드.tex)

vscode: _preamble.tex
	$(call build_pdf,02_GitHub_Copilot_VSCode_가이드.tex)

professor: _preamble.tex
	$(call build_pdf,03-1_GitHub_Copilot_교수용_가이드.tex)

student: _preamble.tex
	$(call build_pdf,03-2_GitHub_Copilot_학생용_가이드.tex)

researcher: _preamble.tex
	$(call build_pdf,03-3_GitHub_Copilot_연구원용_가이드.tex)

admin: _preamble.tex
	$(call build_pdf,03-4_GitHub_Copilot_행정직원용_가이드.tex)

instructions: _preamble.tex
	$(call build_pdf,04_GitHub_Copilot_지침파일_가이드.tex)

# =============================================================================
# 정리 명령
# =============================================================================

# 임시 파일만 삭제 (PDF 유지)
clean:
	@echo "$(YELLOW)▶ 임시 파일 정리 중...$(NC)"
	@rm -f *.aux *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk
	@rm -f *.bbl *.blg *.bcf *.run.xml
	@rm -f *.nav *.snm *.vrb
	@rm -f *.synctex.gz
	@rm -f *.idx *.ind *.ilg
	@echo "$(GREEN)✓ 임시 파일 정리 완료$(NC)"

# PDF 포함 모든 생성 파일 삭제
cleanall: clean
	@echo "$(YELLOW)▶ PDF 파일 삭제 중...$(NC)"
	@rm -f *.pdf
	@echo "$(GREEN)✓ 모든 생성 파일 삭제 완료$(NC)"

# =============================================================================
# 유틸리티
# =============================================================================

# 문서 목록 표시
list:
	@echo "$(GREEN)=== 빌드 가능한 문서 ===$(NC)"
	@echo ""
	@echo "  make web         - 01_GitHub_Copilot_웹_가이드"
	@echo "  make vscode      - 02_GitHub_Copilot_VSCode_가이드"
	@echo "  make professor   - 03-1_GitHub_Copilot_교수용_가이드"
	@echo "  make student     - 03-2_GitHub_Copilot_학생용_가이드"
	@echo "  make researcher  - 03-3_GitHub_Copilot_연구원용_가이드"
	@echo "  make admin       - 03-4_GitHub_Copilot_행정직원용_가이드"
	@echo "  make instructions- 04_GitHub_Copilot_지침파일_가이드"
	@echo ""
	@echo "  make all         - 모든 문서 빌드"
	@echo "  make clean       - 임시 파일 정리"
	@echo "  make cleanall    - PDF 포함 모든 파일 정리"
	@echo ""

# 도움말
help: list

# 파일 변경 감시 (fswatch 필요: brew install fswatch)
watch:
	@echo "$(YELLOW)▶ 파일 변경 감시 시작 (Ctrl+C로 종료)$(NC)"
	@fswatch -o *.tex | xargs -n1 -I{} make all

# =============================================================================
# 특수 타겟
# =============================================================================

# 빠른 빌드 (1회만 컴파일, 목차/참조 미갱신)
quick: LATEXFLAGS += -draftmode
quick:
	@for doc in $(MAIN_DOCS); do \
		echo "$(YELLOW)▶ 빠른 빌드: $$doc$(NC)"; \
		$(LATEX) $(LATEXFLAGS) $$doc > /dev/null 2>&1; \
	done
	@echo "$(GREEN)✓ 빠른 빌드 완료 (목차/참조 미갱신)$(NC)"

# 상세 출력 모드
verbose: LATEXFLAGS = -interaction=nonstopmode -file-line-error
verbose: all
