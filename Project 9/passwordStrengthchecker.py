import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    password = password_entry.get()

    score = 0
    feedback = []

    length_criteria = len(password) >= 8
    upper_criteria = bool(re.search(r"[A-Z]", password))
    lower_criteria = bool(re.search(r"[a-z]", password))
    digit_criteria = bool(re.search(r"[0-9]", password))
    special_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    if length_criteria:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if upper_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if lower_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if digit_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one digit.")

    if special_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one special character (!@#$%^&*...).")

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    result_label.config(text=f"Password Strength: {strength}",
                        fg="green" if strength == "Strong" else "orange" if strength == "Moderate" else "red")

    if feedback:
        messagebox.showinfo("Suggestions", "\n".join(feedback))
    else:
        messagebox.showinfo("Suggestions", "Your password is strong. Great job!")


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 16), fg="blue")
title_label.pack(pady=10)

password_label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", font=("Arial", 12), command=check_password_strength, bg="blue",
                         fg="white")
check_button.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
