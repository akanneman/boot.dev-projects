import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    base = os.path.abspath(working_directory)
    target = os.path.abspath(full_path)
    if os.path.commonpath([base, target]) != base:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target):
        return f'Error: "{directory}" is not a directory'

    entries = os.listdir(target)
    results = []
    for name in entries:
        path = os.path.join(target, name)
        is_dir = os.path.isdir(path)
        size = os.path.getsize(path)
        results.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
    return "\n".join(results)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)



