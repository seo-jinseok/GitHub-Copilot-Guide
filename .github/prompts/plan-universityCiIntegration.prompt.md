## Plan: University CI Integration & Language Setup

This plan integrates the university's CI assets into the documentation site, ensures the landing page defaults to Korean, and enables functional language switching.

### Steps
1.  **Migrate Assets**: Copy `CI/deu.svg` and `CI/symbol_color_300dpi.png` to `docs/images/ci/` for web accessibility.
2.  **Update Layout Header**: Modify `docs/_layouts/default.html` to replace the generic "T" shield with the `deu.svg` logo.
3.  **Fix Landing Page Image**: Update `docs/index.md` to reference the new local path `docs/images/ci/deu.svg` instead of the external `../CI/` path.
4.  **Enable Language Switcher**: Create a basic `docs/en/index.md` (English landing page) and update the toggle logic in `docs/_layouts/default.html` to ensure switching works from the home page.

### Further Considerations
1.  **English Content**: I will create a placeholder English landing page to make the button functional. Do you have specific English text for the landing page, or should I translate the Korean version?
2.  **Logo Sizing**: I will set the logo height to ~40px in the header. Let me know if you prefer a different size.
