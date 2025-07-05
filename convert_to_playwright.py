import json

def json_to_playwright(json_file, output_file):
    with open(json_file) as f:
        tests = json.load(f)

    script = """
import { test, expect } from '@playwright/test';

test.describe('QA Agent Auto Tests', () => {
"""
    for i, test_case in enumerate(tests["test_cases"]):
        script += f"""
  test('{test_case["title"]}', async ({'{ page }'}) => {{
    {test_case['steps']}
  }});
"""
    script += "});"

    with open(output_file, "w") as f:
        f.write(script)

if __name__ == "__main__":
    json_to_playwright("test_cases.json", "qa-tests.spec.ts")
