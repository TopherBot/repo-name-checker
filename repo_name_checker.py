#!/usr/bin/env python3
"""
repo-name-checker – Tiny CLI to validate GitHub repository names.

Author: TopherBot <topherbot@proton.me>
License: MIT
"""

import sys
import urllib.request
import json
from urllib.error import HTTPError

API_URL_TEMPLATE = "https://api.github.com/repos/{owner}/{repo}"  # GitHub REST API


def check_repo_availability(owner: str, repo: str) -> bool:
    """Return True if the repository name is **available** (i.e., does NOT exist)."""
    url = API_URL_TEMPLATE.format(owner=owner, repo=repo)
    request = urllib.request.Request(url, method='HEAD')  # HEAD is sufficient
    try:
        with urllib.request.urlopen(request) as response:
            # If we get a 200, the repo exists → not available
            return False
    except HTTPError as e:
        # 404 means not found → available
        if e.code == 404:
            return True
        # Any other HTTP error is treated as unknown; re‑raise for visibility
        raise
    except Exception as exc:
        print(f"⚠️ Unexpected error: {exc}", file=sys.stderr)
        raise


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if len(argv) != 2:
        print("Usage: python repo_name_checker.py <owner> <repo-name>")
        sys.exit(1)

    owner, repo = argv
    try:
        available = check_repo_availability(owner, repo)
        if available:
            print(f"✅ The repository name \"{repo}\" is available under \"{owner}\".")
        else:
            print(f"❌ The repository name \"{repo}\" already exists under \"{owner}\".")
    except HTTPError as http_err:
        print(f"🚨 HTTP error {http_err.code}: {http_err.reason}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"🚨 Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
