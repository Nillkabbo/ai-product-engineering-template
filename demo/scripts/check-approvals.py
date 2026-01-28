#!/usr/bin/env python3
"""
Check approval status of all key documents and tasks.

This script validates that appropriate approvals are in place
for the current workflow phase.

Usage:
    python scripts/check-approvals.py
    python scripts/check-approvals.py --strict  # Fail if any approval missing
"""

import sys
import re
from pathlib import Path


def check_approval_in_file(file_path, doc_type="document"):
    """Check if a file has proper approval signature."""
    try:
        if not Path(file_path).exists():
            return {
                "exists": False,
                "approved": False,
                "status": "File not found",
                "reviewer": None,
                "date": None,
            }

        with open(file_path, "r") as f:
            content = f.read()

        # Look for approval section
        approval_section = re.search(
            r"\*\*Reviewer\*\*:\s*\[(.*?)\].*?"
            r"\*\*Date\*\*:\s*\[(.*?)\].*?"
            r"\*\*Status\*\*:\s*\[?(✅ Approved|⏳ In Review|🔄 Needs Revision|❌ Rejected)",
            content,
            re.DOTALL,
        )

        if approval_section:
            reviewer = approval_section.group(1).strip()
            date = approval_section.group(2).strip()
            status = approval_section.group(3).strip()

            return {
                "exists": True,
                "approved": status == "✅ Approved",
                "status": status,
                "reviewer": reviewer if reviewer else "Not specified",
                "date": date if date else "Not specified",
            }

        return {
            "exists": True,
            "approved": False,
            "status": "No approval section",
            "reviewer": None,
            "date": None,
        }

    except Exception as e:
        return {
            "exists": False,
            "approved": False,
            "status": f"Error: {e}",
            "reviewer": None,
            "date": None,
        }


def check_architecture_approval(project_root="."):
    """Check ARCHITECTURE.md approval."""
    arch_file = Path(project_root) / "docs" / "ARCHITECTURE.md"
    return check_approval_in_file(arch_file, "ARCHITECTURE.md")


def check_execution_plan_approval(project_root="."):
    """Check EXECUTION_PLAN.md approval."""
    plan_file = Path(project_root) / "docs" / "EXECUTION_PLAN.md"
    return check_approval_in_file(plan_file, "EXECUTION_PLAN.md")


def check_task_approvals(project_root="."):
    """Check all task file approvals."""
    tasks_dir = Path(project_root) / "tasks"

    if not tasks_dir.exists():
        return []

    task_files = list(tasks_dir.glob("TASK_*.md"))
    results = []

    for task_file in sorted(task_files):
        approval = check_approval_in_file(task_file, "task")
        results.append({"file": task_file.name, "path": str(task_file), **approval})

    return results


def get_adrs(project_root="."):
    """Get all ADR files."""
    adr_dir = Path(project_root) / "docs" / "decisions"

    if not adr_dir.exists():
        return []

    # Skip template and README
    adr_files = [
        f for f in adr_dir.glob("*.md") if f.name not in ["template.md", "README.md"]
    ]

    return sorted(adr_files)


def print_status_symbol(approved):
    """Return status symbol."""
    return "✅" if approved else "⚠️ "


def main():
    strict_mode = "--strict" in sys.argv

    print("🔍 Checking approval status...")
    print()

    # Check architecture
    print("📐 ARCHITECTURE.md")
    arch_approval = check_architecture_approval(".")
    if arch_approval["exists"]:
        symbol = print_status_symbol(arch_approval["approved"])
        print(f"   {symbol} Status: {arch_approval['status']}")
        if arch_approval["reviewer"]:
            print(f"   Reviewer: {arch_approval['reviewer']}")
            print(f"   Date: {arch_approval['date']}")
    else:
        print(f"   ⚠️  {arch_approval['status']}")
    print()

    # Check execution plan
    print("📋 EXECUTION_PLAN.md")
    plan_approval = check_execution_plan_approval(".")
    if plan_approval["exists"]:
        symbol = print_status_symbol(plan_approval["approved"])
        print(f"   {symbol} Status: {plan_approval['status']}")
        if plan_approval["reviewer"]:
            print(f"   Reviewer: {plan_approval['reviewer']}")
            print(f"   Date: {plan_approval['date']}")
    else:
        print(f"   ⚠️  {plan_approval['status']}")
    print()

    # Check ADRs
    adrs = get_adrs(".")
    print(f"📝 Architecture Decision Records ({len(adrs)} ADRs)")
    if adrs:
        for adr in adrs:
            print(f"   - {adr.name}")
    else:
        print("   No ADRs found (beyond template defaults)")
    print()

    # Check tasks
    task_approvals = check_task_approvals(".")
    print(f"✅ Task Approvals ({len(task_approvals)} tasks)")

    if not task_approvals:
        print("   No task files found yet")
    else:
        approved_count = sum(1 for t in task_approvals if t["approved"])
        pending_count = len(task_approvals) - approved_count

        print(f"   Approved: {approved_count}")
        print(f"   Pending: {pending_count}")
        print()

        for task in task_approvals:
            symbol = print_status_symbol(task["approved"])
            print(f"   {symbol} {task['file']}: {task['status']}")
            if task["reviewer"]:
                print(f"      Reviewer: {task['reviewer']} on {task['date']}")

    print()
    print("=" * 60)

    # Summary
    all_approved = (
        arch_approval["approved"]
        and plan_approval["approved"]
        and all(t["approved"] for t in task_approvals if t["exists"])
    )

    if all_approved:
        print("✅ All approvals in place!")
    else:
        print("⚠️  Some approvals pending")
        print()
        print("Pending approvals:")

        if not arch_approval["approved"]:
            print("   - ARCHITECTURE.md needs approval")

        if not plan_approval["approved"]:
            print("   - EXECUTION_PLAN.md needs approval")

        pending_tasks = [t for t in task_approvals if t["exists"] and not t["approved"]]
        if pending_tasks:
            print(f"   - {len(pending_tasks)} task(s) need approval:")
            for task in pending_tasks[:5]:  # Show first 5
                print(f"     • {task['file']}")
            if len(pending_tasks) > 5:
                print(f"     ... and {len(pending_tasks) - 5} more")

    print()
    print("See: docs/APPROVAL_GATES.md for complete approval tracking")

    # Exit code
    if strict_mode and not all_approved:
        print()
        print("❌ Strict mode: Failing due to missing approvals")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
