
import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="AI Design Assistant", layout="centered")

st.title("🎨 AI Design Assistant for Creatives")

st.markdown("Upload your moodboard images and describe the style you're aiming for. This tool will analyze your input and generate a design concept.")

# Upload section
uploaded_files = st.file_uploader("Upload Moodboard Images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

# Text input
style_prompt = st.text_input("Style Direction (e.g., 'playful minimalist for a skincare brand')")

if st.button("Generate Design Concept"):
    if uploaded_files and style_prompt:
        st.success("Moodboard and style prompt received!")
        st.markdown("### 🔍 AI-Generated Interpretation (Coming Soon)")
        st.markdown("**Color Palette**: Soft pink, muted olive, warm beige  
**Font Pairing**: 'Playfair Display' with 'Lato'  
**Layout Idea**: Clean hero section with large central image and minimal text")
        st.markdown("➡️ In the future, this will return a downloadable .ai, .svg, or Figma frame.")

        st.markdown("---")
        st.markdown("#### Uploaded Moodboard")
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            st.image(image, caption=uploaded_file.name, use_column_width=True)
    else:
        st.error("Please upload at least one image and provide a style direction.")
