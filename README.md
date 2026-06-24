# 🤖 Gemini AI Chatbot

An AI-powered chatbot built using **Google Gemini API** and **Streamlit**. This chatbot can answer user queries in real-time using Google's latest Gemini models.

## 🚀 Features

* AI-powered conversational chatbot
* Real-time responses using Google Gemini API
* Simple and interactive Streamlit UI
* Secure API key management using environment variables
* Easy to set up and run locally

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API
* Python Dotenv

## 📂 Project Structure

```text
Gemini-AI-Chatbot/
│
├── app.py
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Codesbyashu/gemini-ai-chatbot.git
cd gemini-ai-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Environment File

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### 5. Run the Application

```bash
streamlit run app.py
```

## 📸 Screenshots

### Home Page
![Home Page](screenshots/Screenshot%202026-06-24%20at%203.16.51%E2%80%AFPM.png)

### Chat Response
![Chat Response](screenshots/Screenshot%202026-06-24%20at%203.17.18%E2%80%AFPM.png)


## 🎯 Future Improvements

* Chat History
* PDF Question Answering
* Dark Mode UI
* Multi-Conversation Support
* Deployment on Streamlit Cloud

## 👨‍💻 Author

Ashutosh

B.Tech CSE | Full Stack Development | AI Enthusiast

## 📜 License

This project is licensed under the MIT License.
