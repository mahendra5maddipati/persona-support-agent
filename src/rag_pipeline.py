import os
from pypdf import PdfReader


class LocalRAG:

    def __init__(self):
        self.documents = []

    def load_document(self, filepath):

        if filepath.endswith(".pdf"):

            reader = PdfReader(filepath)

            text = ""

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text

            return text

        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    def ingest_documents(self):

        data_folder = "data"

        for filename in os.listdir(data_folder):

            filepath = os.path.join(
                data_folder,
                filename
            )

            text = self.load_document(filepath)

            self.documents.append({
                "source": filename,
                "content": text
            })

    def retrieve(self, query, top_k=3):


        stop_words = {
            "how", "do", "i", "my", "is",
            "the", "a", "an", "to", "of",
            "and", "for", "in", "on", "with"
        }

        query_words = [
            word.lower()
            for word in query.split()
            if word.lower() not in stop_words
        ]

        results = []

        for doc in self.documents:

            score = 0

            content = doc["content"].lower()

            source = doc["source"].lower()

            for word in query_words:

                if word in content:
                    score += 2

                if word in source:
                    score += 5

            results.append({
                "source": doc["source"],
                "content": doc["content"][:500],
                "score": score
            })

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results[:top_k]