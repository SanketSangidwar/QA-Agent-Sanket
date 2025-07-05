import openai
import json

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_test_cases(transcript):
    prompt = f"""
    Generate Playwright-compatible frontend test cases from this how-to transcript.
    Include core flows, edge cases, accessibility, and performance scenarios.

    Transcript:
    {transcript[:4000]}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    with open("transcript.txt", "r") as f:
        transcript = f.read()

    test_json = generate_test_cases(transcript)

    with open("test_cases.json", "w") as f:
        f.write(test_json)
