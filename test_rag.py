from src.rag_pipeline import LocalRAG

rag = LocalRAG()

rag.ingest_documents()

queries = [
    "reset password",
    "API authentication",
    "duplicate billing charges"
]

for query in queries:

    print(f"\nQUERY: {query}")

    results = rag.retrieve(query)

    for item in results:
        print(
            item["source"],
            "Score:",
            item["score"]
        )