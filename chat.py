def chatbot_response(user_input, user_name):
    responses = {
        "hello": f"Hello, {user_name}! How can I assist you today?",
        "how are you?": f"I'm just a program, so I'm always good! How about you, {user_name}?",
        "what time is it?": "I can't tell the exact time, but you can check your watch or phone.",
        "what's your name?": "I'm a simple chatbot created to assist you.",
        "goodbye": f"Goodbye, {user_name}! Have a great day!",
    }
    
    user_input = user_input.lower()
    
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm sorry, I don't understand your question."

def main():
    print("Hello! I'm a simple chatbot.")
    user_name = input("What's your name? ")
    print(f"Nice to meet you, {user_name}! Type 'goodbye' to exit.")
    
    while True:
        user_input = input(f"{user_name}: ")
        if user_input.lower() == "goodbye":
            print(f"Chatbot: Goodbye, {user_name}! Have a great day!")
            break
        response = chatbot_response(user_input, user_name)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()