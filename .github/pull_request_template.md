## Summary
[Brief description of changes]

## Task Reference
- **Task File**: tasks/[TASK_XXX.md]
- **Related ADR**: docs/decisions/[0XXX-xxx.md] (if applicable)
- **Phase**: [ ] Design [ ] Planning [x] Execution

## AI Model Configuration
- **Primary Model** (from task): [e.g., Claude Sonnet 4]
- **Actual Model Used**: [e.g., Claude Sonnet 4.5]
- **Model Match**: [✅ Match / ⚠️ Fallback / ❌ Mismatch]
- **Metrics File**: .ai-metrics/[YYYY-MM-DD-task-xxx.md]

### Model Change Rationale (if ⚠️ or ❌)
[Explain why a different model was used]

## Changes
[Detailed description of what was changed and why]

## Testing
- [ ] All tests pass locally
- [ ] New tests added for new functionality
- [ ] Manual testing completed
- [ ] Edge cases covered

## Acceptance Criteria
[Copy from task file and check off]
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

## Architecture Compliance
- [ ] ARCHITECTURE.md not violated
- [ ] Follows established patterns and conventions
- [ ] Minimal diff principle followed
- [ ] No unauthorized refactoring

## Documentation
- [ ] WORKING_STATE.md updated
- [ ] ADR created (if architectural decision made)
- [ ] AI metrics logged in .ai-metrics/
- [ ] Code comments added where needed
- [ ] README updated (if public API changed)

## Human Review Checklist
**For Reviewer**: Check these before approving

### Code Quality
- [ ] Code is readable and maintainable
- [ ] No code smells or anti-patterns
- [ ] Error handling is appropriate
- [ ] No security concerns
- [ ] Performance is acceptable

### Testing
- [ ] Tests are comprehensive
- [ ] Tests actually test the right things
- [ ] No flaky tests
- [ ] Coverage is adequate

### Compliance
- [ ] ARCHITECTURE.md not violated
- [ ] Task acceptance criteria met
- [ ] Minimal diff (no unnecessary changes)
- [ ] Dependencies properly managed

## Approval
**To be filled by reviewer**:

- **Reviewer**: [Name]
- **Date**: [YYYY-MM-DD]
- **Status**: [ ] ✅ Approved [ ] 🔄 Needs Revision [ ] ❌ Rejected

### Review Notes
[Feedback, concerns, or praise]
