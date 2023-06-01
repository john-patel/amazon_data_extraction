# import requests
# from bs4 import BeautifulSoup

# url = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"

# # Send a GET request to the URL and retrieve the page content
# response = requests.get(url)

# # Create a BeautifulSoup object
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all the product listings on the page
# product_listings = soup.find_all('div', {'data-component-type': 's-search-result'})

# for listing in product_listings:
#     # Extract the product name
#     product_name = listing.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'}).text.strip()

#     # Extract the price
#     price_element = listing.find('span', {'class': 'a-offscreen'})
#     if price_element:
#         price = price_element.text.strip()
#     else:
#         price = 'N/A'

#     # Extract the rating
#     rating_element = listing.find('span', {'class': 'a-icon-alt'})
#     if rating_element:
#         rating = rating_element.text.strip()
#     else:
#         rating = 'N/A'

#     # Extract the seller name
#     seller_element = listing.find('span', {'class': 'a-size-small a-color-secondary'})
#     if seller_element:
#         seller = seller_element.text.strip()
#     else:
#         seller = 'N/A'

#     # Print the extracted information
#     print("Product Name:", product_name)
#     print("Price:", price)
#     print("Rating:", rating)
#     print("Seller Name:", seller)
#     print("-------------------------------------")

import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"

# Send a GET request to the URL and retrieve the page content
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the product listings on the page
product_listings = soup.find_all('div', {'data-component-type': 's-search-result'})

# Open a CSV file in write mode
with open('products.csv', mode='w', newline='', encoding='utf-8-sig') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the header row
    writer.writerow(['Product Name', 'Price', 'Rating', 'Seller Name'])

    # Iterate over the product listings
    for listing in product_listings:
        # Extract the product name
        product_name = listing.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'}).text.strip()

        # Extract the price
        price_element = listing.find('span', {'class': 'a-offscreen'})
        if price_element:
            price = price_element.text.strip()
            # price = int(price)
        else:
            price = 'N/A'

        # Extract the rating
        rating_element = listing.find('span', {'class': 'a-icon-alt'})
        if rating_element:
            rating = rating_element.text.strip()
        else:
            rating = 'N/A'

        # Extract the seller name
        seller_element = listing.find('span', {'class': 'a-size-small a-color-secondary'})
        if seller_element:
            seller = seller_element.text.strip()
        else:
            seller = "Amazon"


        # Write the row to the CSV file
        writer.writerow([product_name, price, rating, seller])

print("CSV file created successfully.")


