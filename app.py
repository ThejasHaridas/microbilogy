import streamlit as st
from groq import Groq

# Initialize Groq client
client = Groq(api_key="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")

# Streamlit UI
st.set_page_config(page_title="Microbiology Expert Assistant", page_icon="🧫")

st.title("🧫 Microbiology Expert Assistant")
st.write("Ask any microbiology question and get expert explanations.")

# Input box
question = st.text_area(
    "Enter your microbiology question:",
    placeholder="Example: What is the difference between gram-positive and gram-negative bacteria?"
)

# Submit button
if st.button("Get Answer"):
    
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating answer..."):
            
            completion = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a microbiology expert helping students with homework. Explain clearly and simply."
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ],
                temperature=0.3,
                max_tokens=1024
            )
            
            answer = completion.choices[0].message.content
            
            st.success("Answer:")
            st.write(answer)
