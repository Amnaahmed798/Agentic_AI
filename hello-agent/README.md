# Setup Instructions

## What you need to do before running any code

1. **Create a `.env` file** and add your Gemini API key like this:

   ```ini
   GEMINI_API_KEY=your_gemini_key_here
   ```
   This file stores your secret key safely so your program can access Gemini's AI services.

2. **Install required packages** with these commands:

   ```bash
   uv init hello_agent        # Initialize a new project folder
   cd hello_agent             # Enter the folder
   uv add openai-agents python-dotenv  # Install SDK and dotenv package to load env variables
   ```

3. **Run your app** with:

   ```bash
   uv run main.py
   ```
   This runs your Python script that interacts with Gemini.


# Configuration Levels

## 1️⃣ Agent Level Configuration (Configure per Agent)

You create a single agent and assign it to use Gemini. This is good if you want just one agent in your app to talk to Gemini.

### Example:

```python
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner

# Create a client to Gemini API using your API key
client = AsyncOpenAI(
    api_key="your_gemini_key",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Create an AI Agent with custom instructions and Gemini model
agent = Agent(
    name="Assistant",
    instructions="You only respond in haikus.",  # AI behaves as a haiku poet
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=client
    ),
)

# Ask the agent a question and get the response asynchronously
result = await Runner.run(agent, "Tell me about recursion.")
print(result.final_output)
```

**Use this if:** You want to customize the model for only one specific agent.


## 2️⃣ Run Level Configuration (Configure per Run)

You create an agent without specifying a model. When you run the agent, you specify which model and client to use. Good if you want to use different models or providers for different tasks with the same agent.

### Example:

```python
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

external_client = AsyncOpenAI(
    api_key="your_gemini_key",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Hello, how are you.", run_config=config)
print(result.final_output)
```

**Use this if:** You want flexible use of different models on the fly with the same agent.


## 3️⃣ Global Level Configuration (Configure once for whole app)

You set Gemini as the default AI provider for your entire app. All agents and runs automatically use Gemini unless specified otherwise. This makes your app always talk to Gemini without extra setup.

### Example:

```python
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api

external_client = AsyncOpenAI(
    api_key="your_gemini_key",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(True)                # Turn off debug tracing
set_default_openai_api("chat_completions")  # Default task type for the AI
set_default_openai_client(external_client)  # Set Gemini as default client

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gemini-2.0-flash"
)

result = Runner.run_sync(agent, "Hello")
print(result.final_output)
```

**Use this if:** You want every AI agent and request in your app to use Gemini automatically.


# Summary

| Configuration Level | What it does | When to use it |
|---------------------|--------------|----------------|
| Agent Level         | Set Gemini for a single agent | Only one agent needs Gemini |
| Run Level           | Set Gemini per run dynamically | Use different models/providers on the fly |
| Global Level        | Set Gemini as default for all | Use Gemini everywhere by default |
