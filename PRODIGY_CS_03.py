
import tkinter as tk
from tkinter import messagebox
import re


def check_password_strength():
    password = entry.get()
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Use at least one special character.")


    if strength == 5:
        result = "Very Strong"
        color = "green"
    elif strength == 4:
        result = "Strong"
        color = "blue"
    elif strength == 3:
        result = "Moderate"
        color = "orange"
    elif strength == 2:
        result = "Weak"
        color = "orangered"
    else:
        result = "Very Weak"
        color = "red"


    result_label.config(text=f"Password Strength: {result}", fg=color)
    feedback_text.delete("1.0", tk.END)
    if feedback:
        feedback_text.insert(tk.END, "Suggestions:\n" + "\n".join(f"- {f}" for f in feedback))
    else:
        feedback_text.insert(tk.END, "Good job! Your password is strong.")


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)


tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show='*', width=30, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Check Strength", command=check_password_strength, bg="blue", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

feedback_text = tk.Text(root, height=6, width=45, font=("Arial", 10))
feedback_text.pack(pady=10)

root.mainloop()
