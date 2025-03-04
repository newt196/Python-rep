**Project Notes**

Lamp project

Wanted to develop a solution to pull eBay data for better listing info from what is provided in the site.
While also learning some backend for learning purchases.

Currently I am using the following to pull and process data

Python | Ingress & Egress point from Ebay to local and cloud database | Computation for price change done here

MYSQL | Used to sort and organize listing and seller data | Monitor Price and listing data | Indexing hgas been used for speed

HTML & CSS | Frontend to list and showcase any items to purchase based on python math and MySQL storing

PHP | Math and logic to give the user the possibility to showcase any good deals or massive price drops. 

Backup solutions

- CSV for backups on listing for eBay API data. Not really sorted
- AWS RDS to create a cloud backup of database information(learning purpose within AWS)


Security
- accounts have been massively restricted.
- HTTPS has been configured on the Apache site
- You need an account to get into the initial index page for the site.
- Local and cloud backups
- Logging and event logs on the system and user accounts
- API and key data are soon stored within a secure token







I don't have a good way to transfer non-prod to prod notes....Going to summarize the general work notes as concise as possible. 
Cutting as much fat, troubleshooting and personal thoughts as possible. 


2/6


(Done...in a good spot for now)Need to uniform code a bit more.
^^^^Right now the code does what it needs to do. I don't think its in a good spot for uniformity.


adjustments being made:
- (done and complete, unit test has been complete) )Connection check was made for all three def's(will need to make an adjustment here to not have to cpy and paste each three items)
---(done and working for sellers)^^This change has been made going to test, in case allot of code has been adjusted. 
^^^(trending now loops through each item) 
^^^keyword now also works with one check.
- (done)for loop for multiple keyword(trending and sellers has already been done)


(Done)implemented a run every 10 minutes and the database connection to be made every hour. 
May increase depending on real worlds issues and items that come up
^^^will need to do this onsite or with deep
Having issues with the code implementation

MOVING TO PHP FOR NOW
1.(done) KEYWORD:
results display to my knowledge on the server as 

Keyword	Title	Price	Item URL
laptop	Dell XPS 13 2021	$899.99	View
laptop	Apple MacBook Pro 13"	$1,499.99	View
laptop	HP Spectre x360	$1,099.99	View
Need a way to query keyword result and only query given results

2. (done)Sellers data 
Just copied over the format and swapped the tables to accommodate the seller tables

3. Not going to do trending, I think this is currently in a good spot. 

All of this needs to be tested before pushing to prod in a large scale

^^^^(The above has been backed up)


https://www.phpindia.com/boosting-performance-php-mysql-optimization-guide/
^^cant really adjust until i am onsite


Now need a way to figure out how to optimize the data being sent so 
the server does not run into any memory issues. 
Notes for MySQL efficiency(things to look into when onsite and in mysql)
Need to go through how my version of MySQL handles data structures.
variables attached to the following
- Price
- Image(url)
- URL itself

VARCHAR vs. CHAR(need to see if this has been optimizes within my database)

INIT vs. BIGINT Dont think this applies, but still good to check.
Especially when dealing with a bunch of price pushes and pulls. 


Most important detail(Indexing) Need to figure out how to handle large databases within MySQL and php.
Kind of unsure what this is. 

Indexing is critical for performance, especially for large datasets.
Avoid indexing columns that have very high cardinality (a large number of unique values), such as TEXT or BLOB columns, because these consume a lot of memory and slow down write operations.
Consider composite indexes when you frequently query multiple columns together (e.g., WHERE column1 = ? AND column2 = ?).
Use FULLTEXT indexes for searching large text fields efficiently.



APACHE home change
- 



Networking & Cybersecurity adjustments

Apache - Connections(HTTPS & 443 only)
- can only check when onsite
- need to look into why the hosting either from own router or cloudflare tunnel

(python)Secure transmissions between python and MySQL server


(python) Secure api and user password and keys
(MYSQL & Apache)Secure transmissions between MySQL and webserver(Apache)

(Wireshark or TCPdumpNeed to monitor connections that are in clear text
(MYSQL) security and user audits





2/1


(Done)Going to start with 1 seller (see how the application responds) ^^started with a known (cells-sales) This displays properly. The issue was tied to mysql not reading through the results all the way Adding.fetchall maintains that all results get returned to the ide

(fixed)Have an issue, no tables were created within MYSQL Seller page.

Apparently not enough space allocated to the URL first i have seen this error with works mass email issue. Should have seen this issue from work. Same item as optimizing limiting characters to what is needed later on This now works, pending php code.

(Done)Going to resubmit to see if data is replicating ^^^handles resubmissions well :)

(Done)multiple sellers? listings insert and do not duplicates are note repeated

Also api pagination seems to be working which is nice. Moving on

(done)Get item list note: although adds the keyword to the database, the php code just adds the last searched item PHP: need to add buttons and slides for customized list of items.

(done)See how the application lists multiple items and any things that need to be altered

TRENDING ITEMS

(done)Start with 1 item adds the items to the database.

(done)See how the application handles resubmits



1-27

Python

Need to look into why sellers are not being managed properly
Seller data needed to be updated with info that validates the info being sent, in addition to checks for the connection to the Seller Data table. Currently we have a (not-tested) solution for the seller datas. bug - seller data only populates one seller but provides data on all options ^^^^this has been fixed, different sellers are now populated with a separate condition


(fixed)bug - connection error populates on each seller

(fixed), now processes first. Connects or throw an error at the first part and then displays seller data.
another bug - Duplicate results for one listing. Currently fixed, we had a duplicate main function for some oversight.

(dropped..for now)Need a way to find api limits and what is a good refresh limit. 5,10,15 refreshes per hour?



PHP

(pending) optimize the flow of large data sets.
^^^a continuation of this, we need a way to sort each table and allow the user to filter for lets say trending items. (test) need to test to make sure the appropriate amount of info is taken and that the code does not crash. currently added filters that need to be checked
Apache


verify (SHOW STATUS LIKE 'Ssl_cipher'; )


1/25

now working on the backend for serving data and information to the Apache server. Using php as the connecter and ajax as the service manager for the front end



(fixed)HaVING AN ISSUE WITH APACHE CONNECTING to mysql.

Double and even triple checked elements code and files.


-pull seller data(in its basic format)

-Python then connectects to a mysql server that holds the listing data in.

-MYSQL allows Apache to conneect and with a small amount of PHP code, we can disply the python results on a webpage.

STILL PENDING -Local and GlobaL NETWORK -Most important...Cybersecurity(security groups,hardcoded password, audits, and deep scans) -Presentation and code review(test cases)


Networking

(done)HTTPS(in-progress)>>>>(...stil working on this an hour later...ran into a dns issue) www.bamney.net still in the process of authenticating Spent a bit more time I would like on hosting, tried to do it the rough an dirty way with my router. From what I can understand, all info is good on my side. I just dont understand the setting my router enough.
Authentication(in progress)>>>(this has been completed, but not verfied on a public network) (plus i think you can still access the index page..for right now its ok, the main juice is locked up) I am going to switch to cloudflare for now. getting frustrated with hosting, going to move to python for now and come back >:|
(Pending)Audit user account for access
(up to date)check ufw firewall rules



Python

(Done)functionality to add more sellers
(Done)functionality to add more user list and to better strip info from listing(done, more can always be done later)
(Done :))math and logic to monitor price changes
(dropped)better descriptions for items listingf(this will be imperative to not waste time)(not needed at this time)
(Pending)watch for new items that get listed hastily(trening kind of solves this)


Apache/Webdev

(Pending, still looks ugly)Clean up http directory
Logging for connections and malicous content(its own subject here)
Clean up PHP and hopw the site displays lsitings(needs to be waaaay cleaner)
MySQL

Audit user logs
Need logs for ingress and egress poiunts
need scaling or backups of ingress and egress
VM

Remember to backup or schedule them regualrary
Randomn

https://www.reddit.com/r/virtualbox/comments/zr7sww/windows_10_keeps_needing_to_reinstall_every_time/ [I found this fix works best if done in this order: Completely uninstall any VirtualBox currently installed Restart the computer Install the latest version of VirtualBox After install completes do not restart the computer Open the registry editor. Start > Run > regedit Go to: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\VBoxDrv Edit the key called Start. Change it's value from 1 to 3 Close the registry editor and restart your computer. After your computer restarts you should be able to use VirtualBox without any issues. Upon restart ]

Found out i have missing vb dependencies. Time will tell if this new dependcies fixed, my restart issue. weird, still getting the msising error. Will have to proceed for now

1/24

Notes for today

Before writing, I fixed the formatting of the "keyword" def that i loved soo much.


Python

(Done)Code review and documentation
(fixed, (done)just pending test) Seller data is not submitting to MySQL
^once done, check all three defs running at the same time(i cant check really until i get home
(Secure credential Storage) We have info ro storing credentials that a re a bit sensitive. Going to have to test each option later on
PHP

(done)remove seller location
(research) optimize the flow of large data sets.
MySQL

(done) verify the columns, may i have reverted a change unknowingly
(done) figure out and research the time being send and retrieved from ingress and egress points


Apache
(dropped)look into gui format(as seen in "Apache gui tools ubuntu"
ETC

(OpenVPN or WireGuard(recommended) | need to research ) vpn solution for office management
(worth it?)imbedding php files into html
For tomorrow Figure out why this orccurs

(fixed)Why is my data replicating
^btw an issue with the flow of statements. 

(done and tested and working)Figure out if i need to split up each database within its own PHP file hosted on the server



EBAT API CALLS
Some resources to help

https://github.com/hendt/ebay-api -(For data) https://github.com/rgabeflores/eBay-Scrape
Find seller token

-General aspects to incorporate

(Done)Need a way to monitor major businesses and there listings effectively.(this effectively needs to be important)

(Done ref 2/6)Need a way to sort the listings(not that important...to my knowledge)

-API interesting to note and notes (GetSellerList) https://edp.ebay.com/devzone/xml/docs/Reference/eBay/GetSellerList.html What's in the name, returns an array of items matched with the sellers token.

(Tracking listing changes) https://edp.ebay.com/api-docs/user-guides/static/trading-user-guide/track-listing-changes.html Most likely future updates for bids and more advance monitoring

Info to manipulate the Headers and Data Part of the code base

Headers: Content-Type is needed because you are sending the request as application/x-www-form-urlencoded, which is how OAuth expects to receive data for token requests.

Data: grant_type tells eBay’s OAuth server the type of token you want to request (in this case, it's machine-to-machine access via client credentials). scope specifies what your app can do with the generated access token. For now, we are using a general scope.

-Technical aspects

(Very important)(done)(Need to work on CSS structure) layout needs to be clean and easy for the user and I to understand Need a way to manage pricing and price changes of listings (finding good deals and sharp price decreases) Need a way to individually track and monitor specific items and price bought. ()(...sort of Fixed)Limit api call to every 5 minutes....for now 5 calls every day == 60/5 = 12. 12 * 60 = 288. Seems good for now ( Limits calls to 5000 calls per day )

Really cool create this on the server and being able to access on site.(more on this waaaaay later)

General ideas...reddit




Need to install ebaysdk on laptop(done) Need to authenticate with API keys(researching for now)




Part 2 Technical aspects Some recourses for webdev { https://www.reddit.com/r/webdev/ }

For now here is the plan

(AWS replication/Fixed)LOCAL and Cloud option(most info can be found on "EBAY API APP SETUP")

Barebones options > Hosting on the web



VPN to connect local(kind of unknown)
How many instances are to be used
the region
docker based cloud hosting
not much info on route 53 dns hosting(allot of research, but this is waaaay in the future
Current plan

        Ebay Server API > HP windows(Locally hosted/where code is run) > Push (filtered) data to SQL server
        (virtually/locally hosted'maybe EC@ backup') > Push SQL data to website(#need a way to connect EC2 instance with virtual environment)
        
        Notes for pulling ebay data.

(Done)What we need: -clean up the listing data 1 separating user and seller data 2 cleaning up listing data in a more easily format to read.

(Done)a way to parse different info > columns (Title, Price, etc)
created two defs, one for specific items and items the user wants to search.

This can be done with

Initialize an empty list to store all results
all_results = []

Loop through each seller
for seller in sellers: # Construct parameters for the current seller finding_params = { 'keywords': '', 'paginationInput.entriesPerPage': 30, 'itemFilter(0).name': 'Seller', 'itemFilter(0).value': seller }

(Done)remember its monitoring, if the price changes for sellers items dont change the state of the item. We jsut need to be aware of it*
can confirm that python can log the new price and hold the old price with price changes.
confirm the state of the database is immutable on every refresh.
answered in the above, cant confirm until I am home and make the changes.
1-21 - 11:46 notes. I think we are in a good spot in regards to code functionalit>

Patch notes for this update

(Done)Deal checker (huge logic check | Going to need to lock in to check and make sure is functional)




Notes for 1-23

(Done)Python -Need to make make sure ^ 2 that the content being sent to the server are not duplicating upon send.(pending) Insert ignore on info that shares the same info (seller is done) | (get items is done) | (trending items is done) : currently checking if the main functions need to be adjusted

-(Done)Putting checks so that i can work on the logic and checks for python and my sql (this has been done)

(Done)this has been done on all three DEF's with try statements. Pending side quest, need a way to reduce the try time As code gets put down, I feel runtime is coming to a halt in certain searches.

(Forgoet until 2/6)need to optimize code speed SQL -Need to verify the naming convention for many of the tables in use(pending)
Just need to change the all colums in all three defs -Also need to verify the security of the backend.(see Cybersecurity, will need to complete at home)

(Full implantation pending)Need to setup MySQL log monitoring and a #good dashboard for data# <---most important part
Order of work(these need to be uniform in nature) def seller_items def get_item_listings def trending_items


(Done | password is *********************)Cybersecurity Authentication Currently users are under strong password Cons :( I am pretty sure the passwords are being send in clear text Solution, need a secure yaml or json pull to include the data within the python applcaition

(Pending as of 2/6)egress and ingress Currently the solution "just works" Cons: Using encrypted solutions, not as familiar with TLS Solution: an opportunity to learn and troubleshoot secure transmissions(verify verify verify)

(Done)Firewall current solution just works No Cons: Solution: verify what is being allowed and not allowed

1/23/25 9:39

Ran into an error that took 30 minutes of my time.

(Fixed)The error was as follows. Servershutdown WIFI stopped working :( Researched Tried-Wake on lan Powermanagment Checked Yaml configuration file(this was the solution)

changed Gateway > Nameservers
Applied the netplan
Project all toegether

(Fixed)Seller does not want to push data which is super annoying.

(Fixed)(Fixed)Trending items pushes data to the server

(Fixed)Checking items now.

(Fixed | Issue with how api data was integrating with mysql)Need to check why sellers is not pushing data properly.

(Fixed)Super big issue, because the php was already created to host data within Apache, will adjust for now.







There is a portion that is developed that connects to the MYSQL which will be added in the MYSQL portion of this project.

The code is specially called and made to be sent to view later within MYSQL. 



Outline of the Python portion of the project and its functionalit


Three main functions that help inform the user when parameters are passed through.

**def seller_items**

This function retrieves a list of trending eBay items based on a given keyword, focusing specifically on "Buy It Now" listings.

It sends a request to the eBay API with specific parameters, such as keyword, price filter, and completed item results.

The API response is parsed to extract relevant details like the item's title, price, condition, seller information, location, and images.

Items are filtered to include only "Buy It Now" or fixed-price listings.

Returns a list of dictionaries, where each dictionary represents a single item with all its details, or returns an error message if the API call fails.

<img width="683" alt="image" src="https://github.com/user-attachments/assets/faa09cfc-c856-4665-9523-c86b39643899" />




def get_item_listings

Setup Request Parameters:
Constructs API parameters to search for items using the provided keywords.
The paginationInput.entriesPerPage parameter limits the results to 30 items.

Send API Request:
Makes an HTTP GET request to the eBay Finding API with the search parameters.

Process Response:

If the request is successful (status_code == 200), it parses the JSON response.
Retrieves the list of items from the findItemsAdvancedResponse.
Extract and Format Data:

For each item in the response:
Extracts the title, price, and URL of the item.
Retrieves up to three image URLs (from galleryPlusPictureURL or galleryURL).
Adds the extracted information to a list of results.
Return Results:

Returns a list of dictionaries, each representing an item with the following keys:
listing (title), price, url, images.


<img width="739" alt="image" src="https://github.com/user-attachments/assets/d4c9cf96-950e-41b6-959e-2c3968c9322f" />

def trending_items


Setup Request Parameters:
Constructs API parameters with the following filters:

CompletedItemsOnly: Searches only completed listings (sold or unsold).
MinPrice: Filters out items priced below $10.
paginationInput.entriesPerPage: Limits results to 25 items.
Send API Request:
Makes an HTTP GET request to the eBay Finding API with the parameters.

Process Response:

If the request is successful (status_code == 200), it parses the JSON response.
Extracts items from the findItemsAdvancedResponse.
Extract and Format Data:

For each item in the response:
Extracts key details like title, price, condition, seller name, location, and category.
Retrieves up to three image URLs (from galleryPlusPictureURL or galleryURL).
Adds the extracted information to a list of results.


<img width="740" alt="image" src="https://github.com/user-attachments/assets/e33c4e59-a1d4-4e39-8e4a-2b2468b7a4d8" />


