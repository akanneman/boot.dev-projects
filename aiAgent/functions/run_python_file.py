import os
import subprocess
import sys
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_file_path.startswith(abs_working_dir + os.sep):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'

        if not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        cmd = [sys.executable, abs_file_path, *[str(a) for a in args]]
        completed = subprocess.run(
            cmd,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30
        )

        stdout = (completed.stdout or "").strip()
        stderr = (completed.stderr or "").strip()

        parts = []
        if stdout:
            parts.append(f"STDOUT:\n{stdout}")
        if stderr:
            parts.append(f"STDERR:\n{stderr}")
        if completed.returncode != 0:
            parts.append(f"Process exited with code {completed.returncode}")

        if not parts:
            return "No output produced."
        return "\n".join(parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=(
        "Executes a Python file within the working directory and returns its output. "
        "Supports optional CLI arguments."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of CLI args to pass to the Python file.",
            ),
        },
    ),
)

