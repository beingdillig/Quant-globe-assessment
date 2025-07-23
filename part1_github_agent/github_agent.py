import requests
import pandas as pd
from langgraph.graph import StateGraph, START, END
import uuid
from typing import TypedDict, List, Dict, Any

class QualifiedUser(TypedDict):
    username: str
    profile: str
    repos: int
    stars: int
    score: int

class AgentState(TypedDict):
    users: Dict[str, str]
    profile: str
    repos: Dict[str, Dict[str, Any]]
    stars: int
    score: int
    queries: List[str]
    keyword : List[str]
    per_page: int
    integrity_token : str
    qualified_users: List[QualifiedUser]


def get_commit_count(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {
        "Authorization": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "Accept": "application/vnd.github+json"
    }
    params = {"per_page": 100, "page": 1}
    commit_count = 0
    while True:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 451:
            print(f"Access to {owner}/{repo} is restricted due to legal reasons (451).")
            return 0  # or -1 if you want to flag it

        if response.status_code != 200:
            print("Error:", response.status_code)
            break

        data = response.json()
        count = len(data)
        commit_count += count

        if count < 100:
            break
        params["page"] += 1

    return commit_count

def search_users(state:AgentState) -> AgentState:
  # Define your GitHub search query
  queries = state['queries']

  all_users = []


  # GitHub Search API URL
  url = "https://api.github.com/search/users"

  for q in queries:
      params = {
          "q": q,
          "sort": "repositories",
          "order": "desc",
          "per_page": state['per_page'],
          "page" : 1

      }

      headers = {
          "Accept": "application/vnd.github+json",
          "Authorization": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      }

      response = requests.get("https://api.github.com/search/users", headers=headers, params=params)

      if response.status_code == 200:
          users = response.json()["items"]
          all_users.extend(users)
      else:
          print(f"Error: {response.status_code} - {response.text}")


  unique_users = {user["login"]: user['html_url'] for user in all_users}
  state['users'] = unique_users

  print("unique users",len(unique_users))

  return state


def get_repos(state: AgentState) -> AgentState:
    user_repo_map = {}
    unique_users = state['users']

    user_count = 0

    for login, html_url in unique_users.items():
        print("user: ", user_count)
        all_repos = []
        page = 1

        while True:
            url = f"https://api.github.com/users/{login}/repos"
            headers = {
                "Accept": "application/vnd.github+json",
                "Authorization": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            }
            params = {
                "per_page": 100,  # max allowed by GitHub
                "page": page
            }

            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                repos = response.json()
                if not repos:
                    break  # No more repos
                all_repos.extend(repos)
                page += 1
            else:
                print(f"Error fetching {login}: {response.status_code}")
                break

        user_repo_map[login] = {
            "profile": html_url,
            "repos": all_repos
        }

        user_count += 1

    print("user_repo_map", len(user_repo_map), end="\n")
    state['repos'] = user_repo_map
    return state


def evaluate_user(state:AgentState) -> AgentState:
  print("---------------")
  print("Evaluating User")
  print("---------------")
  user_repo_map = state['repos']

  qualified_repo = []

  keyword = state['keyword']
  user_count = 0
  for username, data in user_repo_map.items():
    repos = data["repos"]
    profile = data["profile"]

    repo_count = 0
    stars_total = 0
    commit_total = 0
    visited = 0 
    keyword_hit = False
    user_count+=1
    print(f" {user_count} Username = ", username)
    print("  Total_repos = ", len(repos), end="\n\n")

    for repo in repos:
      visited += 1
      if repo.get("fork"):
        continue
      lang = repo.get('language').lower() if repo['language'] else ""
      stars = repo.get('stargazers_count',0)
      name = repo.get("name").lower()
      desc = repo.get("description").lower() if repo['description'] else ""


      if lang in ['python', 'c++']:
        repo_count += 1
        stars_total += stars
        commit_total += get_commit_count(username, repo['name'])
        for keyw in keyword:
          if keyw in name or keyw in desc:
            keyword_hit = True
            break

      if repo_count >= 2:
        if keyword_hit: 
          if stars_total>=10 or commit_total>=50:
            qualified_repo.append({
                "username" : username,
                "profile" : profile,
                "repos" : repo_count,
                "stars" : stars_total,
                "score": repo_count + stars_total + (20 if keyword_hit else 0),
            })
            print(f"This User: {username} Has Qualified. \n")
            break

  state['qualified_users'] = qualified_repo
  return state


def output(state:AgentState) -> AgentState:
  qualified_users = state['qualified_users']

  if not qualified_users:
    print("No qualified users found.")
  else:
    pd.DataFrame(qualified_users).to_csv("doc.csv")

  print(f"\n🛡️ Integrity Token: {state.get('integrity_token')}")

  return state

graph = StateGraph(AgentState)

graph.add_node('search_user', search_users)
graph.add_node('get_repos', get_repos)
graph.add_node('evaluate_user', evaluate_user)
graph.add_node('output',output)

graph.add_edge(START, 'search_user')
graph.add_edge('search_user','get_repos')
graph.add_edge('get_repos','evaluate_user')
graph.add_edge('evaluate_user','output')
graph.add_edge('output',END)

app = graph.compile()


# ------------------------------------Running The Graph (AGENT) -----------------------------------------
initial_state = {
    "queries" : ["quant repos:>2 language:Python followers:>5","quant repos:>2 language:C++ followers:>5"],
    "per_page": 5,
    "users": [],
    "qualified_users": [],
    "integrity_token": str(uuid.uuid4()),  # 👈 Generate on each run,
    "keyword" : ['backtesting', 'quant', 'pnl', 'alpha', 'risk', 'strategy'],
}


result = app.invoke(initial_state)