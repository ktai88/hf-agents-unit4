import requests
from smolagents import tool

BASE_URL = "https://agents-course-unit4-scoring.hf.space"

@tool
def download_task_file(task_id: str) -> str:
    """
    Downloads a file attached to a GAIA task and saves it locally.
    Returns the local file path or an error message.
    Args:
        task_id: The task ID string from the question.
    """
    url = f"{BASE_URL}/files/{task_id}"
    response = requests.get(url)
    if response.status_code == 200:
        filename = f"task_{task_id}_file"
        with open(filename, "wb") as f:
            f.write(response.content)
        return f"File saved to: {filename}"
    return f"No file for task_id={task_id} (status {response.status_code})"


@tool
def calculator(expression: str) -> str:
    """
    Evaluates a safe math expression and returns the result as a string.
    Args:
        expression: A Python math expression e.g. '3 * (4 + 2) / 2'
    """
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {e}"


@tool
def read_local_file(file_path: str, max_chars: int = 12000) -> str:
    """
    Reads a local text file and returns up to max_chars characters.
    Use this after download_task_file to inspect task attachments.
    Args:
        file_path: Path to the local file to read.
        max_chars: Maximum number of characters to return.
    """
    try:
        with open(file_path, "rb") as f:
            raw = f.read()
    except Exception as e:
        return f"Unable to read file '{file_path}': {e}"

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("latin-1", errors="replace")

    if len(text) > max_chars:
        return text[:max_chars] + "\n\n[TRUNCATED]"
    return text