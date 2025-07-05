import streamlit as st
import os

st.title("QA Agent Test Results")

if st.button("Run Playwright Tests"):
    os.system("npx playwright test qa-tests.spec.ts --output reports")
    st.success("Tests Executed!")

if os.path.exists("reports"):
    for root, _, files in os.walk("reports"):
        for file in files:
            if file.endswith(".png"):
                st.image(os.path.join(root, file), caption=file)
            elif file.endswith(".txt"):
                with open(os.path.join(root, file)) as f:
                    st.code(f.read())
