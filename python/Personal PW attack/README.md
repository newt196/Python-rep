# Password Juicer

**Version 2.0 Update**

Password Juicer is a Python-based wordlist generator designed to create optimized password lists for selected targets, websites, or specific user inputs.

---

## What's New in Version 2.0?

- **Enhanced List Generation:** Users can now select from small, medium, and large wordlists depending on their needs.
- **Threading Implementation:** Threading has been added to improve performance, especially for larger wordlists, preventing crashes caused by too many word entries.
- **Improved Customization:** New options allow for greater control over the generated wordlist, providing flexibility for various use cases.

---

## Key Features

- **Custom Wordlist Sizes:**
    - Small, medium, and large list generation for different target scenarios.
    - Optimized sorting and filtering methods for handling lists of varying sizes.

    ![Small List](https://github.com/user-attachments/assets/7f66797b-203b-4d2f-98d8-a7b1e219ec03)
    *Small List*

    ![Medium List](https://github.com/user-attachments/assets/f5b5c882-e6f9-46f8-b08b-9c60d0b3f20b)
    *Medium List*

    ![Large List](https://github.com/user-attachments/assets/beb38a44-754f-4b64-b855-258a99be9381)
    *Large List*

- **Wordlist Generation for Targeted Inputs:**
    - Create wordlists based on known details about a target, such as name, website, or other relevant information.

    ![Target Input](https://github.com/user-attachments/assets/a0e7dda8-4868-425f-8b13-4e436f864ed3)

- **File Saving and Exporting:**
    - Prompt the user for a destination to save the generated wordlist as a `.txt` file.

    ![Save Prompt](https://github.com/user-attachments/assets/b64a61df-342e-4922-a3b9-5d14d20b83c1)

    - Confirmation of successful file saving.

    ![Save Confirmation](https://github.com/user-attachments/assets/55a29861-3bce-4f4a-9f50-bcc0d8e3e89f)

- **Results Overview:**
    - Once the wordlist is generated, results are displayed for user review.

    ![Results](https://github.com/user-attachments/assets/42f90d77-642c-4560-b6c3-71b19e58123d)

---

**Code Breadkdown**

<img width="292" alt="image" src="https://github.com/user-attachments/assets/86581f2c-0cc5-4c73-aebf-364f3b83a7ff">

Main Imports and Blocks that help run the program. 
** A few notes is that within tkinter(messagebox & filedialog) help control the info and feedback provided within the program. 
** This includes errors and notifications


<img width="355" alt="image" src="https://github.com/user-attachments/assets/ad086355-3e3d-40f1-9eba-b198cf647e2f">

The main Class within cashpass that helps maintain fucntions, and vairables within the main program. Mainly gui and logic control.

**Im not going to get into the style and formatting of the format. 

<img width="296" alt="image" src="https://github.com/user-attachments/assets/a9ea3c04-2c8e-4e99-aa34-6a5a75587378">

Medthod that is called when the user submits a word, start of the program. 

            self.words.append(word)

Appending words into the program with submit and enter. 
            
            self.update_word_display()

a if statments is used to add, and display the word that the user has choosen. 




<img width="317" alt="image" src="https://github.com/user-attachments/assets/c204f6e7-68a8-4e49-be12-408ecb11b22c">
Reset words and update word display is used to better control the flow of variables within the program. 

ALGO 


<img width="350" alt="image" src="https://github.com/user-attachments/assets/46d995c6-0d3c-4995-a3da-006ab05004e2">
For help here: https://www.geeksforgeeks.org/bubble-sort-algorithm/








## How It Works

1. **Input Target Information:**
   Input specific details you know about the target (such as names, keywords, or sites) into the interface.

   ![Target Info Input](https://github.com/user-attachments/assets/e4e83e59-d48c-4954-bb4c-4bd4576523ec)

2. **Select Wordlist Size:**
   Choose between small, medium, or large wordlists depending on your needs.

3. **Save and Export:**
   Once the wordlist is generated, save it to a specified location in `.txt` format for further use.

4. **Review Results:**
   View the generated wordlist directly within the tool to ensure it meets your requirements.

---

## Screenshots

![Overview](https://github.com/user-attachments/assets/164ed813-4228-4d77-baf4-6fcce6fef3f4)
*Overview of Password Juicer*

---

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/password-juicer.git
