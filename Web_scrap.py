import requests
from bs4 import BeautifulSoup
import csv
print('''

SCRAPING DATA
Isme time lagega Sir, But effective hai ..........................................................................
      ............................................
      Bus thora sa time lagega .....................................................................................
      ........................     

''')
# Function to determine the category based on the URL
def get_category(url):
    if "cars" in url:
        return "Cars"
    elif "items/q-Phone" in url:
        return "Phone"
    elif "computers-accessories" in url:
        return "Computer_Accessory"
    elif "bikes" in url:
        return "Bikes"
    else:
        return "Other"

# Function to scrape data from a given URL and write to CSV
def scrape_and_write(url, category):
    with open(f"{category}.csv", "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        # Write headers only once if the file is empty
        if csv_file.tell() == 0:
            writer.writerow(["Title", "Location", "Price", 'Time'])

        for i in range(1, 70):
            full_url = f"{url}{i}"
            response = requests.get(full_url)
            soup = BeautifulSoup(response.text, "html.parser")
            divs = soup.find_all("div", class_="_9bea76df")
            for div in divs:
                try:
                    price = div.find("span", class_="_95eae7db").text.strip()
                except AttributeError:
                    price = ""
                try:
                    title = div.find("h2", class_="a5112ca8").text.strip()
                except AttributeError:
                    title = ""
                try:
                    location = div.find("span", class_="_2fc90438").text.strip()
                except AttributeError:
                    location = ""
                try:
                    time = div.find("span", class_="c4ad15ab f2dd4da1").text.strip()
                except AttributeError:
                    time = ""
                # Write the extracted information to the CSV file
                writer.writerow([title, location, price, time])

# URLs for scraping
urls = [
    "https://www.olx.com.pk/cars_c84?page=",
    "https://www.olx.com.pk/items/q-Phone?page=",
    'https://www.olx.com.pk/computers-accessories_c443?page=',
    "https://www.olx.com.pk/bikes_c1898?page="
]

# Iterate through URLs, scrape data, and write to CSV
for url in urls:
    category = get_category(url)
    scrape_and_write(url, category)

print("Data has been written to separate CSV files for each category.")
