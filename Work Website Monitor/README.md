Mailscape Website Monitoring  


- Runs all throughout the workday.

- Sadly have to manually alert team when an alert pops up.

- IS locks down custom SMTP connections, which is not ideal for automatic alerts through the email channel.



HTML being monitored 

Parts being monitored, unable to show the Server being monitored.


Good

![image](https://github.com/user-attachments/assets/b076b14c-02fe-42bb-b49f-f98a09d1429e)



Error has occured within the mail servers. 

![image](https://github.com/user-attachments/assets/1baee24f-1842-4688-88c7-48edc52ba7f1)




When things are good.


<img width="374" alt="image" src="https://github.com/user-attachments/assets/79808b76-cc7a-418b-b821-c35383af421b">



When things are being hindered or slowing down.


<img width="352" alt="image" src="https://github.com/user-attachments/assets/d2b416b8-db7b-439a-aa27-ffa1b5bbd8a5">




<img width="527" alt="image" src="https://github.com/user-attachments/assets/ba36da79-596c-4b2c-9c8a-ee44497b6634">

For those interested in the logic of the "wwhy" and "what" the code base is :)
Really just used to reiterate on existing python skills, performance, improvements and explanation.


The "Imports and "Froms"


<img width="237" alt="image" src="https://github.com/user-attachments/assets/784bbe00-4691-4c0b-84b4-9f9cbbafa325">


1. Sends requests to HTML in this case, NTLM which is used for the site. (Side Note: I didnt know NTLM was uised because of SSO)
2. BS4 | Beautiful soup package that pulls HTML content which was used to track and monitor for this python alerting program.
3. Time is used for time.sleep(100), which pauses the execution of the program for 100 seconds between iterations of the loop.
4. Controls the requests info and logic for accessing HTTP info
5. platform was used for accessing information about the operating system and hardware.

Used to in the best manner I found, add my AD user and pass to the site. 
Password was saved in a location I only have access to.


<img width="202" alt="image" src="https://github.com/user-attachments/assets/d77ca266-df45-4bdf-a3ee-fb6c974d65f1">


Error checking for the password

<img width="446" alt="image" src="https://github.com/user-attachments/assets/21f99fe4-476d-40eb-a5fc-394be2f289c3">

Domain is pretty straightforward
Simply send a get request to the site to allow access.

<img width="389" alt="image" src="https://github.com/user-attachments/assets/ee094280-eeaf-43e4-b87f-1c0b27ffcec6">


More error checking for the site, in case the site is down or domain has changed.
(Only used once, or I think twice two to site repairs.)

<img width="439" alt="image" src="https://github.com/user-attachments/assets/8025fd53-d68a-49f3-8932-58c17dea3d46">

We host 20+ servers with different utilities being monitored. 
An array has been created for both the servs and the categories of the utilities can be used to scrape and monitor the HTML code of the site. 

The request is used to parse or generally analyze the content in the soup object.


<img width="431" alt="image" src="https://github.com/user-attachments/assets/0a2bbe99-4351-47e0-bd08-2c28b43af1ff">

Loop: Element Status to go through the servers and Catagories in the Array that was earlier declared. 
loops through each server and each category, constructing a URL pattern in the form "{category}.aspx?server={server}"



<img width="397" alt="image" src="https://github.com/user-attachments/assets/5f959dee-2b17-4f4f-a5fd-d109fd9a1990">

The object that changes is alt_text. For context if an error is detected. "OK" = Green will change to "Error" = Red
If Error is found within the img_tag, than the the element status is pinged and the print statement is made.



<img width="382" alt="image" src="https://github.com/user-attachments/assets/37ae440f-f18b-4220-b0bf-9196a88072d6">

While True Logic to give a headsup when "Error" is changed to "OK"

<img width="447" alt="image" src="https://github.com/user-attachments/assets/d876d8f7-d3b3-45ce-b9f7-52f41573935b">





















