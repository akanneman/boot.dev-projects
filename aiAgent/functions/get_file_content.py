import os
from config import MAX_FILE_PREVIEW_CHARS
from google.genai import types
def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not os.path.commonpath([abs_file_path, abs_working_dir]) == abs_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(abs_file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if len(content) > MAX_FILE_PREVIEW_CHARS:
            content = content[:MAX_FILE_PREVIEW_CHARS] + f'[...File "{file_path}" truncated at {MAX_FILE_PREVIEW_CHARS} characters]'
        return content

    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the contents of a text file located under the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file, relative to the working directory.",
            ),
        },
    ),
)
