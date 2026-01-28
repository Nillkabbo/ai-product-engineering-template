# Complete Guide: Using This Template for All Project Types

This guide shows you exactly how to adapt this AI Product Engineering Template for your specific project type, size, and team structure.

---

## Table of Contents

1. [Quick Start by Project Size](#quick-start-by-project-size)
2. [By Project Type](#by-project-type)
3. [By Tech Stack](#by-tech-stack)
4. [By Team Structure](#by-team-structure)
5. [Complete Walkthrough Examples](#complete-walkthrough-examples)
6. [Troubleshooting & FAQ](#troubleshooting--faq)

---

## Quick Start by Project Size

### Tiny Projects (< 100 lines, 1-2 files)
**Example**: Simple CLI script, utility function, small automation

**Template Subset to Use**:
- ✅ ARCHITECTURE.md (1 paragraph)
- ✅ 1 task file
- ✅ WORKING_STATE.md
- ❌ Skip: EXECUTION_PLAN, ADRs, metrics tracking

**Workflow**:
1. Write brief ARCHITECTURE.md describing constraints
2. Create single task file with acceptance criteria
3. Run AI once to implement
4. Update WORKING_STATE.md

**AI Model Recommendation**: GPT-4o-mini (cost-effective for simple tasks)

**Time to Setup**: < 5 minutes

**Example ARCHITECTURE.md**:
```markdown
# Architecture

## Constraints
- Single Python file
- No external dependencies
- Use argparse for CLI

## Tech Stack
- Python 3.11+
- stdlib only
```

---

### Small Projects (100-1000 lines, < 10 files)
**Example**: CLI tool, REST API, small library, personal project

**Template Subset to Use**:
- ✅ Full template as designed (sweet spot!)
- ✅ ARCHITECTURE.md
- ✅ EXECUTION_PLAN.md
- ✅ 2-5 task files
- ✅ WORKING_STATE.md
- ✅ ADRs for major decisions (2-3)
- ✅ AI metrics tracking
- ⚠️ Optional: DEFINITION_OF_DONE (use if quality-critical)

**Workflow**: Full three-phase (Design → Planning → Execution)

**AI Model Recommendation**: 
- Design/Planning: Claude Sonnet 4
- Execution: Task-specific (see MODEL_SELECTION_GUIDE.md)

**Time to Setup**: 15-30 minutes

**Example**: See `example/task-timer-cli/` in this repo

---

### Medium Projects (1k-10k lines, 10-50 files)
**Example**: Web app, mobile app, medium SaaS feature, microservice

**Template Subset to Use**:
- ✅ Full template + enhanced customization
- ✅ ARCHITECTURE.md (comprehensive, multi-section)
- ✅ EXECUTION_PLAN.md with milestones
- ✅ 10-20 task files (organized by phase/module)
- ✅ WORKING_STATE.md (updated frequently)
- ✅ ADRs for all significant decisions (5-10)
- ✅ AI metrics tracking (analyze costs)
- ✅ DEFINITION_OF_DONE (strict quality gates)
- ✅ RELEASE_CHECKLIST.md
- ✅ Per-module task folders: `tasks/auth/`, `tasks/api/`, etc.

**Workflow**: 
- Full three-phase with multiple iterations
- Weekly architecture reviews
- Daily WORKING_STATE updates

**AI Model Recommendation**:
- Design: Claude Sonnet 4 (complex architecture)
- Planning: Claude Sonnet 4 or GPT-4
- Execution: Mixed per module (track costs in metrics)

**Time to Setup**: 1-2 hours

**Team Size**: 2-5 developers

---

### Large Projects (10k-100k lines, 50-500 files)
**Example**: Enterprise application, platform, large SaaS product

**Template Subset to Use**:
- ✅ Core principles + heavy customization
- ✅ ARCHITECTURE.md per module/service
- ✅ EXECUTION_PLAN.md per epic/milestone
- ✅ 50+ task files (organized hierarchically)
- ✅ WORKING_STATE.md per module
- ✅ ADRs per module (20-50 total)
- ✅ AI metrics tracking (cost center analysis)
- ✅ Custom workflows per team
- ✅ Integration with existing PM tools (Jira, Linear, etc.)

**Workflow**:
- Adapt three-phase to existing SDLC
- Module-level architecture reviews
- Automated validation in CI/CD

**AI Model Recommendation**:
- Design: Claude Sonnet 4 + domain experts
- Planning: GPT-4 + project managers
- Execution: Per-team model selection

**Time to Setup**: 4-8 hours (initial), ongoing refinement

**Team Size**: 10+ developers

**Customizations**:
```bash
# Example structure for large project
docs/
  architecture/
    core-architecture.md
    module-auth.md
    module-payments.md
  decisions/
    auth/
    payments/
    infrastructure/
tasks/
  phase1-mvp/
  phase2-scale/
  phase3-optimization/
.ai-metrics/
  team-frontend/
  team-backend/
```

---

### Enterprise Projects (100k+ lines, 500+ files)
**Example**: Legacy modernization, distributed systems, multi-product platform

**Template Subset to Use**:
- ✅ Principles only (adapt to existing processes)
- ✅ File-based truth principle
- ✅ Minimal diff principle
- ✅ Human approval gates
- ✅ Model selection discipline
- ❌ Don't use template structure as-is

**Workflow**: 
- Integrate principles into existing governance
- Use task files for AI work only
- Keep existing PM/architecture processes

**AI Model Recommendation**: 
- Per-team policies
- Centralized cost tracking

**Time to Setup**: Consulting engagement recommended

---

## By Project Type

### Web Applications

#### Frontend (React/Vue/Angular)
**Architecture Focus**:
- Component hierarchy
- State management pattern
- Styling approach (CSS-in-JS, Tailwind, etc.)
- Build tooling

**Recommended Models**:
- Design: GPT-4 (good at UI patterns)
- Components: GPT-4 (React/Vue expertise)
- State logic: Claude Sonnet 4 (complex state)
- Styling: GPT-4o-mini (CSS is straightforward)

**Sample ARCHITECTURE.md Section**:
```markdown
## Frontend Architecture

### Component Structure
- Atomic design: atoms → molecules → organisms → templates → pages
- All components in src/components/

### State Management
- React Context for global state
- useState for local state
- No Redux (keep it simple)

### Styling
- Tailwind CSS
- No custom CSS files
```

**Sample Task**:
```markdown
# Task: User Authentication Form

## AI Model Selection
- Primary: GPT-4
- Rationale: Form components + React hooks, GPT-4 excels here

## Constraints
- Must use existing Button and Input atoms
- Form validation with react-hook-form
- Follow Tailwind design system
```

---

#### Backend (Node.js/Python/Go)
**Architecture Focus**:
- API design (REST/GraphQL)
- Database schema
- Authentication/authorization
- Error handling patterns

**Recommended Models**:
- Design: Claude Sonnet 4 (API architecture)
- CRUD operations: GPT-4 (pattern-based)
- Complex business logic: Claude Sonnet 4
- Database queries: Claude Sonnet 4 (SQL reasoning)

**Sample ARCHITECTURE.md Section**:
```markdown
## Backend Architecture

### API Structure
- RESTful API
- Express.js framework
- Routes in src/routes/
- Controllers in src/controllers/
- Services in src/services/

### Database
- PostgreSQL
- Prisma ORM
- Migrations in prisma/migrations/

### Authentication
- JWT tokens
- Bcrypt for passwords
- Refresh token rotation
```

**Sample Task**:
```markdown
# Task: User Registration Endpoint

## AI Model Selection
- Primary: Claude Sonnet 4
- Rationale: Complex business logic (validation, hashing, transactions)

## Constraints
- Must validate email uniqueness
- Hash password with bcrypt (12 rounds)
- Return JWT token
- Follow error handling pattern in ARCHITECTURE.md
```

---

#### Full-Stack Applications
**Architecture Focus**:
- Clear frontend/backend separation
- API contract definition
- Shared types/interfaces
- Development workflow

**Recommended Models**:
- Design: Claude Sonnet 4 (full-stack reasoning)
- Frontend tasks: GPT-4
- Backend tasks: Claude Sonnet 4
- Integration tasks: Claude Sonnet 4

**Sample Task Breakdown**:
```markdown
# Feature: User Profile

TASK_001: Design API contract (Claude Sonnet 4)
TASK_002: Backend endpoint (Claude Sonnet 4)
TASK_003: Frontend component (GPT-4)
TASK_004: Integration & testing (Claude Sonnet 4)
```

---

### Mobile Applications

#### React Native
**Architecture Focus**:
- Navigation structure
- State management
- Native module usage
- Platform-specific code

**Recommended Models**:
- Design: GPT-4 (React Native patterns)
- UI components: GPT-4
- Complex logic: Claude Sonnet 4
- Native modules: Claude Sonnet 4 (requires deep understanding)

**Sample ARCHITECTURE.md**:
```markdown
## Mobile Architecture

### Navigation
- React Navigation v6
- Stack navigation for main flows
- Tab navigation for home

### State Management
- Redux Toolkit
- Persist with AsyncStorage

### Platform Handling
- Use Platform.select() for platform-specific code
- Minimal platform splits
```

---

#### Native (iOS Swift / Android Kotlin)
**Architecture Focus**:
- MVVM/MVI architecture
- Dependency injection
- Network layer
- Data persistence

**Recommended Models**:
- Design: Claude Sonnet 4 (native patterns complex)
- UI: GPT-4 (SwiftUI/Jetpack Compose)
- Business logic: Claude Sonnet 4
- Networking: Claude Sonnet 4

---

### CLI Tools
**Architecture Focus**:
- Argument parsing
- Output formatting
- Error handling
- Configuration

**Recommended Models**:
- Design: GPT-4 (CLI patterns well-known)
- Implementation: GPT-4 or Claude Sonnet 3.5
- Complex logic: Claude Sonnet 4

**Sample ARCHITECTURE.md**:
```markdown
## CLI Architecture

### Argument Parsing
- Use argparse (Python) / Commander (Node)
- Subcommands: start, stop, list, export

### Output
- Colored output with chalk/colorama
- JSON output mode with --json flag
- Quiet mode with --quiet

### Configuration
- Config file: ~/.myapp/config.json
- Environment variables override config
```

**Example**: See `example/task-timer-cli/` in this repo

---

### Libraries & SDKs
**Architecture Focus**:
- Public API design
- Backward compatibility
- Documentation
- Testing

**Recommended Models**:
- Design: Claude Sonnet 4 (API design critical)
- Implementation: Claude Sonnet 4
- Documentation: GPT-4
- Examples: GPT-4

**Sample ARCHITECTURE.md**:
```markdown
## Library Architecture

### Public API
- All exports from src/index.ts
- No breaking changes without major version
- Semantic versioning

### Compatibility
- Node.js 16+
- TypeScript 4.5+
- No dependencies (bundle size critical)

### Documentation
- JSDoc for all public functions
- README with examples
- API reference auto-generated
```

---

### Data Pipelines & ETL
**Architecture Focus**:
- Data flow
- Error handling & retries
- Idempotency
- Monitoring

**Recommended Models**:
- Design: Claude Sonnet 4 (complex data flows)
- Transformations: Claude Sonnet 4 (logic-heavy)
- SQL: Claude Sonnet 4
- Orchestration: GPT-4

**Sample ARCHITECTURE.md**:
```markdown
## Pipeline Architecture

### Data Flow
1. Extract from API (src/extractors/)
2. Transform (src/transformers/)
3. Load to warehouse (src/loaders/)

### Error Handling
- Retry with exponential backoff (3 attempts)
- Dead letter queue for failures
- Alert on 3 consecutive failures

### Idempotency
- All operations idempotent
- Use upsert, not insert
- Track processing with checkpoint table
```

---

### Machine Learning Projects
**Architecture Focus**:
- Model training pipeline
- Data versioning
- Experiment tracking
- Model serving

**Recommended Models**:
- Design: Claude Sonnet 4 (ML architecture complex)
- Data preprocessing: Claude Sonnet 4
- Model code: Claude Sonnet 4 (subtle bugs critical)
- API serving: GPT-4

**Sample ARCHITECTURE.md**:
```markdown
## ML Architecture

### Training Pipeline
- Data: DVC for versioning
- Experiments: MLflow tracking
- Models: Model registry in MLflow

### Model Serving
- FastAPI endpoint
- Model versioning (A/B testing)
- Monitoring: prediction drift

### Reproducibility
- All random seeds set
- Requirements.txt pinned
- Docker for consistency
```

---

### DevOps & Infrastructure
**Architecture Focus**:
- IaC principles
- Security
- Monitoring
- Disaster recovery

**Recommended Models**:
- Design: Claude Sonnet 4 (infrastructure complexity)
- Terraform/CloudFormation: Claude Sonnet 4
- Scripts: GPT-4
- Documentation: GPT-4

**Sample ARCHITECTURE.md**:
```markdown
## Infrastructure Architecture

### IaC Tooling
- Terraform for all infrastructure
- State in S3 with locking
- Modules in modules/ directory

### Security
- All secrets in AWS Secrets Manager
- No hardcoded credentials
- Least privilege IAM policies

### Environments
- dev, staging, prod
- Identical configs, different scales
```

---

## By Tech Stack

### Python Projects
**Template Customization**:
```markdown
## Architecture

### Project Structure
```
project/
  src/
    __init__.py
    main.py
  tests/
    test_main.py
  requirements.txt
  pyproject.toml
```

### Code Standards
- Black for formatting
- Pylint for linting
- Type hints required (mypy)
- Docstrings (Google style)

### Testing
- pytest
- 80% coverage minimum
```

**AI Model**: Claude Sonnet 4 (excellent Python reasoning)

---

### JavaScript/TypeScript Projects
**Template Customization**:
```markdown
## Architecture

### Project Structure
```
project/
  src/
    index.ts
  tests/
    index.test.ts
  package.json
  tsconfig.json
```

### Code Standards
- ESLint + Prettier
- TypeScript strict mode
- No `any` types

### Testing
- Jest or Vitest
- React Testing Library (if React)
```

**AI Model**: 
- TypeScript types: Claude Sonnet 4
- React: GPT-4
- Node.js: Claude Sonnet 4

---

### Go Projects
**Template Customization**:
```markdown
## Architecture

### Project Structure (Standard Go)
```
project/
  cmd/
    myapp/
      main.go
  pkg/
    mypackage/
  internal/
    app/
  go.mod
```

### Code Standards
- gofmt
- golangci-lint
- Table-driven tests
```

**AI Model**: Claude Sonnet 4 (Go requires understanding of interfaces, concurrency)

---

### Rust Projects
**Template Customization**:
```markdown
## Architecture

### Project Structure
```
project/
  src/
    main.rs
    lib.rs
  tests/
  Cargo.toml
```

### Code Standards
- cargo fmt
- cargo clippy (strict)
- Comprehensive error handling (Result/Option)
```

**AI Model**: Claude Sonnet 4 (Rust is complex, requires deep reasoning)

---

## By Team Structure

### Solo Developer
**Template Usage**:
- Use full template
- You are both AI operator and approver
- Approval gates = self-review checkpoints
- Track metrics to optimize your workflow

**Workflow**:
1. Design phase (30 min thinking + AI)
2. Self-approve architecture
3. Planning phase (AI generates tasks)
4. Self-approve plan
5. Execute tasks one by one
6. Self-review each task before next

**Benefits**:
- Prevents scope creep
- Forces clear thinking
- Buildable portfolio of documented work

---

### Small Team (2-5 people)
**Template Usage**:
- Full template as designed
- Rotate approval responsibility
- Use APPROVAL_GATES.md to track who approved what
- Weekly sync on WORKING_STATE.md

**Workflow**:
1. Product owner fills PRODUCT_VISION.md
2. Tech lead + AI draft ARCHITECTURE.md
3. Team reviews and approves architecture
4. AI + team creates EXECUTION_PLAN.md
5. Team approves plan
6. Developers execute tasks with AI
7. Peer review PRs

**Benefits**:
- Shared understanding
- Clear ownership
- Async-friendly (files are truth)

---

### Medium Team (5-15 people)
**Template Usage**:
- Full template + module separation
- Dedicated architect approves design
- PM approves planning
- Tech leads approve execution
- Use GitHub CODEOWNERS for approval routing

**Workflow**:
1. PM writes PRODUCT_VISION.md per feature
2. Architect + AI draft ARCHITECTURE.md updates
3. Architect approves (ADR created)
4. PM + AI creates EXECUTION_PLAN.md
5. PM approves and assigns tasks
6. Developers execute with AI
7. Tech lead reviews PRs

**Team Roles**:
- Product Manager: PRODUCT_VISION, EXECUTION_PLAN approval
- Architect: ARCHITECTURE.md, ADR approval
- Tech Leads: Code review, quality gates
- Developers: Task execution with AI

---

### Large Team (15+ people)
**Template Usage**:
- Principles only, adapt to existing process
- Use template within teams/squads
- Central architecture board for ADRs
- Integrate with existing PM tools

**Workflow**:
- Use template at squad level (5-7 people)
- Squad architectures roll up to system architecture
- Cross-squad dependencies in EXECUTION_PLAN.md
- Centralized approval tracking

---

## Complete Walkthrough Examples

### Example 1: Solo Developer Building a CLI Tool
**Project**: Personal finance tracker CLI

**Day 1: Setup (15 minutes)**
1. Create repo from template
2. Fill PRODUCT_VISION.md:
```markdown
# Product Vision
Track expenses via CLI. Export to CSV for tax time.
Target: Personal use, maybe share on GitHub later.
```

3. AI drafts ARCHITECTURE.md:
   - "Help me design a CLI expense tracker. Read PRODUCT_VISION.md and draft ARCHITECTURE.md."

4. Review and approve architecture:
   - Self-review: sensible choices?
   - Sign approval in ARCHITECTURE.md

**Day 2: Planning (20 minutes)**
5. AI creates execution plan:
   - "Create execution plan. Break down into tasks."

6. Review task breakdown:
   - 5 tasks total, looks good
   - Sign approval in EXECUTION_PLAN.md

**Days 3-7: Execution (3-5 hours total)**
7. Execute tasks one by one:
   - TASK_001: Project setup + add expense (1 hour)
   - TASK_002: List expenses (45 min)
   - TASK_003: CSV export (30 min)
   - TASK_004: Categories (45 min)
   - TASK_005: Testing + README (1 hour)

8. Each task:
   - Run: `python scripts/sync-model-config.py tasks/TASK_00X.md`
   - AI implements
   - Self-review
   - Merge
   - Update WORKING_STATE.md

**Day 8: Release**
9. Follow RELEASE_CHECKLIST.md
10. Publish to GitHub

**Total Time**: ~8 hours over 1 week

**Cost**: ~$5-10 in AI tokens (using Claude Sonnet 4)

---

### Example 2: Small Team Building a SaaS Feature
**Project**: Add billing module to existing SaaS app

**Team**: 3 developers, 1 PM, 1 designer

**Week 1: Design Phase**
1. **PM** fills PRODUCT_VISION.md with billing requirements
2. **Tech Lead + AI** draft ARCHITECTURE.md:
   - Database schema for subscriptions
   - Stripe integration approach
   - Webhook handling
   - ADRs: Why Stripe, database schema design

3. **Team Review** (1 hour meeting):
   - Discuss architecture
   - Approve or request changes
   - Tech lead signs approval

**Week 2: Planning Phase**
4. **PM + AI** create EXECUTION_PLAN.md:
   - 12 tasks across 3 weeks
   - Dependencies identified
   - Assigned to developers

5. **Team Planning** (1 hour meeting):
   - Review task breakdown
   - Adjust estimates
   - PM signs approval

**Weeks 3-5: Execution Phase**
6. **Developers** execute tasks:
   - Dev 1: Database schema + migrations (3 tasks)
   - Dev 2: Stripe integration (4 tasks)
   - Dev 3: Webhook handlers (3 tasks)
   - All: Integration testing (2 tasks)

7. **Daily workflow per task**:
   - Pick task from EXECUTION_PLAN
   - Run sync script
   - AI implements
   - Create PR
   - Peer review
   - Tech lead approves
   - Merge
   - Update WORKING_STATE.md

**Week 6: QA & Release**
8. Follow RELEASE_CHECKLIST.md
9. Deploy to production

**Total Time**: 6 weeks (includes buffer)

**Cost**: ~$100-200 in AI tokens

**Team Efficiency**: 
- Clear ownership via task files
- No ambiguity (architecture is law)
- Async-friendly (files, not meetings)

---

### Example 3: Enterprise Team Modernizing Legacy System
**Project**: Migrate monolith to microservices

**Team**: 20 developers across 4 squads

**Approach**: Use template principles, not structure

**Setup (Week 1)**:
1. Architecture Board creates master ARCHITECTURE.md:
   - Migration strategy
   - Service boundaries
   - Data migration approach
   - Security requirements

2. Each squad gets subset of template:
   - Squad-level ARCHITECTURE.md (inherits from master)
   - Squad EXECUTION_PLAN.md
   - Squad task files

**Execution (Months 2-12)**:
3. Squads work independently:
   - Use template workflow within squad
   - Escalate architecture questions to board
   - Track progress in squad WORKING_STATE.md

4. Cross-squad coordination:
   - Weekly sync: share WORKING_STATE.md files
   - Dependency tracking in master EXECUTION_PLAN.md
   - ADRs reviewed by architecture board

**Benefits**:
- Autonomy within guardrails
- Consistent process across squads
- Clear escalation path
- Audit trail for compliance

---

## Troubleshooting & FAQ

### "My project doesn't fit any category"
**Solution**: Use core principles only
- File-based truth
- Minimal diff
- Human approval gates
- Model selection discipline

Adapt everything else to your context.

---

### "Template feels too heavy for my small project"
**Solution**: Use minimal subset
- Just ARCHITECTURE.md + 1-2 task files
- Skip metrics, ADRs, execution plan
- Keep core discipline: minimal diff, human ownership

---

### "How do I introduce this to an existing team?"
**Solution**: Phased adoption
1. Week 1: Just ARCHITECTURE.md (document existing state)
2. Week 2: Add task files for new work
3. Week 3: Add WORKING_STATE.md tracking
4. Month 2: Add metrics tracking
5. Month 3: Full workflow with approval gates

---

### "AI keeps violating ARCHITECTURE.md"
**Solution**: Improve SYSTEM_PROMPT.md emphasis
```markdown
CRITICAL: ARCHITECTURE.md is LAW. 
Any violation is a critical failure.
Before ANY change, verify it complies with ARCHITECTURE.md.
If unclear, ask human before proceeding.
```

Also: Review your ARCHITECTURE.md. If AI violates it often, it may be:
- Too vague (add specifics)
- Contradictory (clarify)
- Out of date (update it)

---

### "How do I handle breaking changes to architecture?"
**Solution**: Formal ADR + plan
1. Create ADR documenting why change is needed
2. Update ARCHITECTURE.md
3. Create migration plan in EXECUTION_PLAN.md
4. Get team approval
5. Execute migration tasks

Never change architecture mid-task.

---

### "Team isn't filling out templates properly"
**Solution**: Automate validation
- Use GitHub Actions to check template completeness
- Block PRs without proper task file
- Make templates easy (provide examples)
- Review in team retro, show value

---

## Summary: Choosing Your Setup

| Project Type | Template Subset | Setup Time | Sweet Spot |
|-------------|----------------|------------|------------|
| Tiny (< 100 LOC) | Minimal | 5 min | Quick scripts |
| Small (100-1k) | **Full template** | 15 min | ⭐ **Best fit** |
| Medium (1k-10k) | Full + custom | 1 hour | Multi-feature apps |
| Large (10k-100k) | Principles + adapt | 4 hours | Enterprise features |
| Enterprise (100k+) | Principles only | Consulting | Legacy systems |

**General Rule**: 
- If in doubt, start with **full template for small projects**
- Scale up or down based on pain points
- Keep what works, adapt what doesn't

**Success Metrics**:
- Less time in meetings ✅
- Clearer ownership ✅
- Fewer scope creep incidents ✅
- Buildable track record (ADRs, metrics) ✅
- AI costs under control ✅

---

## Next Steps

1. **Choose your project type** from this guide
2. **Follow the specific walkthrough** for your scenario
3. **Start with design phase** (even if 10 minutes)
4. **Get first approval** (validate workflow)
5. **Execute one task** (prove it works)
6. **Iterate and adapt** (make it yours)

**Questions?** 
- Review: README.md, ONBOARDING.md, MASTER_REFERENCE.md
- Check: example/task-timer-cli/ for working example
- See: docs/AI_WORKFLOW_GUIDE.md for three-phase workflow
- See: docs/MODEL_SELECTION_GUIDE.md for model selection

---

**Last Updated**: January 2026  
**Next Review**: April 2026
