import time
import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/ask"
HEALTH_URL = "http://127.0.0.1:8000/health"

# ======================================
# Page Configuration
# ======================================

st.set_page_config(
    page_title="Medical Research Assistant",
    page_icon="🩺",
    layout="wide"
)

# ======================================
# Sidebar
# ======================================

st.sidebar.title("🩺 MedRAG AI")

st.sidebar.markdown("""
### Medical Research Assistant

Powered by

- 🤖 Google Gemini
- 📚 ChromaDB
- 🔍 Sentence Transformers
- ⚡ FastAPI
- 🎨 Streamlit

---

Version **1.0.0**
""")

# --------------------------------------
# API Status
# --------------------------------------

try:
    health = requests.get(HEALTH_URL, timeout=5).json()
    st.sidebar.success(f"API Status: {health['status']}")
except Exception:
    st.sidebar.error("API Offline")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### About

This application uses **Retrieval-Augmented Generation (RAG)** to answer medical research questions using scientific literature.

### Workflow

1. ❓ User Question
2. 🔍 Semantic Search
3. 📚 ChromaDB Retrieval
4. 🤖 Gemini Generation
5. 📄 Source Citation
""")

st.sidebar.markdown("---")

st.sidebar.subheader("💡 Example Questions")

examples = [
    "What is deep learning in chest X-ray analysis?",
    "What are the advantages of transfer learning in medical imaging?",
    "How are transformers used in medical imaging?",
    "Explain semantic segmentation in medical images."
]

for q in examples:
    st.sidebar.caption(f"• {q}")

# ======================================
# Main Page
# ======================================

st.title("🩺 Medical Research Assistant")

st.write(
    "Ask a medical research question and receive an AI-generated answer "
    "supported by relevant scientific papers."
)

question = st.text_area(
    "Enter your medical question:",
    height=120
)

col1, col2 = st.columns([1,1])

ask_clicked = col1.button("🔎 Ask")

clear_clicked = col2.button("🗑️ Clear")

if clear_clicked:
    st.rerun()

# ======================================
# Ask Button
# ======================================

if ask_clicked:

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        start = time.time()

        with st.spinner("Searching documents and generating answer..."):

            try:

                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=120
                )

            except Exception as e:

                st.error(f"Cannot connect to API.\n\n{e}")
                st.stop()

        elapsed = time.time() - start

        if response.status_code == 200:

            data = response.json()

            st.success("Answer generated successfully!")

            st.caption(f"⏱ Response Time: **{elapsed:.2f} seconds**")

            # ==================================
            # Answer
            # ==================================

            st.subheader("📖 Answer")

            st.write(data["answer"])

            st.download_button(
                label="📄 Download Answer",
                data=data["answer"],
                file_name="medrag_answer.txt",
                mime="text/plain"
            )

            st.divider()

            # ==================================
            # Sources
            # ==================================

            st.subheader("📚 Retrieved Sources")

            st.caption(
                f"Retrieved **{len(data['sources'])}** document chunks."
            )

            for source in data["sources"]:

                score = max(
                    0.0,
                    min(
                        1.0,
                        1 - source["distance"]
                    )
                )

                with st.expander(
                    f"📄 {source['filename']} | Chunk {source['chunk_id']}"
                ):

                    c1, c2 = st.columns([1,2])

                    with c1:

                        st.metric(
                            "Similarity",
                            f"{score:.2%}"
                        )

                    with c2:

                        st.progress(score)

                    st.markdown("### 📁 Document")

                    st.code(source["filename"])

                    st.markdown("### 🔢 Chunk")

                    st.write(source["chunk_id"])

                    st.markdown("### 📏 Distance")

                    st.write(f"{source['distance']:.4f}")

                    st.markdown("### 📄 Retrieved Text")

                    st.write(source["text"])

        else:

            st.error(
                f"API Error ({response.status_code})"
            )

# ======================================
# Footer
# ======================================

st.divider()

st.markdown(
    """
<div style="text-align:center;color:gray">

🩺 <b>MedRAG AI</b>

Retrieval-Augmented Generation for Medical Research

Powered by FastAPI • Google Gemini • ChromaDB • Streamlit

Version 1.0.0

</div>
""",
    unsafe_allow_html=True
)
