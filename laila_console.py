import random

def laila_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hi": ["Hey there! 😊", "Hello! How are you?", "Hi, I’m Laila 💕"],
        "how are you": ["I'm feeling great today!", "Doing awesome! You?"],
        "your name": ["My name is Laila, your AI friend 💖"],
        "bye": ["Goodbye! Take care 💫", "See you soon 😇"]
    }

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "Hmm... batao aur (tell me more) 💭"

print("Laila: Hi! Type 'bye' to exit.")
while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Laila: Bye! 💕")
        break
    print("Laila:", laila_response(user))