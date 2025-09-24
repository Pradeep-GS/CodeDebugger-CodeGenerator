import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("API_KEY")  # Make sure your .env has API_KEY=sk-xxxxxx

def prompts(code, language):
    """
    Generate the AI prompt for debugging code.
    """
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
    """
    Call OpenAI API with the prompt and return the raw response.
    """
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",  # optional
            "X-Title": "<YOUR_SITE_NAME>",      # optional
        },
        model="openai/gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content

def response(codes, language):
    """
    Generate AI debug response for the given code and language.
    Parses JSON from AI and returns a dict with 'explanation' and 'fixedCode'.
    """
    prompt_text = prompts(codes, language)
    raw_response = ansgen(prompt_text)

    try:
        data = json.loads(raw_response)  # parse AI output as JSON
    except json.JSONDecodeError:
        # Return raw text if AI did not return valid JSON
        return {"error": "AI response was not valid JSON", "raw": raw_response}
    return data