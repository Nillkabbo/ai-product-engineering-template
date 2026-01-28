# AI Model Selection Guide

This guide helps you select the right AI model for each task based on complexity, task type, and cost considerations.

## Quick Reference

| Task Type | Recommended Model | Why |
|-----------|------------------|-----|
| Simple CRUD | GPT-4o-mini | Cost-effective, pattern-based |
| UI Components | GPT-4 | Strong React/CSS patterns |
| Complex Logic | Claude Sonnet 4+ | Superior reasoning |
| Architecture Design | Claude Sonnet 4+ | Deep reasoning, consistency |
| Refactoring | Same model that wrote it | Context continuity |
| Documentation | GPT-4o-mini | Cost-effective writing |
| Bug Fixes | Same model that wrote it | Understanding context |
| Database/SQL | Claude Sonnet 4 | Strong SQL reasoning |
| Testing | GPT-4 | Good at test patterns |

---

## Selection Criteria

### 1. Task Complexity

#### Simple Tasks (< 100 LOC, clear requirements)
**Characteristics**:
- Well-defined, pattern-based work
- Little ambiguity
- Straightforward implementation

**Recommended Models**:
- **Primary**: GPT-4o-mini, Claude Haiku
- **Cost**: $0.10-0.50 per task
- **Speed**: Fast

**Examples**:
- Add a new field to a form
- Create a simple CRUD endpoint
- Write basic documentation
- Add logging statements
- Simple CSS styling

---

#### Medium Tasks (100-500 LOC, moderate complexity)
**Characteristics**:
- Requires some design decisions
- Multiple components interact
- Some edge cases to consider

**Recommended Models**:
- **Primary**: GPT-4, Claude Sonnet 3.5
- **Cost**: $1-3 per task
- **Speed**: Moderate

**Examples**:
- User authentication flow
- Data validation with business rules
- API integration
- Component with complex state
- Database migration

---

#### Complex Tasks (> 500 LOC, high complexity)
**Characteristics**:
- Significant architectural decisions
- Many edge cases
- Requires deep reasoning
- Performance considerations

**Recommended Models**:
- **Primary**: Claude Sonnet 4+, o1-preview
- **Cost**: $5-15 per task
- **Speed**: Slower, but accurate

**Examples**:
- Design entire feature architecture
- Complex state management
- Performance optimization
- Security-critical code
- Algorithm implementation

---

### 2. Task Type Categories

#### Frontend Work

**UI Components (React/Vue/Angular)**
- **Model**: GPT-4
- **Why**: Excellent at component patterns, JSX, CSS-in-JS
- **Fallback**: Claude Sonnet 3.5

**State Management**
- **Model**: Claude Sonnet 4
- **Why**: Complex state logic requires reasoning
- **Fallback**: GPT-4

**Styling (CSS/Tailwind)**
- **Model**: GPT-4o-mini
- **Why**: CSS is well-defined, cost-effective choice
- **Fallback**: GPT-4

---

#### Backend Work

**API Endpoints (REST/GraphQL)**
- **Model**: Claude Sonnet 4
- **Why**: Business logic, validation, error handling
- **Fallback**: GPT-4

**Database Work**
- **Model**: Claude Sonnet 4
- **Why**: Strong SQL reasoning, schema design
- **Fallback**: GPT-4

**Authentication/Security**
- **Model**: Claude Sonnet 4
- **Why**: Security-critical, requires deep understanding
- **Fallback**: None (don't compromise on security)

---

#### Infrastructure/DevOps

**Terraform/CloudFormation**
- **Model**: Claude Sonnet 4
- **Why**: Complex IaC reasoning
- **Fallback**: GPT-4

**CI/CD Scripts**
- **Model**: GPT-4
- **Why**: Well-established patterns
- **Fallback**: Claude Sonnet 3.5

**Monitoring/Logging**
- **Model**: GPT-4o-mini
- **Why**: Straightforward instrumentation
- **Fallback**: GPT-4

---

#### Special Cases

**Refactoring Existing Code**
- **Model**: **Same model that wrote the original code**
- **Why**: Maintains consistency, understands context
- **Check**: Review .ai-metrics/ to find which model was used

**Bug Fixes**
- **Model**: **Same model that wrote the code** (if known)
- **Why**: Better context understanding
- **Fallback**: Claude Sonnet 4 (debugging reasoning)

**Documentation**
- **Model**: GPT-4o-mini
- **Why**: Cost-effective, good at writing
- **Fallback**: GPT-4

**Testing**
- **Model**: GPT-4
- **Why**: Strong at test patterns, edge cases
- **Fallback**: Claude Sonnet 3.5

---

### 3. Cost vs Quality Tradeoffs

#### Budget Tiers

**Tier 1: Cost-Optimized (Startup/Personal)**
- **Budget**: < $50/month
- **Strategy**: Use cheaper models, upgrade for critical tasks
- **Model Mix**:
  - 70% GPT-4o-mini
  - 20% GPT-4
  - 10% Claude Sonnet 4 (critical only)

**Tier 2: Balanced (Small Team)**
- **Budget**: $100-500/month
- **Strategy**: Match model to task complexity
- **Model Mix**:
  - 30% GPT-4o-mini (simple)
  - 40% GPT-4 (medium)
  - 30% Claude Sonnet 4 (complex)

**Tier 3: Quality-Focused (Enterprise)**
- **Budget**: > $500/month
- **Strategy**: Best model for each task
- **Model Mix**:
  - 10% GPT-4o-mini (docs/simple)
  - 30% GPT-4 (frontend/patterns)
  - 60% Claude Sonnet 4+ (everything else)

---

#### Cost Estimation

**Approximate Token Costs** (as of January 2026):

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Typical Task Cost |
|-------|---------------------|----------------------|------------------|
| GPT-4o-mini | $0.15 | $0.60 | $0.10-0.50 |
| GPT-4 | $2.50 | $10.00 | $1-3 |
| Claude Haiku | $0.25 | $1.25 | $0.10-0.50 |
| Claude Sonnet 3.5 | $3.00 | $15.00 | $1-3 |
| Claude Sonnet 4 | $3.00 | $15.00 | $2-5 |
| o1-preview | $15.00 | $60.00 | $10-20 |

**Note**: Prices change frequently. Check provider pricing pages for current rates.

**Estimating Task Cost**:
- Small task (~5k tokens total): $0.10-0.50 (GPT-4o-mini), $0.50-1.50 (GPT-4), $1-2 (Claude Sonnet)
- Medium task (~20k tokens): $0.50-1 (GPT-4o-mini), $2-5 (GPT-4), $3-8 (Claude Sonnet)
- Large task (~50k tokens): $1-2 (GPT-4o-mini), $5-15 (GPT-4), $10-20 (Claude Sonnet)

---

### 4. Language/Framework Specific

#### Python
- **General**: Claude Sonnet 4 (excellent Python reasoning)
- **Data Science/ML**: Claude Sonnet 4 (complex logic)
- **Scripts**: GPT-4o-mini (simple automation)

#### JavaScript/TypeScript
- **TypeScript types**: Claude Sonnet 4 (type reasoning)
- **React components**: GPT-4 (strong patterns)
- **Node.js backend**: Claude Sonnet 4 (async logic)
- **Simple JS**: GPT-4o-mini (straightforward)

#### Go
- **Recommended**: Claude Sonnet 4
- **Why**: Go's concurrency and interfaces require deep understanding

#### Rust
- **Recommended**: Claude Sonnet 4
- **Why**: Ownership model is complex, requires careful reasoning

#### SQL
- **Recommended**: Claude Sonnet 4
- **Why**: Strong SQL reasoning, query optimization

---

## Decision Framework

Use this flowchart to select a model:

```
1. Is this refactoring or fixing code AI wrote?
   YES → Use the same model that wrote it (check .ai-metrics/)
   NO → Continue to step 2

2. Is this security-critical or involves authentication?
   YES → Claude Sonnet 4 (no fallback)
   NO → Continue to step 3

3. What's the task complexity?
   SIMPLE (< 100 LOC) → GPT-4o-mini
   MEDIUM (100-500 LOC) → GPT-4 or Claude Sonnet 3.5
   COMPLEX (> 500 LOC) → Claude Sonnet 4+

4. What's the task type?
   UI/Frontend → GPT-4
   Backend/Logic → Claude Sonnet 4
   Database/SQL → Claude Sonnet 4
   Documentation → GPT-4o-mini
   Testing → GPT-4

5. Budget constraint?
   TIGHT → Downgrade by one tier (e.g., Sonnet → GPT-4 → GPT-4o-mini)
   NORMAL → Use recommended model
   UNLIMITED → Use best model (Claude Sonnet 4+)
```

---

## Recording Your Choice

In your task file (tasks/TASK_XXX.md):

```markdown
## AI Model Selection
- **Primary Model**: Claude Sonnet 4
- **Fallback Model**: GPT-4
- **Rationale**: Complex authentication logic with security implications. Requires deep reasoning (Complexity: High, Type: Backend/Security, Budget: Normal)
- **Task Complexity**: Complex
- **Task Type**: Backend/Security
- **Budget Constraint**: None
```

**Why document this?**
- Track what works for your project
- Analyze costs in .ai-metrics/
- Learn which models perform best for your use cases
- Maintain consistency (refactors use same model)

---

## Model Change Protocol

### When to Change Models Mid-Task

**Acceptable Reasons**:
- Primary model unavailable/rate limited
- Cost exceeded budget unexpectedly
- Model struggling with specific subtask (switch for that part)

**Document in .ai-metrics/**:
```markdown
## Model Change Log
- Started with: Claude Sonnet 4
- Switched to: GPT-4
- Reason: API rate limit hit
- At step: Database migration (step 3 of 5)
- Impact: Slight quality decrease, acceptable for this task
```

### When NOT to Change Models

❌ Don't switch just because:
- First attempt had bugs (debug, don't switch)
- You're impatient (better model takes time)
- Curious about other model (not during production work)

---

## Best Practices

### 1. Start Conservative, Upgrade if Needed
- Begin with recommended model from this guide
- If struggling, upgrade to next tier
- Document why you upgraded

### 2. Track Your Metrics
- Log actual model used in .ai-metrics/
- Note task completion time
- Estimate cost
- Assess quality (bugs found in review)
- **Learn your patterns**: Maybe GPT-4 works fine for your React work

### 3. Consistency for Related Tasks
- Use same model for entire feature (unless good reason)
- Definitely use same model for refactoring

### 4. Budget Management
- Set monthly budget
- Track spending in .ai-metrics/
- Alert at 80% budget consumed
- Have fallback strategy (use cheaper models)

### 5. Security-Critical Work
- Never compromise: Always use best model
- Claude Sonnet 4 minimum for auth/security
- Consider human security review in addition

---

## Examples

### Example 1: Simple Form Field Addition
```markdown
## AI Model Selection
- **Primary Model**: GPT-4o-mini
- **Fallback Model**: GPT-4
- **Rationale**: Adding a single email field to existing form. Well-established pattern, < 50 LOC (Complexity: Simple, Type: Frontend/UI, Budget: Cost-optimized)
- **Task Complexity**: Simple
- **Task Type**: Frontend/UI
- **Estimated Cost**: $0.20
```

### Example 2: Payment Integration
```markdown
## AI Model Selection
- **Primary Model**: Claude Sonnet 4
- **Fallback Model**: None (quality critical)
- **Rationale**: Stripe integration with webhook handling. Security-critical, complex error handling, transaction safety required (Complexity: Complex, Type: Backend/Security, Budget: Normal)
- **Task Complexity**: Complex
- **Task Type**: Backend/Security
- **Estimated Cost**: $5-8
```

### Example 3: Refactor Function
```markdown
## AI Model Selection
- **Primary Model**: Claude Sonnet 4 (same as original - see .ai-metrics/2025-12-15-task-003.md)
- **Fallback Model**: GPT-4
- **Rationale**: Refactoring calculateTotal() originally written by Claude Sonnet 4 in TASK_003. Maintaining context continuity (Complexity: Medium, Type: Refactoring)
- **Task Complexity**: Medium
- **Task Type**: Refactoring
```

---

## FAQ

**Q: Can I use different models for different parts of a task?**  
A: Yes, but document it clearly in .ai-metrics/. Keep it simple when possible.

**Q: What if my budget model struggles?**  
A: Upgrade to next tier for that task. Quality > cost for broken code.

**Q: How do I know which model wrote original code?**  
A: Check .ai-metrics/ session files. Search for the file/function name.

**Q: Should I always use the most expensive model?**  
A: No. Match model to task. Over-engineering costs add up. GPT-4o-mini handles many tasks perfectly.

**Q: What about new models (GPT-5, Claude Opus, etc.)?**  
A: Test them on non-critical tasks first. Update this guide based on results.

**Q: Can I automate model selection?**  
A: Partially. Use this guide as input to your choice. Some judgment always needed.

---

## Updating This Guide

This guide should evolve with your project:

1. **Track what works**: Note in ADRs or WORKING_STATE.md
2. **Update cost estimates**: Model pricing changes frequently
3. **Add project-specific guidance**: Your React work might differ from baseline
4. **Review quarterly**: Adjust based on metrics

**Template for project-specific additions**:
```markdown
## Project-Specific Model Guidance (Our Project)

Based on 3 months of metrics:

- Our React components: GPT-4 works perfectly (90% success rate)
- Our Python backend: Claude Sonnet 4 required (GPT-4 struggled with our patterns)
- Cost savings: Switching docs to GPT-4o-mini saved $30/month
```

---

## Related Documentation

- See: `docs/AI_WORKFLOW_GUIDE.md` - For when to use which model in each workflow phase
- See: `.ai-metrics/README.md` - For tracking actual model usage and costs
- See: `tasks/TASK_TEMPLATE.md` - For documenting model selection in tasks
- See: `docs/decisions/0002-ai-model-selection.md` - For the ADR on model selection strategy

---

**Last Updated**: January 2026  
**Next Review**: April 2026
