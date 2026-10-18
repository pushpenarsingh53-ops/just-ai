import os
import streamlit as st
from google import genai
from google.genai import types

# Page Config
st.set_page_config(page_title="Just AI - Search Engine", page_icon="🌾")
st.title("🌱 Just AI: Farming & Books Search Engine")

# Fetch API Key
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("API Key nahi mili! Kripya Streamlit Secrets me GEMINI_API_KEY set karein.")
else:
    client = genai.Client(api_key=api_key)

    # Category Selection
    category = st.radio("Aap kya khojna chahte hain?", ["🌾 Kheti (Farming)", "📚 Kitabein (Books)"])

    # System Instructions
    if category == "🌾 Kheti (Farming)":
        system_prompt = (
            "You are Just AI, a helpful agricultural expert. "
            "Give easy-to-understand advice in Hindi or simple English about crops, fertilizers, pest control, and farming."
        )
    else:
        system_prompt = (
            "You are Just AI, a helpful book expert. "
            "Give clear summaries, main lessons, and book suggestions in Hindi or simple English."
        )

    # User Input
    user_query = st.text_input("Apna sawal yahan likhein:", placeholder="E.g. Aalu me rog niyantran ya Rich Dad Poor Dad summary")

    if st.button("Khojein (Search)"):
        if not user_query.strip():
            st.warning("Kripya pehle kuch sawal likhein!")
        else:
            with st.spinner("Just AI khoj raha hai..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-1.5-flash",
                        contents=user_query,
                        config=types.GenerateContentConfig(
                            system_instruction=system_prompt,
                            temperature=0.3
                        )
                    )
                    st.success("Parinaam:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
