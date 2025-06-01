
# 🤖 Sync Hello Agent (with Gemini API)

## 📖 Overview

**Sync Hello Agent** is a simple Python script that synchronously runs an AI agent using the **Gemini API**, via an OpenAI-compatible client. It demonstrates how to build and run a conversational agent that processes a single prompt and returns a response instantly.

This version uses `Runner.run_sync()` to execute the agent without relying on `asyncio`, making it ideal for quick tests or integration into sync-based applications.

---

## 📦 Features

- Synchronous agent execution (no need for `asyncio`)
- Integration with Gemini via OpenAI-compatible API
- Secure API key management using `.env`
- Simple and clean design for beginner-friendly usage

---

## 🚀 How to Run

### 1. 📁 Setup `.env` File

Create a `.env` file in your project directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```
Replace `your_gemini_api_key_here` with your actual Gemini API key from Google AI Studio.

### 2. 📦 Install Dependencies

Install the required Python packages:

```bash
pip install python-dotenv
```
Make sure any other needed libraries (like httpx, openai, or the agents package you are using) are also installed.

### 3. ▶️ Run the Script

Use:

```bash
python main.py
```

Expected output:

```bash
CALLING AGENT

I'm just a program, but I'm here and ready to help you!
```

## 🧠 How It Works

1. Loads your API key securely from the .env file.
2. Connects to Gemini using an OpenAI-compatible async client.
3. Wraps the model using OpenAIChatCompletionsModel.
4. Initializes an agent with simple instructions.
5. Sends a prompt synchronously using `Runner.run_sync()`.
6. Prints the response directly to the console.

## 📚 Reference

[Gemini OpenAI-Compatible API](https://ai.google.dev/gemini-api/docs/openai)

## 🔧 Customization Ideas

- Change the prompt and instructions for the agent.
- Integrate with a CLI or GUI.
- Wrap in a Flask or FastAPI app for web-based interactions.
- Extend to support multiple turns in conversation.

## 🔐 Security Note

- Never share or commit your .env file.
- Always store API keys securely using environment variables or secret managers.

Let me know if you want this converted into a chatbot, web API, or used in a larger app context!
