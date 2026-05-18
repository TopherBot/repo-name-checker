# Repo Name Checker

A **tiny** utility written in Python that validates whether a repository name is already taken on GitHub for a specific user or organization. Perfect for developers who want to pre‑validate repo names before initializing a new project.

## Features
- Instant scaffolding: just run the script and get an immediate yes/no answer.
- Supports personal user accounts and organizations.
- No external dependencies beyond the Python standard library.

## Usage
```bash
python repo_name_checker.py <owner> <repo-name>
```
- `<owner>` – GitHub username or organization name.
- `<repo-name>` – Desired repository name you want to check.

### Example
```bash
$ python repo_name_checker.py octocat hello-world
✅ The repository name "hello-world" is available under "octocat".
```

If the name is taken:
```bash
$ python repo_name_checker.py octocat hello-world
❌ The repository name "hello-world" already exists under "octocat".
```

## Why this tiny tool?
- **Pre‑validation of repo names** saves you time and prevents duplicate creation errors.
- **No idle periods** – instant feedback.
- **Lightweight** – no need for a full CI pipeline for a simple check.

## License
MIT © 2026 TopherBot

---
*Created with a love for proactive external assistance and a dislike for duplicate repository names.*