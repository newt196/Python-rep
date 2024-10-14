from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    """Open a file dialog to select an image (JPEG or PNG) and extract its metadata."""
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if filename:  
        extract_metadata(filename)

def extract_metadata(imagename):
    """Extract metadata from the selected image and display it in the text box."""
    if not os.path.isfile(imagename):
        messagebox.showerror("Error", f"The file {imagename} does not exist.")
        return

    try:
        image = Image.open(imagename)

        info_dict = {
            "Filename": image.filename,
            "Image Size": image.size,
            "Image Height": image.height,
            "Image Width": image.width,
            "Image Format": image.format,
            "Image Mode": image.mode,
            "Image is Animated": getattr(image, "is_animated", False),
            "Frames in Image": getattr(image, "n_frames", 1)
        }

        text_box.config(state=tk.NORMAL)  
        text_box.delete(1.0, tk.END)

        text_box.insert(tk.END, "Basic Metadata:\n")
        for label, value in info_dict.items():
            text_box.insert(tk.END, f"{label:25}: {value}\n")

        image_info = image.info
        text_box.insert(tk.END, "\nImage Specific Metadata:\n")
        if image_info:
            for key, value in image_info.items():
                text_box.insert(tk.END, f"{key:25}: {value}\n")
        else:
            text_box.insert(tk.END, "No specific metadata found.\n")

        text_box.config(state=tk.DISABLED)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract metadata: {e}")

root = tk.Tk()
root.title("Photo Juicer")
root.geometry("500x400")  
root.configure(bg="#D9EAF5") 

open_button = tk.Button(root, text="Open Image (JPEG/PNG)", command=open_file, bg="#64B5F6", fg="white", font=('Comic Sans MS', 12))
open_button.pack(padx=20, pady=20)

text_box = tk.Text(root, wrap=tk.WORD, width=60, height=20, font=('Comic Sans MS', 10))
text_box.pack(padx=10, pady=10)

text_box.config(state=tk.DISABLED)

root.mainloop()
