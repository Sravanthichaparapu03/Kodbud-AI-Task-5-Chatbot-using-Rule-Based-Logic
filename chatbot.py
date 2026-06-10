print("Simple Chatbot")
print("Type 'bye' to exit")

while True:
    user = input("\nYou: ").lower()

    if user == "hello":
        print("Bot: Hi! How are you?")

    elif user == "hi":
        print("Bot: Hello!")

    elif user == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Bot: I am a Python Chatbot.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
