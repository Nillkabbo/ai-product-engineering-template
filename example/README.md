# Example Project Quick Reference

## What's Here

This `example/` folder demonstrates the AI Product Engineering template in action with a real, working project.

### Project: task-timer-cli
A simple Python CLI tool for tracking time spent on coding tasks.

---

## Directory Structure

```
example/
├── VALIDATION_SUMMARY.md          # Complete validation report
└── task-timer-cli/                # Working example project
    ├── timer.py                   # The actual working CLI tool
    ├── README.md                  # Project-specific README
    ├── WORKING_STATE.md           # Current project state
    ├── CHANGELOG.md               # Version history
    │
    ├── docs/                      # All filled documentation
    │   ├── PRODUCT_VISION.md
    │   ├── ARCHITECTURE.md
    │   ├── EXECUTION_PLAN.md
    │   ├── DEFINITION_OF_DONE.md
    │   ├── RELEASE_CHECKLIST.md
    │   └── decisions/             # Architecture Decision Records
    │       ├── 0003-json-data-storage.md
    │       └── 0004-argparse-cli.md
    │
    ├── tasks/                     # Task management
    │   └── TASK_001_project_setup_core_timer.md
    │
    └── .ai-metrics/               # AI session tracking
        └── 2026-01-27-task-001.md
```

---

## Try It Out

```bash
cd example/task-timer-cli

# See available commands
python timer.py --help

# Start a timer
python timer.py start "Learning the template"

# Stop the timer
python timer.py stop

# Check the data file
cat ~/.task-timer/data.json
```

---

## What This Demonstrates

### 1. **Template Workflow** ✅
- Started from template files
- Filled all docs before coding
- Created task file first
- Implemented minimal diff
- Updated state after completion

### 2. **Documentation Quality** ✅
- ARCHITECTURE.md prevented scope creep
- ADRs explain technical choices
- WORKING_STATE.md shows progress clearly
- Everything links together

### 3. **AI-Assisted Development** ✅
- Model selection recorded (Claude Sonnet 4.5)
- Session metrics tracked
- Cost estimated ($0.15)
- Outcome documented

### 4. **Architecture Compliance** ✅
- Zero violations of ARCHITECTURE.md
- ADR decisions followed strictly
- Constraints respected (stdlib only)

---

## Validation Results

**Template Status:** ✅ PRODUCTION READY (98% confidence)

**What Worked:**
- Documentation-first prevented over-engineering
- Task template had all necessary sections
- Minimal diff principle kept code focused
- WORKING_STATE.md provided instant status

**Metrics:**
- Task completion: 1/5 (Phase 1 complete)
- Code: 125 lines
- Dependencies: 0 external
- Tests passed: 3/3
- Acceptance criteria: 4/4

See `VALIDATION_SUMMARY.md` for complete analysis.

---

## Next Steps

### To Continue This Example Project:
1. Review `tasks/TASK_001_project_setup_core_timer.md`
2. Create `TASK_002_list_display.md` using `TASK_TEMPLATE.md`
3. Implement list/summary commands
4. Update WORKING_STATE.md
5. Log AI session in .ai-metrics/

### To Use Template for Your Project:
1. Copy all template files from the root directory
2. Read `MASTER_REFERENCE.md` once
3. Fill `docs/PRODUCT_VISION.md` and `docs/ARCHITECTURE.md`
4. Create your first task in `tasks/`
5. Follow `ONBOARDING.md` workflow

---

## Key Files to Review

**To understand the workflow:**
- `VALIDATION_SUMMARY.md` - Complete validation report
- `task-timer-cli/docs/ARCHITECTURE.md` - See how constraints work
- `task-timer-cli/tasks/TASK_001_project_setup_core_timer.md` - Example task

**To see the results:**
- `task-timer-cli/timer.py` - Working Python code
- `task-timer-cli/WORKING_STATE.md` - State tracking in action
- `task-timer-cli/.ai-metrics/2026-01-27-task-001.md` - AI session log

---

**This example proves the template works for real projects, not just theory.**
