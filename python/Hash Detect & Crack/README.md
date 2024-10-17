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


```bash
pip install hashlib















