#!/usr/bin/env python3
"""
Task Timer CLI - A simple time tracking tool for developers.
Version: 0.1.0
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path


class TaskTimer:
    """Manages time tracking for tasks."""

    def __init__(self, data_dir=None):
        """Initialize the task timer with a data directory."""
        if data_dir is None:
            data_dir = Path.home() / ".task-timer"
        self.data_dir = Path(data_dir)
        self.data_file = self.data_dir / "data.json"
        self._ensure_data_dir()

    def _ensure_data_dir(self):
        """Create data directory if it doesn't exist."""
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def _load_data(self):
        """Load data from JSON file."""
        if not self.data_file.exists():
            return {"entries": [], "active": None}

        try:
            with open(self.data_file, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}", file=sys.stderr)
            return {"entries": [], "active": None}

    def _save_data(self, data):
        """Save data to JSON file."""
        try:
            with open(self.data_file, "w") as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}", file=sys.stderr)
            sys.exit(1)

    def start(self, task_name):
        """Start a new timer for a task."""
        data = self._load_data()

        if data["active"] is not None:
            print(f"Error: Timer already active for '{data['active']['task']}'")
            print("Please stop the current timer first.")
            sys.exit(1)

        data["active"] = {"task": task_name, "start": datetime.now().isoformat()}

        self._save_data(data)
        print(f"Timer started for: {task_name}")

    def stop(self):
        """Stop the active timer."""
        data = self._load_data()

        if data["active"] is None:
            print("Error: No active timer")
            sys.exit(1)

        end_time = datetime.now()
        start_time = datetime.fromisoformat(data["active"]["start"])
        duration = (end_time - start_time).total_seconds()

        entry = {
            "task": data["active"]["task"],
            "start": data["active"]["start"],
            "end": end_time.isoformat(),
            "duration": duration,
        }

        data["entries"].append(entry)
        data["active"] = None

        self._save_data(data)

        hours = int(duration // 3600)
        minutes = int((duration % 3600) // 60)
        seconds = int(duration % 60)

        print(f"Timer stopped for: {entry['task']}")
        print(f"Duration: {hours:02d}:{minutes:02d}:{seconds:02d}")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Task Timer CLI - Track time spent on tasks"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Start command
    start_parser = subparsers.add_parser("start", help="Start a new timer")
    start_parser.add_argument("task", help="Task name or description")

    # Stop command
    subparsers.add_parser("stop", help="Stop the active timer")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    timer = TaskTimer()

    if args.command == "start":
        timer.start(args.task)
    elif args.command == "stop":
        timer.stop()


if __name__ == "__main__":
    main()
