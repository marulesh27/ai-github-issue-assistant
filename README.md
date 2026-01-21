# 🧠 AI-Powered GitHub Issue Assistant

A lightweight web application that helps developers quickly **understand, classify, and prioritise GitHub issues** by analysing issue details and discussions and generating a structured JSON summary.

---

## 🚀 Project Overview

GitHub issues often contain long descriptions and multiple comments, making it time-consuming to understand their intent and urgency.  
This project automates that process by:

- Fetching issue data from GitHub
- Analysing the issue using an AI-style processing layer
- Producing a **structured JSON output** with summary, type, priority, labels, and impact
- Displaying the result in a simple, clean UI

---

## ✨ Features

- 🔗 Works with **any public GitHub repository**
- 🧾 Fetches issue **title, body, and comments**
- 🧠 AI-inspired logic for issue classification and prioritisation
- 📊 Outputs a **strictly defined JSON format**
- 🖥️ Simple and easy-to-use Streamlit frontend
- 📘 Automatic API documentation via FastAPI (Swagger UI)

---

## 🏗️ System Architecture

User
↓
Streamlit Frontend
↓
FastAPI Backend (/analyze)
↓
GitHub REST API
↓
AI Processing Layer
↓
Structured JSON Response


---

## 🛠️ Tech Stack

| Component     |  Technology |
|---------------|---------------|
| Backend API   | FastAPI (Python) |
| Frontend UI   | Streamlit |
| AI Logic      | Rule-based AI Processing |
| External API  | GitHub REST API |
| Documentation | Swagger UI |



## 📂 Project Structure

ai-github-issue-assistant/
│
├── backend/
│ ├── main.py # FastAPI backend
│ ├── github_client.py # GitHub API integration
│ ├── llm_service.py # AI processing logic
│ └── schemas.py
│
├── frontend/
│ └── app.py # Streamlit UI
│
├── requirements.txt
├── README.md
└── .gitignore


---

## ⚙️ Setup & Run (Under 5 Minutes)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/marulesh27/ai-github-issue-assistant.git
cd ai-github-issue-assistant
2️⃣ Create Virtual Environment
python -m venv venv

Activate it:

Windows: venv\Scripts\activate
Mac / Linux: source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Backend API
uvicorn backend.main:app --reload
Backend runs at:

http://127.0.0.1:8000
Swagger UI:

http://127.0.0.1:8000/docs
5️⃣ Run Frontend UI
Open a new terminal (activate venv again):

streamlit run frontend/app.py

🔌 API Endpoint
POST /analyze
Request Body

{
  "repo_url": "https://github.com/facebook/react",
  "issue_number": 1
}
📊 Example Output
{
  "summary": "Run each test in its own <iframe>",
  "type": "other",
  "priority_score": "2 - Low urgency",
  "suggested_labels": [
    "discussion",
    "needs-review"
  ],
  "potential_impact": "Limited direct impact on users."
}
🧠 AI Processing Approach
The backend includes a dedicated AI processing layer that:

Analyses issue title and description

Classifies issues into categories such as bug, feature request, or discussion

Assigns a priority score with justification

Suggests relevant GitHub labels

Explains potential user impact

The design is modular, making it easy to replace the logic with an actual LLM in the future.

🚀 Going the Extra Mile
📘 Built-in Swagger UI for easy API testing

⚠️ Graceful error handling for invalid inputs and GitHub API failures

🧩 Clean separation of concerns for maintainability and extensibility

🏁 Conclusion
This project demonstrates an end-to-end AI-powered workflow that combines API integration, AI-style reasoning, clean system design, and a usable frontend to solve a real-world developer problem.

📎 License
This project is intended for educational and evaluation purposes.