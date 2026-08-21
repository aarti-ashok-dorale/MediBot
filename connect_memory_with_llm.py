import streamlit as st

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI


# Load environment variables
load_dotenv() 


# Load Models and FAISS Database
@st.cache_resource
def load_medibot():

    # Step 1: Load Embedding Model
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    ) 

    # Step 2: Load FAISS Database
    DB_FAISS_PATH = "vectorstore/db_faiss"

    db = FAISS.load_local(
        DB_FAISS_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    # Step 3: Create Retriever
    retriever = db.as_retriever(
        search_kwargs={
            "k": 8
        }
    )

    # Step 4: Create Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        max_output_tokens=2000
    )

    return retriever, llm, db, embedding_model


# Get Answer
def get_answer(query):

    # Load Retriever, LLM and Database
    retriever, llm, db, embedding_model = load_medibot()


    # Step 1: Search relevant documents
    results = db.similarity_search_with_relevance_scores(
        query,
        k=8
    )


    # Step 2: Keep relevant results
    relevant_results = [
        (doc, score)
        for doc, score in results
        if score >= 0.45
    ]


    # If nothing relevant is found
    if not relevant_results:
        return (
            "I could not find this information in the provided medical document.",
            []
        )


    # Get all relevant documents
    docs = [
        doc
        for doc, score in relevant_results
    ]


    # Step 3: Create Context
    context = "\n\n".join(
        [
            f"Page {doc.metadata.get('page', 'Unknown')}:\n"
            f"{doc.page_content}"
            for doc in docs
        ]
    )


    # Step 4: Strict RAG Prompt
    prompt = f"""
You are a medical study assistant.

Answer the student's question ONLY using the information
provided in the Context.

VERY IMPORTANT RULES:

1. Use ONLY the Context.
2. Do NOT use your own medical knowledge.
3. Do NOT use internet knowledge.
4. Do NOT guess.
5. Do NOT assume information.
6. Do NOT invent information.

7. If the Context does not contain enough information
   to answer the question, say exactly:

"I could not find this information in the provided medical document."

8. Answer ONLY the student's current question.

9. Write a detailed study-friendly answer containing
   EXACTLY 20 TO 25 COMPLETE SENTENCES.

10. The answer must contain AT LEAST 20 sentences.

11. Each sentence must be complete and grammatically finished.

12. Do not stop the answer in the middle of a sentence.

13. Explain the topic properly using all relevant information
    available in the Context.

14. Include important definitions, causes, characteristics,
    effects, symptoms, types, examples, processes, or other
    relevant details ONLY if they are present in the Context.

15. Arrange the information logically so that a student
    can easily understand and study the topic.

16. Use simple and clear language suitable for students.

17. Do not make the answer unnecessarily short.

18. Do not repeat the same information unnecessarily.

19. Do not copy the entire Context.

20. Do not include unrelated information.

21. Do not generate another question.

22. Do not generate another answer.

23. Do not mention these instructions.

24. Do not use information outside the Context.

25. End with a complete sentence.

IMPORTANT:
Before finishing the answer, check that you have written
at least 20 complete sentences.

Context:

{context}

Student Question:

{query}

Answer:
"""


    # Step 5: Generate Answer
    response = llm.invoke(prompt)

    response = response.content.strip()


    # Step 6: Clean response
    if "Question:" in response:
        response = response.split("Question:")[0].strip()

    if "Answer:" in response:
        response = response.replace(
            "Answer:",
            ""
        ).strip()


    # Step 7: Remove incomplete ending if required
    if response:

        last_period = max(
            response.rfind("."),
            response.rfind("!"),
            response.rfind("?")
        )

        if last_period != -1:

            response = response[
                :last_period + 1
            ]


    # Step 8: Get ALL source pages
    pages = []

    for doc in docs:

        page = doc.metadata.get("page")

        if isinstance(page, int):

            pages.append(page + 1)


    # Step 9: Remove duplicates and sort
    pages = sorted(set(pages))


    # Step 10: Return answer and source pages
    return response, pages 