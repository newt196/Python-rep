import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to merge files
def merge_files(file1, file2, output_folder):
    if os.path.exists(file1) and os.path.exists(file2):
        try:
            with open(file1, encoding="latin-1") as f1, open(file2, encoding="utf-8") as f2:
                list1 = f1.read().splitlines()
                list2 = f2.read().splitlines()

            merged_list = list(set(list1 + list2))

            output_file = os.path.join(output_folder, "merged_list.txt")
            with open(output_file, "w", encoding="utf-8") as outfile:
                for item in merged_list:
                    outfile.write("%s\n" % item)

            messagebox.showinfo("Success", f"Merged list saved to: {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showerror("Error", "One or both files do not exist")

# Function to browse and select files
def browse_file(entry):
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)

# Main GUI code
def main():
    root = tk.Tk()
    root.title("File Merger")

    # Set a blue-themed background
    root.configure(bg='#d0e7f9')

    # Set a consistent font style
    label_font = ("Helvetica", 12)
    button_font = ("Helvetica", 10, "bold")

    # File 1 select
    tk.Label(root, text="Select File 1:", bg='#d0e7f9', font=label_font).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    file1_entry = tk.Entry(root, width=50)
    file1_entry.grid(row=0, column=1, padx=10, pady=10)
    file1_button = tk.Button(root, text="Browse", bg='#005f99', fg='white', font=button_font, command=lambda: browse_file(file1_entry))
    file1_button.grid(row=0, column=2, padx=10, pady=10)

    # File 2 select
    tk.Label(root, text="Select File 2:", bg='#d0e7f9', font=label_font).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    file2_entry = tk.Entry(root, width=50)
    file2_entry.grid(row=1, column=1, padx=10, pady=10)
    file2_button = tk.Button(root, text="Browse", bg='#005f99', fg='white', font=button_font, command=lambda: browse_file(file2_entry))
    file2_button.grid(row=1, column=2, padx=10, pady=10)

    # Output folder select
    tk.Label(root, text="Select Output Folder:", bg='#d0e7f9', font=label_font).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    output_entry = tk.Entry(root, width=50)
    output_entry.grid(row=2, column=1, padx=10, pady=10)
    output_button = tk.Button(root, text="Browse", bg='#005f99', fg='white', font=button_font, command=lambda: browse_file(output_entry))
    output_button.grid(row=2, column=2, padx=10, pady=10)

    # Merge Button
    merge_button = tk.Button(root, text="Merge Files", bg='#007acc', fg='white', font=button_font, width=20, command=lambda: merge_files(file1_entry.get(), file2_entry.get(), output_entry.get()))
    merge_button.grid(row=3, column=0, columnspan=3, pady=20)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
