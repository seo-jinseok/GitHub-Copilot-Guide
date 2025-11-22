# Task Master AI - University Copilot Guide Project

## Project Overview

**Project Type**: Documentation-only (no code compilation, testing, or builds)  
**Primary Goal**: Consolidate multilingual GitHub Copilot learning materials for non-technical university admin staff  
**Languages**: Korean (primary), English (secondary)  
**Target Audience**: University administrative staff with minimal technical background

## Quick Start for New Sessions

```bash
# Resume work
task-master next                    # Get next available task
task-master show <id>               # View task details

# Update progress during work
task-master update-subtask --id=<id> --prompt="consolidation progress notes"

# Complete work
task-master set-status --id=<id> --status=done
```

## Project-Specific Guidelines

### Content Priority for Consolidation

When merging content from multiple sources, follow this priority order:

1. **`docs/ko/` and `docs/en/`** - Primary structured content (Levels 1-3, appendices)
2. **`staging/refined_content.md`** - Refined/reviewed content waiting for integration
3. **`legacy/`** - Historical content for reference only (mark as deprecated)
4. **Root files** (`University_Copilot_Guide_*.md`) - Original drafts (verify before using)

### Style & Tone Requirements

**Korean Content (ALL Korean text must follow these rules)**:
- Use polite honorifics: "하십시오" or "해요" style (from `.github/copilot-instructions.md`)
- Encouraging tone: Act as helpful partner, not just tool
- Date format: `YYYY. MM. DD.` (e.g., 2025. 11. 21.)
- Avoid technical jargon (target audience: non-technical admin staff)
- Use correct university terminology: '수강신청' not '수업신청', '단과대학' not '학부'

**English Content**:
- Professional but approachable tone
- Clear, simple language (avoid complex technical terms)
- Parallel structure to Korean content where possible

**Markdown Standards** (from `STYLE_GUIDE.md`):
- One H1 (`#`) per file only
- Logical header hierarchy: don't skip levels (e.g., `##` → `####`)
- Code blocks MUST include language identifiers: ` ```bash `, not ` ``` `
- Lists: Use `-` or `*` with 4-space indentation
- Emoji usage:
  - 💡 Tips/ideas
  - ⚠️ Warnings/caution
  - ✅ Success/completion
  - ❌ Failures/errors
  - 📝 Notes/additional info

**Learning Progress Checkboxes**:
- Use `- [ ]` format in TOCs for learner tracking
- Example: `- [ ] [1. Setup](./level-1-basics/01-setup.md)`

### Commit Message Convention

Follow Angular-style commits (from `CONTRIBUTING.md`):

```
type: subject

(optional body)

(optional footer)
```

**Types**:
- `docs`: Documentation changes (MOST COMMON for this project)
- `feat`: New features (rare - only for new doc structure/systems)
- `fix`: Bug fixes (typos, broken links)
- `refactor`: Restructuring without content change
- `style`: Formatting only

**Examples**:
```bash
docs: consolidate Level 1 Korean content into single file
docs: add 12 Mermaid diagrams for workflow visualization
fix: correct broken links in English appendix
```

### Visual Requirements

Add 10-15 visualizations using:
- **Mermaid diagrams** (preferred - renders in GitHub)
- **SVG graphics** (for complex diagrams)

**Common diagram types needed**:
- Learning path flowcharts
- GitHub Copilot workflow sequences
- Feature comparison tables (as diagrams)
- Exercise progression maps

## Task Master Commands Reference

### Documentation Workflow Commands

```bash
# Project Setup (if starting fresh)
task-master init
task-master parse-prd .taskmaster/docs/prd.txt --force    # Replace all tasks
# OR
task-master parse-prd .taskmaster/docs/prd.txt --append   # Keep history, add new

# Analysis & Planning
task-master analyze-complexity --research       # AI-powered complexity analysis
task-master complexity-report                   # View analysis results
task-master expand --id=<id> --research        # Break task into subtasks
task-master expand --all --research            # Expand all eligible tasks

# Daily Documentation Workflow
task-master list                               # View all tasks
task-master next                               # Get next available task
task-master show <id>                         # View detailed task info

# During Work (LOG YOUR PROGRESS!)
task-master update-subtask --id=<id> --prompt="merged Level 1-3 Korean docs, added 3 Mermaid diagrams for setup workflow"

# Mark Complete
task-master set-status --id=<id> --status=done

# Task Management
task-master add-task --prompt="add accessibility guidelines for diagrams" --research
task-master update-task --id=<id> --prompt="changes based on review feedback"
task-master update --from=<id> --prompt="update all remaining tasks with new diagram requirements"

# Dependencies & Organization
task-master add-dependency --id=5 --depends-on=3    # Task 5 depends on Task 3 completion
task-master validate-dependencies                   # Check for circular/broken deps
```

### AI-Powered Operations (takes ~30-60 seconds)

These commands make API calls to AI models:
- `parse-prd` - Generate tasks from PRD
- `analyze-complexity` - Analyze task complexity scores
- `expand` / `expand --all` - Break tasks into subtasks
- `add-task` - Create new task with AI
- `update` / `update-task` / `update-subtask` - Modify tasks with AI

## Project Structure

```
Github_Copilot_Guide/
├── .taskmaster/
│   ├── tasks/
│   │   ├── tasks.json              # Main task database (auto-managed)
│   │   └── task-*.md              # Individual task files (auto-generated)
│   ├── docs/
│   │   └── prd.txt                # Product Requirements Document
│   ├── reports/
│   │   └── task-complexity-report.json
│   └── config.json                # AI model configuration
│
├── docs/
│   ├── ko/                        # Korean content (PRIMARY SOURCE)
│   │   ├── level-1-basics/
│   │   ├── level-2-practical/
│   │   ├── level-3-expert/
│   │   └── appendix/
│   └── en/                        # English content (SECONDARY SOURCE)
│       └── (same structure)
│
├── staging/
│   └── refined_content.md         # Reviewed content awaiting integration
│
├── legacy/
│   └── (historical files)         # Reference only - mark as deprecated
│
├── templates/exercises/           # Template files for learners
│
├── dist/ (TO BE CREATED)
│   ├── University_Copilot_Guide_Complete_KO.md   # FINAL OUTPUT
│   └── University_Copilot_Guide_Complete_EN.md   # FINAL OUTPUT
│
├── .github/
│   ├── copilot-instructions.md   # Korean tone guidelines
│   └── workflows/validate.yml     # CI/CD validation
│
├── AGENTS.md                      # This file
├── STYLE_GUIDE.md                # Markdown standards
└── CONTRIBUTING.md               # Commit conventions & workflow
```

## Documentation Consolidation Workflow

### Phase 1: Content Audit & Preparation

1. Review all source content locations
2. Identify duplicates and conflicts
3. Create backup of all source files
4. Log content mapping in subtasks

### Phase 2: Korean Content Consolidation

```bash
task-master show <korean-task-id>

# During work, log progress
task-master update-subtask --id=<id> --prompt="
Merged sections:
- Level 1 basics (3 files) → single H2 section
- Level 2 practical (3 files) → single H2 section
- Added 4 Mermaid diagrams for workflows
- Verified all emoji usage matches STYLE_GUIDE.md
- Used polite 하십시오 form throughout
"

# Create output file
# [Work on consolidation]
# Output: dist/University_Copilot_Guide_Complete_KO.md

task-master set-status --id=<id> --status=done
```

### Phase 3: English Content Consolidation

```bash
# Follow same pattern as Korean
# Ensure parallel structure to Korean version
# Output: dist/University_Copilot_Guide_Complete_EN.md
```

### Phase 4: Visual Enhancements

```bash
# Add 10-15 diagrams using Mermaid syntax
# Examples:
# - Learning path flowchart
# - Feature comparison tables
# - Workflow sequences
# - Exercise progression maps

task-master update-subtask --id=<diagram-task-id> --prompt="
Added 12 visualizations:
- 3 flowcharts (learning paths)
- 4 sequence diagrams (Copilot workflows)
- 3 class/component diagrams (feature comparisons)
- 2 state diagrams (exercise progressions)
All use Mermaid syntax for GitHub rendering
"
```

### Phase 5: Verification & Cleanup

```bash
# Verification checklist (log in subtask):
# - [ ] All source content included (docs/ → staging/ → legacy/)
# - [ ] No duplicate content
# - [ ] Korean uses correct honorifics (하십시오/해요)
# - [ ] English maintains parallel structure
# - [ ] 10-15 diagrams added and rendering
# - [ ] All links functional
# - [ ] Emoji usage follows STYLE_GUIDE.md
# - [ ] Checkboxes added to TOCs (- [ ])
# - [ ] Backup verified before cleanup

task-master update-subtask --id=<verify-id> --prompt="
Verification complete:
✅ Content audit: all sources merged
✅ Korean honorifics verified
✅ 14 Mermaid diagrams rendering
✅ Backup created: backup-YYYYMMDD/
⚠️ Found 3 broken links - fixed
"
```

## Best Practices for This Project

### Content Work Best Practices

1. **Always backup before consolidation**: Copy source directories to `backup-YYYYMMDD/`
2. **Log all merges in subtasks**: Document which files merged into which sections
3. **Verify tone for Korean content**: Use polite honorifics consistently
4. **Maintain parallel structure**: English structure should mirror Korean
5. **Test all links**: Use markdown link checkers before marking complete
6. **Verify diagram rendering**: Check Mermaid syntax renders correctly in GitHub preview

### Task Master Integration

1. **Log progress frequently**: Use `update-subtask` to document consolidation decisions
2. **Break large tasks**: Use `expand` to create manageable subtasks
3. **Use dependencies**: If English consolidation needs Korean complete first, add dependency
4. **Commit after each task**: Use proper commit format: `docs: consolidate Level 1 Korean content`

### Git Workflow for Documentation

```bash
# Start work on task
git checkout -b docs/task-<id>-description

# Make changes to consolidation
# [work on files]

# Commit with Task Master reference
git add dist/University_Copilot_Guide_Complete_KO.md
git commit -m "docs: consolidate Level 1-3 Korean content (task 2.1)

- Merged 9 files from docs/ko/ into single structure
- Added 4 Mermaid diagrams for workflows
- Verified polite honorifics throughout
- Added progress checkboxes to TOC"

# Push and create PR
git push origin docs/task-<id>-description
gh pr create --title "Complete task <id>: Korean content consolidation" \
  --body "Consolidates all Korean learning content into single file per PRD requirements. See task <id> for details."
```

## MCP Integration (Optional)

If using Claude Code with MCP, configure `.mcp.json`:

```json
{
  "mcpServers": {
    "task-master-ai": {
      "command": "npx",
      "args": ["-y", "task-master-ai"],
      "env": {
        "ANTHROPIC_API_KEY": "your_key_here",
        "PERPLEXITY_API_KEY": "your_key_here"
      }
    }
  }
}
```

**Useful MCP tools for documentation**:
- `get_tasks` - List all tasks
- `next_task` - Get next available task
- `update_subtask` - Log consolidation progress
- `set_task_status` - Mark tasks complete

## Troubleshooting Documentation Issues

### Content Conflicts

```bash
# If source files have conflicting content:
task-master update-subtask --id=<id> --prompt="
Found conflict between docs/ko/level-1/01-setup.md and staging/refined_content.md
Resolution: Used docs/ko/ version (priority 1) + added clarification from staging/
"
```

### Link Verification

```bash
# Use markdown link checker (if available)
npx markdown-link-check dist/*.md

# Or manually verify internal links
grep -r "](\./" dist/
```

### Diagram Rendering Issues

```bash
# Test Mermaid syntax online: https://mermaid.live/
# Common issues:
# - Missing quotes in labels
# - Incorrect arrow syntax
# - Unsupported node shapes
```

## Important Reminders

**DO**:
- Use `task-master update-subtask` frequently to log consolidation decisions
- Follow Korean honorifics rules for ALL Korean content
- Backup source files before consolidation
- Test Mermaid diagrams render correctly
- Commit after each completed subtask

**DON'T**:
- Manually edit `.taskmaster/tasks/tasks.json` (use commands)
- Skip content priority order (docs/ → staging/ → legacy/ → root)
- Forget to add language identifiers to code blocks
- Use generic commits like "docs: update files" (be specific!)
- Delete source files until consolidation verified

---

**Current Phase**: Ready to parse PRD and begin consolidation workflow  
**Target Output**: 2 single-file guides (`dist/*.md`) with 10-15 visualizations  
**Estimated Timeline**: Based on task complexity analysis after PRD parsing
