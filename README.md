# KalpitAI-llm-chatbot
<img width="1439" height="857" alt="Screenshot 2568-12-26 at 12 16 53 AM" src="https://github.com/user-attachments/assets/20387467-c754-4906-ba00-02b6621550b0" />
<img width="1440" height="859" alt="Screenshot 2568-12-26 at 12 14 26 AM" src="https://github.com/user-attachments/assets/9c8ed217-fce1-40b0-a841-e75ed65c1192" />

--
# 🤖 KalpitAI – Streamlit AI Chatbot (https://kalpitai.streamlit.app/)
Note: The `KalpitAI`  has been live for 7 days. However, I have intentionally configured a placeholder API key to prevent live text generation while maintaining the user interface for demonstration purpose only.

`KalpitAI` is a ChatGPT-like AI chatbot built using **Streamlit** and **OpenAI**, designed with a clean UI and secure deployment practices. The app supports real-time conversations.

---

## 🚀 Features

- `ChatGPT`-style conversational UI
- Built with **Streamlit**
- Uses **OpenAI language models**
- Secure API key handling via environment variables
- Ready for **Streamlit Cloud deployment**
- Lightweight, clean, and easy to extend

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **OpenAI API**
- **GitHub**
- **Streamlit Cloud**

---

## 📁 Project Structure
```
kalpitai-streamlit-chatbot/
│
├── GenAI_app.py        # Main Streamlit application
├── requirements.txt   
├── runtime.txt        
├── kalpit_logo.png    
├── Avatar_icon.png    
├── user_icon.png      
└── README.md
```

## How It Works

- The chatbot UI is rendered using Streamlit’s `st.chat_message`.
- Messages are stored in Streamlit `session_state`.
- OpenAI API is called securely using environment variables (secrete path).



