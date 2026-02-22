# 🤖 Joke Explainer AI

A lightweight AI-powered web application that explains jokes using the GPT-4o Mini model via GitHub Models API.

🔗 **Live App:** https://jokeexplainer11.streamlit.app/  
🔗 **Repository:** https://github.com/SaurabhLP88/joke  

---

## 📌 Overview

- Joke Explainer AI is a mini web application built with Streamlit that integrates a Large Language Model (LLM) using GitHub’s AI inference API.
- Users can enter any joke, and the application generates a clear explanation using GPT-4o Mini.
- This project demonstrates practical API integration, environment security handling, and AI-powered application development.

---

## 🎯 Problem Statement

- Learn how to access and use Large Language Models via API
- Implement secure authentication using environment variables
- Build a simple interactive web interface
- Deploy an AI-powered application to production
- Understand production-level environment separation (local vs cloud)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **OpenAI SDK**
- **GitHub Models API**
- **Environment Variables / Secrets Management**

---

## 🧠 How It Works

1. User enters a joke.
2. The app sends the input to GPT-4o Mini via GitHub’s inference endpoint.
3. The model generates a contextual explanation.
4. The response is displayed in the UI.

---

## ⚙️ Technical Decisions

- Used **Streamlit** for rapid UI development.
- Used **openai/gpt-4o-mini** for lightweight and efficient inference.
- Used **GitHub Models API** instead of direct OpenAI API.
- Implemented **secure token handling** via:
  - `.env` for local development
  - Streamlit Secrets for production
- Used structured chat messages (`system`, `user`) for controlled output.

---

## 🔐 Security Implementation

- API keys are never hardcoded.
- Local development uses `.env`.
- Production uses Streamlit Cloud Secrets.
- `.env` is excluded via `.gitignore`.

This ensures secure deployment practices aligned with industry standards.

---

## 🚀 Running Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SaurabhLP88/joke.git
cd joke
```

## 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Create a .env file

```bash
GITHUB_TOKEN=your_personal_access_token
```

## 4️⃣ Run the app

```bash
streamlit run app.py
```

## 🌍 Deployment

- Deployed using Streamlit Cloud with environment secrets configured securely.

## 📚 Key Learnings

- Working with Large Language Models programmatically
- API authentication using Personal Access Tokens
- Environment configuration management
- Differences between local and production environments
- Building and deploying AI-powered applications

## 👨‍💻 Author

Saurabh Lakhanpal
Full Stack Developer | Senior Frontend Developer
