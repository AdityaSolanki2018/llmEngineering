# FlightAI – Multi-Modal Airline Assistant ✈️🤖
FlightAI is an interactive AI-powered airline assistant built with OpenAI GPT-4o-mini and Gradio.
It answers customer questions about ticket prices, generates beautiful vacation images for destinations,
and maintains a short, courteous conversational style.

---

## 🚀 Features
AI Chatbot: Provides short, polite, and accurate responses.

Tool Integration: Retrieves ticket prices from predefined data.

Dynamic Image Generation: Creates vibrant pop-art style travel images using DALL·E 3.

Gradio Web Interface: Clean, interactive, browser-based chat interface.

---

## 🛠️ Tech Stack
1. Python 3.9+

2. OpenAI API – for GPT & DALL·E models

3. Gradio – web UI for chatbot

4. Pillow (PIL) – image handling

5. python-dotenv – environment variable management

---

## 📂 Project Structure
```
FlightAI/
│
├── flight_ai.py        # Main script
├── .env                # Contains your OpenAI API key
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Setup & Installation
Clone this repository

```bash
git clone https://github.com/yourusername/FlightAI.git
cd FlightAI
Create a virtual environment (recommended)
```

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Install dependencies
```

```bash
pip install -r requirements.txt
Set your OpenAI API Key
Create a .env file in the root folder and add:
```

```
OPENAI_API_KEY=your_api_key_here
Run the application
```

```bash
python flight_ai.py
The chatbot will launch in your browser.
```
---

## 💡 How It Works
- System Prompt: Guides the assistant to stay short, polite, and accurate.

- Function Calling: GPT detects when to retrieve a ticket price.

- Image Generation: Uses DALL·E 3 to generate unique destination art.

- Gradio UI: Displays chat messages and generated images in real-time.

---

## 🖼 Example Interaction
- User: "How much is a ticket to Tokyo?"
- AI: "A return ticket to Tokyo costs $1400."
(Generates a vibrant image of Tokyo's tourist attractions)
<img width="1912" height="955" alt="image" src="https://github.com/user-attachments/assets/4f4a71a6-922a-47e7-9bfe-0d78aaac10d7" />


---

## 📜 License
This project is licensed under the MIT License – see the LICENSE file for details.

  
