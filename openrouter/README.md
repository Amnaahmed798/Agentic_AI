# OpenRouter

OpenRouter is a platform that lets you access lots of different AI language models (LLMs) from many companies like OpenAI, Google, Anthropic, and also open-source models like Mistral or LLaMA.

Instead of signing up separately for each AI model provider, you just use OpenRouter's single API (a way for your app to talk to these models).

It acts like a middleman (proxy) — it sends your requests to the actual providers and gives you back the results. This makes it easy to switch between models without changing your app code much.

## What can you do with OpenRouter?

- Use over 200 AI models through one interface.
- Interact via a web chat interface or use it in your programs with their API.
- It supports features like function calling (where the AI can suggest calling external tools, like a weather API).
- You get tools for managing usage and costs, like monitoring tokens used.

## OpenRouter's Compatibility

OpenRouter supports the OpenAI Chat Completion API, which means:

- If your app already works with OpenAI, switching to OpenRouter is easy — just change the API key and base URL.
- You can use OpenRouter with OpenAI-compatible SDKs (software tools) without rewriting your code.

## Free Models on OpenRouter

OpenRouter offers about 50 free AI models to use. These models have some usage limits to prevent abuse:

- Usually 200 requests per day total.
- And about 20 requests per minute.

Among these free models, 6 have very large context windows (can handle over 1 million tokens at once), which is rare for free options. These free models are great for personal projects, testing, or low-usage scenarios.

## Rate Limits Compared

- **OpenRouter free models:** 200 requests/day max, 20 requests/min max.
- **Google Gemini free tier:** 1,500 requests/day max, 15 or 30 requests/min, and very high token limits (good for development/testing).

Because OpenRouter's free limits are lower, many developers use Google Gemini models for heavy testing and keep OpenRouter as a backup or to try lots of different models quickly.

## Summary Table

| Feature                | Details                                      |
|------------------------|----------------------------------------------|
| Number of free models  | About 50                                     |
| Rate limits            | 200 requests/day, 20 requests/min            |
| Special free models    | 6 models with 1 million+ token context windows |
| API compatibility      | Works with OpenAI Chat Completion API        |
| Model hosting          | Proxy, routes to third-party providers       |
| Use cases              | Development, testing, personal projects      |

## Why Use OpenRouter?

- Access many AI models easily without juggling multiple keys.
- Save money by using free models with some limits.
- Switch between models seamlessly in your app.
- Good for experimenting and development.
