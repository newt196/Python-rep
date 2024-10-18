# Password Scraper

A Python-based project that simulates the functionality of [Cewl](https://github.com/digininja/CeWL). This tool scrapes web pages and generates wordlists that can be used for password generation or analysis.

---

## Features

- **Error Handling:** Automatically detects and handles errors, such as being unable to connect to a website.
- **Customizable Word Count:** Users can set the number of words to scrape from a given website.
- **Character Length Flexibility:** The tool can display and extract words of any length.
- **Variability in Wordlist Generation:** Option to add symbols, numbers, and capitalization to the generated wordlist.
- **User-Friendly Interface:** Simple and intuitive for users to quickly add sites to scrape and configure settings.

## Code Writeup

tkinter - Gui builder for Windows and Linux.
messagebox - Logic within Tkinter to show popups and alerts.
BeautifulSoup - Used to gather HTML content.
request - to fetch the content from a URL.
Counter - Counts the elements of an object.(Important for counting and organizing the elements within the site and then the program. 
re - REGEX for processing text. (Vital for processing elements on the program)




<img width="406" alt="image" src="https://github.com/user-attachments/assets/82229633-3d65-460c-bbae-77d7fe46a7b7">

Define a function that cleans the text foudn within the 

Define a function that cleans the text found within the search results. Also notating the limit of 4 characters to avoid words that dont matter.
REGEX usage here "re.findall" Finds all word-like patterns (\b\w+\b)
The limit is  \b meaning what the word is bound to, and \w+ matches any word 
Filtering Words: The programmer limits the words to those that have at least 4 characters. This avoids common small words (e.g., "the", "is", "on") that aren't very useful for word frequency analysis.
After the filter is run through, the list of cleaned words is then returned to us.

<img width="421" alt="image" src="https://github.com/user-attachments/assets/5ee9176a-1a0c-4480-b143-d7b804f8bf21">








---

## Usage Overview

### 1. Error Checking for Site Connectivity
If a website cannot be connected or scraped, the tool will handle the error gracefully, ensuring a smooth user experience.

![Error Checking](https://github.com/user-attachments/assets/ed043d01-6a79-4da7-922e-4e396ad246ac)

---

### 2. Adding a Site to Scrape
Users can easily input the URL of the website they want to scrape for words.

![Add Site](https://github.com/user-attachments/assets/597f549f-a11d-4caf-90c3-422f462996e6)

---

### 3. Adjustable Word Count
Users have control over how many words the program scrapes from the site.

![Adjust Word Count](https://github.com/user-attachments/assets/ba87aef5-837d-4ce8-89f5-1427456d862f)

---

### 4. Display Flexibility
The program supports displaying as many characters as needed based on the site's content.

![Character Display](https://github.com/user-attachments/assets/d54ddbce-95e2-4e72-be01-6c2887733785)

---

## Version 0.5

- **Enhanced Wordlist Variability:** Add symbols, numbers, and capitalize words to the wordlist for more complex password generation.
- **Improved Scraping Efficiency:** Faster and more robust scraping engine with better error handling.

![Version 0.5](https://github.com/user-attachments/assets/9d1ae180-e00b-42d6-9165-6a0412282b89)

---

## Future Plans
- **Expanded Website Support:** Future updates will focus on broadening support for different types of websites.
- **Advanced Scraping Options:** Planned features include scraping specific tags or sections of a website for more targeted wordlists.

---

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/password-scraper.git
# Password Scraper

A Python-based project that simulates the functionality of [Cewl](https://github.com/digininja/CeWL). This tool scrapes web pages and generates wordlists that can be used for password generation or analysis.

---

## Features

- **Error Handling:** Automatically detects and handles errors, such as being unable to connect to a website.
- **Customizable Word Count:** Users can set the number of words to scrape from a given website.
- **Character Length Flexibility:** The tool can display and extract words of any length.
- **Variability in Wordlist Generation:** Option to add symbols, numbers, and capitalization to the generated wordlist.
- **User-Friendly Interface:** Simple and intuitive for users to quickly add sites to scrape and configure settings.

---

## Usage Overview

### 1. Error Checking for Site Connectivity
If a website cannot be connected or scraped, the tool will handle the error gracefully, ensuring a smooth user experience.

![Error Checking](https://github.com/user-attachments/assets/ed043d01-6a79-4da7-922e-4e396ad246ac)

---

### 2. Adding a Site to Scrape
Users can easily input the URL of the website they want to scrape for words.

![Add Site](https://github.com/user-attachments/assets/597f549f-a11d-4caf-90c3-422f462996e6)

---

### 3. Adjustable Word Count
Users have control over how many words the program scrapes from the site.

![Adjust Word Count](https://github.com/user-attachments/assets/ba87aef5-837d-4ce8-89f5-1427456d862f)

---

### 4. Display Flexibility
The program supports displaying as many characters as needed based on the site's content.

![Character Display](https://github.com/user-attachments/assets/d54ddbce-95e2-4e72-be01-6c2887733785)

---

## Version 1.0

- **Enhanced Wordlist Variability:** Add symbols, numbers, and capitalize words to the wordlist for more complex password generation.
- **Improved Scraping Efficiency:** Faster and more robust scraping engine with better error handling.

![Version 1.0](https://github.com/user-attachments/assets/9d1ae180-e00b-42d6-9165-6a0412282b89)

---

## Future Plans
- **Expanded Website Support:** Future updates will focus on broadening support for different types of websites.
- **Advanced Scraping Options:** Planned features include scraping specific tags or sections of a website for more targeted wordlists.

---

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/password-scraper.git
