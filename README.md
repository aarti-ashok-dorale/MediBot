# 🩺 MediBot – AI Medical PDF Study Assistant

MediBot is an AI-powered medical study assistant that uses **RAG (Retrieval-Augmented Generation)** to answer questions from a pre-loaded medical PDF document.

It uses **LangChain, FAISS, Hugging Face embeddings, and Google Gemini 2.5 Flash** to retrieve relevant information and generate answers with source-page references.

> ⚠️ This chatbot is for educational purposes only and is not a substitute for professional medical advice.

---

## 🚀 Live Demo

🔗 **Streamlit Community Cloud:**  
https://medibot-4i7wtumxxruckjjjjlzged.streamlit.app/

---

## ✨ Features

- Ask questions from a pre-loaded medical PDF
- Retrieval-Augmented Generation (RAG)
- Hugging Face `all-MiniLM-L6-v2` embeddings
- FAISS vector database for similarity search
- Google Gemini 2.5 Flash for answer generation
- Source page references
- Simple Streamlit interface
- Deployed on Streamlit Community Cloud
- Secure API key management using environment variables / Streamlit Secrets

---

## 📄 Document Used

MediBot works with a **pre-loaded medical reference PDF** that is processed before running the application.

The PDF is converted into text chunks and stored as vectors in the FAISS database.

**Users do not need to upload a PDF.** The medical document is already processed and included with the application. Users can directly enter their medical-related questions.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini 2.5 Flash
- Hugging Face
- Sentence Transformers
- FAISS
- PyPDF
- RAG

---

## 🏗️ How It Works

```text
Pre-loaded Medical PDF
        ↓
   PDF Loading
        ↓
  Text Extraction
        ↓
   Text Chunking
        ↓
Hugging Face Embeddings
        ↓
 FAISS Vector Database
        ↓
   User Question
        ↓
   Similarity Search
        ↓
Relevant Document Chunks
        ↓
Google Gemini 2.5 Flash
        ↓
Answer + Source Page
```

---

## 🗃️ FAISS Vector Database

The medical PDF is processed into embeddings and stored in a FAISS vector database.

```text
Medical PDF
     ↓
Text Chunks
     ↓
Hugging Face Embeddings
     ↓
FAISS
```

The generated FAISS database contains:

```text
vectorstore/
└── db_faiss/
    ├── index.faiss
    └── index.pkl
```

When a user asks a question, MediBot searches this vector database to retrieve the most relevant information from the pre-loaded medical document.

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/aarti-ashok-dorale/MediBot.git
cd MediBot
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 API Key Setup

Create a `.env` file and add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_google_api_key
```
---

## ▶️ Run Locally

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📸 Screenshots

### 🏠 MediBot Interface

<!-- Add your screenshot here -->

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d4d4840c-d730-46e0-922a-dff0dffe235d" />

### 💬 Question & Answer

<!-- Add your screenshot here -->
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/082ea975-c45a-43ac-9104-4bb2c530c03b" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a62e9d3e-b8bb-48e8-bf80-3a35b8a79307" />

### 📑 Irrelevant Question & Answer

<!-- Add your screenshot here -->
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/78e3a005-d6ad-4379-98ec-1efa98c68217" /> 

### 📑 No Input Question
<!-- Add your screenshot here -->
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e6ba0676-73bf-48c4-a540-ab3c11a4c3d4" />

---
---

## ☁️ Deployment

MediBot is deployed using **Streamlit Community Cloud**.

### Deployment Configuration

- **Repository:** `MediBot`
- **Branch:** `main`
- **Main file:** `app.py`
- **Platform:** Streamlit Community Cloud
- **Secrets:** Google Gemini API key
-  **Live Application**
-  
## 📌 Future Improvements

- 💬 Conversational chat history
- 📚 Support for multiple pre-loaded medical PDFs
- 🔎 Improved document retrieval
- 🎤 Voice-based questions
- 🌐 Support for additional LLMs
- 🎨 Improved user interface
- 📑 More detailed source citations

---

## ⚠️ Disclaimer

MediBot is developed for **educational and study purposes only**.

It should not be used for diagnosis, treatment, or making medical decisions. Always consult a qualified healthcare professional for medical advice.

---

## 👩‍💻 Author

**Aarti Ashok Dorale**

🔗 GitHub Repository:  
https://github.com/aarti-ashok-dorale/MediBot
