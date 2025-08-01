data = {
    "hi": "Hi there! I'm a friendly chatbot here to assist you.",
    "hello": "Hello! How can I help you today?",
    "what is your name": "I'm just a chatbot, so I don't have a name, but you can call me ChatBot.",
    "where are you from": "I'm from the digital world, always ready to chat!",
    "how are you": "I'm just a chatbot, but I'm here to assist you.",
    "do you have any hobbies or interests?": "I'm always busy helping users, so my hobby is chatting with people like you!",
    "what did you eat today": "I don't eat, but I can help you find delicious recipes and food-related information.",
    "what is your favorite color?": "I'm a chatbot, so I don't have personal preferences for colors.",
    "do you enjoy listening to music?": "I can't listen to music, but I'm here to chat about it!",
    "bye": "Bye! Take care and have a great day!"
}

def get_response(user_input):
    for pattern, response in data.items():
        if pattern in user_input.lower():
            return response
    return "I'm sorry, I didn't understand that. Can you please rephrase your sentence?"

print("Chatbot: Hi! I'm a simple chatbot, I'm here to assist you!")

while True:
    user_input = input("Me: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
