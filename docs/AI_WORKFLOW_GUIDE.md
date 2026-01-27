# AI-Assisted Development Workflow

This guide describes the complete three-phase workflow for AI-assisted development with human approval gates.

## Overview

This template supports a structured, disciplined workflow:

```
DESIGN → PLANNING → EXECUTION
   ↓         ↓          ↓
 Approve   Approve   Approve (per task)
```

**Key Principle**: AI assists at every phase, humans approve at every gate.

---

## Three-Phase Workflow

### Phase 1: DESIGN
**Goal**: Define architecture and constraints

**AI Role**: Propose solutions  
**Human Role**: Review and approve  
**Duration**: Hours to days  
**Artifact**: ARCHITECTURE.md + ADRs

---

### Phase 2: PLANNING  
**Goal**: Break down into executable tasks

**AI Role**: Create detailed task breakdown  
**Human Role**: Review and approve  
**Duration**: Hours  
**Artifact**: EXECUTION_PLAN.md + Task files

---

### Phase 3: EXECUTION
**Goal**: Implement the code

**AI Role**: Write code per task  
**Human Role**: Review and merge  
**Duration**: Days to weeks  
**Artifact**: Code + Tests + Metrics

---

## Phase 1: Design (AI-Assisted, Human-Approved)

### When to Use This Phase
- Starting a new project
- Adding a major feature
- Changing architecture significantly
- Technology stack decisions

### AI Responsibilities

1. **Read requirements**
   - Study PRODUCT_VISION.md thoroughly
   - Understand goals, constraints, and scope

2. **Propose architecture**
   - Draft ARCHITECTURE.md with clear sections
   - Define tech stack
   - Establish patterns and conventions
   - Identify constraints

3. **Create ADRs**
   - Document significant decisions
   - Explain alternatives considered
   - Justify choices

4. **Recommend models**
   - Suggest which AI models for implementation
   - Provide rationale (see MODEL_SELECTION_GUIDE.md)

### Human Responsibilities

1. **Review architecture**
   - Does it meet requirements?
   - Are constraints realistic?
   - Can the team execute this?

2. **Challenge decisions**
   - Question ADRs
   - Request alternatives
   - Push back on complexity

3. **Approve or request changes**
   - Explicit sign-off required
   - Document approval in ARCHITECTURE.md

### Artifacts Created

```
docs/
  ARCHITECTURE.md (filled)
  decisions/
    0001-use-adr.md
    0002-ai-model-selection.md
    0003-your-decision.md
    ...
```

### Model Recommendation

**Preferred**: Claude Sonnet 4+  
**Why**: Architecture design requires deep reasoning, consistency across multiple files, and understanding of complex tradeoffs.

**Fallback**: GPT-4 (if budget constrained)

### Approval Checklist

Use this before approving design phase:

- [ ] ARCHITECTURE.md is complete and clear
- [ ] All major decisions have ADRs
- [ ] Tech choices are justified
- [ ] Constraints are explicit and realistic
- [ ] Patterns are defined
- [ ] Security considerations addressed
- [ ] Performance expectations documented
- [ ] Team has capability to execute

### Approval Format

Add to bottom of `docs/ARCHITECTURE.md`:

```markdown
---

## Design Phase Approval

**Reviewer**: [Your Name]  
**Date**: 2026-01-27  
**Status**: ✅ Approved

**Notes**: Architecture is sound. Ready to proceed to planning phase.
```

### Exit Criteria

✅ **Architecture approved** → Proceed to Planning Phase

❌ **Architecture rejected** → AI revises and resubmits

---

## Phase 2: Planning (AI-Assisted, Human-Approved)

### When to Use This Phase
- After architecture is approved
- Before writing any code
- When breaking down epics into tasks

### AI Responsibilities

1. **Read approved architecture**
   - Understand all constraints
   - Follow established patterns

2. **Create execution plan**
   - Define milestones
   - Break down into tasks
   - Estimate effort
   - Identify dependencies
   - Propose timeline

3. **Generate task files**
   - Create task file for each task
   - Use TASK_TEMPLATE.md
   - Fill in all sections
   - Select appropriate AI model per task

4. **Risk analysis**
   - Identify blockers
   - Propose mitigations

### Human Responsibilities

1. **Review task breakdown**
   - Is it complete?
   - Right granularity? (not too big, not too small)
   - Dependencies correct?

2. **Validate estimates**
   - Are they realistic?
   - Buffer for unknowns?

3. **Prioritize**
   - Adjust task order if needed
   - Mark critical path

4. **Approve or request changes**
   - Explicit sign-off required
   - Document approval in EXECUTION_PLAN.md

### Artifacts Created

```
docs/
  EXECUTION_PLAN.md (filled)
tasks/
  TASK_001_setup.md
  TASK_002_auth.md
  TASK_003_api.md
  ...
```

### Model Recommendation

**Preferred**: Claude Sonnet 4 or GPT-4  
**Why**: Task breakdown requires understanding architecture and decomposing complexity.

**Fallback**: Claude Sonnet 3.5

### Approval Checklist

Use this before approving planning phase:

- [ ] EXECUTION_PLAN.md has all milestones
- [ ] Tasks are well-defined
- [ ] Each task has acceptance criteria
- [ ] Dependencies are identified
- [ ] Estimates are reasonable
- [ ] Each task has appropriate model selected
- [ ] Critical path is clear
- [ ] Risks are documented

### Approval Format

Add to bottom of `docs/EXECUTION_PLAN.md`:

```markdown
---

## Planning Phase Approval

**Reviewer**: [Your Name]  
**Date**: 2026-01-27  
**Status**: ✅ Approved

**Adjustments Made**:
- Increased estimate for TASK_003 (auth complexity)
- Reordered TASK_005 before TASK_004 (dependency)

**Notes**: Plan is solid. Ready to execute.
```

### Exit Criteria

✅ **Execution plan approved** → Proceed to Execution Phase

❌ **Plan needs work** → AI revises and resubmits

---

## Phase 3: Execution (AI-Assisted, Human-Approved)

### When to Use This Phase
- After planning is approved
- For each individual task
- Iteratively until all tasks complete

### AI Responsibilities (Per Task)

1. **Read task file**
   - Understand goal and acceptance criteria
   - Follow constraints

2. **Verify architecture compliance**
   - Check ARCHITECTURE.md
   - Follow patterns
   - Respect constraints

3. **Implement solution**
   - Write code
   - Add tests
   - Minimal diff only

4. **Update state**
   - Update WORKING_STATE.md
   - Log metrics in .ai-metrics/
   - Note any deviations

5. **Create PR**
   - Use PR template
   - Reference task file
   - Fill all sections

### Human Responsibilities (Per Task)

1. **Review code**
   - Quality acceptable?
   - Tests comprehensive?
   - Architecture not violated?

2. **Test manually**
   - Run locally
   - Verify acceptance criteria

3. **Approve or request changes**
   - Provide clear feedback
   - Request fixes if needed

4. **Merge when satisfied**
   - Update task file with approval
   - Move to next task

### Artifacts Created (Per Task)

```
src/
  [implementation code]
tests/
  [test files]
.ai-metrics/
  2026-01-27-task-001.md
tasks/
  TASK_001_setup.md (updated with approval)
```

### Model Recommendation

**Per Task**: Use model specified in task file  
**See**: MODEL_SELECTION_GUIDE.md for selection criteria

If you must use a different model (fallback or other reason):
- Document why in .ai-metrics/ session file
- Note impact on quality/cost

### Approval Checklist (Per Task)

Use this before approving each task:

- [ ] All acceptance criteria met
- [ ] Tests pass
- [ ] Code quality is acceptable
- [ ] ARCHITECTURE.md not violated
- [ ] Minimal diff principle followed
- [ ] No unauthorized refactoring
- [ ] WORKING_STATE.md updated
- [ ] AI metrics logged

### Approval Format

Add to task file (`tasks/TASK_XXX.md`):

```markdown
---

## Human Review & Approval

**Reviewer**: [Your Name]  
**Date**: 2026-01-27  
**Status**: ✅ Approved

**Code Quality**: Excellent  
**Tests**: Comprehensive  
**Architecture Compliance**: ✅ No violations

**Notes**: Clean implementation. Ready to merge.
```

### Exit Criteria (Per Task)

✅ **Task approved** → Merge PR → Next task

❌ **Changes requested** → AI fixes → Resubmit

---

## Workflow Commands

### Starting Design Phase

**Human Creates**:
```markdown
# docs/PRODUCT_VISION.md

## Product Goal
[Your vision]

## Scope
[What's included/excluded]

## Constraints
[Any known constraints]
```

**AI Prompt**:
```
You are in the DESIGN PHASE.

Help me design the architecture for this project.

Tasks:
1. Read PRODUCT_VISION.md thoroughly
2. Draft ARCHITECTURE.md with clear constraints
3. Create ADRs for all significant decisions
4. Propose appropriate AI models for implementation

Remember:
- You are proposing, not deciding
- Humans will review and approve
- Be specific and clear

When done, say: "Design complete. Ready for human approval."
```

**Run**: Paste prompt into your AI tool (Claude, ChatGPT, Cursor, etc.)

---

### Approving Design Phase

**Human Reviews**:
1. Read ARCHITECTURE.md
2. Review all ADRs
3. Ask questions if unclear
4. Request changes OR approve

**If Approved**:
```bash
# Add approval signature to docs/ARCHITECTURE.md
# (See approval format above)

# Commit the approved architecture
git add docs/ARCHITECTURE.md docs/decisions/
git commit -m "docs: approve design phase - architecture defined"
```

---

### Starting Planning Phase

**AI Prompt**:
```
You are in the PLANNING PHASE.

Help me create an execution plan.

Tasks:
1. Read approved ARCHITECTURE.md
2. Create detailed task breakdown in EXECUTION_PLAN.md
3. Generate task files for each task (use TASK_TEMPLATE.md)
4. Select appropriate model for each task (see MODEL_SELECTION_GUIDE.md)

Remember:
- Follow approved architecture strictly
- Tasks should be 1-8 hours each
- Clear acceptance criteria for each
- Identify dependencies

When done, say: "Planning complete. Ready for human approval."
```

**Run**: Paste prompt into your AI tool

---

### Approving Planning Phase

**Human Reviews**:
1. Read EXECUTION_PLAN.md
2. Review each task file
3. Validate estimates
4. Adjust priorities if needed
5. Request changes OR approve

**If Approved**:
```bash
# Add approval signature to docs/EXECUTION_PLAN.md
# (See approval format above)

# Commit the approved plan
git add docs/EXECUTION_PLAN.md tasks/
git commit -m "docs: approve planning phase - tasks defined"
```

---

### Executing a Task

**Sync Model Configuration** (Optional but recommended):
```bash
python scripts/sync-model-config.py tasks/TASK_001_setup.md
```

This creates `.ai-metrics/2026-01-27-task-001.md` with model pre-filled.

**AI Prompt**:
```
You are in the EXECUTION PHASE.

Execute tasks/TASK_001_setup.md.

Requirements:
- Follow ARCHITECTURE.md strictly
- Minimal diff only
- Update WORKING_STATE.md when done
- Log metrics in .ai-metrics/

When done, say: "Task complete. Ready for human review."
```

**Run**: Paste prompt into your AI tool

**AI Creates**: PR using `.github/pull_request_template.md`

---

### Approving Task Execution

**Human Reviews**:
1. Read PR description
2. Review code changes
3. Run tests locally
4. Verify acceptance criteria
5. Request changes OR approve

**If Approved**:
```bash
# Add approval to task file
# (See approval format above)

# Approve and merge PR on GitHub
gh pr review --approve
gh pr merge

# Or via GitHub UI
```

**Then**: Move to next task

---

## Model Selection Across Phases

| Phase | Recommended Model | Why |
|-------|------------------|-----|
| Design | Claude Sonnet 4+ | Deep reasoning, architecture |
| Planning | Claude Sonnet 4 / GPT-4 | Task decomposition |
| Execution (varies by task) | See task file | Match model to task type |

**See**: `docs/MODEL_SELECTION_GUIDE.md` for detailed guidance

---

## Phase Transition Checklist

### Before Moving Design → Planning

- [ ] ARCHITECTURE.md complete and approved
- [ ] All ADRs created and approved
- [ ] Team understands and accepts architecture
- [ ] Approval signature in ARCHITECTURE.md
- [ ] Changes committed to git

### Before Moving Planning → Execution

- [ ] EXECUTION_PLAN.md complete and approved
- [ ] All task files created
- [ ] Each task has model selected
- [ ] Dependencies identified
- [ ] Approval signature in EXECUTION_PLAN.md
- [ ] Changes committed to git

### Before Moving to Next Task

- [ ] Current task complete
- [ ] PR approved and merged
- [ ] WORKING_STATE.md updated
- [ ] Approval in task file
- [ ] No blockers for next task

---

## Handling Exceptions

### Architecture Change Needed During Execution

**Process**:
1. Stop current task
2. Create ADR proposing change
3. Update ARCHITECTURE.md (if approved)
4. Get human approval
5. Update affected tasks in EXECUTION_PLAN.md
6. Resume execution with new architecture

**Never**: Change architecture mid-task without approval

---

### Task Blocked

**Process**:
1. Document blocker in WORKING_STATE.md
2. Update task status to "Blocked"
3. Notify team
4. Work on unblocked tasks
5. Resolve blocker
6. Resume task

---

### Budget Exceeded

**Process**:
1. Review .ai-metrics/ for spending
2. Identify high-cost tasks
3. Consider cheaper models for remaining tasks
4. Update task files with fallback models
5. Get approval for model changes
6. Continue with adjusted budget

---

## Best Practices

### 1. Don't Skip Phases

❌ **Bad**: Jump straight to coding without design/planning  
✅ **Good**: Follow Design → Planning → Execution

Even for small changes:
- Quick design (5 min) is better than none
- Quick planning (10 min) prevents scope creep

### 2. One Task at a Time

❌ **Bad**: Start multiple tasks simultaneously  
✅ **Good**: Complete one task fully before starting next

Benefits:
- Clear focus
- Easier reviews
- No context switching

### 3. Approve Explicitly

❌ **Bad**: Assume approval if no response  
✅ **Good**: Explicit signature in document

Prevents:
- Ambiguity
- Miscommunication
- Rework

### 4. Update State Frequently

❌ **Bad**: Update WORKING_STATE.md once a week  
✅ **Good**: Update after every task completion

Benefits:
- Team stays synced
- Handoffs are smooth
- Audit trail is complete

### 5. Track Metrics

❌ **Bad**: Skip .ai-metrics/ logging  
✅ **Good**: Log every session

Benefits:
- Cost visibility
- Model performance analysis
- Learn what works

---

## Examples

### Example 1: Solo Developer, Small CLI Tool

**Design Phase** (15 minutes):
- Fill PRODUCT_VISION.md
- AI drafts ARCHITECTURE.md (10 min)
- Self-review and approve (5 min)

**Planning Phase** (20 minutes):
- AI creates EXECUTION_PLAN.md with 5 tasks (15 min)
- Self-review and approve (5 min)

**Execution Phase** (4 hours):
- TASK_001: Setup (45 min)
- TASK_002: Core feature (1.5 hours)
- TASK_003: Export (45 min)
- TASK_004: Testing (1 hour)
- Self-review each task (5-10 min each)

**Total**: ~5 hours

---

### Example 2: Small Team, SaaS Feature

**Design Phase** (3 hours):
- PM writes PRODUCT_VISION.md (30 min)
- Tech lead + AI draft ARCHITECTURE.md (1.5 hours)
- Team reviews ADRs (1 hour meeting)
- Tech lead approves

**Planning Phase** (2 hours):
- PM + AI create EXECUTION_PLAN.md (1 hour)
- Team reviews task breakdown (1 hour meeting)
- PM approves and assigns tasks

**Execution Phase** (3 weeks):
- 15 tasks across 3 developers
- Daily: Execute 1-2 tasks per developer
- Peer review PRs (30 min average)
- Tech lead final approval

**Total**: ~3 weeks elapsed time

---

## Troubleshooting

### "AI keeps violating ARCHITECTURE.md"

**Solutions**:
1. Make ARCHITECTURE.md more explicit
2. Add examples to ARCHITECTURE.md
3. Update SYSTEM_PROMPT.md with stronger emphasis
4. Use Claude Sonnet 4 (better at following rules)

---

### "Too much overhead for small tasks"

**Solutions**:
1. Use minimal templates for tiny tasks
2. Combine micro-tasks into one task
3. Skip ADRs for trivial decisions
4. Keep it lightweight but don't skip phases entirely

---

### "Team isn't following the workflow"

**Solutions**:
1. Show the value (less rework, clearer ownership)
2. Start with one feature using full workflow
3. Compare results to previous approach
4. Adjust process based on feedback
5. Make it easy (scripts, automation)

---

## Related Documentation

- See: `docs/MODEL_SELECTION_GUIDE.md` - Which AI model to use
- See: `docs/PROJECT_TYPE_GUIDE.md` - Adapt workflow for your project type
- See: `docs/APPROVAL_GATES.md` - Track all approvals
- See: `SYSTEM_PROMPT.md` - AI instructions for each phase
- See: `MASTER_REFERENCE.md` - Core principles

---

**Last Updated**: January 2026  
**Next Review**: April 2026
