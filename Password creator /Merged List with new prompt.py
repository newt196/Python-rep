import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to merge files
def merge_files(file1, file2, output_folder):
    if os.path.exists(file1) and os.path.exists(file2):
        # Read the contents of the files with specified encoding
        with open(file1, encoding="latin-1") as f1, open(file2, encoding="utf-8") as f2:
            list1 = f1.read().splitlines()
            list2 = f2.read().splitlines()

        # Merge and remove 
        merged_list = list(set(list1 + list2))

        output_file = os.path.join(output_folder, "New_list.txt")
        with open(output_file, "w", encoding="utf-8") as outfile:
            for item in merged_list:
                outfile.write("%s\n" % item)

        print("List saved to:", output_file)
        messagebox.showinfo("Success", f"List saved to: {output_file}")
    else:
        print("Something maybe missing?")
        messagebox.showerror("Error", "One or both of the files do not exist.")

root = tk.Tk()
root.withdraw()  # Hide the root window

file1 = filedialog.askopenfilename(title="Select the first file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
if not file1:
    messagebox.showerror("Error", "No file selected.")
    exit()

file2 = filedialog.askopenfilename(title="Select the second file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
if not file2:
    messagebox.showerror("Error", "No file selected.")
    exit()

# Define the path of the folder in use with the merged list
documents_folder = os.path.expanduser("~/Documents/wire")
if not os.path.exists(documents_folder):
    os.makedirs(documents_folder)

# Merge the files
merge_files(file1, file2, documents_folder)

# Possible incorporation of a more refined GUI that asks the user to add two lists.
# Current iteration is fine
# Should also prompt the user where to direct the file output.
# Maybe even prompt the user what changes were made and what items have been removed. 
# Possible incorporation of a more refined GUI that asks the user to add two lists.
# Current iteration is fine
# Should also prompt the user where to direct the file output.
# Maybe even prompt the user what changes were made and what items have been removed. 
# right now the documents/wire is default becasue its from an old version of this code. 
