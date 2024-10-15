# **Simple Password Merger**

## Overview

This Python application provides an easy-to-use graphical user interface (GUI) for merging the contents of two text files into a single output file. The merged file automatically removes any duplicate lines and saves the result to a user-specified output folder.

## Features

- **Select and merge**: Choose two text files to merge.
- **Output folder**: Select the folder where the merged file will be saved.
- **Duplicate removal**: The application automatically removes duplicate lines.
- **Easy-to-use GUI**: Simple graphical interface built using Tkinter.
- **File selection**: Uses native file dialogs to select files and folders.

## Requirements

You will need the following to run the application:

- **Python 3.x**
- Python libraries:
  - `tkinter` (usually pre-installed with Python)
  - `os` (part of the Python standard library)

## Installation

1. **Clone the repository** or download the code files.
2. **Ensure Python 3.x** is installed on your machine.
3. Install the required dependencies (if not already available):

    ```bash
    pip install tk
    ```

## How to Use

1. **Run the application**: Execute the script by running the following command:

    ```bash
    python main.py
    ```

2. **Select files**:
   - Click "Browse" to select File 1.
   - Click "Browse" again to select File 2.
   - Choose an output folder where the merged file will be saved.

3. **Merge the files**: 
   - Click the "Merge Files" button to start the process.
   - The merged file will be saved as `merged_list.txt` in the selected output folder.
   - A success message will appear once the merge is complete.

---

## Example Screenshots

### **File Selection Interface**

This is where you select the two text files for merging:

![File Selection Interface](https://github.com/user-attachments/assets/0bbfb613-aeae-4f74-b1da-992b3f93336b)

---

### **Merge Success Message**

A confirmation popup will appear once the files are successfully merged:

![Merge Success](https://github.com/user-attachments/assets/30cb1420-3103-4f59-86c4-74e5ac4813ba)

---

### **Application Interface**

Here is a view of the entire interface, showing file selection and output folder options:

![Application Interface](https://github.com/user-attachments/assets/106a054d-b389-4f7e-960b-3660c653e3e0)




![Application Interface](https://github.com/user-attachments/assets/3635b1e7-17d3-4c93-b276-47119bced8b4">)


