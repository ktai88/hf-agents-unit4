import os, requests
from dotenv import load_dotenv
from smolagents import CodeAgent, DuckDuckGoSearchTool, Model, LiteLLMModel, GoogleSearchTool
from tools import download_task_file, calculator, read_local_file

load_dotenv()

BASE_URL    = "https://agents-course-unit4-scoring.hf.space"
HF_USERNAME = "{username}"  # ← change this
HF_SPACE    = "https://huggingface.co/spaces/{username}/agentcourse/tree/main"

# ── System prompt ────────────────────────────────────────
SYSTEM_PROMPT = """
You are a precise AI assistant solving GAIA benchmark questions.
RULES (follow strictly):
- Reply with ONLY the final answer. No explanation, no preamble.
- Never include the text "FINAL ANSWER" in your output.
- Be exact: number → just the number, name → just the name.
- If the question mentions a file, call download_task_file first.
- After downloading a file, call read_local_file on the saved path to inspect its contents.
- For arithmetic, always use the calculator tool.
- For facts you are unsure about, use web search.
"""

# # ── Model & Agent ────────────────────────────────────────
# model = InferenceClientModel(
#     # model_id="",
#     # token=os.getenv("AIzaSyDkEZjtPsN1D-20UAurZMp7u1JNMkDm9dI")
# )

# agent = CodeAgent(
#     tools=[DuckDuckGoSearchTool(), download_task_file, calculator],
#     model=model,
#     max_steps=5,
# )

model = LiteLLMModel(
    model_id="ollama_chat/qwen2:7b",  # Or try other Ollama-supported models
    api_base="http://127.0.0.1:11434",  # Default Ollama local server
    num_ctx=8192,
)

agent = CodeAgent(
    model=model,
    tools=[DuckDuckGoSearchTool(), download_task_file, read_local_file, calculator],
)

# ── Fetch questions ──────────────────────────────────────
print("Fetching questions...")
questions = requests.get(f"{BASE_URL}/questions").json()
print(f"{len(questions)} questions loaded\n")

# ── Run agent ────────────────────────────────────────────
answers_payload = []

for i, q in enumerate(questions):
    task_id  = q["task_id"]
    question = q["question"]
    has_file = bool(q.get("file_name"))

    print(f"[{i+1}/{len(questions)}] {question[:90]}...")

    prompt = question
    if has_file:
        prompt = (
            f"This question has a file attached.\n"
            f"First call download_task_file('{task_id}') to retrieve it.\n\n"
            + question
        )

    try:
        answer = str(agent.run(SYSTEM_PROMPT + "\n\nQuestion: " + prompt)).strip()
    except Exception as e:
        answer = ""
        print(f"  ERROR: {e}")

    print(f"  → {answer}\n")
    answers_payload.append({"task_id": task_id, "submitted_answer": answer})

# ── Save answers locally ──────────────────────────────────
import json
with open("answers.json", "w") as f:
    json.dump(answers_payload, f, indent=2)

print("✓ Answers saved to answers.json — run submit.py to submit.")