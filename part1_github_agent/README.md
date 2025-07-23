# 🔎 GitHub Users Filter Agent

This project implements an intelligent agent using LangGraph to identify and filter qualified GitHub users based on custom-defined criteria like programming language, repository activity, and keyword relevance.

---

## Overview

The agent searches for GitHub users matching specific queries, evaluates their public repositories based on predefined filters, and outputs a list of qualified developers. This is particularly useful for sourcing contributors, collaborators, or candidates for development work.

---

## ⚙️ Workflow

The agent is built using a 4-step LangGraph pipeline:

1. **search_user**
   Searches for users matching the given queries using GitHub's User Search API.

2. **get_repos**
   For each found user, fetches all public repositories (with pagination support).

3. **evaluate_user**
   Filters repositories based on the requirements:

   - Language: Python or C++
   - Keywords in repo name or description: `['backtesting', 'quant', 'pnl', 'alpha', 'risk', 'strategy']`
   - Star count ≥ 10 OR commit count ≥ 50
   - Minimum 2 qualified repositories

4. **output**
   Outputs all qualifying users to a CSV file: `developers.csv`.

---

## Criteria for Qualified Users

To be considered a qualified developer, a user must have:

- ✅ At least **2 repositories** in **Python** or **C++**
- ✅ Repositories containing any **relevant keyword**
- ✅ Either:
  - ⭐ Total **stars ≥ 10**, or
  - 🧾 Total **commits ≥ 50**

Forked repositories are excluded.

---

## Integrity Token

Each run generates a unique integrity token using `uuid.uuid4()` to ensure output traceability.

```python
"integrity_token": str(uuid.uuid4())
```

## Output

The final CSV (developers.csv) contains:

- GitHub username

- Profile URL

- Qualified repo count

- Total stars

- Computed score

---

## Tech Stack

Python

LangGraph

GitHub REST API

Pandas

---

## How to Run

Set your GitHub API token:

```
"Authorization": "token YOUR_GITHUB_PERSONAL_ACCESS_TOKEN"
```

Customize your queries and keywords in initial_state:

```
initial_state = {
    "queries": ["quant repos:>2 language:Python followers:>5", "quant repos:>2 language:C++ followers:>5"],
    "keyword": ['backtesting', 'quant', 'pnl', 'alpha', 'risk', 'strategy'],
    ...
}
```

Compile and run your LangGraph agent.

---

## Major challenge faced

- GitHub API Pagination -> Handled paginated responses for users, repos, and commits using per_page and page logic.

- Rate Limits & Error Codes (e.g., 451) -> Managed restricted or blocked repositories and handled errors like HTTP 451 (legal restrictions).

- Commit Count Efficiency -> Fetched commits across multiple pages per repo, which was slow and risked hitting API rate limits.

---

## 🤖 One Improvement I Would Like to Make

Integrate an LLM-Based Ranking System After CSV Generation
After collecting and filtering GitHub users into a CSV, I’d integrate a Large Language Model (LLM) to analyze each user's data (repos, stars, keywords, commit activity) as context and automatically rank or recommend top users tailored to specific goals (e.g., backtesting experts or strategy developers).

This would:

Eliminate the need to manually go through every user

Leverage semantic understanding (beyond just numeric filters)

Help stakeholders quickly identify the most promising contributors

---

## Files

- **github_agent.py** – Main implementation of the agent

- **AGENT_DESIGN.md** – Design document detailing each step

- **developers.csv** – Output file containing qualified users
- **README.md** - Brief summary of the approach.
