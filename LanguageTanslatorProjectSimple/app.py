import streamlit as st
from translator import translate_text, get_language_codes

# Streamlit UI Configuration
st.set_page_config(page_title="Language Translator", page_icon="🌍")

st.title("🌍 Language Translation Tool")
st.write("Translate text between multiple languages using Google Translate API.")

# Get all available languages
languages = get_language_codes()

# User Inputs
text = st.text_area("Enter text to translate:", "")

src_lang = st.selectbox("Select source language", list(languages.keys()))
dest_lang = st.selectbox("Select target language", list(languages.keys()))

# Translate button
if st.button("Translate"):
    if text.strip():
        translated_text = translate_text(text, languages[src_lang], languages[dest_lang])
        st.success(f"**Translated Text:** {translated_text}")
    else:
        st.warning("Please enter text to translate.")
