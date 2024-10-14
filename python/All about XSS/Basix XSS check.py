import requests # where the magic happens on layer 7. Logic for the Requests.
from pprint import pprint  # used for displaying data.
from bs4 import BeautifulSoup as bs # used to sift through HTML.
from urllib.parse import urljoin # used to work with relative and base URL's | Helps pasing HTML info 
import tkinter as tk # gui of course, need to be aware when migrating to online content.
from tkinter import scrolledtext, messagebox 

def get_forms(url): # used to fetch what is needed on an HTML page.
    try: # used to fetch HTML and throw an error if an exception is made. 
        soup = bs(requests.get(url).content, "html.parser") # note the get request sent on the users behalf. 
        return soup.find_all("form") # soup ius initalized here to parse the "form" content
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve forms: {e}")
        return []

    # Form is used because that is typically used for asking the user for info. (text Box)

def get_details(form): #gets the details, more info in stackoverflow.
    details = {} #basic but used to store the details within "{}"
    action = form.attrs.get("action", "").lower() # storing content for the site to be used later.
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# after all actions and details have been retrieved, they can be used for later.

def submit_form(form_details, url, value): # submits the form to eventually parse the data
    target_url = urljoin(url, form_details["action"]) 
    inputs = form_details["inputs"]
    data = {}
# loop iterates over each input field in the inputs list.


    for input in inputs:
        if input["type"] in ["text", "search", "textarea"]:
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    try:
        if form_details["method"] == "post":
            return requests.post(target_url, data=data)
        else:
            return requests.get(target_url, params=data)
    except requests.RequestException as e:
        print(f"[-] Failed to submit form: {e}")
        return None

def scan_xss(url): # uses the data to see if the site is vuln
    forms = get_forms(url)  # all necessary has been filled to launch the basic script
    output_text.insert(tk.END, f"[+] Detected {len(forms)} forms on {url}.\n")
    js_script = "<Script>alert('hi')</scripT>"
    is_vulnerable = False
    
    for form in forms:
        form_details = get_details(form)
        response = submit_form(form_details, url, js_script)
        # two use cases for if the submission is blank and whether the submitted script has been decoded.
        if response and js_script in response.content.decode():
            output_text.insert(tk.END, f"[+] XSS Detected on {url}\n")
            output_text.insert(tk.END, "[*] Form details:\n")
            output_text.insert(tk.END, pprint(form_details, indent=2, width=80) + "\n")
            is_vulnerable = True
    if not is_vulnerable: # searches for if vuln or not
        output_text.insert(tk.END, f"No XSS vulnerabilities found on {url}.\n")

def scan(): # logic for seeing if vuln
    url = url_entry.get()
    if url:
        output_text.delete(1.0, tk.END)  
        scan_xss(url)
    else: # error
        messagebox.showwarning("Input Error", "Please enter a URL.")

# this needs to be removed if moving to Flask or other online forms
app = tk.Tk()
app.title("BAsIc X33")
app.configure(bg="#e0f7fa")

url_label = tk.Label(app, text="Enter URL:", bg="#e0f7fa", font=("Comic Sans MS", 14, "bold"))
url_label.pack(pady=10)

url_entry = tk.Entry(app, width=50, font=("Comic Sans MS", 12))
url_entry.pack(pady=5)

scan_button = tk.Button(app, text="Scan", command=scan, bg="#ffab40", fg="black", font=("Comic Sans MS", 12, "bold"))
scan_button.pack(pady=10)

output_text = scrolledtext.ScrolledText(app, height=20, width=80, font=("Comic Sans MS", 12))
output_text.pack(pady=10)

app.mainloop()
