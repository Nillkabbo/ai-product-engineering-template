#!/usr/bin/env python3
"""
Check current workflow phase (Design/Planning/Execution).

This script determines the current phase based on approval signatures
in key documents.

Usage:
    python scripts/check-phase.py
"""

import sys
import re
from pathlib import Path


def check_approval_signature(file_path):
    """Check if document has human approval signature."""
    try:
        if not Path(file_path).exists():
            return False, "File not found"

        with open(file_path, "r") as f:
            content = f.read()

        # Look for approval section with status
        approval_match = re.search(
            r"\*\*Status\*\*:\s*\[?(✅ Approved|⏳ In Review|🔄 Needs Revision|❌ Rejected)",
            content,
        )

        if approval_match:
            status = approval_match.group(1)
            is_approved = status == "✅ Approved"
            return is_approved, status

        return False, "No approval section found"

    except Exception as e:
        return False, f"Error: {e}"


def get_current_phase(project_root="."):
    """Detect current workflow phase based on approvals."""
    arch_file = Path(project_root) / "docs" / "ARCHITECTURE.md"
    plan_file = Path(project_root) / "docs" / "EXECUTION_PLAN.md"

    arch_approved, arch_status = check_approval_signature(arch_file)
    plan_approved, plan_status = check_approval_signature(plan_file)

    if not arch_approved:
        return {
            "phase": "DESIGN",
            "description": "Architecture design and approval",
            "next_step": "Complete and approve ARCHITECTURE.md",
            "arch_status": arch_status,
            "plan_status": "N/A (not yet relevant)",
        }
    elif not plan_approved:
        return {
            "phase": "PLANNING",
            "description": "Task planning and breakdown",
            "next_step": "Complete and approve EXECUTION_PLAN.md",
            "arch_status": arch_status,
            "plan_status": plan_status,
        }
    else:
        return {
            "phase": "EXECUTION",
            "description": "Task execution and implementation",
            "next_step": "Execute tasks from EXECUTION_PLAN.md",
            "arch_status": arch_status,
            "plan_status": plan_status,
        }


def main():
    print("🔍 Checking current workflow phase...")
    print()

    phase_info = get_current_phase(".")

    print(f"📍 Current Phase: {phase_info['phase']}")
    print(f"   Description: {phase_info['description']}")
    print()
    print("📋 Approval Status:")
    print(f"   ARCHITECTURE.md: {phase_info['arch_status']}")
    print(f"   EXECUTION_PLAN.md: {phase_info['plan_status']}")
    print()
    print(f"➡️  Next Step: {phase_info['next_step']}")
    print()

    if phase_info["phase"] == "DESIGN":
        print("💡 Design Phase Actions:")
        print("   1. Fill PRODUCT_VISION.md with requirements")
        print("   2. Use AI to draft ARCHITECTURE.md")
        print("   3. Create ADRs for significant decisions")
        print("   4. Get human approval for architecture")
        print()
        print("   See: docs/AI_WORKFLOW_GUIDE.md#phase-1-design")

    elif phase_info["phase"] == "PLANNING":
        print("💡 Planning Phase Actions:")
        print("   1. Use AI to create EXECUTION_PLAN.md")
        print("   2. Generate task files for each task")
        print("   3. Select appropriate model for each task")
        print("   4. Get human approval for plan")
        print()
        print("   See: docs/AI_WORKFLOW_GUIDE.md#phase-2-planning")

    elif phase_info["phase"] == "EXECUTION":
        print("💡 Execution Phase Actions:")
        print("   1. Pick a task from EXECUTION_PLAN.md")
        print("   2. Run: python scripts/sync-model-config.py tasks/TASK_XXX.md")
        print("   3. Execute task with AI using recommended model")
        print("   4. Create PR and get human approval")
        print("   5. Update WORKING_STATE.md")
        print()
        print("   See: docs/AI_WORKFLOW_GUIDE.md#phase-3-execution")

    # Exit code: 0 for EXECUTION, 1 for DESIGN, 2 for PLANNING
    exit_codes = {"DESIGN": 1, "PLANNING": 2, "EXECUTION": 0}
    sys.exit(exit_codes.get(phase_info["phase"], 3))


if __name__ == "__main__":
    main()
