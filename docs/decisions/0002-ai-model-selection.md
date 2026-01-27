# ADR 0002: AI Model Selection Strategy

## Status
Accepted

## Context
Different AI models are better suited to different tasks. Model selection affects cost, quality, and development speed. We need a systematic approach to choosing models.

## Decision
1. Document primary and fallback models in each task file
2. Follow MODEL_SELECTION_GUIDE.md for model selection criteria
3. Track actual model usage in .ai-metrics/ for each session
4. Validate model consistency via automated scripts and GitHub Actions
5. Require documented rationale when deviating from recommended models

## Implementation

### Model Selection
- See: `docs/MODEL_SELECTION_GUIDE.md` for detailed selection criteria
- Task files specify primary and fallback models with rationale
- Selection based on: complexity, task type, and budget constraints

### Tracking
- Actual model used logged in `.ai-metrics/YYYY-MM-DD-task-xxx.md`
- Track tokens, cost, and session duration
- Compare recommended vs actual model performance

### Validation
- Script: `scripts/sync-model-config.py` - Auto-creates metrics template from task
- Script: `scripts/validate-model.py` - Validates model consistency
- GitHub Action: `.github/workflows/model-validation.yml` - CI validation
- Warning-only (not blocking) to maintain flexibility

### Workflow Integration
- Design phase: Select models for implementation tasks
- Planning phase: Document model choice in each task file
- Execution phase: Use recommended model, track in metrics

## Consequences

### Positive
- Model choices are transparent and justified
- Easy to analyze which models work best for our project
- Cost tracking enables budget management
- Team learns optimal model selection over time
- Consistency in model usage across similar tasks

### Negative
- Additional overhead in task planning
- Need to maintain MODEL_SELECTION_GUIDE.md as models evolve
- Metrics tracking requires discipline

### Neutral
- Team must learn model characteristics and strengths
- Periodic review needed to update model recommendations

## References
- Task template: `tasks/TASK_TEMPLATE.md`
- Model selection guide: `docs/MODEL_SELECTION_GUIDE.md`
- AI workflow guide: `docs/AI_WORKFLOW_GUIDE.md`
- Metrics template: `.ai-metrics/session-template.md`
- Validation script: `scripts/validate-model.py`
