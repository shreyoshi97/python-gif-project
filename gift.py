import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("🎁 A Special Gift")
window.geometry("500x600")
window.resizable(False, False)

# Title
title = tk.Label(
    window,
    text="🎁 A Little Surprise For You 🎁",
    font=("Arial", 22, "bold")
)
title.pack(pady=30)

# Gift box
gift = tk.Label(
    window,
    text="🎁",
    font=("Arial", 120)
)
gift.pack(pady=20)

# Message
message = tk.Label(
    window,
    text="Something special is waiting inside...",
    font=("Arial", 14)
)
message.pack(pady=20)


# Function for the button
def open_gift():
    gift.config(text="💝")
    message.config(
        text="✨ SURPRISE! ✨\n\n"
             "Believe in yourself.\n"
             "Keep learning, keep dreaming,\n"
             "and never give up! 💖"
    )

    button.config(
        text="💖 Gift Opened!",
        state="disabled"
    )


# Open button
button = tk.Button(
    window,
    text="🎀 Open My Gift 🎀",
    font=("Arial", 16, "bold"),
    command=open_gift,
    padx=20,
    pady=10
)
button.pack(pady=30)

# Start the program
window.mainloop()