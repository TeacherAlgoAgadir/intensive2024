import tkinter as tk
import random

class GuessingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.target_number = random.randint(1, 100)
        self.attempts = 0
        
         # Set background color for the entire window
        self.root.config(bg="lightblue")

        # Create and place widgets
        self.instruction_label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.instruction_label.pack(pady=5)

        self.guess_entry = tk.Entry(root, width=20)
        self.guess_entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack(pady=5)

        self.restart_button = tk.Button(root, text="Restart Game", command=self.restart_game)
        self.restart_button.pack(pady=10)
        self.restart_button.config(state=tk.DISABLED)  # Initially disabled
        
    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number!")
            return

        self.attempts += 1

        if guess < self.target_number:
            self.feedback_label.config(text="Too low! Try again.")
        elif guess > self.target_number:
            self.feedback_label.config(text="Too high! Try again.")
        else:
            self.feedback_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.")
            self.restart_button.config(state=tk.NORMAL)
        
    def restart_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.feedback_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.restart_button.config(state=tk.DISABLED)
        
# Set up the main application window
root = tk.Tk()
app = GuessingGameApp(root)

# Run the application
root.mainloop()
