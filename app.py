import streamlit as st
from connect_memory_with_llm import get_answer

st.set_page_config(
    page_title="MediBot",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 MediBot")

st.write(
    "AI-powered Medical Question Answering System"
)

st.markdown("---")

query = st.text_input(
    "Enter your medical question:",
    placeholder="e.g. What is cancer?"
)

if st.button("🔍 Ask MediBot"):

    if query.strip():

        with st.spinner("MediBot is thinking..."):

            try:
                response, pages = get_answer(query)

                st.subheader("🤖 Answer")
                st.write(response)

                st.subheader("📄 Source Page(s)")

                if pages:
                    for page in pages:
                        st.write(f"Page {page}")
                else:
                    st.write("Source page not available.")

            except Exception as e:
                st.error(f"Error occurred: {e}")

    else:
        st.warning("Please enter a medical question.")

st.markdown("---")

st.info(
    "⚕️ This chatbot is for educational purposes only. "
    "It is not a substitute for professional medical advice."
)