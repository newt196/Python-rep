# **Simple Password Merger**

## Overview

This Python application provides an easy-to-use graphical user interface (GUI) for merging the contents of two text files into a single output file. The merged file automatically removes any duplicate lines and saves the result to a user-specified output folder.

## Features

- **Select and merge**: Choose two text files to merge.
- **Output folder**: Select the folder where the merged file will be saved.
- **Duplicate removal**: The application automatically removes duplicate lines.
- **Easy-to-use GUI**: Simple graphical interface built using Tkinter.
- **File selection**: Uses native file dialogs to select files and folders.

## Code and Logic

OS is used to create and control the logic behind the file paths that are wanting to be merged.
Tkinter is the logic behind the GUI


<img width="286" alt="image" src="https://github.com/user-attachments/assets/f498fe19-37d6-49d7-85e6-cb31a9aa3768">


I like this part because it gave me the most trouble.
Starting with the merge_files function that control each file.
We first need to look at the opening utf file 1 and file 2. UTF-8 was used because it supported all of the characters within a wordlist.
I by default used latin-8 and other symbols were not covered and the program would through an error.
Didn't know this would be an issue until running it in Chatgpt and confirming the best use in Stackoverflow. 

 For list1 = and list2= .splitlines() is a string method that splits the file content into individual lines. 
 Them removing the newline characters (\n) from each line



<img width="476" alt="image" src="https://github.com/user-attachments/assets/5afcf09a-25d2-4e5e-a3ed-30f0814565dd">


This is where the output is defined and the import OS comes in. 
The merged list is hardcoded, which I could see being an issue when merging multipel lists.
The same encoding is used just in case.


 outfile.write("%s\n" % item)  is responmcislbe for writing each line in the file. 

The %s is a placeholder for a string value. 
\n represents a newline character, which ensures that each item (line) from the list will be written on a new line in the output file.


<img width="455" alt="image" src="https://github.com/user-attachments/assets/9fe1b7d8-8fb0-492c-926c-9d6b36bf0b21">








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


### **Test**

![Application Interface](<https://github.com/user-attachments/assets/5809c25e-3ec4-48f5-94e9-4ca2486f41a5>)

![Application Interface](https://github.com/user-attachments/assets/31fed744-ebd2-406f-bf2b-c4df24628993)

![Application Interface](https://github.com/user-attachments/assets/3bb2f3b8-dfff-4ffd-90e9-11870716bdd5)







