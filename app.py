import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Joke Explainer AI", page_icon="🤖")

st.title("🤖 Joke Explainer using GPT-4o Mini")
st.write("Enter a joke and let AI explain it!")

# Check token
if not os.getenv("GITHUB_TOKEN"):
    st.error("GITHUB_TOKEN not found. Please configure your .env file.")
    st.stop()

# User Input
joke_input = st.text_area("Enter your joke here:")

if st.button("Explain Joke"):
    if joke_input.strip() == "":
        st.warning("Please enter a joke first.")
    else:
        client = OpenAI(
            base_url="https://models.github.ai/inference",
            api_key=os.getenv("GITHUB_TOKEN"),
        )

        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="openai/gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that explains jokes clearly."},
                    {"role": "user", "content": joke_input},
                ],
                temperature=0.7,
                max_tokens=500,
            )

            explanation = response.choices[0].message.content
            st.success("Explanation:")
            st.write(explanation)