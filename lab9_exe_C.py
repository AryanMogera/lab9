"""
===================================================
Name        : lab9.exe_C.py
Assignment  : Lap, Exercise C
Author(s)   : Aryan Mogera, Sheharyar
Submission  : March 20, 2024
Description : Fetch data by Python
===================================================
"""

import requests
import json 

'''Fetches product data from the given URL, returns list of dictionaries
containing product details. Returns None if an error occurs.'''

def fetch_product_data(url):
    try:
        response = requests.get(url)
        # Raises an error for bad responses
        response.raise_for_status()
        # The JSON structure includes a 'products' key
        return response.json()['products']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    
"""Lists all products in the given list of dictionaries"""
def list_all_products(products):
    for product in products:
        print(f"{product.get('title')}")

""" Searches for a product with the given name in the list of dictionaries.
returns the product if found, otherwise prints an error message and returns None."""
def search_product(products, name):
    found_products = [product for product in products if product.get('title').lower() == name.lower()]
    if found_products:
        return found_products[0]
    else:
        print(f"Product '{name}' not found")
        return None

def main():
    products_url = "https://dummyjson.com/products"
    products = fetch_product_data(products_url)

    if products:
        while True:
            choice = input("Choose an option:\n1. List all products\n2. Search for a product\n3. Exit\n")
            if choice == "1":
                list_all_products(products)
            elif choice == "2":
                product_name = input("Enter product name: ")
                product = search_product(products, product_name)
                if product:
                    print("\nProduct details:")
                    # Pretty print the product details
                    print(json.dumps(product, indent=4))
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Failed to fetch product data.")

if __name__ == "__main__":
    main()
