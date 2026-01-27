# AI Product Engineering Template

This repository provides a disciplined, model-aware workflow for building production software with AI assistance.

## Core Rules
- Files are the source of truth
- No task file → no AI work
- ARCHITECTURE.md is authoritative
- Minimal diff only
- Update WORKING_STATE.md after each session

## Getting Started

### Quick Start
1. Click "Use this template" to create a new repository
2. Read MASTER_REFERENCE.md once
3. Fill docs/PRODUCT_VISION.md
4. Fill docs/ARCHITECTURE.md
5. Create tasks in /tasks using TASK_TEMPLATE.md

### For Team Onboarding
See ONBOARDING.md for a 1-page guide.

## See It In Action

Check out `example/task-timer-cli/` for a complete, working demonstration:
- Filled documentation (PRODUCT_VISION, ARCHITECTURE, etc.)
- Architecture Decision Records (ADRs)
- Task file with model selection
- Working Python CLI code (125 lines)
- AI session metrics
- See `example/VALIDATION_SUMMARY.md` for full analysis

**Try it:**
```bash
cd example/task-timer-cli
python timer.py start "Testing the template"
python timer.py stop
```

## What's Included

### Core Template Files
- **MASTER_REFERENCE.md** - Complete bundled rules
- **SYSTEM_PROMPT.md** - Paste into your AI tool
- **ONBOARDING.md** - 1-page team guide

### Documentation Structure
- **docs/PRODUCT_VISION.md** - Product goals & scope
- **docs/ARCHITECTURE.md** - Authoritative design (never violate)
- **docs/EXECUTION_PLAN.md** - Milestones & timeline
- **docs/DEFINITION_OF_DONE.md** - Quality gates
- **docs/RELEASE_CHECKLIST.md** - Release process
- **docs/decisions/** - Architecture Decision Records (ADR)

### Task Management
- **tasks/TASK_TEMPLATE.md** - Model-aware task template
- **tasks/README.md** - Task discipline rules

### AI Metrics
- **.ai-metrics/** - Session tracking & cost logging

### GitHub Integration
- **.github/pull_request_template.md** - Standard PR format
- **.github/workflows/ai-guardrails.yml** - Task validation (warning-only)

## Validation Status

✅ **Production Ready** (98% confidence)

Validated with task-timer-cli test project:
- Zero ARCHITECTURE.md violations
- All template sections used successfully
- Minimal diff principle maintained
- Complete state tracking demonstrated

See `example/VALIDATION_SUMMARY.md` for detailed metrics.

## Use Cases

### Minimal Projects (<500 lines)
Use: ARCHITECTURE.md + 1-3 task files + WORKING_STATE.md

### Small Projects (500-5k lines) ⭐ Sweet Spot
Use: Full template as designed

### Medium Projects (5k-50k lines)
Use: Everything + more granular tasks + regular ADRs

### Large Projects (50k+ lines)
Use: Core principles + customized state tracking

## Why This Template?

- **File-based truth** - No session amnesia
- **AI-aware** - Tracks models, costs, outcomes
- **Architecture discipline** - ARCHITECTURE.md prevents drift
- **Minimal diff** - Prevents AI over-engineering
- **Team-ready** - 1-minute onboarding via ONBOARDING.md
- **Tool-agnostic** - Works with Claude, Cursor, Copilot, any AI

## Contributing

This template is designed to be stable. If you find issues or have suggestions:
1. Check example/ to see if it's already demonstrated
2. Open an issue with your use case
3. Share metrics from your project

## License

MIT License - use freely for any project.
