import json
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api = os.getenv("API_KEY")
def prompts(code, language):
    return f"""
You are a professional coding tutor and debugging assistant. 
Your task is to carefully analyze the following code and return a structured response.

Follow these steps strictly:
1. Identify all syntax errors, runtime errors, and logical mistakes in the code.
2. Explain each error in clear, beginner-friendly language (avoid jargon unless necessary).
3. Provide the corrected version of the code with proper formatting and indentation.
4. If there are multiple possible fixes, choose the most efficient and standard approach.
5. Keep your explanation and code separate in the output.

Language: {language}
User Code:
{code}

Your response format must be strictly JSON:
{{
  "explanation": "Detailed explanation of errors and fixes.",
  "fixedCode": "Corrected code here"
}}
"""

def ansgen(prompt):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api,
    )

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",
            "X-Title": "<YOUR_SITE_NAME>",
        },
        model="openai/gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content

def response(codes, language):
    pro = prompts(codes, language)
    raw_response = ansgen(pro)

    try:
        data = json.loads(raw_response)  # Parse AI output as JSON
    except json.JSONDecodeError:
        return {"error": "AI response was not valid JSON", "raw": raw_response}

    return data

# Example usage
result = response(
    """a = "5"
b = 2
print(a + b)""",
    "python"
)

print("Explanation:\n", result["explanation"])
print("\nFixed Code:\n")
print(result["fixedCode"])
