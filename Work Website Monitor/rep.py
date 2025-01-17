from requests_ntlm import HttpNtlmAuth
from bs4 import BeautifulSoup
import time
import requests
import platform



with open('password', 'r') as file:
    password = file.read().strip()

# As much as I like my password in plain text, I wanted a way to access the site with NTLM without my password being accessibnle to the whole office.

if not password:
    raise ValueError("Password file is empty or could not be read")


# will obuscate when moved to Github


username = 'domain\\newt'
url = "website"
response = requests.get(url, auth=HttpNtlmAuth(username, password))

if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
servers = ["Server-01", "Server-02", "Server-03", "Server-04", "Server-05", "Server-06"]
categories = ["Functionality", "Network", "Disk", "Services", "Backup", "Resources"]
# format of the site when monitering the mail servers. 


def check_status():
    if not servers or not categories:
        print("Servers or categories are not populated.")
        return None

    try:
        response = requests.get(url, auth=HttpNtlmAuth(username, password))
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        element_status = {}

        for server in servers:
            for category in categories:
                href_pattern = f"{category}.aspx?server={server}"

                link = soup.find('a', href=href_pattern)
                if link:
                    img_tag = link.find('img', alt=True)
                    if img_tag:
                        alt_text = img_tag['alt']

                        if alt_text == "Error":
                            element_status[(server, category)] = alt_text
                            print(f"Error found for {category} in {server}.")
        return element_status

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None


previous_status = check_status()
while True:
    current_status = check_status()

    if current_status is not None:
        if current_status != previous_status:
            print(f"Status changed: {previous_status} -> {current_status}")


    time.sleep(100)
