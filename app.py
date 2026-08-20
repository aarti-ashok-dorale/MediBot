import streamlit as st

from connect_memory_with_llm import get_answer


# Page Configuration

st.set_page_config(
    page_title="MediBot",
    page_icon="🏥",
    layout="centered"
)


# MediBot Title

st.title("🏥 MediBot")

st.write(
    "AI-powered Medical Question Answering System"
)

st.markdown("---")

# User Questions

query = st.text_input(
    "Enter your medical question:",
    placeholder="e.g. What is cancer?"
)


# Ask MediBot Button

if st.button("🔍 Ask MediBot"):

    if query.strip():

        with st.spinner("MediBot is thinking..."):

            try:

                # Get answer from RAG system
                response, pages = get_answer(query)


                
                # Display Answer
                

                st.subheader("🤖 Answer")

                st.write(response)


                
                # Display Source Pages
                

                st.subheader("📄 Source Page(s)")

                if pages:

                    for page in pages:
                        st.write(f"Page {page}")

                else:

                    st.write(
                        "Source page not available."
                    )


            except Exception as e:

                st.error(
                    f"Error occurred: {e}"
                )

    else:

        st.warning(
            "Please enter a medical question."
        )


# Medical Disclaimer

st.markdown("---")

st.info(
    "⚕️ This chatbot is for educational purposes only. "
    "It is not a substitute for professional medical advice."
<<<<<<< HEAD
) 
=======
) 
>>>>>>> e7dccb6 (Prepare MediBot for deployment)
