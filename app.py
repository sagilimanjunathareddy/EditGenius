import streamlit as st
from scraper import scrape_website
from ai_engine.ai_writer import generate_content
from screenshot import capture_screenshot
from utils import save_as_pdf, save_feedback
import os

st.set_page_config(page_title="EditGenius AI Rewriter", layout="wide")
st.title("🧠 EditGenius - AI Content Improver")
st.sidebar.header("📎 Tools")


url = st.text_input("Enter URL to scrape:")


if "original" not in st.session_state:
    st.session_state.original = ""
if "rewritten" not in st.session_state:
    st.session_state.rewritten = ""


if st.button("Scrape & Rewrite"):
    if url:
        with st.spinner("Scraping website..."):
            original = scrape_website(url)
            st.session_state.original = original

        with st.spinner("Rewriting with AI..."):
            rewritten = generate_content(original)
            st.session_state.rewritten = rewritten


if st.session_state.original:
    st.subheader("📜 Original Content")
    st.text_area("Original Text", value=st.session_state.original, height=200)

if st.session_state.rewritten:
    st.subheader("✍️ Rewritten Content")
    st.text_area("Rewritten Text", value=st.session_state.rewritten, height=200)

 
    if st.sidebar.button("📸 Capture Screenshot"):
        screenshot_path = capture_screenshot()
        if screenshot_path:
            st.sidebar.success("Screenshot saved!")
            st.sidebar.image(screenshot_path, use_container_width=True)


    if st.sidebar.button("💾 Save as PDF"):
        pdf_path = save_as_pdf(st.session_state.original, st.session_state.rewritten)
        if pdf_path:
            with open(pdf_path, "rb") as f:
                st.sidebar.download_button("⬇️ Download PDF", f, file_name=os.path.basename(pdf_path), mime="application/pdf")

    if st.sidebar.button("📝 Save Feedback"):
        feedback_path = save_feedback(st.session_state.original, st.session_state.rewritten)
        if feedback_path:
            with open(feedback_path, "rb") as f:
                st.sidebar.download_button("⬇️ Download Feedback", f, file_name=os.path.basename(feedback_path), mime="text/plain")


elif url:
    st.warning("Click 'Scrape & Rewrite' to generate content.")
