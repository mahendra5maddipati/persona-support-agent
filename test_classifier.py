from src.classifier import classify_persona

tests = [
    "API authentication error occurred",
    "Nothing works I am frustrated",
    "What is the business impact and timeline"
]

for msg in tests:
    print(classify_persona(msg))