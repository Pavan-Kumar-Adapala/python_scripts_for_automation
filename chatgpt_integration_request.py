import os
import requests
import argparse

# argparse object
parse = argparse.ArgumentParser(description="Send prompts to OpenAI API and get responses.")
# Adding arguments
parse.add_argument("prompt", help="Prompt to send to OpenAI API")
parse.add_argument("--max_tokens", type=int, default=150, help="The response text length")
parse.add_argument("--model", default="gpt-4o-mini", help="Machine learning model to generate text")
# Reading all arguments
args = parse.parse_args()


# api end point
api_endpoint = "https://api.openai.com/v1/chat/completions"
# api key
api_key = os.getenv("OPENAI_API_KEY")
# request header
request_header = {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + api_key
                }
# request data
request_data = {
                "model": f"{args.model}",
                "messages": [{"role": "user", 
                              "content": [{"type": "text", "text": f"{args.prompt}"}]
                            }],
                "max_completion_tokens": f"{args.max_tokens}",
                "temperature": 0.5,
                }


response = requests.post(url=api_endpoint, headers=request_header, json=request_data)

if response.status_code == 200:
    print(response.json()["choices"][0]["message"])
else:
    print(f"Request failed to with status code: {str(response.status_code)}")