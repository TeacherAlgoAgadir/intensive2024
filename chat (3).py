import datetime
import tkinter as tk
from tkinter import scrolledtext

def chatbot_response(user_input, user_name):
    responses = {
        "hello": f"Hello, {user_name}! How can I assist you today?",
        "how are you?": f"I'm just a program, so I'm always good! How about you, {user_name}?",
        "what time is it?": datetime.datetime.now().strftime("The current time is %H:%M:%S."),
        "what's your name?": "I'm a simple chatbot created to assist you.",
        "goodbye": f"Goodbye, {user_name}! Have a great day!",
        "what is the king of animals" : "is the lion",
        "what is the capital of france" : "is paris",
    }
    
    user_input = user_input.lower()
    
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm sorry, I don't understand your question."

def send_message():
    user_input = entry.get()
    if user_input:
        chat_window.configure(state='normal')
        chat_window.insert(tk.END, f"You: {user_input}\n")
        response = chatbot_response(user_input, user_name)
        chat_window.insert(tk.END, f"Chatbot: {response}\n")
        chat_window.configure(state='disabled')
        chat_window.yview(tk.END)
        entry.delete(0, tk.END)

def main():
    global user_name
    user_name = input("What's your name? ")
    
    # Tkinter setup
    root = tk.Tk()
    root.title("ChatGPT Chatbot")
    
    global chat_window
    chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=20, width=50)
    chat_window.grid(column=0, row=0, columnspan=2)
    
    global entry
    entry = tk.Entry(root, width=40)
    entry.grid(column=0, row=1)
    
    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.grid(column=1, row=1)
    
    root.mainloop()

if __name__ == "__main__":
    main()
