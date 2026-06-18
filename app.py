import streamlit as st

from src.classifier import classify_persona
from src.rag_pipeline import LocalRAG
from src.generator import generate_response
from src.escalator import (
    should_escalate,
    generate_handoff_summary
)

st.set_page_config(
    page_title="Persona Adaptive Support Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Persona Adaptive Customer Support Agent")

st.markdown(
    """
This AI support assistant:

- Detects customer persona
- Retrieves support documentation
- Adapts response style
- Escalates when needed
"""
)

# Load KB once

if "rag" not in st.session_state:

    rag = LocalRAG()
    rag.ingest_documents()

    st.session_state.rag = rag

rag = st.session_state.rag

query = st.text_area(
    "Customer Message",
    height=150
)

if st.button("Generate Response"):

    if not query.strip():

        st.warning("Please enter a message")

    else:

        persona_data = classify_persona(query)

        persona = persona_data["persona"]

        docs = rag.retrieve(query)

        response = generate_response(
            persona,
            query,
            docs
        )

        escalated = should_escalate(
            query,
            docs
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Detected Persona")

            st.info(persona)

        with col2:

            st.subheader("Escalation Status")

            if escalated:
                st.error("Escalated")
            else:
                st.success("Resolved")

        st.subheader("Retrieved Sources")

        for doc in docs:

            st.write(
                f"📄 {doc['source']} | Score: {doc['score']}"
            )

        st.subheader("Generated Response")

        st.write(response)

        if escalated:

            st.subheader(
                "Human Handoff Summary"
            )

            st.json(
                generate_handoff_summary(
                    persona,
                    query,
                    docs
                )
            )