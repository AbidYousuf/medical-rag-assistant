# app/app.py
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
from rag.rag_pipeline import RAGPipeline

st.set_page_config(
    page_title="Medical RAG Assistant",
    layout="wide"
)

st.title("🩺 Medical RAG Assistant")
st.write("Ask questions from medical research PDFs using Retrieval-Augmented Generation.")

# Initialize RAG pipeline
@st.cache_resource
def load_rag():
    return RAGPipeline()

rag = load_rag()

# User input
query = st.text_input(
    "Enter your medical question:",
    placeholder="e.g. What are the clinical features of Wolfram syndrome?"
)

if st.button("Get Answer") and query:
    with st.spinner("Retrieving and generating answer..."):
        answer, sources = rag.run(query, top_k=3)

    st.subheader("✅ Answer")
    st.write(answer)

    st.subheader("📚 Sources")
    for src in sources:
        st.markdown(
            f"- **{src['metadata']['document']}**, Page {src['metadata']['page']}"
        )

    with st.expander("🔍 Retrieved Context"):
        for src in sources:
            st.write(src["text"])
