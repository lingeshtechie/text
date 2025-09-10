import streamlit as st
from modules.generator import generate_text

prompt = st.text_input("Enter your prompt:")

if st.button("Generate"):
    if prompt and prompt.strip():  # Ensure prompt is not empty or only whitespace
        with st.spinner("Generating..."):
            result = generate_text(prompt)
            st.success("Success!")
            st.write(result)  # Display the generated result
    else:
        st.warning("Please enter the prompt correctly.")
    