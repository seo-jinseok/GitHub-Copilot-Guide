## Plan: Remove Redundant Navigation Links

The global header in `_layouts/default.html` already provides comprehensive navigation. I will remove the manual "Home | Web Guide | VS Code Guide" links from the individual subpages to clean up the interface and avoid duplication.

### Steps
1. Remove the navigation line `[🏠 홈]...` from [`docs/common/ko/copilot_web.md`](docs/common/ko/copilot_web.md).
2. Remove the navigation line from [`docs/admin/ko/index.md`](docs/admin/ko/index.md).
3. Remove the navigation line from [`docs/professor/ko/index.md`](docs/professor/ko/index.md).
4. Remove the navigation line from [`docs/researcher/ko/index.md`](docs/researcher/ko/index.md).
5. Remove the navigation line from [`docs/student/ko/index.md`](docs/student/ko/index.md).

### Further Considerations
1. **Prompt Files:** I noticed a reference to adding these links in `.github/prompts/plan-reorganizeDocumentation.prompt.md`. I will leave this file as is, assuming it's a historical record or template, unless you want it updated too.
2. **English Pages:** I only checked Korean pages based on your request. Should I also check and remove similar links from English pages (e.g., `docs/common/en/copilot_web.md`) if they exist?
