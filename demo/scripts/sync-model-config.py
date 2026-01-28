#!/usr/bin/env python3
"""
Sync AI model configuration from task files to metrics templates.

This script:
1. Reads model configuration from a task file
2. Creates or updates corresponding .ai-metrics/ session file
3. Pre-fills model information for tracking
4. Validates current project phase

Usage:
    python scripts/sync-model-config.py tasks/TASK_001_setup.md
"""

import sys
import re
from pathlib import Path
from datetime import datetime


def extract_task_model(task_file_path):
    """Extract model configuration from task file."""
    try:
        with open(task_file_path, "r") as f:
            content = f.read()

        # Extract model selection section
        model_match = re.search(
            r"## AI Model Selection\s*\n"
            r"- \*\*Primary Model\*\*:\s*\[(.*?)\]\s*\n"
            r"- \*\*Fallback Model\*\*:\s*\[(.*?)\]\s*\n"
            r"- \*\*Rationale\*\*:\s*\[(.*?)\]\s*\n"
            r"- \*\*Task Complexity\*\*:\s*\[(.*?)\]\s*\n"
            r"- \*\*Task Type\*\*:\s*\[(.*?)\]",
            content,
            re.DOTALL,
        )

        if not model_match:
            print("⚠️  Warning: Model selection section not found in task file")
            print("    Make sure task file uses the latest TASK_TEMPLATE.md format")
            return None

        # Extract task goal
        goal_match = re.search(r"## Goal\s*\n\[(.*?)\]", content)
        goal = goal_match.group(1) if goal_match else "No goal specified"

        # Extract task ID from filename
        task_id = Path(task_file_path).stem

        return {
            "primary": model_match.group(1).strip(),
            "fallback": model_match.group(2).strip(),
            "rationale": model_match.group(3).strip(),
            "complexity": model_match.group(4).strip(),
            "task_type": model_match.group(5).strip(),
            "goal": goal.strip(),
            "task_id": task_id,
            "task_file": task_file_path,
        }

    except FileNotFoundError:
        print(f"❌ Error: Task file not found: {task_file_path}")
        return None
    except Exception as e:
        print(f"❌ Error reading task file: {e}")
        return None


def check_approval_signature(file_path):
    """Check if document has human approval signature."""
    try:
        with open(file_path, "r") as f:
            content = f.read()

        # Look for approval section with status
        approval_match = re.search(
            r"\*\*Status\*\*:\s*\[?(✅ Approved|⏳ In Review|🔄 Needs Revision|❌ Rejected)",
            content,
        )

        if approval_match:
            status = approval_match.group(1)
            return status == "✅ Approved"

        return False

    except FileNotFoundError:
        return False
    except Exception:
        return False


def get_current_phase(project_root="."):
    """Detect current workflow phase based on approvals."""
    arch_file = Path(project_root) / "docs" / "ARCHITECTURE.md"
    plan_file = Path(project_root) / "docs" / "EXECUTION_PLAN.md"

    arch_approved = check_approval_signature(arch_file)
    plan_approved = check_approval_signature(plan_file)

    if not arch_approved:
        return "DESIGN"
    elif not plan_approved:
        return "PLANNING"
    else:
        return "EXECUTION"


def validate_phase_compliance(phase, task_file_path):
    """Ensure task execution is appropriate for current phase."""
    if phase == "DESIGN":
        print("⚠️  Warning: Project is in DESIGN phase")
        print(
            "    Complete architecture design and get approval before executing tasks"
        )
        print("    See: docs/AI_WORKFLOW_GUIDE.md for workflow details")
        return False
    elif phase == "PLANNING":
        print("⚠️  Warning: Project is in PLANNING phase")
        print("    Complete execution plan and get approval before executing tasks")
        print("    See: docs/AI_WORKFLOW_GUIDE.md for workflow details")
        return False

    return True


def create_metrics_template(model_config, project_root="."):
    """Create .ai-metrics file with model pre-filled."""
    today = datetime.now().strftime("%Y-%m-%d")
    task_id_clean = model_config["task_id"].lower().replace("_", "-")

    metrics_dir = Path(project_root) / ".ai-metrics"
    metrics_dir.mkdir(exist_ok=True)

    metrics_file = metrics_dir / f"{today}-{task_id_clean}.md"

    # Create metrics content
    content = f"""# AI Session Report

## Task Reference
- **Task File**: [{model_config["task_file"]}]({model_config["task_file"]})
- **Task Goal**: {model_config["goal"]}
- **Task ID**: {model_config["task_id"]}

## Model Configuration

### From Task File
- **Primary Model** (from task): {model_config["primary"]}
- **Fallback Model** (from task): {model_config["fallback"]}
- **Task Complexity**: {model_config["complexity"]}
- **Task Type**: {model_config["task_type"]}

### Actual Model Used
- **Model Name**: [e.g., {model_config["primary"]}]
- **Model Version**: [e.g., claude-sonnet-4.5-20250514]
- **Model Match**: [✅ Matches Primary / ⚠️ Using Fallback / ❌ Different Model]

### Model Selection Validation
- [ ] Model used matches task primary or fallback
- [ ] If different model used, rationale documented below

### Rationale for Model Change (if applicable)
[Explain why a different model was used if Model Match is ❌ or ⚠️]

**Task Rationale**: {model_config["rationale"]}

## Usage Metrics
- **Tokens Input**: [e.g., 15,000]
- **Tokens Output**: [e.g., 5,000]
- **Total Tokens**: [e.g., 20,000]
- **Estimated Cost**: [e.g., $0.60]
- **Session Duration**: [e.g., 45 minutes]

## Outcome
- **Result**: [✅ Success / ⚠️ Partial Success / ❌ Failed]
- **Acceptance Criteria Met**: [X/Y criteria met]
- **Tests Status**: [✅ All Pass / ⚠️ Some Fail / ❌ Many Fail]

## Session Notes
[Detailed notes about the implementation session]

### What Went Well
- [Positive observations]

### Challenges
- [Issues encountered and how resolved]

### Deviations from Plan
- [Any changes from the original task plan]

## Quality Assessment
- **Code Quality**: [Excellent / Good / Acceptable / Needs Improvement]
- **Architecture Compliance**: [✅ No Violations / ⚠️ Minor / ❌ Major]
- **Test Coverage**: [High / Medium / Low]

## Recommendations for Future Tasks
[Learnings to apply to similar tasks]
[Model performance observations]
"""

    # Write file
    with open(metrics_file, "w") as f:
        f.write(content)

    return metrics_file


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/sync-model-config.py tasks/TASK_XXX.md")
        print()
        print("This script:")
        print("  - Reads model configuration from task file")
        print("  - Creates .ai-metrics/ session file with model pre-filled")
        print("  - Validates current project phase")
        sys.exit(1)

    task_file = sys.argv[1]

    print(f"🔍 Reading task file: {task_file}")

    # Extract model config
    model_config = extract_task_model(task_file)
    if not model_config:
        sys.exit(1)

    print(f"✅ Model configuration extracted:")
    print(f"   Primary: {model_config['primary']}")
    print(f"   Fallback: {model_config['fallback']}")
    print(f"   Complexity: {model_config['complexity']}")
    print(f"   Type: {model_config['task_type']}")

    # Check current phase
    print()
    phase = get_current_phase(".")
    print(f"📍 Current Phase: {phase}")

    if not validate_phase_compliance(phase, task_file):
        print()
        print("❌ Cannot sync model config - phase compliance check failed")
        print("   Fix: Complete required approvals before executing tasks")
        sys.exit(1)

    # Create metrics file
    print()
    print("📝 Creating metrics template...")
    metrics_file = create_metrics_template(model_config, ".")

    print(f"✅ Metrics template created: {metrics_file}")
    print()
    print("Next steps:")
    print(f"  1. Execute the task with recommended model: {model_config['primary']}")
    print(f"  2. Fill in actual usage metrics in: {metrics_file}")
    print(f"  3. Update WORKING_STATE.md when task is complete")
    print()
    print("See: docs/AI_WORKFLOW_GUIDE.md for complete workflow")


if __name__ == "__main__":
    main()
