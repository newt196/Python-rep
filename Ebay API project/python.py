import requests
from requests.auth import HTTPBasicAuth
import mysql.connector

# General notes for the following ""CREDS""

# CREDS - will be removed in GIT until tokens are in place

mysql_host = 'no'  
mysql_database = 'no'
mysql_user = 'no'
mysql_password = 'no'

client_id = 'no'
client_secret = 'no'

# CREDS - will be removed in GIT until tokens are in place


# API - flow of information
url = 'https://api.ebay.com/identity/v1/oauth2/token'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {
    'grant_type': 'client_credentials',
    'scope': 'https://api.ebay.com/oauth/api_scope'
}

finding_api_url = 'https://svcs.ebay.com/services/search/FindingService/v1'
finding_headers = {
    'X-EBAY-SOA-SECURITY-APPNAME': client_id,
    'X-EBAY-SOA-OPERATION-NAME': 'findItemsAdvanced',
    'X-EBAY-SOA-RESPONSE-DATA-FORMAT': 'JSON'
}

# API - flow of information


# MySQL Connection function and conntrol

def connect_to_database():
    """Connect to the MySQL database."""
    try:
        conn = mysql.connector.connect( # calls back to the original creds to send to the mysql
            host=mysql_host,            # server to connect to. Will try to return an error if there is a 
            database=mysql_database,    # a break in the connection or creds
            user=mysql_user,
            password=mysql_password
        )
        if conn.is_connected():
            print("Successfully connected to the database.")
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

# Creates or Update the eBay Listings Table within MYSQL where applicable.
def create_table():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ebay_listings (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(255),
                    price DECIMAL(10, 2),
                    currency VARCHAR(10),
                    item_url TEXT,
                    seller VARCHAR(100),
                    location VARCHAR(255),
                    category VARCHAR(100),
                    condition VARCHAR(50),
                    images TEXT
                )
            ''')
            print("Table 'ebay_listings' is ready.")
        finally:
            conn.close()

# tasked with inserting the listing pulled within the Ebay API.
# Need to make sure that all listings are uniform as to remove
# confusion
def insert_listings(listings):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            for listing in listings:
                cursor.execute('''
                    INSERT INTO ebay_listings (title, price, currency, item_url, seller, location, category, condition, images)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', (
                    listing['listing'],
                    listing['price'],
                    'USD',  
                    listing['url'],
                    listing.get('seller', 'N/A'),
                    listing.get('location', 'N/A'),
                    listing.get('category', 'N/A'),
                    listing.get('condition', 'N/A'),
                    ', '.join(listing['images'])
                ))
            conn.commit()
            print(f"{len(listings)} listings inserted into the database.")
        finally:
            conn.close()

# main function here is to manage and track certail sellers and price, listing and title
# adjustments(still pending)
# where needed
def seller_items(sellers):
    all_results = {}
    db_connection_successful = False    # to test the application outside of my network 
    try:                                # I needed to skip the connection phase of mysql with "try"                       
        conn = mysql.connector.connect( # Will bypass the connection to simply test the python info pulled
            host=mysql_host,            # from ebay API.
            database=mysql_database,    # This has been implmented in both two other functions
            user=mysql_user,
            password=mysql_password
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1")  
        db_connection_successful = True
        print("Database connection established successfully.")
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

    for seller in sellers:
        print(f"\nFetching listings for seller: {seller}")  
        seller_listings = []
        page_number = 1
        entries_per_page = 200  # According to ebay API docs, 200 per page
                                # need to be aware of this when sellers have more than 200 
        while True:             # listings and pagination is needing to be done.
            finding_params = {
                'keywords': '',
                'paginationInput.entriesPerPage': entries_per_page,
                'paginationInput.pageNumber': page_number,
                'itemFilter(0).name': 'Seller',
                'itemFilter(0).value': seller
            }

            try:
                finding_response = requests.get(finding_api_url, headers=finding_headers, params=finding_params)

                if finding_response.status_code == 200:
                    finding_data = finding_response.json()
                    search_results = finding_data.get('findItemsAdvancedResponse', [])[0].get('searchResult', [{}])[0]

                    item_count = int(search_results.get('@count', 0))       # certain cases where the seller was wrong
                    if item_count == 0:                                     # and nothing would happen, could troubleshooting in 
                        print(f"No listings found for seller: {seller}")    # case the seller was mistyped.
                        break  

                    for item in search_results.get('item', []):             # price change testing, need to check on own store
                        title = item.get('title', [])[0]                    
                        price = float(item.get('sellingStatus', [])[0].get('currentPrice', [])[0].get('__value__'))
                        url = item.get('viewItemURL', [])[0]
                        images = item.get('galleryPlusPictureURL', item.get('galleryURL', []))
                        images = [images] if not isinstance(images, list) else images[:3]

                        seller_listings.append({
                            'seller': seller,
                            'title': title,
                            'price': price,
                            'url': url,
                            'images': images  
                        })

                    if item_count < entries_per_page:
                        break  
                    else:
                        page_number += 1  
                else:
                    print(f"Error fetching data for seller {seller}: {finding_response.status_code}, {finding_response.text}")
                    break 

            except requests.exceptions.RequestException as e:
                print(f"Request failed for seller {seller}: {e}")
                break  

        all_results[seller] = seller_listings
                                                # results should be processed and sent to the mysql server
        if db_connection_successful:            # in a clean format. 
            try:
                conn = mysql.connector.connect(
                    host=mysql_host,
                    database=mysql_database,
                    user=mysql_user,
                    password=mysql_password
                )
                cursor = conn.cursor()
                                                # Creates the function table if it doesnt exist.
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS seller_items_listings (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        seller VARCHAR(100),
                        title VARCHAR(255),
                        price DECIMAL(10, 2),
                        old_price DECIMAL(10, 2),
                        url TEXT UNIQUE,
                        price_last_updated DATETIME,
                        images TEXT
                    )
                ''')

                for listing in seller_listings:     # saw an issue where duplicate data was being resent
                    try:                            # we now have checks for duplicate data(soon need logic and math on price changes)               
                        cursor.execute('SELECT price FROM seller_items_listings WHERE url = %s', (listing['url'],))
                        result = cursor.fetchone()

                        if result:
                            existing_price = result[0]
                            if listing['price'] != existing_price:
                                print(f"Updating price for {listing['url']} from {existing_price} to {listing['price']}")
                                cursor.execute('''
                                    UPDATE seller_items_listings
                                    SET old_price = %s, price = %s, price_last_updated = NOW()
                                    WHERE url = %s
                                ''', (existing_price, listing['price'], listing['url']))
                        else:
                            print(f"Inserting new listing for URL: {listing['url']}")   # info most related to keyword that informs user purchase and reselling
                            cursor.execute('''
                                INSERT INTO seller_items_listings (seller, title, price, old_price, url, price_last_updated, images)
                                VALUES (%s, %s, %s, NULL, %s, NOW(), %s)
                            ''', (listing['seller'], listing['title'], listing['price'], listing['url'], ', '.join(listing['images'])))

                    except mysql.connector.IntegrityError as err:                                   # various checks for duplicate listings and titles
                        if "Duplicate entry" in str(err):
                            print(f"Duplicate entry detected for URL: {listing['url']}. Skipping.")
                        else:
                            print(f"Integrity error: {err}")

                conn.commit()
                print(f"Data committed for seller: {seller}")
            except mysql.connector.Error as err:
                print(f"Database error while processing seller {seller}: {err}")
            finally:
                if 'conn' in locals() and conn.is_connected():
                    conn.close()
        else:
            print(f"Skipping database updates for seller: {seller} due to earlier connection failure.")

    return all_results
# Main function is to pull and monitor certain items and storing price changes
# within the mysql server. Initially what started the project, although trending gives
# more insight on certain items a bit more now. May consider discontinuing in the future 



def get_item_listings(keywords):
    finding_params = {
        'keywords': keywords,
        'paginationInput.entriesPerPage': 30
    }
                                                # similar logic with the keyword to sellers.
                                                # will pull data in regards to what the user puts
                                                # in the parameters
    finding_response = requests.get(finding_api_url, headers=finding_headers, params=finding_params)

    if finding_response.status_code == 200:
        finding_data = finding_response.json()
        search_results = finding_data.get('findItemsAdvancedResponse', [])[0].get('searchResult', [{}])[0]

        if int(search_results.get('@count', 0)) == 0:
            print("No results found.")
            return []
        else:
            items = []
            for item in search_results.get('item', []):
                title = item.get('title', [])[0]
                price = float(item.get('sellingStatus', [])[0].get('currentPrice', [])[0].get('__value__'))
                url = item.get('viewItemURL', [])[0]

                items.append({                  # info most related to keyword monitoring, 
                    'keyword': keywords,        # will update with price changes later
                    'title': title,
                    'price': price,
                    'url': url
                })

            try:                                # as mentioned, info in regards to ensuring the table and columns 
                                                # were created and checked if not not created
                conn = mysql.connector.connect(host=mysql_host, database=mysql_database, user=mysql_user, password=mysql_password)
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS keyword_item_listings (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        keyword VARCHAR(100),
                        title VARCHAR(255),
                        price DECIMAL(10, 2),
                        url TEXT
                    )
                ''')
                for item in items:              # simple for loop that iterates over gathered items into MYSQL. 
                    cursor.execute('''
                        INSERT INTO keyword_item_listings (keyword, title, price, url)
                        VALUES (%s, %s, %s, %s)
                    ''', (item['keyword'], item['title'], item['price'], item['url']))

                conn.commit()
            except mysql.connector.Error as e:
                print(f"Database error: {e}. Proceeding without saving data to the database.")
            finally:
                if 'conn' in locals() and conn.is_connected():
                    conn.close()

            print(f"\n{keywords.capitalize()} Listings:")
            for item in items:
                print("Listing:")
                print(f"  Title: {item['title']}")
                print(f"  Price: ${item['price']}")
                print(f"  URL: {item['url']}")

            return items
    else:
        print(f"Error: {finding_response.status_code}, {finding_response.text}")
        return []
# ending notes, a bit simpler. This is meant to take advantage of pricing trends within certain items plugged in.
# although trendind does a better job, keywords, does a better job at price tracking. 



def trending_items(keyword):
    print(f"Fetching items for keyword: {keyword}")  
    finding_params = {
        'keywords': keyword,
        'paginationInput.entriesPerPage': 25,
        'sortOrder': 'BestMatch',
        'itemFilter(0).name': 'CompletedItemsOnly',
        'itemFilter(1).name': 'MinPrice',
        'itemFilter(1).value': '10',
    }

    finding_response = requests.get(finding_api_url, headers=finding_headers, params=finding_params)
    if finding_response.status_code == 200:
        finding_data = finding_response.json()
        search_results = finding_data.get('findItemsAdvancedResponse', [])[0].get('searchResult', [{}])[0]

        if int(search_results.get('@count', 0)) == 0:
            return []

        items = []
        for item in search_results.get('item', []):
            title = item.get('title', [])[0]
            price = float(item.get('sellingStatus', [])[0].get('currentPrice', [])[0].get('__value__'))
            url = item.get('viewItemURL', [])[0]
            condition = item.get('condition', [{}])[0].get('conditionDisplayName', 'Unknown')
            seller = item.get('sellerInfo', [{}])[0].get('sellerUserName', 'Unknown')
            location = item.get('location', '')

            if isinstance(condition, list):
                condition = condition[0]
            if isinstance(seller, list):
                seller = seller[0]
            if isinstance(location, list):
                location = location[0]

            items.append({
                'keyword': keyword,
                'title': title,
                'price': price,
                'url': url,
                'seller': seller,
                'condition': condition,
                'location': location
            })

        try:
            conn = mysql.connector.connect(host=mysql_host, database=mysql_database, user=mysql_user, password=mysql_password)
            cursor = conn.cursor()
                                    # items that are related to the trending tab. 
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS trending_items_listings (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    keyword VARCHAR(100),
                    title VARCHAR(255),
                    price DECIMAL(10, 2),
                    url TEXT,
                    seller VARCHAR(100),
                    `condition` VARCHAR(100),
                    location VARCHAR(100)
                )
            ''')
                                    # dame for loop that inserts items within mysql
            for item in items:
                cursor.execute('''
                    INSERT INTO trending_items_listings (keyword, title, price, url, seller, `condition`, location)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                ''', (item['keyword'], item['title'], item['price'], item['url'], item['seller'], item['condition'], item['location']))

            conn.commit()
        except mysql.connector.Error as err:
            print(f"Database connection error: {err}")
            print("Proceeding without saving to the database.")
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()

        return items
    else:
        return f"Error: {finding_response.status_code}, {finding_response.text}"

# ending notes, need to make sure that trending and keywords is used correctly.
# Trending seems to be special deals while keyword is jsut a general search for matching
# parameters.

# I need to test whether trending data can be tracked. 


# multiple items = ["apple", "orange", "banana"]
# sinlge item = ["apple"]
if __name__ == "__main__":
    sellers = ["new.techies"]  
    seller_listings = seller_items(sellers)  

    print("\nSeller Listings:")
    for seller, listings in seller_listings.items():
        print(f"\nSeller: {seller}")
        if isinstance(listings, str):  
            print(listings)
        elif not listings:
            print("No active listings found.")
        else:
            for listing in listings:
                print("Listing:")
                print(f"  Title: {listing['title']}")
                print(f"  Price: {listing['price']}")
                print(f"  URL: {listing['url']}")
                print(f"  Images: {', '.join(listing['images'])}")


if __name__ == "__main__":
    keyword_list = []
    for keyword in keyword_list:
        print(f"\nFetching listings for: {keyword.capitalize()}")
        item_listings = get_item_listings(keyword)

        # Display results
        print(f"\n{keyword.capitalize()} Listings:")
        if isinstance(item_listings, str):
            print(item_listings)  
        elif not item_listings:
            print("No active listings found.")
        else:
            for listing in item_listings:
                print("Listing:")
                print(f"  Title: {listing['title']}")
                print(f"  Price: {listing['price']}")
                print(f"  URL: {listing['url']}")




if __name__ == "__main__":        
    trending_keywords = []  
    for trending_keyword in trending_keywords:
        print(f"\nTrending Listings for {trending_keyword.capitalize()} (Excluding 'For parts or not working'):")  
        trending_items_list = trending_items(trending_keyword)  
        if isinstance(trending_items_list, str):
            print(trending_items_list) 
        elif not trending_items_list:
            print("No trending items found.")
        else:
            for item in trending_items_list:
                print("Item of note:")
                print(f"  Title: {item['title']}")
                print(f"  Price: ${item['price']}")
                print(f"  URL: {item['url']}")
                print(f"  Condition: {item['condition']}")
                print(f"  Seller: {item['seller']}")
                print(f"  Location: {item['location']}")
