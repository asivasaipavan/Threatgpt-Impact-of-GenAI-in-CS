# 🚀 ThreatGPT — AI Cybersecurity Analyzer

ThreatGPT is an AI-powered web application that analyzes user input for potential cybersecurity threats such as phishing, malware, prompt injection, and privacy risks using advanced language models.

---

## 🌐 Live Demo

🔗 https://huggingface.co/spaces/asivasaipavan/ThreatGPT

---

## 🧠 Features

* 🔍 Detects phishing attempts and malicious scripts
* 🛡️ Identifies prompt injection and privacy leaks
* ⚡ Fast analysis using Groq-powered LLM
* 🌐 Simple and interactive web interface (Gradio)
* 📦 Lightweight deployment (no heavy ML models required)

---

## 🛠️ Tech Stack

* **Frontend**: Gradio
* **Backend**: Python
* **AI/LLM**: Groq API, LangChain
* **Deployment**: Hugging Face Spaces

---

## 📂 Project Structure

```
├── app.py                  # Gradio app interface
├── threat_analyzer.py      # Core threat detection logic
├── requirements.txt        # Dependencies
├── static/                # Frontend assets (optional)
├── samples/               # Example inputs for testing
```

---

## ⚙️ Installation (Local Setup)

### 1. Clone the repository

```
git clone https://github.com/asivasaipavan/Threatgpt-Impact-of-GenAI-in-CS
cd Threatgpt-Impact-of-GenAI-in-CS
```

### 2. Create environment

```
conda create -n threatgpt python=3.10
conda activate threatgpt
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

### 5. Run the app

```
python app.py
```

---

## 🔑 Environment Variables

| Variable     | Description       |
| ------------ | ----------------- |
| GROQ_API_KEY | Your Groq API key |

---

## 📸 Usage

1. Enter any text (email, script, message, etc.)
2. Click analyze
3. View detected threats and insights

---

## 📸 Screenshots

### 🏠 Home Interface
![Home](home.png)

### ✍️ User Input Example
![Input](input.png)

### 🔍 Analysis Result
![Output](output.png)

---

## 🚀 Future Improvements

* 🎯 Improve detection accuracy
* 📊 Add visualization dashboard
* 🔐 User authentication system
* 🌍 Deploy with custom domain

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve the project.

---

## 📜 License

This project is for educational and research purposes.

---

## 👨‍💻 Author

**Siva Sai Pavan**
🔗 https://github.com/asivasaipavan

---

⭐ If you like this project, give it a star!
