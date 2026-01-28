# Approval Gates

This document tracks all human approval gates in the AI-assisted workflow.

## Purpose

- Centralized record of all approvals
- Audit trail for decisions
- Accountability tracking
- Process transparency

## Quick Reference

| Phase | Document | Status | Approved By | Date |
|-------|----------|--------|-------------|------|
| Design | ARCHITECTURE.md | - | - | - |
| Planning | EXECUTION_PLAN.md | - | - | - |
| Execution | See task files | - | - | - |

---

## Design Phase Approvals

### Architecture (ARCHITECTURE.md)
| Version | Date | Approved By | Status | Notes |
|---------|------|-------------|--------|-------|
| - | - | - | - | Awaiting initial design |

### Architecture Decision Records
| ADR | Title | Date | Approved By | Status |
|-----|-------|------|-------------|--------|
| 0001 | Use ADR | - | - | Template default |
| 0002 | Model Selection | - | - | Template default |

**Add new ADRs as they are created and approved**

---

## Planning Phase Approvals

### Execution Plan
| Version | Date | Approved By | Status | Notes |
|---------|------|-------------|--------|-------|
| - | - | - | - | Awaiting planning phase |

### Task Plan Approvals
| Task | Created | Planned By | Approved By | Status | Notes |
|------|---------|------------|-------------|--------|-------|
| - | - | - | - | - | No tasks yet |

**Add tasks as they are created during planning**

---

## Execution Phase Approvals

### Task Completions
| Task | PR # | Completed | Reviewed By | Status | Notes |
|------|------|-----------|-------------|--------|-------|
| - | - | - | - | - | No tasks completed yet |

**Add tasks as they are completed and approved**

---

## Approval Statistics

### Overall Progress
- **Design Phase**: ⏳ Not started
- **Planning Phase**: ⏳ Not started  
- **Execution Phase**: ⏳ Not started

### Metrics (Update quarterly)
- Total design approvals: 0
- Total planning approvals: 0
- Total task approvals: 0
- Average review time: - hours
- Rejection rate: -%

---

## Approval Guidelines

### Design Phase
**Who Approves**: Tech Lead, Architect, or Senior Engineer  
**What to Check**:
- ARCHITECTURE.md is complete
- ADRs are justified
- Technical decisions are sound
- Team can execute the design

**Approval Format**:
```markdown
**Approved by**: [Name]  
**Date**: YYYY-MM-DD  
**Status**: ✅ Approved
```

---

### Planning Phase
**Who Approves**: Product Manager, Project Lead, or Tech Lead  
**What to Check**:
- Tasks are well-defined
- Estimates are realistic
- Dependencies identified
- Timeline is achievable

**Approval Format**:
```markdown
**Approved by**: [Name]  
**Date**: YYYY-MM-DD  
**Status**: ✅ Approved
```

---

### Execution Phase (Per Task)
**Who Approves**: Code reviewer, Peer developer, or Tech Lead  
**What to Check**:
- Code quality acceptable
- Tests pass
- Acceptance criteria met
- Architecture not violated

**Approval Format**:
```markdown
**Reviewer**: [Name]  
**Date**: YYYY-MM-DD  
**Status**: ✅ Approved
```

---

## Status Legend

- ✅ **Approved** - Reviewed and accepted
- ⏳ **In Review** - Currently being reviewed
- 🔄 **Revision Requested** - Needs changes
- ❌ **Rejected** - Not approved, significant changes needed
- ⏸️ **On Hold** - Paused, awaiting external input

---

## How to Use This Document

### For Design Approvals
1. After ARCHITECTURE.md is drafted, reviewer examines it
2. Reviewer adds entry to "Architecture" table above
3. Reviewer signs approval in ARCHITECTURE.md itself
4. Update this document with approval record

### For Planning Approvals
1. After EXECUTION_PLAN.md is created, reviewer examines it
2. Reviewer adds entry to "Execution Plan" table above
3. Reviewer signs approval in EXECUTION_PLAN.md itself
4. Update this document with approval record

### For Task Approvals
1. After PR is created, reviewer examines code
2. Reviewer approves PR in GitHub
3. Reviewer adds entry to "Task Completions" table above
4. Reviewer signs approval in task file (tasks/TASK_XXX.md)

---

## Example Entries

### Example: Design Approval
```markdown
### Architecture (ARCHITECTURE.md)
| Version | Date | Approved By | Status | Notes |
|---------|------|-------------|--------|-------|
| v1.0 | 2026-01-27 | Jane Doe | ✅ Approved | Initial architecture solid |
| v1.1 | 2026-02-15 | Jane Doe | ✅ Approved | Added caching layer |
```

### Example: Planning Approval
```markdown
### Execution Plan
| Version | Date | Approved By | Status | Notes |
|---------|------|-------------|--------|-------|
| v1.0 | 2026-01-28 | John Smith (PM) | ✅ Approved | Timeline aggressive but doable |
```

### Example: Task Approval
```markdown
### Task Completions
| Task | PR # | Completed | Reviewed By | Status | Notes |
|------|------|-----------|-------------|--------|-------|
| TASK_001 | #12 | 2026-01-29 | Alice Chen | ✅ Approved | Clean implementation |
| TASK_002 | #13 | 2026-01-30 | Bob Lee | 🔄 Revision Requested | Needs more tests |
| TASK_002 | #14 | 2026-01-31 | Bob Lee | ✅ Approved | Tests added |
```

---

## Related Documentation

- See: `docs/AI_WORKFLOW_GUIDE.md` - Three-phase workflow with approval gates
- See: `docs/ARCHITECTURE.md` - Design phase approval location
- See: `docs/EXECUTION_PLAN.md` - Planning phase approval location
- See: `tasks/TASK_TEMPLATE.md` - Execution phase approval location per task

---

**Last Updated**: January 2026  
**Maintained By**: [Project Lead Name]
