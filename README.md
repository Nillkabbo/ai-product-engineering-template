# AI Product Engineering Template

This repository provides a disciplined, model-aware, three-phase workflow for building production software with AI assistance.

## Core Rules
- Files are the source of truth
- Three-phase workflow: Design → Planning → Execution
- Human approval gates at each phase
- ARCHITECTURE.md is authoritative and must never be violated
- Minimal diff only
- Update WORKING_STATE.md after each task

## Three-Phase Workflow

```
DESIGN → PLANNING → EXECUTION
  ↓         ↓          ↓
Approve   Approve   Approve (per task)
```

1. **Design**: AI drafts architecture → Human approves
2. **Planning**: AI creates task breakdown → Human approves
3. **Execution**: AI implements tasks → Human reviews each

See: `docs/AI_WORKFLOW_GUIDE.md` for complete details

## Getting Started

### Quick Start
1. Click "Use this template" to create a new repository
2. Read MASTER_REFERENCE.md once (10 minutes)
3. Review `docs/PROJECT_TYPE_GUIDE.md` for your project type
4. Follow the three-phase workflow:
   - Phase 1: Fill PRODUCT_VISION.md, AI drafts ARCHITECTURE.md, you approve
   - Phase 2: AI creates EXECUTION_PLAN.md + tasks, you approve
   - Phase 3: Execute tasks one by one with AI, review each

### For Team Onboarding
See ONBOARDING.md for a 1-page guide.

### Scripts & Automation
```bash
# Check current phase
python scripts/check-phase.py

# Sync model config when starting a task
python scripts/sync-model-config.py tasks/TASK_001.md

# Check approval status
python scripts/check-approvals.py

# Validate model consistency
python scripts/validate-model.py
```

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
- **SYSTEM_PROMPT.md** - Paste into your AI tool (phase-aware)
- **ONBOARDING.md** - 1-page team guide

### Documentation Structure
- **docs/PRODUCT_VISION.md** - Product goals & scope
- **docs/ARCHITECTURE.md** - Authoritative design (never violate)
- **docs/EXECUTION_PLAN.md** - Milestones & timeline
- **docs/DEFINITION_OF_DONE.md** - Quality gates
- **docs/RELEASE_CHECKLIST.md** - Release process
- **docs/decisions/** - Architecture Decision Records (ADR)

### Workflow & Model Selection Guides
- **docs/AI_WORKFLOW_GUIDE.md** - Complete three-phase workflow
- **docs/MODEL_SELECTION_GUIDE.md** - Which AI model for which task
- **docs/PROJECT_TYPE_GUIDE.md** - Adapt template for all project types
- **docs/APPROVAL_GATES.md** - Centralized approval tracking

### Task Management
- **tasks/TASK_TEMPLATE.md** - Model-aware task template with approval checklist
- **tasks/README.md** - Task discipline rules

### AI Metrics
- **.ai-metrics/** - Session tracking & cost logging

### Automation Scripts
- **scripts/sync-model-config.py** - Auto-create metrics from task file
- **scripts/check-phase.py** - Detect current workflow phase
- **scripts/check-approvals.py** - Validate approval signatures
- **scripts/validate-model.py** - Check model consistency

### GitHub Integration
- **.github/pull_request_template.md** - Standard PR format with approval checklist
- **.github/workflows/model-validation.yml** - Automated model & phase validation
- **.ai-metrics/** - Session tracking & cost logging

### GitHub Integration
- **.github/pull_request_template.md** - Standard PR format
### GitHub Integration
- **.github/pull_request_template.md** - Standard PR format with approval checklist
- **.github/workflows/model-validation.yml** - Automated model & phase validation

## Validation Status

✅ **Production Ready** (98% confidence)

Validated with task-timer-cli test project:
- Zero ARCHITECTURE.md violations
- All template sections used successfully
- Minimal diff principle maintained
- Complete state tracking demonstrated
- Three-phase workflow validated
- Model selection and tracking proven

See `example/VALIDATION_SUMMARY.md` for detailed metrics.

## Use Cases

### By Project Size

#### Minimal Projects (<500 lines) 
Use: ARCHITECTURE.md + 1-3 task files + WORKING_STATE.md  
Skip: Most ceremony, keep core discipline

#### Small Projects (500-5k lines) ⭐ Sweet Spot
Use: Full template as designed  
Perfect fit for the three-phase workflow

#### Medium Projects (5k-50k lines)
Use: Everything + more granular tasks + regular ADRs  
Add: Per-module organization

#### Large Projects (50k+ lines)
Use: Core principles + customized state tracking  
Adapt: To existing team processes

**See**: `docs/PROJECT_TYPE_GUIDE.md` for detailed guidance on all project types

### By Project Type
- Web Applications (Frontend/Backend/Full-stack)
- Mobile Applications (React Native, Native iOS/Android)
- CLI Tools & Scripts
- Libraries & SDKs
- Data Pipelines & ETL
- Machine Learning Projects
- DevOps & Infrastructure

**See**: `docs/PROJECT_TYPE_GUIDE.md` for specific guidance per project type

## Why This Template?

✅ **Three-phase discipline** - Design → Planning → Execution with human approval gates  
✅ **File-based truth** - No session amnesia, complete audit trail  
✅ **AI-aware** - Tracks models, costs, outcomes for each task  
✅ **Architecture discipline** - ARCHITECTURE.md prevents drift  
✅ **Minimal diff** - Prevents AI over-engineering  
✅ **Model selection** - Choose optimal AI model per task type  
✅ **Team-ready** - 1-minute onboarding via ONBOARDING.md  
✅ **Tool-agnostic** - Works with Claude, ChatGPT, Cursor, Copilot, any AI  
✅ **Automated validation** - Scripts and GitHub Actions enforce consistency

## Quick Reference

### Starting a New Project
```bash
# 1. Create from template
# 2. Fill product vision
cat > docs/PRODUCT_VISION.md << EOF
## Product Goal
[Your vision]
EOF

# 3. Check phase (should be DESIGN)
python scripts/check-phase.py

# 4. Use AI to draft architecture (see AI_WORKFLOW_GUIDE.md)
# 5. Approve architecture
# 6. Move to planning phase
```

### Executing a Task
```bash
# 1. Sync model config
python scripts/sync-model-config.py tasks/TASK_001_feature.md

# 2. Give task to AI (see SYSTEM_PROMPT.md)
# 3. AI creates PR
# 4. Review and approve
# 5. Update working state
```

### Validation
```bash
# Check current phase
python scripts/check-phase.py

# Check all approvals
python scripts/check-approvals.py

# Validate models
python scripts/validate-model.py
```

## Documentation

### Essential Reading (Start Here)
1. **MASTER_REFERENCE.md** - Core rules (10 min read)
2. **ONBOARDING.md** - Quick start guide (5 min read)
3. **docs/AI_WORKFLOW_GUIDE.md** - Three-phase workflow (20 min read)

### Deep Dives
- **docs/MODEL_SELECTION_GUIDE.md** - Complete model selection criteria
- **docs/PROJECT_TYPE_GUIDE.md** - Adapt for any project type
- **docs/APPROVAL_GATES.md** - Approval tracking

### Templates
- **tasks/TASK_TEMPLATE.md** - Copy for each new task
- **.ai-metrics/session-template.md** - Auto-created by sync script

## Contributing

This template is designed to be stable. If you find issues or have suggestions:
1. Check `example/` to see if it's already demonstrated
2. Check `docs/PROJECT_TYPE_GUIDE.md` for adaptation guidance
3. Open an issue with your use case
4. Share metrics from your project

## License

MIT License - use freely for any project.

---

**Get Started**: Read MASTER_REFERENCE.md, then follow the three-phase workflow in docs/AI_WORKFLOW_GUIDE.md
