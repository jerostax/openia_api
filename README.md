# 🤖 GPT-Napoleon CLI Chatbot

This is a simple command-line chatbot that sends your prompts to the OpenAI API and responds as if it were... Napoleon Bonaparte! 👑🇫🇷

## 🧠 Features

- Interactive chat using OpenAI's GPT model (`gpt-4o-mini`)
- Custom role: responds like Napoleon Bonaparte
- Maintains conversation history for contextual replies
- Uses environment variables for secure API key handling

## 🗂️ Project Structure

```
.
├── app.py             # Main chatbot script
├── .env.example       # Example environment configuration
```

## ⚙️ Requirements

- Python 3.7 or higher
- An OpenAI account and a valid API key

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd <your-project-folder>
   ```

2. **(Optional) Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install requests python-dotenv
   ```

4. **Set up environment variables:**

   - Rename `.env.example` to `.env`
   - Add your OpenAI API key:

     ```
     API_KEY=sk-your-api-key-here
     ```

## 🚀 How to Run

Start the chatbot using:

```bash
python app.py
```

You will be prompted to enter a question. Napoleon will reply.  
To exit the chatbot, press `Enter` on an empty line.

## ✏️ Example

```
Your prompt or question : What is your opinion on modern warfare?
> Modern warfare lacks the elegance of strategy and spirit we once commanded. Victory lies not just in arms, but in vision.
```

## ❗ Notes

- The API URL used in `app.py` is `https://api.openai.com/v1/responses`, which is **not the official OpenAI endpoint**.  
  If you're using the standard OpenAI API, replace it with:
  `https://api.openai.com/v1/chat/completions`

- This script is meant for exploration and can be extended with:
  - Dynamic persona switching
  - Command-line arguments
  - Error handling and retries
  - UI (e.g. web or desktop)

## 📜 License

This project is open-source and available under the MIT License.

## 🙌 Author

Developed by **Jeremy** — a passionate web developer who enjoys historical roleplay, clean code, and epic mountain hikes. 🇫🇷🏔️
