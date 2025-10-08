# laila_chatbot.py

def laila_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi! I’m Laila, your AI friend 😊"
    elif "how are you" in user_input:
        return "I’m good! What about you?"
    elif "your name" in user_input:
        return "My name is Laila, made by you 💖"
    elif "bye" in user_input:
        return "Bye! Take care 🌸"
    else:
        return "Hmm... I didn't understand that. Can you say it differently?"

# Chat loop
print("🤖 Laila: Hello! I’m ready to chat. Type 'bye' to exit.\n")
while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Laila: Bye! See you soon 💫")
        break
    print("Laila:", laila_response(user))