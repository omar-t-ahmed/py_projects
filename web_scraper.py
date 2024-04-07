import urllib.request
import re

def scrape_website(url, search_term):

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')

        matches = re.findall(r"(?i)" + search_term, html)  

        if matches:
            print(f"Found {len(matches)} instances of '{search_term}':")
            print("\n".join(matches))
        else:
            print(f"No instances of '{search_term}' found.")

    except urllib.error.URLError as e:
        print(f"An error occurred: {e}")

url = "https://www.amazon.com"
search_term = "price" 

scrape_website(url, search_term)