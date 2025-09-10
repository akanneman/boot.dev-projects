import os
from dotenv import load_dotenv
from google import genai

# 1. Load API key from .env
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# 2. Initialize Gemini client
client = genai.Client(api_key=api_key)

# 3. Send a prompt to the Gemini model
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)

# 4. Print the model’s response
print(response.text)

# 5. Print token usage
print("Prompt tokens:", response.usage_metadata.prompt_token_count)
print("Response tokens:", response.usage_metadata.candidates_token_count)

