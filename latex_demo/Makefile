# =============================================================================
# LaTeX Demo Makefile
# macOS + TeX Live 2025 환경용
# =============================================================================

# 변수 설정
LATEX = xelatex
LUALATEX = lualatex
PDFLATEX = pdflatex
MAIN = full_demo
OUTDIR = output
FLAGS = -interaction=nonstopmode -file-line-error -synctex=1

# 색상 출력 (터미널용)
GREEN = \033[0;32m
YELLOW = \033[0;33m
RED = \033[0;31m
NC = \033[0m # No Color

# 기본 타겟
.PHONY: all clean xelatex lualatex watch help info fonts check

# 기본 빌드 (XeLaTeX 사용)
all: xelatex
	@echo "$(GREEN)✓ 빌드 완료!$(NC)"

# XeLaTeX으로 빌드 (한글 폰트 지원 - 권장)
xelatex: $(MAIN).tex
	@echo "$(YELLOW)▶ XeLaTeX으로 컴파일 중...$(NC)"
	$(LATEX) $(FLAGS) $(MAIN).tex
	$(LATEX) $(FLAGS) $(MAIN).tex
	@echo "$(GREEN)✓ $(MAIN).pdf 생성 완료 (XeLaTeX)$(NC)"

# LuaLaTeX으로 빌드 (대안)
lualatex: $(MAIN).tex
	@echo "$(YELLOW)▶ LuaLaTeX으로 컴파일 중...$(NC)"
	$(LUALATEX) $(FLAGS) $(MAIN).tex
	$(LUALATEX) $(FLAGS) $(MAIN).tex
	@echo "$(GREEN)✓ $(MAIN).pdf 생성 완료 (LuaLaTeX)$(NC)"

# 빠른 빌드 (1회만 컴파일 - 목차/참조 없이)
quick: $(MAIN).tex
	@echo "$(YELLOW)▶ 빠른 빌드 중...$(NC)"
	$(LATEX) $(FLAGS) $(MAIN).tex
	@echo "$(GREEN)✓ 빠른 빌드 완료$(NC)"

# 변경 감지 및 자동 빌드 (fswatch 필요: brew install fswatch)
watch:
	@echo "$(YELLOW)▶ 파일 변경 감지 모드 (Ctrl+C로 종료)$(NC)"
	@fswatch -o $(MAIN).tex | xargs -n1 -I{} make quick

# 임시 파일 정리
clean:
	@echo "$(YELLOW)▶ 임시 파일 정리 중...$(NC)"
	rm -f *.aux *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk
	rm -f *.synctex.gz *.nav *.snm *.vrb *.bbl *.blg *.bcf *.run.xml
	rm -f *.idx *.ilg *.ind *.glg *.glo *.gls *.ist
	rm -rf _minted-*
	@echo "$(GREEN)✓ 정리 완료$(NC)"

# PDF 포함 전체 정리
distclean: clean
	@echo "$(YELLOW)▶ PDF 포함 전체 정리 중...$(NC)"
	rm -f *.pdf
	@echo "$(GREEN)✓ 전체 정리 완료$(NC)"

# PDF 열기 (macOS)
view: $(MAIN).pdf
	@echo "$(YELLOW)▶ PDF 열기...$(NC)"
	open $(MAIN).pdf

# 빌드 후 바로 열기
run: xelatex view

# 시스템 폰트 목록 확인
fonts:
	@echo "$(YELLOW)▶ 시스템 한글 폰트 목록:$(NC)"
	@fc-list :lang=ko family 2>/dev/null | sort -u | head -20
	@echo ""
	@echo "$(YELLOW)▶ 시스템 영문 폰트 목록 (일부):$(NC)"
	@fc-list :lang=en family 2>/dev/null | grep -E "^(Arial|Times|Helvetica|Georgia|Verdana|Courier|Menlo|Monaco)" | sort -u | head -20

# LaTeX 패키지 설치 확인
check:
	@echo "$(YELLOW)▶ 필수 패키지 설치 확인:$(NC)"
	@echo -n "fontspec: " && (kpsewhich fontspec.sty > /dev/null && echo "$(GREEN)✓$(NC)" || echo "$(RED)✗$(NC)")
	@echo -n "tikz: " && (kpsewhich tikz.sty > /dev/null && echo "$(GREEN)✓$(NC)" || echo "$(RED)✗$(NC)")
	@echo -n "pgfplots: " && (kpsewhich pgfplots.sty > /dev/null && echo "$(GREEN)✓$(NC)" || echo "$(RED)✗$(NC)")
	@echo -n "tcolorbox: " && (kpsewhich tcolorbox.sty > /dev/null && echo "$(GREEN)✓$(NC)" || echo "$(RED)✗$(NC)")
	@echo -n "listings: " && (kpsewhich listings.sty > /dev/null && echo "$(GREEN)✓$(NC)" || echo "$(RED)✗$(NC)")
	@echo -n "fontawesome5: " && (kpsewhich fontawesome5.sty > /dev/null && echo "$(GREEN)✓$(NC)" || echo "$(RED)✗$(NC)")
	@echo -n "chemfig: " && (kpsewhich chemfig.sty > /dev/null && echo "$(GREEN)✓$(NC)" || echo "$(RED)✗$(NC)")
	@echo -n "circuitikz: " && (kpsewhich circuitikz.sty > /dev/null && echo "$(GREEN)✓$(NC)" || echo "$(RED)✗$(NC)")
	@echo -n "forest: " && (kpsewhich forest.sty > /dev/null && echo "$(GREEN)✓$(NC)" || echo "$(RED)✗$(NC)")
	@echo -n "qrcode: " && (kpsewhich qrcode.sty > /dev/null && echo "$(GREEN)✓$(NC)" || echo "$(RED)✗$(NC)")
	@echo -n "babel: " && (kpsewhich babel.sty > /dev/null && echo "$(GREEN)✓$(NC)" || echo "$(RED)✗$(NC)")

# TeX Live 버전 확인
info:
	@echo "$(YELLOW)▶ TeX Live 정보:$(NC)"
	@xelatex --version | head -3
	@echo ""
	@lualatex --version | head -3

# 도움말
help:
	@echo "$(GREEN)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━$(NC)"
	@echo "$(GREEN)  LaTeX Demo Makefile - 사용 가능한 명령어$(NC)"
	@echo "$(GREEN)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━$(NC)"
	@echo ""
	@echo "  $(YELLOW)make$(NC) 또는 $(YELLOW)make all$(NC)    기본 빌드 (XeLaTeX)"
	@echo "  $(YELLOW)make xelatex$(NC)           XeLaTeX으로 빌드 (한글 폰트 지원)"
	@echo "  $(YELLOW)make lualatex$(NC)          LuaLaTeX으로 빌드"
	@echo "  $(YELLOW)make quick$(NC)             빠른 빌드 (1회 컴파일)"
	@echo "  $(YELLOW)make run$(NC)               빌드 후 PDF 열기"
	@echo "  $(YELLOW)make view$(NC)              PDF 열기"
	@echo "  $(YELLOW)make watch$(NC)             파일 변경 자동 감지 빌드"
	@echo "  $(YELLOW)make clean$(NC)             임시 파일 정리"
	@echo "  $(YELLOW)make distclean$(NC)         PDF 포함 전체 정리"
	@echo "  $(YELLOW)make fonts$(NC)             시스템 폰트 목록 확인"
	@echo "  $(YELLOW)make check$(NC)             필수 패키지 설치 확인"
	@echo "  $(YELLOW)make info$(NC)              TeX Live 버전 정보"
	@echo "  $(YELLOW)make help$(NC)              이 도움말 표시"
	@echo ""
	@echo "$(GREEN)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━$(NC)"
