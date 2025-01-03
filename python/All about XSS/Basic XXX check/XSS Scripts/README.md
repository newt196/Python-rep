## Overview

The XSS Vulnerability Scanner is a tool designed to automatically detect Cross-Site Scripting (XSS) vulnerabilities in web applications. This scanner works by crawling a given URL, identifying forms, and submitting various XSS payloads to see if the application is susceptible to attacks. 



<img width="427" alt="image" src="https://github.com/user-attachments/assets/17c0d10c-6442-4dc1-94e8-78713c1965aa">


## Features

- **Automated Form Detection**: The scanner identifies all forms on a specified web page.
- **XSS Payload Testing**: A variety of predefined XSS payloads are tested against each form.
- **Results Reporting**: The tool outputs detailed results, including any vulnerabilities discovered during the scan.
- **Robots.txt Compliance**: Optionally respects the rules specified in `robots.txt`, allowing for ethical web crawling.
- **Graphical User Interface**: A simple GUI for easier interaction and displaying results.

## Installation

To run the XSS Vulnerability Scanner, you'll need Python and a few libraries. Follow the steps below to set it up:

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install required packages**:
    ```bash
    pip install requests beautifulsoup4 colorama
    ```

3. **Run the scanner**:
    ```bash
    python xss_scanner.py --url <target-url> [--obey-robots]
    ```

## Usage

- **Command-line Arguments**:
    - `--url`: The target URL to scan for XSS vulnerabilities (required).
    - `--obey-robots`: If specified, the scanner will respect `robots.txt` rules.
 


  <img width="422" alt="image" src="https://github.com/user-attachments/assets/d05a81f9-4b63-4ab3-9882-a09b2a7db9e0">


## Example

To scan a website for XSS vulnerabilities, run the following command:
```bash
python xss_scanner.py --url https://example.com --obey-robots

