import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file

WORKING_DIR = "./calculator"

FUNCTION_TABLE = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
}

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    kwargs = dict(function_call_part.args)
    kwargs["working_directory"] = WORKING_DIR

    if verbose:
        print(f"Calling function: {function_name}({kwargs})")
    else:
        print(f" - Calling function: {function_name}")

    func = FUNCTION_TABLE.get(function_name)
    if not func:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    result = func(**kwargs)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": result},
            )
        ],
    )


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Missing GEMINI_API_KEY in .env", file=sys.stderr)
        return 1

    user_prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Say something nice"

    client = genai.Client(api_key=api_key)

    config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=SYSTEM_PROMPT,
    )

    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=user_prompt)],
        )
    ]

    for step in range(20):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=config,
            )

            made_tool_call = False

            if getattr(response, "candidates", None):
                for cand in response.candidates:
                    if getattr(cand, "content", None):
                        msg = cand.content
                        msg.role = "model"
                        messages.append(msg)

                        for part in getattr(msg, "parts", []):
                            fc = getattr(part, "function_call", None)
                            if fc:
                                made_tool_call = True
                                tool_result = call_function(fc, verbose=True)
                                messages.append(
                                    types.Content(
                                        role="user",
                                        parts=[
                                            types.Part.from_function_response(
                                                name=fc.name,
                                                response={
                                                    "result": tool_result.parts[0].function_response.response.get("result")
                                                },
                                            )
                                        ],
                                    )
                                )

            if not made_tool_call and getattr(response, "text", None) and response.text.strip():
                print("Final response:\n" + response.text)
                break

        except Exception as e:
            err_msg = types.Content(role="user", parts=[types.Part(text=f"Tool error: {e}")])
            messages.append(err_msg)
            print(f"Agent error: {e}")
            break
    else:
        print("Agent hit the 20-step limit without a final answer.")

if __name__ == "__main__":
    sys.exit(main())
