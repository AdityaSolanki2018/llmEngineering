# 🌐 Website Summarizer with GPT-4o + BeautifulSoup

This project is a lightweight AI-based tool that scrapes a given website and generates a **short, readable summary** using OpenAI’s `GPT-4o-mini` model.

Perfect for:
- 🗞️ News summary
- 🧾 Landing page analysis
- 👀 Quick website overviews

---

## 🧠 What It Does

- Takes in a website URL
- Scrapes the content using `requests` + `BeautifulSoup`
- Filters out irrelevant HTML elements (scripts, styles, images, inputs)
- Passes the cleaned content into OpenAI's GPT-4o-mini with a summary prompt
- Outputs a short **markdown summary**

---

## 🚀 Features

- ✅ Website scraping with headers for better access
- ✅ Summarization in markdown format
- ✅ Ignores navigation/UI junk content
- ✅ Clear OOP structure via a `Website` class
- ✅ Supports any public URL

---

## 🛠️ Technologies Used

- Python 3.x
- `requests`
- `beautifulsoup4`
- `openai`
- `dotenv` (for API key management)

---

## 📦 How to Run

1. Clone this repo
2. Add your OpenAI API key in a `.env` file like:

3. Install dependencies:

```bash
pip install openai python-dotenv
```

4. Run the app:

```bash
python main.py
```

🔮 Future Improvements
Add CLI/Gradio UI to make it interactive

Allow user to choose between tones: formal, fun, technical

Add PDF/CSV export options

👋 About
This was built as part of my Agentic AI Engineering journey and Python practice series.
Check out my full learning repo 👉 GitHub

Built with Python, OpenAI, and curiosity. 🧠💻