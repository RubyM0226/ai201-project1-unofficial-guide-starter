from query import ask

print("UF Study Spots Guide — type 'quit' to exit\n")

while True:
    question = input("Your question: ").strip()
    if question.lower() == "quit":
        break
    if not question:
        continue
    result = ask(question)
    print(f"\nAnswer:\n{result['answer']}")
    print(f"\nSources:")
    for s in result["sources"]:
        print(f"  - {s}")
    print()