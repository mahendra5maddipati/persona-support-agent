from src.classifier import classify_persona
from src.rag_pipeline import LocalRAG
from src.generator import generate_response
from src.escalator import (
    should_escalate,
    generate_handoff_summary
)

rag = LocalRAG()

rag.ingest_documents()

query = input("User: ")

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

print("\nPersona:")
print(persona)

print("\nRetrieved Sources:")
for doc in docs:
    print(doc["source"])

print("\nResponse:")
print(response)

print("\nEscalated:")
print(escalated)

if escalated:

    print(
        generate_handoff_summary(
            persona,
            query,
            docs
        )
    )