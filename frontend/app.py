import streamlit as st
import requests

st.set_page_config(page_title="AI GitHub Issue Assistant")

st.title("AI-Powered GitHub Issue Assistant")

# Input fields
repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/facebook/react"
)

issue_number = st.number_input(
    "Issue Number",
    min_value=1,
    step=1
)

# Button
if st.button("Analyze Issue"):
    if not repo_url or not issue_number:
        st.error("Please enter both repository URL and issue number.")
    else:
        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            json={
                "repo_url": repo_url,
                "issue_number": int(issue_number)
            }
        )

        if response.status_code == 200:
            st.subheader("Analysis Result")
            st.json(response.json())
        else:
            st.error("Failed to analyze the issue.")
