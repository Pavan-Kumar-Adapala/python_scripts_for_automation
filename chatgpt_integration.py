# Import OpenAPI SDK, Before that install openai SDK from python package manager
from openai import OpenAI
import os
import argparse

# argparse object
parse = argparse.ArgumentParser(description="Send prompts to OpenAI API and get responses.")
# Adding arguments
parse.add_argument("prompt", help="Prompt to send to OpenAI API")
parse.add_argument("--max_tokens", type=int, default=150, help="The response text length")
parse.add_argument("--model", default="gpt-4o-mini", help="Machine learning model to generate text")
# Reading all arguments
args = parse.parse_args()

# Fetch API Key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("ERROR: OPENAI_API_KEY is not set in the environment.")
    exit(1)

# Initialize OpenAI Client
client = OpenAI(api_key=api_key)
    # os.environ.get("OPENAI_API_KEY"),
    # organization='org-asekYbtoWg9EZoIqivjobM7z',
    # project='Default project'

# API request
try:
    response = client.chat.completions.create(messages=[{"role": "user", "content": args.prompt}], 
                                              model=args.model, 
                                              max_tokens=args.max_tokens, 
                                              temperature=0.5,)
    print(response.choices[0].message["content"])
except Exception as e:
    print(f"ERROR: {e}")
