# Aaron Truong
# Lab 12 CIS 247 C

import tkinter as tk
from tkinter import messagebox


class TestScoreCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Test Score Calculator")
        self.root.geometry("320x220")
        self.create_widgets()

    def create_widgets(self):
        self.entries = []
        for i in range(1, 4):
            frame = tk.Frame(self.root)
            frame.pack(pady=5)
            tk.Label(frame, text=f"Score for Test {i}:").pack(side=tk.LEFT)
            entry = tk.Entry(frame, width=10)
            entry.pack(side=tk.LEFT, padx=(10, 0))
            self.entries.append(entry)

        frame_avg = tk.Frame(self.root)
        frame_avg.pack(pady=10)
        tk.Label(frame_avg, text="Average:").pack(side=tk.LEFT)
        self.average_label = tk.Label(frame_avg, text="")
        self.average_label.pack(side=tk.LEFT, padx=(10, 0))

        frame_btn = tk.Frame(self.root)
        frame_btn.pack(pady=10)
        calculate_button = tk.Button(frame_btn, text="Calculate Average", command=self.calculate_average)
        calculate_button.pack()

    def calculate_average(self):
        try:
            scores = [float(entry.get()) for entry in self.entries]
            average = sum(scores) / len(scores)
            self.average_label.config(text=f"{average:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for all test scores.")
            self.average_label.config(text="")

    def run(self):
        self.root.mainloop()



try:
    app = TestScoreCalculator()
    app.run()
except Exception as e:
    print(f"An error occurred: {e}")
    messagebox.showerror("Error", f"An unexpected error occurred: {e}")