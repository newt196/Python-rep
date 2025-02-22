# XSS Vul with Selenium 

A simple Cross-Site Scripting (XSS) vulnerability scanner built using Python. This application scans web pages for forms and attempts to submit XSS payloads to check for vulnerabilities.
Used for both static and dynamic pages that a user want so scan. 

<img width="593" alt="image" src="https://github.com/user-attachments/assets/54a141e5-42d6-43a3-b523-5307d654eb3b">


## Features

- Scans a given URL for HTML forms.
- Submits XSS payloads to check if the site is vulnerable.
- Supports both traditional form submission and Selenium-based scanning for dynamic web pages.
- User-friendly graphical interface using Tkinter. (need to remove or adjust if FLASK is used)
- Displays detailed output of the scan results.

## Requirements

- Python 3.x
- Libraries:
  - requests
  - beautifulsoup4
  - colorama
  - selenium
  - Tkinter 

### Install Required Libraries

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4 colorama selenium

