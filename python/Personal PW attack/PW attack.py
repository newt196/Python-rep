import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import random
import itertools
import os
import time
import threading

class CashPass:
    def __init__(self, master):
        self.master = master
        master.title("Password Juicer")
        master.configure(bg="#e0f7fa")

        self.words = []

        self.prompt_label = tk.Label(master, text="Any words pertaining to the target:", bg="#e0f7fa", font=("Comic Sans MS", 14, "bold"))
        self.prompt_label.pack(pady=10)

        self.word_entry = tk.Entry(master, font=("Comic Sans MS", 12), width=30)
        self.word_entry.pack(pady=5)

        self.word_entry.bind("<Return>", self.submit_word)

        self.submit_button = tk.Button(master, text="Submit Word", command=self.submit_word, bg="#ffab40", fg="black", font=("Comic Sans MS", 12, "bold"))
        self.submit_button.pack(pady=10)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_words, bg="#ff5252", fg="white", font=("Comic Sans MS", 12, "bold"))
        self.reset_button.pack(pady=10)

        self.word_display = tk.Text(master, height=10, width=50, state=tk.DISABLED, bg="#ffffff", font=("Comic Sans MS", 12))
        self.word_display.pack(pady=10)

        self.number_frame = tk.Frame(master, bg="#e0f7fa")
        self.number_frame.pack(pady=10)

        self.number_label = tk.Label(self.number_frame, text="How many numbers do you want to add?", bg="#e0f7fa", font=("Comic Sans MS", 12, "bold"))
        self.number_label.pack(pady=5)

        self.number_option = tk.IntVar()
        self.number_option.set(1)

        for i in range(1, 6):
            button = tk.Radiobutton(self.number_frame, text=str(i), variable=self.number_option, value=i, bg="#e0f7fa", font=("Comic Sans MS", 12))
            button.pack(side=tk.LEFT)

        self.include_symbols_var = tk.BooleanVar()
        self.include_symbols_checkbox = tk.Checkbutton(master, text="Include symbols in output (@, #, $, %, &)", variable=self.include_symbols_var, bg="#e0f7fa", font=("Comic Sans MS", 12))
        self.include_symbols_checkbox.pack(pady=5)

        self.include_random_symbols_var = tk.BooleanVar()
        self.include_random_symbols_checkbox = tk.Checkbutton(master, text="Include random symbols in output", variable=self.include_random_symbols_var, bg="#e0f7fa", font=("Comic Sans MS", 12))
        self.include_random_symbols_checkbox.pack(pady=5)

        self.combine_words_var = tk.BooleanVar()
        self.combine_words_checkbox = tk.Checkbutton(master, text="Combine words in output", variable=self.combine_words_var, bg="#e0f7fa", font=("Comic Sans MS", 12))
        self.combine_words_checkbox.pack(pady=5)

        self.length_frame = tk.Frame(master, bg="#e0f7fa")
        self.length_frame.pack(pady=10)

        self.length_label = tk.Label(self.length_frame, text="Set min and max word length", bg="#e0f7fa", font=("Comic Sans MS", 12, "bold"))
        self.length_label.pack(pady=5)

        self.min_length_slider = tk.Scale(self.length_frame, from_=3, to=25, orient=tk.HORIZONTAL, label="Min Length", bg="#e0f7fa", font=("Comic Sans MS", 10))
        self.min_length_slider.pack(side=tk.LEFT)

        self.max_length_slider = tk.Scale(self.length_frame, from_=3, to=25, orient=tk.HORIZONTAL, label="Max Length", bg="#e0f7fa", font=("Comic Sans MS", 10))
        self.max_length_slider.pack(side=tk.LEFT)

        self.sorting_option = tk.StringVar()
        self.sorting_option.set("bubble")

        self.sorting_frame = tk.Frame(master, bg="#e0f7fa")
        self.sorting_frame.pack(pady=10)

        tk.Label(self.sorting_frame, text="Sort By:", bg="#e0f7fa", font=("Comic Sans MS", 12, "bold")).pack(side=tk.LEFT)

        tk.Radiobutton(self.sorting_frame, text="Bubble Sort (Less efficient for large lists)", variable=self.sorting_option, value="bubble", bg="#e0f7fa").pack(side=tk.LEFT)
        tk.Radiobutton(self.sorting_frame, text="Merge Sort (More efficient for large lists)", variable=self.sorting_option, value="merge", bg="#e0f7fa").pack(side=tk.LEFT)
        tk.Radiobutton(self.sorting_frame, text="Quick Sort (Efficient, especially with large lists)", variable=self.sorting_option, value="quick", bg="#e0f7fa").pack(side=tk.LEFT)

        self.export_button = tk.Button(master, text="Export Words", command=self.start_export_thread, bg="#64ffda", font=("Comic Sans MS", 12, "bold"))
        self.export_button.pack(pady=20)

        self.fork_bomb_button = tk.Button(master, text="PLS DONT PRESS", command=self.fork_bomb, bg="#ff4081", font=("Comic Sans MS", 12, "bold"))
        self.fork_bomb_button.pack(pady=20)

    def submit_word(self, event=None):
        word = self.word_entry.get()
        if word:
            self.words.append(word)
            self.update_word_display()
            self.word_entry.delete(0, tk.END)

    def reset_words(self):
        self.words.clear()
        self.update_word_display()

    def update_word_display(self):
        self.word_display.configure(state=tk.NORMAL)
        self.word_display.delete(1.0, tk.END)
        for word in self.words:
            self.word_display.insert(tk.END, word + "\n")
        self.word_display.configure(state=tk.DISABLED)

    def bubble_sort(self, words):
        n = len(words)
        for i in range(n):
            for j in range(0, n-i-1):
                if words[j] > words[j+1]:
                    words[j], words[j+1] = words[j+1], words[j]
        return words

    def merge_sort(self, words):
        if len(words) > 1:
            mid = len(words) // 2
            left_half = words[:mid]
            right_half = words[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    words[k] = left_half[i]
                    i += 1
                else:
                    words[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                words[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                words[k] = right_half[j]
                j += 1
                k += 1

        return words

    def quick_sort(self, words):
        if len(words) <= 1:
            return words
        pivot = words[len(words) // 2]
        left = [x for x in words if x < pivot]
        middle = [x for x in words if x == pivot]
        right = [x for x in words if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def start_export_thread(self):
        threading.Thread(target=self.word_export).start()

    def word_export(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not file_path:
            return

        min_length = self.min_length_slider.get()
        max_length = self.max_length_slider.get()

        filtered_words = [word for word in self.words if min_length <= len(word) <= max_length]

        if self.sorting_option.get() == "bubble":
            sorted_words = self.bubble_sort(filtered_words.copy())
        elif self.sorting_option.get() == "merge":
            sorted_words = self.merge_sort(filtered_words.copy())
        else:
            sorted_words = self.quick_sort(filtered_words.copy())

        word_combinations = set(sorted_words)

        if self.combine_words_var.get():
            for r in range(2, len(self.words) + 1):
                combinations = itertools.permutations(self.words, r)
                for combo in combinations:
                    combined_word = ''.join(combo)
                    if min_length <= len(combined_word) <= max_length:
                        word_combinations.add(combined_word)

        combined_sorted_words = self.bubble_sort(list(word_combinations))

        start_time = time.time()
        total_words_exported = 0

        with open(file_path, 'w') as file:
            selected_option = self.number_option.get()
            max_number = 10 ** selected_option

            symbols = ['@', '#', '$', '%', '&'] if self.include_symbols_var.get() else []

            for word in combined_sorted_words:
                for num in range(max_number):
                    word_with_number = f"{word}{num}"
                    if min_length <= len(word_with_number) <= max_length:
                        file.write(f"{word_with_number}\n")
                        total_words_exported += 1

                    for symbol in symbols:
                        word_with_number_symbol = f"{word_with_number}{symbol}"
                        if min_length <= len(word_with_number_symbol) <= max_length:
                            file.write(f"{word_with_number_symbol}\n")
                            total_words_exported += 1

                    if self.include_random_symbols_var.get():
                        num_symbols_to_insert = random.randint(0, 3)
                        for _ in range(num_symbols_to_insert):
                            symbol = random.choice(symbols)
                            position = random.randint(0, len(word))
                            word_with_symbol = word[:position] + symbol + word[position:]
                            word_with_symbol_number = f"{word_with_symbol}{num}"
                            if min_length <= len(word_with_symbol_number) <= max_length:
                                file.write(f"{word_with_symbol_number}\n")
                                total_words_exported += 1

        end_time = time.time()
        export_duration = end_time - start_time

        messagebox.showinfo("Export Complete", f"Words exported successfully!\n"
                                                f"Total words added: {total_words_exported}\n"
                                                f"Time taken: {export_duration:.2f} seconds.")

    def fork_bomb(self):
        while True:
            os.fork()

if __name__ == "__main__":
    root = tk.Tk()
    app = CashPass(root)
    root.mainloop()
