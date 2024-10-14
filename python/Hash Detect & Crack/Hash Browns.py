import hashlib
from tkinter import *
from tkinter import messagebox

# Supported hash types, need to add more in the future.
# Stack says that this may require importing different packages.
# This also includes more distros for detecting the hash type.
# Need more research
hash_names = [
    'blake2b', 
    'blake2s', 
    'md5', 
    'sha1', 
    'sha224', 
    'sha256', 
    'sha384', 
    'sha3_224', 
    'sha3_256', 
    'sha3_384', 
    'sha3_512', 
    'sha512',
    'sha512_224',  
    'sha512_256',  
    'sha3_128',    
    'shake_128',   
    'shake_256',
    'crc32',
    'crc32c',
    'ripemd160',
    'tiger',
    'whirlpool',
    'gost',
    'fletcher32'
]

def detect_hash_type(hash_value):
    for hash_type in hash_names:
        try:
            hash_fn = getattr(hashlib, hash_type, None)
            if hash_fn:
                test_hash = hash_fn(b'test').hexdigest()
                if len(test_hash) == len(hash_value):
                    return hash_type
        except Exception as e:
            continue
    return None  # If no hash type matches, return None


def create_gui():
    root = Tk()
    root.title("Hash Browns")
    root.geometry("400x300")

    root.configure(bg="#D9EAF5")  

    Label(root, text="Enter Hash:", bg="#D9EAF5", font=('Comic Sans MS', 12)).pack(pady=5)
    hash_input = Entry(root, width=50)
    hash_input.pack(pady=5)

    Label(root, text="Enter Wordlist File Path:", bg="#D9EAF5", font=('Comic Sans MS', 12)).pack(pady=5)
    wordlist_input = Entry(root, width=50)
    wordlist_input.pack(pady=5)

    detected_label = Label(root, text="Detected Hash Type: Not yet detected", fg="blue", bg="#D9EAF5", font=('Comic Sans MS', 12))
    detected_label.pack(pady=10)

    def detect_and_show_hash_type():
        user_hash = hash_input.get().strip()
        detected_hash = detect_hash_type(user_hash)
        if detected_hash:
            detected_label.config(text=f"Detected Hash Type: {detected_hash}")
        else:
            detected_label.config(text="Detected Hash Type: Unknown")

    def crack_hash():
        user_hash = hash_input.get().strip()
        wordlist_path = wordlist_input.get().strip()
        hash_type = detect_hash_type(user_hash)
        
        if not hash_type:
            messagebox.showerror("Error", "Could not detect the hash type.")
            return

        try:
            with open(wordlist_path, 'r') as wordlist:
                for line in wordlist:
                    if hashlib.new(hash_type, line.strip().encode()).hexdigest() == user_hash:
                        messagebox.showinfo("Success", f"Password found: {line.strip()}")
                        return
            messagebox.showwarning("Failed", "Password not found in wordlist")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    detect_button = Button(root, text="Detect Hash Type", command=detect_and_show_hash_type, bg="#64B5F6", fg="white", font=('Comic Sans MS', 12))
    detect_button.pack(pady=5)

    crack_button = Button(root, text="Crack Hash", command=crack_hash, bg="#42A5F5", fg="white", font=('Comic Sans MS', 12))
    crack_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
