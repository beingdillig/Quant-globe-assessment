# AGENT_DESIGN.md

## Agent Purpose

This is an autonomous agent which is designed to search for GitHub users based on specific queries and identify qualified users who meet certain criteria related to stars, commits, language, and keywords by evaluating their repositories.

## Workflow

The agent task is divided into 4 steps:

1. **search_user**

   - Queries GitHub users using filters like `repos:>2`, `language:Python`, and `followers:>5`.
   - Stores each unique username and profile URL.

2. **get_repos**

   - For each user, fetches all public repositories (including pagination).
   - Repositories are stored per user for evaluation.

3. **evaluate_user**

   - Repositories are filtered by language (Python/C++).
   - Criteria for qualification:
     - At least **2 Python/C++ repos**
     - Contains any of the keywords: `['backtesting', 'quant', 'pnl', 'alpha', 'risk', 'strategy']`
     - Either **≥10 total stars** or **≥50 total commits**
   - Forks are excluded.
   - Commits are retrieved using the GitHub API.

4. **output**
   - Qualified users are written to `developers.csv`
   - Each run includes a unique `integrity_token` to verify run consistency.

## Integrity Token

Each run generates a UUID-based `integrity_token`:

```python
"integrity_token": str(uuid.uuid4())
```
