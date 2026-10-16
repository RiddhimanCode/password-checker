import tkinter as tk
from tkinter import ttk
from backend import password_strength  # Importing the backend logic

class PasswordCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        # Configure style
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Title Label
        title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"))
        title_label.pack(pady=15)

        # Password Input Frame
        input_frame = tk.Frame(root)
        input_frame.pack(pady=5, padx=20, fill="x")

        tk.Label(input_frame, text="Enter Password:", font=("Arial", 10)).pack(anchor="w")
        
        self.password_var = tk.StringVar()
        self.password_var.trace_add("write", self.check_password)

        self.password_entry = tk.Entry(input_frame, textvariable=self.password_var, show="*", font=("Arial", 12))
        self.password_entry.pack(fill="x", pady=5, ipady=3)

        # Show/Hide Password Checkbox
        self.show_var = tk.BooleanVar()
        show_checkbox = tk.Checkbutton(input_frame, text="Show Password", variable=self.show_var, command=self.toggle_password)
        show_checkbox.pack(anchor="w")

        # Strength Display Frame
        strength_frame = tk.Frame(root, pady=10)
        strength_frame.pack(fill="x", padx=20)

        self.strength_label = tk.Label(strength_frame, text="Strength: Very Weak", font=("Arial", 12, "bold"))
        self.strength_label.pack(anchor="w")

        self.score_label = tk.Label(strength_frame, text="Score: 0% (0 / 6)", font=("Arial", 10), fg="gray")
        self.score_label.pack(anchor="w", pady=2)

        # Criteria Checklist Frame
        criteria_frame = tk.LabelFrame(root, text=" Requirements ", font=("Arial", 10, "bold"), padx=10, pady=10)
        criteria_frame.pack(fill="both", padx=20, pady=10)

        self.criteria_labels = {}
        requirements = [
            ("length_8", "At least 8 characters"),
            ("length_12", "12+ characters (Bonus points)"),
            ("uppercase", "At least one uppercase letter (A-Z)"),
            ("digit", "At least one number (0-9)"),
            ("special", "At least one special character (!@#...)")
        ]

        for key, text in requirements:
            lbl = tk.Label(criteria_frame, text=f"❌ {text}", font=("Arial", 9), fg="red")
            lbl.pack(anchor="w", pady=1)
            self.criteria_labels[key] = (lbl, text)

    def toggle_password(self):
        if self.show_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def check_password(self, *args):
        pwd = self.password_var.get()
        result = password_strength(pwd)  # Calls the function from backend.py
        
        score = result["score"]
        percentage = result["percentage"]
        strength = result["strength"]
        details = result["details"]

        # Update Strength Text & Percentage Score (Out of 6)
        self.strength_label.config(text=f"Strength: {strength}")
        self.score_label.config(text=f"Score: {percentage}% ({score} / 6)")

        color_map = {
            "Very Weak": "#ff4d4d", # Red
            "Weak": "#ffa500",      # Orange
            "Moderate": "#cccc00",  # Yellow-Green
            "Strong": "#28a745"     # Green
        }
        self.strength_label.config(fg=color_map.get(strength, "black"))

        # Update Checklist UI
        for key, (lbl, text) in self.criteria_labels.items():
            if details[key]:
                lbl.config(text=f"✔ {text}", fg="green")
            else:
                lbl.config(text=f"❌ {text}", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordCheckerApp(root)
    root.mainloop()