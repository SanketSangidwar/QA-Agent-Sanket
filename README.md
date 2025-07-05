# QAAgent Task – Sanket Sangidwar

## Modules

- `transcribe.py`: Extracts transcript from Recruter.ai YouTube video
- `generate_test_cases.py`: Uses OpenAI GPT to produce test case JSON
- `convert_to_playwright.py`: Converts test JSON to Playwright script
- `qa-tests.spec.ts`: Sample test script
- `dashboard.py`: Streamlit dashboard for result viewing
- `test_cases.json`: Sample JSON test cases
- `.gitignore`: Ignore Python & Node.js generated files

## How to Run

```bash
# Step 1: Transcribe
python transcribe.py

# Step 2: Generate test cases
python generate_test_cases.py

# Step 3: Convert to Playwright
python convert_to_playwright.py

# Step 4: Run Playwright tests
npx playwright test

# Step 5: Launch dashboard
streamlit run dashboard.py
```
