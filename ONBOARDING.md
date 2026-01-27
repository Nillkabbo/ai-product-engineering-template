# 1-Page Coworker Onboarding

## Quick Start
1. Read MASTER_REFERENCE.md once
2. Understand the three-phase workflow: Design → Planning → Execution
3. Use SYSTEM_PROMPT.md in your AI tool for each phase
4. Get human approval at each gate before proceeding

## Three-Phase Workflow

### Phase 1: DESIGN (Architecture & ADRs)
**What**: Define architecture and key decisions  
**Who**: Tech lead + AI  
**Duration**: Hours to days

1. Fill PRODUCT_VISION.md (human writes requirements)
2. AI drafts ARCHITECTURE.md + ADRs (major decisions)
3. **GATE**: Human reviews and approves
4. Sign approval in ARCHITECTURE.md

**Output**: Approved architecture documentation

---

### Phase 2: PLANNING (Task Breakdown)
**What**: Break work into executable tasks  
**Who**: PM/Tech lead + AI  
**Duration**: Hours

1. AI reads approved ARCHITECTURE.md
2. AI creates EXECUTION_PLAN.md + individual task files
3. AI selects appropriate models for each task
4. **GATE**: Human reviews and approves
5. Sign approval in EXECUTION_PLAN.md

**Output**: Approved task list with estimates

---

### Phase 3: EXECUTION (Implementation)
**What**: Implement code per task  
**Who**: Developer + AI  
**Duration**: Days to weeks (iterative)

1. Pick a task from EXECUTION_PLAN.md
2. Run: `python scripts/sync-model-config.py tasks/TASK_XXX.md`
3. AI implements using recommended model
4. AI creates PR with filled template
5. **GATE**: Human reviews PR
6. Human approves and merges
7. Update WORKING_STATE.md
8. Repeat for next task

**Output**: Working code, merged to main

---

## File Map
- **ARCHITECTURE.md**: Law. Must not be violated. (Approved in Design phase)
- **EXECUTION_PLAN.md**: Task roadmap (Approved in Planning phase)
- **tasks/**: Work queue - one file per task (Each approved before merge)
- **WORKING_STATE.md**: Rolling state, updated after each task
- **.ai-metrics/**: Session tracking for cost and model analysis

## AI Model Selection
Different tasks need different models:
- **Design/Architecture**: Claude Sonnet 4 (deep reasoning)
- **Frontend/UI**: GPT-4 (strong React/CSS patterns)
- **Backend/Logic**: Claude Sonnet 4 (complex reasoning)
- **Simple tasks**: GPT-4o-mini (cost-effective)

**See**: `docs/MODEL_SELECTION_GUIDE.md` for complete criteria

## AI Usage Rules
- No task file → no AI work
- One task at a time
- ARCHITECTURE.md is LAW (never violate)
- Minimal diff only (no unnecessary changes)
- Update WORKING_STATE.md before ending
- Human approval required at every gate

## Scripts & Automation

```bash
# Check what phase you're in
python scripts/check-phase.py

# Sync model config when starting a task
python scripts/sync-model-config.py tasks/TASK_001.md

# Check all approvals
python scripts/check-approvals.py

# Validate model consistency
python scripts/validate-model.py
```

## First Task Walkthrough

### Step 1: Setup (5 minutes)
1. Copy TASK_TEMPLATE.md → `tasks/TASK_001_my_feature.md`
2. Fill in: Goal, Context, Deliverables, Acceptance Criteria

### Step 2: Select Model (2 minutes)
3. Review `docs/MODEL_SELECTION_GUIDE.md`
4. Choose primary and fallback models
5. Document rationale in task file

### Step 3: Sync & Execute (varies)
6. Run: `python scripts/sync-model-config.py tasks/TASK_001_my_feature.md`
7. Give task file to your AI tool
8. AI implements per ARCHITECTURE.md constraints

### Step 4: Review & Approve (10-30 minutes)
9. Review AI's PR
10. Run tests locally
11. Approve and merge OR request changes
12. Update WORKING_STATE.md

**Done!** Move to next task.

## Documentation Reference
- **MASTER_REFERENCE.md**: Complete bundled rules
- **docs/AI_WORKFLOW_GUIDE.md**: Deep dive on three-phase workflow
- **docs/MODEL_SELECTION_GUIDE.md**: Which model for which task
- **docs/PROJECT_TYPE_GUIDE.md**: Adapt template for your project type
- **docs/APPROVAL_GATES.md**: Track all approvals centrally

## Common Scenarios

### Solo Developer
- You are both AI operator and approver
- Self-approve at each gate (but do the checkpoint!)
- Track metrics to optimize your workflow

### Small Team (2-5 people)
- Rotate approval responsibility
- Use APPROVAL_GATES.md to track who approved what
- Weekly sync on WORKING_STATE.md

### Medium Team (5-15 people)
- Architect approves design
- PM approves planning
- Tech leads approve execution (code review)

## Troubleshooting

**Q: AI violated ARCHITECTURE.md**  
A: Reject the PR. Emphasize ARCHITECTURE.md in next session.

**Q: Not sure which AI model to use**  
A: See `docs/MODEL_SELECTION_GUIDE.md` decision flowchart.

**Q: Template feels too heavy**  
A: See `docs/PROJECT_TYPE_GUIDE.md` for minimal setup options.

**Q: How do I introduce this to my team?**  
A: Start with one feature using full workflow. Show the value.

## Next Steps
1. Read MASTER_REFERENCE.md (10 minutes)
2. Review example: `example/task-timer-cli/` (working implementation)
3. Pick your project type from `docs/PROJECT_TYPE_GUIDE.md`
4. Start Phase 1: Fill PRODUCT_VISION.md and draft architecture

**Welcome aboard!** 🚀
