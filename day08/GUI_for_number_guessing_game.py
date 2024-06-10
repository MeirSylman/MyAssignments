import random
import tkinter as tk
from tkinter import messagebox

def generate_number():
    return random.randint(1, 20)

def check_guess():
    global number_of_attempts
    guess = guess_entry.get()
    if guess == 'x':
        root.destroy()
    elif guess == 'n':
        restart_game()
    else:
        try:
            guess = int(guess)
            number_of_attempts += 1
            if guess == secret_number:
                messagebox.showinfo("Result", f"Correct! Number of guesses: {number_of_attempts}.")
                root.destroy()
            elif guess < secret_number:
                result_label.config(text="Too low! Try again.")
            else:
                result_label.config(text="Too high! Try again.")
        except ValueError:
            result_label.config(text="Use a number, 'x' to exit, or 'n' to restart.")

# Function to show the secret number
def show_secret():
    messagebox.showinfo("Secret Number", f"The secret number is: {secret_number}")

# Function to restart the game
def restart_game():
    global secret_number, number_of_attempts
    secret_number = generate_number()
    number_of_attempts = 0
    guess_entry.delete(0, tk.END)
    result_label.config(text="Game restarted. Enter your guess:")

# Function to exit the game
def exit_game():
    root.destroy()

# Main function to set up the GUI
def main():
    global root, guess_entry, result_label
    root = tk.Tk()
    root.title("Number Guessing Game")
    root.geometry("400x300")  # Set the window size

    instructions = tk.Label(root, text="Guess the number between 1 and 20.")
    instructions.pack()

    result_label = tk.Label(root, text="Enter your guess:")
    result_label.pack()

    guess_entry = tk.Entry(root)
    guess_entry.pack()

    check_button = tk.Button(root, text="Check Guess", command=check_guess)
    check_button.pack()

    cheat_button = tk.Button(root, text="Cheat", command=show_secret)
    cheat_button.pack()

    restart_button = tk.Button(root, text="Restart Game", command=restart_game)
    restart_button.pack()

    exit_button = tk.Button(root, text="Exit Game", command=exit_game)
    exit_button.pack()

    root.mainloop()

# Initialize game variables
secret_number = generate_number()
number_of_attempts = 0

if __name__ == "__main__":
    main()

