import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

model_name = "gemini-2.0-flash-001"

def main ():
    load_dotenv()

    args = sys.argv[1:]
    verbose = "--verbose" in args

    if not args :
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = " ".join(args)
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model = model_name, 
        contents = messages,
    )

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")  # type: ignore
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}") # type: ignore
        
    print(response.text)


if __name__ == "__main__":
    main()
