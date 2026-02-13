import streamlit as st
import requests
import google.generativeai as genai

# ---------------- CONFIG ---------------- #



st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🚀 AI Powered Assistant")
st.caption("Generate intelligent outputs in seconds")





# Load secrets
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
GITHUB_TOKEN = st.secrets.get("GITHUB_TOKEN", None)

genai.configure(api_key=GEMINI_API_KEY)

# ✅ USE A VALID MODEL (very important)
model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- UI ---------------- #

st.title("🚀 GitHub Portfolio Analyzer & Enhancer")
st.write("Turn your GitHub into recruiter-ready proof.")

username = st.text_input("Enter GitHub Username")

# ---------------- FUNCTIONS ---------------- #

def get_headers():
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    return headers


def fetch_repos(user):
    url = f"https://api.github.com/users/{user}/repos"
    response = requests.get(url, headers=get_headers())

    if response.status_code != 200:
        return None

    return response.json()


def calculate_score(repos):
    score = 0

    repo_count = len(repos)

    if repo_count >= 10:
        score += 20
    elif repo_count >= 5:
        score += 10

    readme_score = sum(1 for r in repos if r["description"])
    score += min(readme_score * 2, 20)

    stars = sum(r["stargazers_count"] for r in repos)
    score += min(stars, 20)

    languages = set(r["language"] for r in repos if r["language"])
    score += min(len(languages) * 5, 20)

    recent = sum(
        1 for r in repos
        if r["updated_at"] > "2024-01-01"
    )
    score += min(recent * 2, 20)

    return min(score, 100)


def generate_ai_feedback(user, repos, score):

    repo_names = [r["name"] for r in repos[:10]]

    prompt = f"""
You are a senior tech recruiter.

Analyze this GitHub profile.

Username: {user}
Repositories: {repo_names}
Portfolio Score: {score}/100

Give:

1. Strengths
2. Red flags
3. 5 SPECIFIC actionable improvements
4. Which repos should be pinned
5. How to impress recruiters in 10 seconds

Be direct and professional.
"""

    response = model.generate_content(prompt)

    return response.text


# ---------------- BUTTON ---------------- #

if st.button("✨ Generate Output"):

    if not username:
        st.warning("Please enter a username.")
        st.stop()

    with st.spinner("Analyzing GitHub profile..."):

        repos = fetch_repos(username)

        if repos is None:
            st.error("Invalid GitHub username or API error.")
            st.stop()

        score = calculate_score(repos)

        st.metric("🔥 Portfolio Score", f"{score}/100")

        st.subheader("🤖 Recruiter Feedback")

        try:
            feedback = generate_ai_feedback(username, repos, score)
            st.write(feedback)

        except Exception as e:
            st.error("Gemini error — restart Streamlit once.")
            st.write(e)
