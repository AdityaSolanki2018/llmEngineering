# 🧠 Website Brochure Generator with GPT-4o + Gradio

This is an **AI-powered brochure generator** that scrapes a website, selects relevant pages (like About, Careers), and generates a **fun, humorous, and informative brochure** using `GPT-4o-mini`.

Built with:

- 🧠 OpenAI GPT-4o-mini (chat + streaming)
- 🌐 Gradio (interactive front-end)
- 🕸️ Custom Website scraper (OOP-style)
- 🔐 dotenv for secure API key management

---

## 🚀 Features

- 🔍 Scrapes key company pages like:
  - About Us
  - Careers
  - Mission
- 🧠 Streams real-time markdown content using GPT-4o-mini
- 🤝 Built-in logic to skip junk pages like Terms, Privacy, email links
- 🎨 Fun + humorous tone for engaging content
- ⚡ Live web app interface via Gradio

---

## 🛠️ Technologies Used

- Python 3.x
- OpenAI API (`gpt-4o-mini`)
- Gradio
- `dotenv`
- `json`, `os`, `typing`
- Custom OOP module `website.py`

---

## 🧪 How to Run

1. Clone this repo
2. Add your OpenAI key to a `.env` file:
   OPENAI_API_KEY=your_openai_key_here
3. Install dependencies:

```bash
pip install openai gradio python-dotenv
```

4. Run the app:

```bash
python main.py
```

🖼️ Example Output
Welcome to [Company X], where we treat bugs like features and interns like royalty...

(Insert screenshot of your output if available)

📬 Let’s Connect
This project is part of my journey into Agentic AI Engineering.
Follow along at:

💼 LinkedIn

💻 GitHub

🔮 What's Next?
Add retry/error handling for broken links

Option to choose tone (formal, funny, professional)

Option to save brochure as PDF
```
