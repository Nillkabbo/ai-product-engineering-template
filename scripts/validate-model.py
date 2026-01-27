#!/usr/bin/env python3
"""
Validate model consistency between task files and metrics.

This script checks that the AI model used in execution matches
the model specified in the task file (or fallback).

Usage:
    python scripts/validate-model.py
    python scripts/validate-model.py tasks/TASK_001.md  # Check specific task
"""

import sys
import re
from pathlib import Path


def extract_task_model(task_file_path):
    """Extract model configuration from task file."""
    try:
        with open(task_file_path, "r") as f:
            content = f.read()

        # Extract primary and fallback models
        primary_match = re.search(r"\*\*Primary Model\*\*:\s*\[(.*?)\]", content)
        fallback_match = re.search(r"\*\*Fallback Model\*\*:\s*\[(.*?)\]", content)

        if not primary_match:
            return None

        return {
            "primary": primary_match.group(1).strip() if primary_match else None,
            "fallback": fallback_match.group(1).strip() if fallback_match else None,
        }

    except Exception:
        return None


def extract_metrics_model(metrics_file_path):
    """Extract actual model used from metrics file."""
    try:
        with open(metrics_file_path, "r") as f:
            content = f.read()

        # Extract actual model name
        model_match = re.search(r"\*\*Model Name\*\*:\s*\[(.*?)\]", content)
        match_status = re.search(r"\*\*Model Match\*\*:\s*\[(.*?)\]", content)

        return {
            "model": model_match.group(1).strip() if model_match else None,
            "match_status": match_status.group(1).strip() if match_status else None,
        }

    except Exception:
        return None


def find_metrics_for_task(task_file_path, project_root="."):
    """Find corresponding metrics file for a task."""
    task_id = Path(task_file_path).stem.lower().replace("_", "-")
    metrics_dir = Path(project_root) / ".ai-metrics"

    if not metrics_dir.exists():
        return None

    # Look for metrics file with task ID
    metrics_files = list(metrics_dir.glob(f"*-{task_id}.md"))

    if metrics_files:
        # Return most recent if multiple
        return max(metrics_files, key=lambda p: p.stat().st_mtime)

    return None


def validate_model_match(task_model, metrics_model):
    """Validate that models match."""
    if not task_model or not metrics_model:
        return {"valid": False, "reason": "Missing model information"}

    actual_model = metrics_model["model"]

    if not actual_model or actual_model.startswith("["):
        return {"valid": None, "reason": "Metrics not filled yet"}

    # Check if matches primary
    if task_model["primary"] and task_model["primary"].lower() in actual_model.lower():
        return {
            "valid": True,
            "match_type": "primary",
            "reason": f"Matches primary model: {task_model['primary']}",
        }

    # Check if matches fallback
    if (
        task_model["fallback"]
        and task_model["fallback"].lower() in actual_model.lower()
    ):
        return {
            "valid": True,
            "match_type": "fallback",
            "reason": f"Using fallback model: {task_model['fallback']}",
        }

    # Mismatch
    return {
        "valid": False,
        "match_type": "mismatch",
        "reason": f"Model '{actual_model}' doesn't match primary '{task_model['primary']}' or fallback '{task_model['fallback']}'",
    }


def validate_single_task(task_file, project_root="."):
    """Validate a single task's model consistency."""
    print(f"🔍 Validating: {task_file}")

    # Extract task model
    task_model = extract_task_model(task_file)
    if not task_model or not task_model["primary"]:
        print(f"   ⚠️  Could not extract model from task file")
        return False

    print(f"   Expected: {task_model['primary']} (fallback: {task_model['fallback']})")

    # Find metrics file
    metrics_file = find_metrics_for_task(task_file, project_root)
    if not metrics_file:
        print(f"   ⏳ No metrics file found (task not started or metrics not tracked)")
        return None

    print(f"   Metrics: {metrics_file.name}")

    # Extract metrics model
    metrics_model = extract_metrics_model(metrics_file)
    if not metrics_model or not metrics_model["model"]:
        print(f"   ⏳ Metrics file exists but model not filled yet")
        return None

    print(f"   Actual: {metrics_model['model']}")

    # Validate
    validation = validate_model_match(task_model, metrics_model)

    if validation["valid"] is None:
        print(f"   ⏳ {validation['reason']}")
        return None
    elif validation["valid"]:
        if validation["match_type"] == "primary":
            print(f"   ✅ {validation['reason']}")
        else:
            print(f"   ⚠️  {validation['reason']}")
        return True
    else:
        print(f"   ❌ {validation['reason']}")
        return False


def validate_all_tasks(project_root="."):
    """Validate all tasks in the project."""
    tasks_dir = Path(project_root) / "tasks"

    if not tasks_dir.exists():
        print("No tasks directory found")
        return []

    task_files = sorted(tasks_dir.glob("TASK_*.md"))

    if not task_files:
        print("No task files found")
        return []

    results = []
    for task_file in task_files:
        result = validate_single_task(task_file, project_root)
        results.append({"file": task_file.name, "result": result})
        print()

    return results


def main():
    if len(sys.argv) > 1:
        # Validate specific task
        task_file = sys.argv[1]
        result = validate_single_task(task_file, ".")

        if result is False:
            sys.exit(1)
        else:
            sys.exit(0)

    else:
        # Validate all tasks
        print("🔍 Validating model consistency for all tasks...")
        print()

        results = validate_all_tasks(".")

        if not results:
            print("No tasks to validate")
            sys.exit(0)

        # Summary
        print("=" * 60)
        print("Summary:")

        valid = [r for r in results if r["result"] is True]
        invalid = [r for r in results if r["result"] is False]
        pending = [r for r in results if r["result"] is None]

        print(f"  ✅ Valid: {len(valid)}")
        print(f"  ❌ Invalid: {len(invalid)}")
        print(f"  ⏳ Pending: {len(pending)}")

        if invalid:
            print()
            print("⚠️  Model mismatches found:")
            for r in invalid:
                print(f"     - {r['file']}")
            print()
            print("Action required:")
            print("  1. Check .ai-metrics/ files for these tasks")
            print("  2. If model change was intentional, document rationale")
            print("  3. If unintentional, consider re-running with correct model")
            print()
            print("See: docs/MODEL_SELECTION_GUIDE.md for model selection guidelines")

            sys.exit(1)
        else:
            print()
            print("✅ All validated tasks use correct models!")
            sys.exit(0)


if __name__ == "__main__":
    main()
