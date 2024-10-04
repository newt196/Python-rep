import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import random

# Create the main application class
class WordApp:
    def __init__(self, master):
        self.master = master
        master.title("Word Collector")
        master.configure(bg="#e0f7fa")  

        
        self.words = [] # object to store words with no pause

        
        self.prompt_label = tk.Label(master, text="Any words pertaining to the target:", bg="#e0f7fa", font=("Comic Sans MS", 14, "bold"))
        self.prompt_label.pack(pady=10)
        # Prompt info with classic style

        
        self.word_entry = tk.Entry(master, font=("Comic Sans MS", 12), width=30)
        self.word_entry.pack(pady=5)

        # Tricky, but this helps with hitting returnkey will submit the word forward into the program.
        # huge save not having to hit the submit button manually
        self.word_entry.bind("<Return>", self.submit_word)

        # Submit
        self.submit_button = tk.Button(master, text="Submit Word", command=self.submit_word, bg="#ffab40", fg="black", font=("Comic Sans MS", 12, "bold"))
        self.submit_button.pack(pady=10)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_words, bg="#ff5252", fg="white", font=("Comic Sans MS", 12, "bold"))         # Reset logic and style

        self.reset_button.pack(pady=10)

        self.word_display = tk.Text(master, height=10, width=50, state=tk.DISABLED, bg="#ffffff", font=("Comic Sans MS", 12)) # Display
        self.word_display.pack(pady=10)

        self.number_frame = tk.Frame(master, bg="#e0f7fa")  # helps frame the numbers with style
        self.number_frame.pack(pady=10)

        self.number_label = tk.Label(self.number_frame, text="How many numbers do you want to add?", bg="#e0f7fa", font=("Comic Sans MS", 12, "bold"))
        self.number_label.pack(pady=5)

        self.number_option = tk.IntVar()  # logic to add numbers to the inital list, with options
        self.number_option.set(1)  

        for i in range(1, 6):
            button = tk.Radiobutton(self.number_frame, text=str(i), variable=self.number_option, value=i, bg="#e0f7fa", font=("Comic Sans MS", 12)) # research states this is a radio button for user slection
            button.pack(side=tk.LEFT)

        self.include_symbols_var = tk.BooleanVar()
        self.include_symbols_checkbox = tk.Checkbutton(master, text="Include symbols in output (@, #, $, %, &)", variable=self.include_symbols_var, bg="#e0f7fa", font=("Comic Sans MS", 12))
        self.include_symbols_checkbox.pack(pady=5)

        self.include_random_symbols_var = tk.BooleanVar() # randomn symbols logic
        self.include_random_symbols_checkbox = tk.Checkbutton(master, text="Include random symbols in output", variable=self.include_random_symbols_var, bg="#e0f7fa", font=("Comic Sans MS", 12))
        self.include_random_symbols_checkbox.pack(pady=5)

        
        self.export_button = tk.Button(master, text="Export Words", command=self.export_words, bg="#76ff03", fg="black", font=("Comic Sans MS", 12, "bold"))
        self.export_button.pack(pady=10)
        self.export_button.config(state=tk.NORMAL)  # Export logic

    def submit_word(self, event=None):  
        word = self.word_entry.get()
        if word:
            self.words.append(word)
            self.word_entry.delete(0, tk.END)  

            
            self.word_display.config(state=tk.NORMAL)  
            self.word_display.insert(tk.END, f"{word}\n")  
            self.word_display.config(state=tk.DISABLED)  
        else:
            messagebox.showwarning("Input Error", "Please enter a word.")

    def reset_words(self):
        self.words.clear()
        self.word_display.config(state=tk.NORMAL)  
        self.word_display.delete('1.0', tk.END)  
        self.word_display.config(state=tk.DISABLED)  

         
        self.word_entry.delete(0, tk.END) # RRREEEEset

        self.number_option.set(1)
        self.include_symbols_var.set(False)
        self.include_random_symbols_var.set(False)

    def export_words(self): # need logic for exporting the ext file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt"),
                                                              ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file: # logic for writing out the file
                for word in self.words:
                    file.write(word + "\n")  # \n to add

                selected_option = self.number_option.get()
                max_number = 10 ** selected_option  

                symbols = ['@', '#', '$', '%', '&'] if self.include_symbols_var.get() else []

                for word in self.words:
                    for num in range(max_number):
                        file.write(f"{word}{num}\n")  

                        for symbol in symbols:
                            file.write(f"{word}{num}{symbol}\n")  

                        if self.include_random_symbols_var.get():
                            num_symbols_to_insert = random.randint(0, 3)
                            for _ in range(num_symbols_to_insert):
                                symbol = random.choice(symbols)
                                position = random.randint(0, len(word))  
                                word_with_symbol = word[:position] + symbol + word[position:]
                                file.write(f"{word_with_symbol}{num}\n")  

            messagebox.showinfo("Success", "Words exported successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WordApp(root)
    root.mainloop()
