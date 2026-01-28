AI Product Engineering - GitHub Template Repository

Purpose
This repository is a ready-to-use GitHub template for AI-assisted, production-grade software engineering. It is tool-agnostic and works with any AI assistant.

Core Rules
- Files are the source of truth. Chat history is not the source of truth.
- ARCHITECTURE.md is authoritative and must never be violated.
- One task at a time. One AI session = one task.
- Minimal diff only. No refactors unless explicitly allowed in the task.
- No task file, no AI work.
- Before ending any session, update WORKING_STATE.md.
- Humans own decisions and releases. AI proposes, humans approve.

Three-Phase Workflow
DESIGN → PLANNING → EXECUTION (with human approval gates at each phase)

1. Design Phase: Draft architecture and ADRs → Human approves
2. Planning Phase: Create task breakdown → Human approves  
3. Execution Phase: Implement code → Human reviews each task

See: docs/AI_WORKFLOW_GUIDE.md for complete workflow details

Repository Structure
- MASTER_REFERENCE.md: This bundled rules document
- SYSTEM_PROMPT.md: The system prompt to paste into AI tools
- docs/: Product, architecture, and workflow documentation
- tasks/: Task templates and active tasks
- WORKING_STATE.md: Rolling compressed state for the project
- CHANGELOG.md: Project change log
- .ai-metrics/: AI session tracking and cost analysis
- scripts/: Automation scripts for validation and syncing

Task Discipline
- One task = one file under tasks/
- Task file is required before any AI work
- Model choice must be recorded in the task file
- Do not start a new task until the current task is complete
- Each task requires human approval before merge

Architecture Discipline
- ARCHITECTURE.md is the single source of truth
- Any change that affects architecture requires an explicit decision
- If architecture must change, update ARCHITECTURE.md first
- Create ADR (Architecture Decision Record) for significant decisions
- Get human approval for architecture changes

Minimal Diff Principle
- Make the smallest change necessary to meet the task goal
- Avoid refactors, renames, or reorganizations unless the task requires it
- Preserve existing patterns and style

Human Ownership & Approval Gates
- Humans own decisions and releases
- AI can propose, but humans approve at every phase
- Design phase: Architect/Tech lead approves ARCHITECTURE.md
- Planning phase: PM/Tech lead approves EXECUTION_PLAN.md  
- Execution phase: Code reviewer approves each task PR
- Release decisions must be documented in RELEASE_CHECKLIST.md

Model Selection Discipline
- Select AI model according to task complexity and type
- Document model choice in task file with rationale
- Use scripts/sync-model-config.py to propagate to metrics
- Track actual model used in .ai-metrics/ directory
- CI validates model consistency (warning-only)
- See: docs/MODEL_SELECTION_GUIDE.md for selection criteria

Scripts & Automation
Available scripts in scripts/ directory:

- sync-model-config.py: Create .ai-metrics file from task with model pre-filled
- check-phase.py: Determine current workflow phase
- check-approvals.py: Validate all approval signatures
- validate-model.py: Check model consistency between tasks and metrics

GitHub Actions:
- .github/workflows/model-validation.yml: Automated validation on PRs

Documentation
Core guides in docs/:

- AI_WORKFLOW_GUIDE.md: Complete three-phase workflow
- MODEL_SELECTION_GUIDE.md: Which AI model for which task
- PROJECT_TYPE_GUIDE.md: Using template for all project types
- APPROVAL_GATES.md: Centralized approval tracking
- ARCHITECTURE.md: System architecture (design phase output)
- EXECUTION_PLAN.md: Task breakdown (planning phase output)

Key Workflows
Design Phase:
1. Fill PRODUCT_VISION.md
2. AI drafts ARCHITECTURE.md + ADRs
3. Human reviews and approves
4. Proceed to planning

Planning Phase:
1. AI creates EXECUTION_PLAN.md + task files
2. AI selects model for each task
3. Human reviews and approves
4. Proceed to execution

Execution Phase (per task):
1. Run: python scripts/sync-model-config.py tasks/TASK_XXX.md
2. AI implements task
3. AI creates PR
4. Human reviews and approves
5. Update WORKING_STATE.md
6. Next task
