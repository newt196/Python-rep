





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


