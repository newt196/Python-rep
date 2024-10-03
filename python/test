import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def clean_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if len(word) >= 4]
# instead of removing prep and basic words, just limited the number of char given
    return filtered_words

def extract_visible_text(soup):
    for script in soup(["script", "style"]):
# somewhat accurate, off by one or to counts when testing on different sites. 
        script.extract()  
    return soup.get_text()


# may need to clean the logic for stripping the site tags. Should be fine for now
# may need to adjust depending on the size of the site. 

def get_top_words(url, top_n=10): # 10 is default for checking, altghough 50-200 I can see being viable
    try:
        response = requests.get(url)
        if response.status_code != 200: # obvious error checking is obvious
            return f"Failed to fetch page, status code: {response.status_code}"
        
        soup = BeautifulSoup(response.content, "html.parser")
        visible_text = extract_visible_text(soup)
        words = clean_text(visible_text)
        word_counts = Counter(words)
        common_words = word_counts.most_common(top_n)
        
        return common_words
    except Exception as e:
        return str(e)

def show_top_words():
    url = url_entry.get()
    top_n = int(num_words_entry.get()) #need to define the N of the common words, hence top_n
    

    
    result = get_top_words(url, top_n)
    
    if isinstance(result, str):
        messagebox.showerror("Error", result)
    else:
        result_text.delete(1.0, tk.END)  
        for word, count in result:
            result_text.insert(tk.END, f"{word}: {count}\n") # counter end result

# Need to make more presentable
root = tk.Tk()
root.title("Words+Site=Passwords")


tk.Label(root, text="Enter URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Number of Top Words:").grid(row=1, column=0, padx=10, pady=10)
num_words_entry = tk.Entry(root, width=10)
num_words_entry.insert(tk.END, '10')  
num_words_entry.grid(row=1, column=1, padx=10, pady=10)


result_text = tk.Text(root, width=60, height=20)
result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

fetch_button = tk.Button(root, text="Get Top Words", command=show_top_words)
fetch_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
