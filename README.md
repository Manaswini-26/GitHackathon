🎯 GitHub Portfolio Analyzer & Enhancer
"Turn your GitHub into recruiter-ready proof."

📖 Overview
This project is an AI-powered evaluation tool built for the UnsaidTalks Hackathon. It bridges the gap between raw code and professional presentation by analyzing a user's GitHub profile through the lens of a Senior Tech Recruiter.

Most developers have great code but fail to showcase it effectively. This tool identifies "red flags," highlights strengths, and provides a roadmap to make a profile irresistible to hiring managers.

✨ Key Features
Objective Portfolio Scoring: A custom algorithm that evaluates repository volume, README quality, stars (impact), tech stack diversity, and recent activity.

AI Recruiter Insights: Integration with Gemini 2.5 Flash to provide deep-dive feedback, including specific "Red Flags" and 5 actionable improvement tips.

Repository Optimization: Suggests which specific repositories should be pinned for maximum 10-second impact.

Real-time Data: Fetches live data directly from the GitHub REST API.

🛠️ Technical Architecture
Frontend: Streamlit (Python)

AI Engine: Google Gemini 2.5 Flash

Data Source: GitHub REST API

Deployment: Streamlit Community Cloud

🚀 Installation & Local Setup
Clone the repository

Bash
git clone https://github.com/Manaswini-26/GitHackathon.git
cd YOUR_REPO_NAME
Install dependencies

Bash
pip install -r requirements.txt
Set up Secrets
Create a .streamlit/secrets.toml file (or set environment variables):

Ini, TOML
GEMINI_API_KEY = "your_google_gemini_api_key"
GITHUB_TOKEN = "your_github_personal_access_token"
Run the app

Bash
streamlit run app.py
📊 The Scoring System
Our "Portfolio Score" is calculated using five key engineering pillars:
| Metric | Description | Max Points |
| :--- | :--- | :--- |
| Quantity | Total number of public repositories. | 20 |
| Description | Completeness of project summaries. | 20 |
| Social Impact | Total stars across all projects. | 20 |
| Versatility | Number of unique languages used. | 20 |
| Activity | Frequency of updates in the current year. | 20 |

🎥 Demo Video
https://www.loom.com/share/bd4ded264f9847f5adf8571b86926014
Mandatory for hackathon evaluation!

💡 Future Roadmap
[ ] Support for private repository analysis.

[ ] Integration with LinkedIn for a 360-degree career view.

[ ] Automatic README generation for "empty" repositories.


Created with ❤️ for the UnsaidTalks Hackathon.
