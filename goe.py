import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

# Function to select files
def select_files(entry_widget):
    files = filedialog.askopenfilenames(filetypes=[("Excel files", "*.xlsx *.xls")])
    if files:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, ", ".join(files))

# Compare and find matching entries
def compare_and_find_matching(search_bucket_files, list_files):
    matches = []
    for search_file in search_bucket_files:
        search_df = pd.read_excel(search_file)
        for list_file in list_files:
            list_df = pd.read_excel(list_file)
            common = search_df.merge(list_df, how='inner')
            matches.append(common)
    if matches:
        result = pd.concat(matches)
        result.to_excel("data/matching_results.xlsx", index=False)
        messagebox.showinfo("Success", "Matching entries found and saved to data/matching_results.xlsx")
    else:
        messagebox.showinfo("No Matches", "No matching entries found.")

# Main Application Class
class GodExcelApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("GOE (God Of Excel)")
        self.geometry("800x600")
        
        # Sidebar Frame
        self.sidebar_frame = ctk.CTkFrame(self, width=200)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, pady=10, padx=10, sticky="ns")

        # Toggles in Sidebar
        self.toggle_match = ctk.CTkCheckBox(self.sidebar_frame, text="Compare and Find Matching")
        self.toggle_match.pack(pady=10, padx=10)
        self.toggle_missing = ctk.CTkCheckBox(self.sidebar_frame, text="Compare and Find Missing")
        self.toggle_missing.pack(pady=10, padx=10)
        self.toggle_duplicates = ctk.CTkCheckBox(self.sidebar_frame, text="Remove Duplicates")
        self.toggle_duplicates.pack(pady=10, padx=10)
        self.toggle_sort = ctk.CTkCheckBox(self.sidebar_frame, text="Sort, Count, Summarize")
        self.toggle_sort.pack(pady=10, padx=10)
        self.toggle_criteria = ctk.CTkCheckBox(self.sidebar_frame, text="Look for Lines Meeting Criteria")
        self.toggle_criteria.pack(pady=10, padx=10)

        # Main Content Frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")
        self.grid_columnconfigure(1, weight=1)

        # Search Bucket Files
        self.label_search_bucket = ctk.CTkLabel(self.main_frame, text="Search Bucket Files:")
        self.label_search_bucket.grid(row=0, column=0, pady=10, padx=10)
        self.entry_search_bucket = ctk.CTkEntry(self.main_frame, width=400)
        self.entry_search_bucket.grid(row=0, column=1, pady=10, padx=10)
        self.button_search_bucket = ctk.CTkButton(self.main_frame, text="Browse", command=lambda: select_files(self.entry_search_bucket))
        self.button_search_bucket.grid(row=0, column=2, pady=10, padx=10)

        # List Files
        self.label_list_files = ctk.CTkLabel(self.main_frame, text="List Files:")
        self.label_list_files.grid(row=1, column=0, pady=10, padx=10)
        self.entry_list_files = ctk.CTkEntry(self.main_frame, width=400)
        self.entry_list_files.grid(row=1, column=1, pady=10, padx=10)
        self.button_list_files = ctk.CTkButton(self.main_frame, text="Browse", command=lambda: select_files(self.entry_list_files))
        self.button_list_files.grid(row=1, column=2, pady=10, padx=10)

        # Run Button
        self.button_run = ctk.CTkButton(self.main_frame, text="Run", command=self.run_script)
        self.button_run.grid(row=2, column=0, columnspan=3, pady=20, padx=10)

    def run_script(self):
        search_bucket_files = self.entry_search_bucket.get().split(", ")
        list_files = self.entry_list_files.get().split(", ")
        
        if not search_bucket_files or not list_files:
            messagebox.showerror("Error", "Please specify files for both search bucket and list.")
            return
        
        if self.toggle_match.get():
            compare_and_find_matching(search_bucket_files, list_files)
        if self.toggle_missing.get():
            compare_and_find_missing(search_bucket_files, list_files)
        if self.toggle_duplicates.get():
            remove_duplicates(search_bucket_files)
        if self.toggle_sort.get():
            sort_count_summarize(search_bucket_files)
        if self.toggle_criteria.get():
            look_for_lines_meeting_criteria(search_bucket_files)
        
        messagebox.showinfo("Success", "Script executed successfully!")

if __name__ == "__main__":
    app = GodExcelApp()
    app.mainloop()
