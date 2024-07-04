import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Import operations
from src.Operations.compare_and_find_matching import compare_and_find_matching
# from src.Operations.compare_and_find_missing import compare_and_find_missing
# from src.Operations.remove_duplicates import remove_duplicates
# from src.Operations.sort_count_summarize import sort_count_summarize
from src.gui_criteria import CriteriaGUI

# Function to select files
def select_files(entry_widget):
    files = filedialog.askopenfilenames(filetypes=[("Excel files", "*.xlsx *.xls")])
    if files:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, ", ".join(files))

# Function to select a directory
def select_directory(entry_widget):
    directory = filedialog.askdirectory()
    if directory:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, directory)

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

        # File Entry and Button
        self.file_entry = ctk.CTkEntry(self.main_frame, width=400)
        self.file_entry.grid(row=0, column=0, pady=10, padx=10)
        self.file_button = ctk.CTkButton(self.main_frame, text="Select File", command=lambda: select_files(self.file_entry))
        self.file_button.grid(row=0, column=1, pady=10, padx=10)

        # Directory Entry and Button
        self.dir_entry = ctk.CTkEntry(self.main_frame, width=400)
        self.dir_entry.grid(row=1, column=0, pady=10, padx=10)
        self.dir_button = ctk.CTkButton(self.main_frame, text="Select Directory", command=lambda: select_directory(self.dir_entry))
        self.dir_button.grid(row=1, column=1, pady=10, padx=10)

        # Execute Button
        self.execute_button = ctk.CTkButton(self.main_frame, text="Execute", command=self.execute_operations)
        self.execute_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

    def execute_operations(self):
        try:
            file_path = self.file_entry.get()
            directory_path = self.dir_entry.get()
            
            if self.toggle_match.get():
                compare_and_find_matching(
                    missing_list_path=file_path, 
                    tracking_folder_path=directory_path, 
                    imei_folder_path=directory_path,
                    found_tracking_path=os.path.join(directory_path, 'Found_Tracking.xlsx'),
                    found_imei_path=os.path.join(directory_path, 'Found_IMEI.xlsx'),
                    not_found_path=os.path.join(directory_path, 'Not_Found.xlsx')
                )
            elif self.toggle_criteria.get():
                criteria_window = CriteriaGUI(self, file_path)
                criteria_window.grab_set()

            # Add similar blocks for other operations here...

            messagebox.showinfo("Success", "Operation completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    app = GodExcelApp()
    app.mainloop()
