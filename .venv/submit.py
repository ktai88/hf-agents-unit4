import json, requests

BASE_URL    = "https://agents-course-unit4-scoring.hf.space"
HF_USERNAME = "{username}"  # ← change this
HF_SPACE    = "https://huggingface.co/spaces/{username}/your-space/tree/main"

with open("answers.json") as f:
    answers = json.load(f)

submission = {
    "username": HF_USERNAME,
    "agent_code": HF_SPACE,
    "answers": answers,
}

print(f"Submitting {len(answers)} answers...")
response = requests.post(f"{BASE_URL}/submit", json=submission)
data = response.json()

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"Score   : {data.get('score')}%")
print(f"Correct : {data.get('correct_count')} / {data.get('total_count')}")
print(f"Message : {data.get('message')}")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")