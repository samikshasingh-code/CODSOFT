# Simple Rule-Based Chatbot
# Created as part of internship task

def chatbot():
    print("Bot: Hello! I’m your friendly chatbot. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Bot: Goodbye! Have a nice day 😊")
            break

        elif user_input in ["hello", "hi", "hey"]:
            print("Bot: Hi there! How can I help you?")

        elif "how are you" in user_input:
            print("Bot: I’m doing great! Thanks for asking. How about you?")

        elif "your name" in user_input:
            print("Bot: I’m a simple chatbot, still waiting for a cool name!")

        elif "help" in user_input:
            print("Bot: Sure! You can ask me things like 'what can you do', 'tell me a joke', or 'who created you'.")

        elif "what can you do" in user_input:
            print("Bot: I can chat with you using simple rules. I can also tell jokes!")

        elif "joke" in user_input:
            print("Bot: Why did the computer go to the doctor? Because it had a virus! 😄")

        elif "who created you" in user_input:
            print("Bot: I was created by a human, just like you — as part of an internship project!")

        else:
            print("Bot: Hmm... I’m not sure how to respond to that. Try asking something else.")

# Start the chatbot
chatbot()
