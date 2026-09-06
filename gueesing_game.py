import tkinter as tk
from tkinter import messagebox
import random


class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("460x520")
        self.root.resizable(False, False)

        # Colors
        self.bg = "#171923"
        self.card = "#242735"
        self.accent = "#6C63FF"
        self.accent_hover = "#7D75FF"
        self.text = "#F5F5F7"
        self.secondary = "#A0A4B8"
        self.input_bg = "#303342"
        self.success = "#4ADE80"
        self.error = "#FB7185"

        self.root.configure(bg=self.bg)

        self.number = 0
        self.attempts = 0
        self.max_attempts = 7
        self.game_active = True

        self.create_ui()
        self.new_game()

    def create_ui(self):
        # Main card
        self.card_frame = tk.Frame(
            self.root,
            bg=self.card
        )
        self.card_frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=400,
            height=450
        )

        # Title
        title = tk.Label(
            self.card_frame,
            text="Guess The Number",
            font=("Segoe UI", 24, "bold"),
            bg=self.card,
            fg=self.text
        )
        title.pack(pady=(35, 8))

        subtitle = tk.Label(
            self.card_frame,
            text="I'm thinking of a number between 1 and 100",
            font=("Segoe UI", 10),
            bg=self.card,
            fg=self.secondary
        )
        subtitle.pack()

        # Attempts label
        self.attempts_label = tk.Label(
            self.card_frame,
            text="Attempts: 0 / 7",
            font=("Segoe UI", 11, "bold"),
            bg=self.card,
            fg=self.accent
        )
        self.attempts_label.pack(pady=(25, 12))

        # Input
        self.guess_entry = tk.Entry(
            self.card_frame,
            font=("Segoe UI", 16),
            justify="center",
            bg=self.input_bg,
            fg=self.text,
            insertbackground=self.text,
            relief="flat",
            bd=0
        )
        self.guess_entry.pack(
            padx=50,
            fill="x",
            ipady=12
        )

        self.guess_entry.bind("<Return>", lambda event: self.check_guess())

        # Guess button
        self.guess_button = tk.Button(
            self.card_frame,
            text="GUESS",
            font=("Segoe UI", 11, "bold"),
            bg=self.accent,
            fg="white",
            activebackground=self.accent_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.check_guess
        )
        self.guess_button.pack(
            pady=(18, 12),
            padx=50,
            fill="x",
            ipady=10
        )

        # Status
        self.status_label = tk.Label(
            self.card_frame,
            text="Good luck!",
            font=("Segoe UI", 11),
            bg=self.card,
            fg=self.secondary,
            wraplength=330
        )
        self.status_label.pack(pady=10)

        # New game button
        self.new_game_button = tk.Button(
            self.card_frame,
            text="NEW GAME",
            font=("Segoe UI", 9, "bold"),
            bg=self.card,
            fg=self.secondary,
            activebackground=self.card,
            activeforeground=self.text,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.new_game
        )
        self.new_game_button.pack(pady=(12, 0))

    def new_game(self):
        self.number = random.randint(1, 100)
        self.attempts = 0
        self.game_active = True

        self.guess_entry.delete(0, tk.END)
        self.guess_entry.config(state="normal")
        self.guess_button.config(state="normal")

        self.attempts_label.config(
            text=f"Attempts: 0 / {self.max_attempts}"
        )

        self.status_label.config(
            text="Good luck! Make your first guess.",
            fg=self.secondary
        )

        self.guess_entry.focus()

    def check_guess(self):
        if not self.game_active:
            return

        value = self.guess_entry.get().strip()

        try:
            guess = int(value)
        except ValueError:
            self.status_label.config(
                text="Please enter a valid number.",
                fg=self.error
            )
            return

        if guess < 1 or guess > 100:
            self.status_label.config(
                text="Your number must be between 1 and 100.",
                fg=self.error
            )
            return

        self.attempts += 1

        self.attempts_label.config(
            text=f"Attempts: {self.attempts} / {self.max_attempts}"
        )

        self.guess_entry.delete(0, tk.END)

        if guess == self.number:
            self.status_label.config(
                text=f"🎉 Correct! You guessed it in {self.attempts} attempts!",
                fg=self.success
            )

            self.end_game()
            return

        if self.attempts >= self.max_attempts:
            self.status_label.config(
                text=f"Game over! The number was {self.number}.",
                fg=self.error
            )

            self.end_game()
            return

        if guess < self.number:
            self.status_label.config(
                text="Too low! Try a higher number.",
                fg=self.accent
            )
        else:
            self.status_label.config(
                text="Too high! Try a lower number.",
                fg=self.accent
            )

    def end_game(self):
        self.game_active = False

        self.guess_entry.config(state="disabled")
        self.guess_button.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGame(root)
    root.mainloop()