# ✈️ AI Airline Assistant

An interactive AI-powered airline assistant built with **OpenAI's GPT-4o-mini** and **Gradio**, capable of answering customer queries and fetching real-time ticket prices for specific destinations.

---

## 🚀 Features
- 💬 **Conversational AI** — Short, courteous, and accurate responses.
- 🛫 **Ticket Price Lookup** — Integrated tool to fetch return ticket prices for selected cities.
- 🖥 **Web Interface** — Built with Gradio for quick and simple deployment.
- 🔒 **Secure API Key Handling** — Uses `.env` file for environment variables.

---

## 🗂 Project Structure
AI-Airline-Assistant/
│
├── main.py # Main application code
├── requirements.txt # Python dependencies
├── .env # Stores your OpenAI API key (not tracked in Git)
└── README.md # Project documentation

---

## 🛠 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/AdityaSolanki2018/AI-Airline-Assistant.git
cd AI-Airline-Assistant
````
### 2️⃣ Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Create a .env file
```bash
OPENAI_API_KEY=your_api_key_here
```

### ▶ Usage
```bash
python main.py
```
---

## 🧠 How It Works
- System Prompt — The AI is instructed to be short, polite, and accurate.

- Function Calling — If a user asks for ticket prices, the model calls the get_ticket_price() function.

- Response Generation — The result is returned to the user in natural language.

- Interface — Gradio provides a chat interface accessible in your browser.

---

## 📍 Example Interaction
1. User: "How much is a ticket to Tokyo?"
2. Assistant: "A return ticket to Tokyo costs $1499."

---

## 📌 Future Improvements
- 🔄 Real-time integration with airline APIs

- 🌍 Support for more cities

- 🗣️ Voice-based interaction

---

### Made with ❤️ using Python, OpenAI, and 
