import streamlit as st
import openai

# Initialize the OpenAI API with your API key
openai.api_key = 'your_openai_api_key'

def review_code(code):
    # Use the OpenAI API to review the code
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Review the following Python code and identify potential bugs, errors, or areas of improvement:\n\n{code}\n\nProvide suggestions for fixes and improvements along with fixed code snippets.",
        max_tokens=500
    )
    return response.choices[0].text.strip()

def main():
    st.title("GenAI App - AI Code Reviewer")
    st.write("Submit your Python code for review and receive feedback on potential bugs along with suggestions for fixes.")
    
    code = st.text_area("Enter your Python code here:", height=300)
    if st.button("Review Code"):
        if code.strip() == "":
            st.error("Please enter some code to review.")
        else:
            with st.spinner("Reviewing code..."):
                review = review_code(code)
            st.subheader("Code Review Feedback")
            st.write(review)

if __name__ == "__main__":
    main()