import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.title("AI Blog Generator")

topic=st.text_input("Enter Blog topic")
length=st.selectbox(
    "Select Blog Length",
    [
        "Short",
        "Medium",
        "Long",
    ]
)

tone=st.selectbox(
    "Select Blog Tone",
    [
        "Professional",
        "Educational",
        "Friendly",
        "Technical",
    ]
)

if st.button("Generate Blog"):
    prompt = f"""
    Write a {length} blog on:
    
    {topic}
    
    Tone: {tone}
    
    Include:
    
    1.Catchy Title
    2.Introduction
    3.Main Content
    4.Conclusion
    """

    response=(
        client.chat.completions.create(
            model= "llama-3.3-70b-versatile",

                messages=[
                    {
                        "role":"user",
                        "content": prompt
                    }
                ]
        )
    )
    blog=response.choices[0].message.content
    st.subheader("Generated Blog")
    st.write(blog)
    st.download_button("Download Blog",
                       blog)