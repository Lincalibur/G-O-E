import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
import os
from src.Operations.look_for_lines_meeting_criteria import apply_criteria

class CriteriaGUI(ctk.CTkToplevel):
    def __init__(self, master=None, file_path=None):
        super().__init__(master)
        self.title("Add Criteria")
        self.geometry("600x400")

        self.file_path = file_path
        self.criteria = []

        self.column_label = ctk.CTkLabel(self, text="Column Name:")
        self.column_label.grid(row=0, column=0, padx=10, pady=10)
        self.column_entry = ctk.CTkEntry(self)
        self.column_entry.grid(row=0, column=1, padx=10, pady=10)

        self.condition_label = ctk.CTkLabel(self, text="Condition:")
        self.condition_label.grid(row=0, column=2, padx=10, pady=10)
        self.condition_entry = ctk.CTkEntry(self)
        self.condition_entry.grid(row=0, column=3, padx=10, pady=10)

        self.add_button = ctk.CTkButton(self, text="Add", command=self.add_condition)
        self.add_button.grid(row=0, column=4, padx=10, pady=10)

        self.criteria_text = tk.Text(self, height=10, width=70)
        self.criteria_text.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

        self.save_button = ctk.CTkButton(self, text="Save", command=self.save_criteria)
        self.save_button.grid(row=2, column=0, columnspan=5, pady=10)

    def add_condition(self):
        column = self.column_entry.get().strip()
        condition = self.condition_entry.get().strip()
        if column and condition:
            criterion = f'{column} looking for {condition}'
            self.criteria.append(criterion)
            self.criteria_text.insert(tk.END, criterion + "\n")
            self.column_entry.delete(0, tk.END)
            self.condition_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Both Column Name and Condition must be filled.")

    def save_criteria(self):
        criteria_file_path = "criteria.txt"
        with open(criteria_file_path, 'w') as f:
            for criterion in self.criteria:
                f.write(criterion + "\n")

        output_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if output_path:
            apply_criteria(self.file_path, criteria_file_path, output_path)
            messagebox.showinfo("Success", f"Criteria applied and saved to {output_path}")
        self.destroy()
