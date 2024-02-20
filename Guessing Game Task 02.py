import tkinter as tk
from tkinter import ttk
import random

class GuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def reset(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def check_guess(self, guess):
        self.attempts += 1
        if guess == self.secret_number:
            feedback = "Congratulations! You guessed the number {} correctly in {} attempts.".format(guess, self.attempts)
            return feedback
        elif guess < self.secret_number:
            return "Too low! Try again."
        else:
            return "Too high! Try again."

def handle_guess():
    guess = int(guess_entry.get())
    feedback = game.check_guess(guess)
    result_label.config(text=feedback)

def reset_game():
    game.reset()
    result_label.config(text="Game reset. Guess a new number.")

# Create main application window
root = tk.Tk()
root.title("Guessing Game")

# Create GuessingGame instance
game = GuessingGame()

# Create input widgets
instruction_label = ttk.Label(root, text="Guess a number between 1 and 100:")
instruction_label.pack(pady=10)

guess_entry = ttk.Entry(root, width=10)
guess_entry.pack()

guess_button = ttk.Button(root, text="Guess", command=handle_guess)
guess_button.pack(pady=5)

# Create reset button
reset_button = ttk.Button(root, text="Reset", command=reset_game)
reset_button.pack(pady=5)

# Create output widget
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()