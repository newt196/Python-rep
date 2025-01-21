import requests
from requests.auth import HTTPBasicAuth

client_id = nicetry'
client_secret = 'nicetry'
    
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

def seller_items(sellers):
    """Retrieve and organize listings for a list of sellers, including image URLs."""
    all_results = {}

    for seller in sellers:
        finding_params = {
            'keywords': '',
            'paginationInput.entriesPerPage': 30,
            'itemFilter(0).name': 'Seller',
            'itemFilter(0).value': seller
        }

        finding_response = requests.get(finding_api_url, headers=finding_headers, params=finding_params)

        if finding_response.status_code == 200:
            finding_data = finding_response.json()
            search_results = finding_data.get('findItemsAdvancedResponse', [])[0].get('searchResult', [{}])[0]

            if int(search_results.get('@count', 0)) == 0:
                all_results[seller] = [] 
            else:
                seller_listings = []
                for item in search_results.get('item', []):
                    listing = item.get('title', [])[0]
                    price = float(item.get('sellingStatus', [])[0].get('currentPrice', [])[0].get('__value__'))
                    item_url = item.get('viewItemURL', [])[0]

                    image_urls = item.get('galleryPlusPictureURL', item.get('galleryURL', []))
                    if isinstance(image_urls, list):
                        images = image_urls[:3] 
                    else:
                        images = [image_urls]

                    seller_listings.append({
                        'listing': listing,
                        'price': price,
                        'url': item_url,
                        'images': images
                    })
                all_results[seller] = seller_listings
        else:
            all_results[seller] = f"Error: {finding_response.status_code}, {finding_response.text}"

    return all_results


def get_item_listings(keywords):
    """Retrieve and organize listings for specific keywords, including image URLs."""
    finding_params = {
        'keywords': keywords,
        'paginationInput.entriesPerPage': 30
    }

    finding_response = requests.get(finding_api_url, headers=finding_headers, params=finding_params)

    if finding_response.status_code == 200:
        finding_data = finding_response.json()
        search_results = finding_data.get('findItemsAdvancedResponse', [])[0].get('searchResult', [{}])[0]

        if int(search_results.get('@count', 0)) == 0:
            return []  
        else:
            items = []
            for item in search_results.get('item', []):
                listing = item.get('title', [])[0]
                price = float(item.get('sellingStatus', [])[0].get('currentPrice', [])[0].get('__value__'))
                item_url = item.get('viewItemURL', [])[0]

                # Extract image URLs
                image_urls = item.get('galleryPlusPictureURL', item.get('galleryURL', []))
                if isinstance(image_urls, list):
                    images = image_urls[:3]  
                else:
                    images = [image_urls]

                items.append({
                    'listing': listing,
                    'price': price,
                    'url': item_url,
                    'images': images  
                })
            return items
    else:
        return f"Error: {finding_response.status_code}, {finding_response.text}"



def trending_items(keyword):
    """Get trending items based on sold listings for specific keywords, excluding 'For parts or not working' items."""
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
        else:
            items = []
            for item in search_results.get('item', []):
                listing = item.get('title', [])[0]
                price = float(item.get('sellingStatus', [])[0].get('currentPrice', [])[0].get('__value__'))
                item_url = item.get('viewItemURL', [])[0]
                condition_value = item.get('condition', [{}])[0].get('conditionDisplayName', '')
                seller_name = item.get('sellerInfo', [{}])[0].get('sellerUserName', 'Unknown')
                number_of_bids = item.get('sellingStatus', [{}])[0].get('bidCount', 0)
                shipping_details = item.get('shippingInfo', [{}])[0].get('shippingServiceCost', [{}])[0].get('__value__', 'Free Shipping')
                item_location = item.get('location', '')
                item_category = item.get('primaryCategory', [{}])[0].get('categoryName', 'Unknown')
                buy_it_now_price = item.get('buyItNowPrice', [{}])[0].get('__value__', 'N/A')
                image_urls = item.get('galleryPlusPictureURL', item.get('galleryURL', []))
                if isinstance(image_urls, list):
                    images = image_urls[:3]  # Check with MysQL
                else:
                    images = [image_urls]

                items.append({
                    'listing': listing,
                    'price': price,
                    'url': item_url,
                    'condition': condition_value,
                    'seller': seller_name,
                    'location': item_location,
                    'category': item_category,
                    'images': images  
                })
            return items
    else:
        return f"Error: {finding_response.status_code}, {finding_response.text}"


if __name__ == "__main__":
    # multiple items = ["apple", "orange", "banana"]
    # sinlge item = ["apple"]
    sellers = []
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
                print(f"  Title: {listing['listing']}")
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
                print(f"  Title: {listing['listing']}")
                print(f"  Price: {listing['price']}")
                print(f"  URL: {listing['url']}")
                print(f"  Images: {', '.join(listing['images'])}")


if __name__ == "__main__":
    trending_keywords = ["gaming laptop"]  
    for trending_keyword in trending_keywords:
        print(f"\nFetching trending items for: {trending_keyword.capitalize()}")
        trending_items_list = trending_items(trending_keyword)  
        
        # Display results
        print(f"\nTrending Items for {trending_keyword.capitalize()} (Excluding 'For parts or not working'):")
        if isinstance(trending_items_list, str):
            print(trending_items_list) 
        elif not trending_items_list:
            print("No trending items found.")
        else:
            for item in trending_items_list:
                condition = item['condition']
                if isinstance(condition, list):
                    condition = condition[0]  
                print("Item of note:")
                print(f"  Title: {item['listing']}")
                print(f"  Price: ${item['price']}")
                print(f"  URL: {item['url']}")
                print(f"  Condition: {condition}")
                print(f"  Seller: {item['seller']}")
                print(f"  Location: {item['location']}")
                print(f"  Images: {', '.join(item['images'])}")
 
