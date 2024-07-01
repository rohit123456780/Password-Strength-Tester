import tkinter as tk
import string
import math

class PasswordStrengthTester:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Strength Tester")

        self.label = tk.Label(master, text="Enter your password:")
        self.label.pack()

        self.password_entry = tk.Entry(master, show='*', width=50)
        self.password_entry.pack()

        self.check_button = tk.Button(master, text="Check Strength", command=self.check_strength)
        self.check_button.pack()

        self.result_label = tk.Label(master, text="", fg="blue")
        self.result_label.pack()

    def check_strength(self):
        password = self.password_entry.get()
        strength = self.evaluate_password(password)
        self.result_label.config(text=strength)

    def evaluate_password(self, password):
        length = len(password)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
        entropy = self.calculate_entropy(password)

        if length < 6:
            return f"Weak: Too short (entropy: {entropy:.2f} bits)"
        elif length >= 6 and length < 8 and (has_upper or has_lower) and has_digit:
            return f"Weak: Length >= 6 but < 8, and lacks complexity (entropy: {entropy:.2f} bits)"
        elif length >= 8 and (has_upper and has_lower and has_digit and has_special):
            return f"Strong (entropy: {entropy:.2f} bits)"
        else:
            return f"Medium (entropy: {entropy:.2f} bits)"

    def calculate_entropy(self, password):
        charset_size = 0
        if any(c.islower() for c in password):
            charset_size += 26
        if any(c.isupper() for c in password):
            charset_size += 26
        if any(c.isdigit() for c in password):
            charset_size += 10
        if any(c in string.punctuation for c in password):
            charset_size += len(string.punctuation)
        
        if charset_size == 0:
            return 0

        entropy = len(password) * math.log2(charset_size)
        return entropy

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthTester(root)
    root.mainloop()
