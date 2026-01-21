from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.github_client import fetch_issue
from backend.llm_service import analyze_issue_with_llm

app = FastAPI(title="AI GitHub Issue Assistant")


class IssueRequest(BaseModel):
    repo_url: str
    issue_number: int


@app.get("/")
def root():
    return {"message": "Backend is running successfully"}


@app.post("/analyze")
def analyze_issue(data: IssueRequest):
    try:
        issue_details = fetch_issue(data.repo_url, data.issue_number)
        return analyze_issue_with_llm(issue_details)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
