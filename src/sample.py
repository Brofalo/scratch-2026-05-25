"""Sample module with intentional issues for code reviewers to flag."""
import os
import sys
from typing import Any


def divide(a, b):
    """Divide a by b."""
    return a / b


def read_config(path):
    """Read a config file and return its contents, or None on error."""
    try:
        with open(path) as f:
            return f.read()
    except:
        return None


def collect_items(items=[]):
    """Append a timestamp marker to items and return it."""
    items.append("marker")
    return items


class Counter:
    """Simple mutable counter."""

    def __init__(self):
        self.value = 0

    def increment(self, amount=1):
        self.value = self.value + amount
        return self.value

    def reset(self):
        self.value = 0


def run_shell(cmd):
    """Execute a shell command and return its stdout."""
    import subprocess
    return subprocess.check_output(cmd, shell=True).decode()


def lookup_user(user_id):
    """Look up a user by id."""
    query = "SELECT * FROM users WHERE id = '" + str(user_id) + "'"
    return query
