def analyze_issue_with_llm(issue_data: dict):
    title = issue_data.get("title", "").lower()
    body = issue_data.get("body", "").lower()

    # Classification logic
    if "bug" in title or "error" in body or "fail" in body:
        issue_type = "bug"
        priority = "4 - Likely impacts functionality"
        labels = ["bug", "needs-fix"]
        impact = "May affect users by causing unexpected behaviour or failures."

    elif "feature" in title or "enhancement" in body:
        issue_type = "feature_request"
        priority = "3 - Improvement request"
        labels = ["feature", "enhancement"]
        impact = "Adds new functionality for users."

    else:
        issue_type = "other"
        priority = "2 - Low urgency"
        labels = ["discussion", "needs-review"]
        impact = "Limited direct impact on users."

    return {
        "summary": issue_data.get("title", "GitHub issue analysis"),
        "type": issue_type,
        "priority_score": priority,
        "suggested_labels": labels,
        "potential_impact": impact
    }
