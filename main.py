import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt

from call_function import available_functions, call_function

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(
            role="user", 
            parts=[types.Part(text=args.user_prompt)]
        )
    ]

    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0,
            tools=[available_functions]
        )
    )

    if response is None or response.usage_metadata is None: 
        raise RuntimeError("Failed to get a valid response from Gemini API")

    if response.candidates[0].content.parts[0].function_call:
        
        function_results = []
        
        for part in response.candidates[0].content.parts:
            if part.function_call:
                fn = part.function_call
                
                function_call_result = call_function(fn, verbose=True)
                
                if not function_call_result.parts:
                    raise Exception("Function call result has no parts.")
                    
                func_response_obj = function_call_result.parts[0].function_response
                if func_response_obj is None:
                    raise Exception("Function call result part has no function_response.")
                    
                if func_response_obj.response is None:
                    raise Exception("function_response has no response data.")
                
                function_results.append(function_call_result.parts[0])
                
                print(f"-> {func_response_obj.response}")
                    
    else:
        print(response.text)

    # if args.verbose:
    #     print(f"User prompt: {args.user_prompt}")
    #     print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    #     print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()