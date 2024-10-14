# XSS Vulnerability Scanner

This project is a simple Cross-Site Scripting (XSS) vulnerability scanner built using Python and Tkinter. The scanner identifies potential XSS vulnerabilities by submitting JavaScript payloads to web forms and analyzing the server's responses.

## Overview

The scanner performs the following tasks:
1. Retrieves all forms from a specified web page.
2. Submits a predefined JavaScript payload to each form.
3. Checks if the submitted payload is reflected in the server's response, indicating a potential XSS vulnerability.
4. Outputs the results of the scan, detailing any vulnerabilities found.

<img width="608" alt="image" src="https://github.com/user-attachments/assets/ef8968ac-5554-4e0d-bff5-4125be4a3eec">


## Key Function: `scan_xss(url)`

The core functionality for scanning XSS vulnerabilities is encapsulated in the `scan_xss` function. Below is a detailed breakdown of how this function works:

### Function Definition
```python
def scan_xss(url):  # uses the data to see if the site is vuln

<img width="611" alt="image" src="https://github.com/user-attachments/assets/87d75e40-d372-4908-812b-7a27011bc281">



