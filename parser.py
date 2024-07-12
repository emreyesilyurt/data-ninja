from bs4 import BeautifulSoup

def parse_item_details(page_content):
    print("Parsing item details...")
    soup = BeautifulSoup(page_content, 'html.parser')
    item_name = soup.find('h1', {'class': 'product-name'}).text.strip()
    item_description = soup.find('div', {'class': 'product-description'}).text.strip()
    item_specs = soup.find('table', {'class': 'product-specs'}).text.strip()
    
    print("Item details parsed successfully.")
    return {
        'name': item_name,
        'description': item_description,
        'specs': item_specs
    }
