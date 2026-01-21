import requests

GITHUB_API_BASE = "https://api.github.com"


def parse_repo_url(repo_url: str):
    """
    Extract owner and repo name from GitHub URL
    Example: https://github.com/facebook/react
    """
    try:
        parts = repo_url.rstrip("/").split("/")
        owner = parts[-2]
        repo = parts[-1]
        return owner, repo
    except Exception:
        return None, None


def fetch_issue(repo_url: str, issue_number: int):
    owner, repo = parse_repo_url(repo_url)

    if not owner or not repo:
        raise ValueError("Invalid GitHub repository URL")

    issue_url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/issues/{issue_number}"
    comments_url = f"{issue_url}/comments"

    issue_response = requests.get(issue_url)
    comments_response = requests.get(comments_url)

    if issue_response.status_code != 200:
        raise ValueError("Issue not found or GitHub API error")

    issue_data = issue_response.json()
    comments_data = comments_response.json()

    issue_details = {
        "title": issue_data.get("title", ""),
        "body": issue_data.get("body", ""),
        "comments": [comment.get("body", "") for comment in comments_data]
    }

    return issue_details
