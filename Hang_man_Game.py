import tkinter as tk
from tkinter import messagebox
import random

# List of words for Hangman game
word_list = ["python", "java", "programming", "hangman", "developer", "computer"]

# Initialize the main window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("500x500")
root.config(bg="#f4f4f4")

# Game variables
word = random.choice(word_list).upper()
guessed_word = ["_" for _ in word]
attempts_left = 6
guessed_letters = []

# Function to update the word display
def update_word_display():
    word_display.config(text=" ".join(guessed_word))

# Function to reset the game
def reset_game():
    global word, guessed_word, attempts_left, guessed_letters
    word = random.choice(word_list).upper()
    guessed_word = ["_" for _ in word]
    attempts_left = 6
    guessed_letters = []
    update_word_display()
    feedback_label.config(text="Guess a letter!")
    attempts_label.config(text=f"Attempts left: {attempts_left}")
    for button in letter_buttons.values():
        button.config(state="normal", bg="#ffffff")

# Function to handle a letter guess
def guess_letter(letter):
    global attempts_left

    letter_buttons[letter].config(state="disabled", bg="#b3b3b3")
    guessed_letters.append(letter)

    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                guessed_word[i] = letter
        update_word_display()
        if "_" not in guessed_word:
            feedback_label.config(text="You guessed the word!", fg="green")
            disable_buttons()
            messagebox.showinfo("Hangman Game", f"Congratulations! You guessed the word: {word}")
    else:
        attempts_left -= 1
        attempts_label.config(text=f"Attempts left: {attempts_left}")
        if attempts_left == 0:
            feedback_label.config(text=f"You lost! The word was {word}.", fg="red")
            disable_buttons()
            messagebox.showinfo("Hangman Game", f"Game Over! The word was: {word}")

# Function to disable all letter buttons
def disable_buttons():
    for button in letter_buttons.values():
        button.config(state="disabled")

# UI Components
title_label = tk.Label(root, text="Hangman Game", font=("Helvetica", 20, "bold"), bg="#f4f4f4", fg="#333")
title_label.pack(pady=20)

word_display = tk.Label(root, text=" ".join(guessed_word), font=("Helvetica", 18), bg="#f4f4f4", fg="#333")
word_display.pack(pady=20)

feedback_label = tk.Label(root, text="Guess a letter!", font=("Helvetica", 14), bg="#f4f4f4", fg="#555")
feedback_label.pack(pady=10)

attempts_label = tk.Label(root, text=f"Attempts left: {attempts_left}", font=("Helvetica", 14), bg="#f4f4f4", fg="#555")
attempts_label.pack(pady=10)

# Frame for letter buttons
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=20)

# Creating letter buttons A-Z
letter_buttons = {}
for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    button = tk.Button(button_frame, text=letter, font=("Helvetica", 14), width=4, height=2, bg="#ffffff", 
                       command=lambda l=letter: guess_letter(l))
    button.grid(row=i // 9, column=i % 9, padx=5, pady=5)
    letter_buttons[letter] = button

# Reset button
reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 14), bg="#ff6666", fg="#ffffff", command=reset_game)
reset_button.pack(pady=20)

# Start the game with the initial display
update_word_display()

# Run the application
root.mainloop()
