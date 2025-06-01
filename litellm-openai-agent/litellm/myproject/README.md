# What Is LiteLLM and Why Use It?

LiteLLM is a Python tool that helps you easily connect to many AI models (LLMs) like:

- OpenAI (ChatGPT)
- Anthropic (Claude)
- Google Gemini
- HuggingFace
- Azure OpenAI
- And more!

Instead of learning different APIs for each company, LiteLLM gives you one simple way to talk to all these AI models.

## What You Can Do with LiteLLM

- Send messages to AI models and get responses
- Switch between models easily by just changing the name
- Handle errors in the same way for all models
- Automatically retry if something goes wrong
- Log and monitor your AI usage with tools like Lunary or Helicone

## How to Use It (Step-by-Step)

1. **Install LiteLLM**

   ```bash
   pip install litellm
   ```

2. **Set Your API Keys**

   Put your API keys in environment variables like this:

   ```python
   import os
   os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
   os.environ["GEMINI_API_KEY"] = "your_gemini_api_key"
   ```

3. **Send a Message to a Model**

   ```python
   from litellm import completion

   messages = [{"role": "user", "content": "Hello, how are you?"}]
   response = completion(model="gpt-3.5-turbo", messages=messages)
   print(response['choices'][0]['message']['content'])
   ```

4. **Use Any Model You Want**

   Just change the `model=` name:

   ```python
   completion(model="claude-2", messages=messages)        # Claude
   completion(model="gemini-2.0", messages=messages)      # Gemini
   ```

5. **Use Streaming (See Output in Real-Time)**

   ```python
   response = completion(model="gpt-3.5-turbo", messages=messages, stream=True)
   for part in response:
       print(part['choices'][0]['delta'].get('content', ''), end='')
   ```

6. **Handle Errors the Same Way**

   ```python
   from openai.error import OpenAIError

   try:
       response = completion(model="claude-2", messages=messages)
   except OpenAIError as e:
       print("An error occurred:", e)
   ```

7. **Fallback: Use Another Model If One Fails**

   If Claude fails, try Gemini:

   ```python
   from litellm import completion, exceptions

   try:
       response = completion(model="claude-2", messages=messages)
   except exceptions.BadRequestError:
       response = completion(model="gemini-2.0", messages=messages)
   ```

8. **Logging Usage**

   To track what the AI is doing (for debugging or analytics):

   ```python
   os.environ["LUNARY_PUBLIC_KEY"] = "your_lunary_key"
   os.environ["HELICONE_API_KEY"] = "your_helicone_key"
   litellm.success_callback = ["lunary", "helicone"]
   ```

## In Short

LiteLLM = One tool to talk to 100+ AI models in the same way.

It makes it easier to:

- Build apps with different LLMs
- Switch between models
- Handle errors and retries
- Monitor what your AI is doing
