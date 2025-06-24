import os
from dotenv import load_dotenv
from google import genai
import sys

input = sys.argv[1]
print(f"Input: {input}")

if input == None or input == "":
    print("No input provided. Exiting.")
    sys.exit(1)
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash-001", contents=input)

print(response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
