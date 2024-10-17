**Hash and Crack**


# Hash Browns - Hash Cracker GUI

## Overview

**Hash Browns** is a simple graphical user interface (GUI) application designed to help users detect and crack various types of cryptographic hashes. Utilizing Python's `hashlib` library, it supports multiple hashing algorithms and allows users to input a hash value and a wordlist to attempt to crack the hash.

## Features

- **Hash Type Detection**: Automatically detects the type of hash based on its length and known patterns.
- **Hash Cracking**: Uses a wordlist to find the original string that generated the provided hash.
- **User-Friendly GUI**: Built using Tkinter, providing a visually appealing and easy-to-use interface.

## Supported Hash Types

The application supports the following hash types:

- **Hash Functions**:
  - Blake2b
  - Blake2s
  - MD5
  - SHA-1
  - SHA-224
  - SHA-256
  - SHA-384
  - SHA-512
  - SHA-512/224
  - SHA-512/256
  - SHA-3 (224, 256, 384, 512)
  - SHAKE (128, 256)
  - RIPEMD-160
  - Tiger
  - Whirlpool
  - GOST
  - CRC32
  - CRC32C
  - Fletcher32
 
## Code Writeup
Imports and Froms

Hashing library import that contains all of the hash functions that are basic. Like md5 and Sha.
Tkinter does not need a intro. Logic to control the GUI.



<img width="230" alt="image" src="https://github.com/user-attachments/assets/2cdfa517-27ea-44ad-a1af-9dc8a2803f9f">


Array of hashes that are supported for the user.
Need to add a bigger library as more uncommon hashes are used. 



<img width="109" alt="image" src="https://github.com/user-attachments/assets/3a97ee0a-9b90-4681-b12f-dcfe2eb2000f">

As the "def" says, this function is used try and detect the hash plugged in.
"try" ius used to pass the getattr to compare in the used " if" statements. 
Comparing the hash length test hash used in the library to the test function. 
If a match is found, then python will return what it thinks the users hash is.
Sadly, it only checks the length and does not dynamically compare salts, algorithms, or time based hashes. 

Keeping it simple for now.




<img width="347" alt="image" src="https://github.com/user-attachments/assets/31a1c29a-9d72-424f-bd3e-a2b1758ad98a">



Logic within the Gui that will display either the "detected hash" or the program struggle to determine what it was given.
This is done the program retrieving the input hash, passes it to detect_hash_type(), and updates the display with the detected hash type.



<img width="403" alt="image" src="https://github.com/user-attachments/assets/c38d27ff-ce13-4a29-b870-585cb414f3cc">




Where the magic happens and the item that makes script kiddies happy. 

The fucntion with the gui that tries and compares the hash by matchiong it within the library provided and store it for the "try" statment belwo.

The hash is saved and is ran within the below fucntion
Excpetions are made  with "if not" if the hash is not found within the library



<img width="399" alt="image" src="https://github.com/user-attachments/assets/329148e4-bdd1-4876-8c9b-4c7d7bbdbba0">



Where the magic happens and the item that makes script kiddies happy. 
The logic goes as follows. 
"Try" is used to catch an error if they occur, which should be caught and handled in the except block.
The wordlist is opened in read only with the "with" statement, handling its operation smoothly.

as wordlists declares the wordlist as an object allowing the items within, he wordlist to be iterated over with.


"for" line "in" wordlists uses each line within the wordlist to pass over in the if statements down below
the "if" statement compares the hash provided earlier by the user and uses encode to then compare the same hashes word within the line.
Not to mention strip is used to make sure that any blank spaces are used. 



In all the "if" statement compares the computed hash (from the wordlist password) to the user-provided hash (user_hash). If they match, that means the current wordlist entry is the correct password for the given hash.





<img width="494" alt="image" src="https://github.com/user-attachments/assets/b08eeaec-ae92-4349-868e-a058615a793f">

A messaage is then returend either Success or Faliure if the same hash is not found.  



<img width="480" alt="image" src="https://github.com/user-attachments/assets/6b5414ea-f9d3-4ad0-80f1-4ab4ed74f334">










## Installation

Ensure you have Python installed. The `tkinter` module is included with Python installations. If `hashlib` is not available, you may need to install it via pip:


MD5:

<img width="295" alt="image" src="https://github.com/user-attachments/assets/7c28f31e-bd88-48b0-bd16-5e24a8192837">


SHA224:

<img width="298" alt="image" src="https://github.com/user-attachments/assets/0897df91-cf05-46d4-80d0-c08c11ae9488">


IF passsword is found:


<img width="305" alt="image" src="https://github.com/user-attachments/assets/d8a56f20-07a8-4b8c-b71a-26505fcb67ff">

If no password is found :(


<img width="314" alt="image" src="https://github.com/user-attachments/assets/6927bdcc-5a4f-4c5d-ba58-be599954bd6c">


















