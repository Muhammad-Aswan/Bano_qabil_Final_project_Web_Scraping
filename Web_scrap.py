import requests
from bs4 import BeautifulSoup
import csv

####             SCRAPING OF DATA FROM OLX.com
#                Scraping Car data 
                #  Phones Data 
                #  Bikes and Computer data
                #  from olx.com

# Open the CSV file in append mode
with open("Supreme.csv", "a", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    # Write headers only once if the file is empty
    if csv_file.tell() == 0:
        writer.writerow(["Title", "Location", "Price", 'Time'])

    urls = [
        "https://www.olx.com.pk/vehicles_c5?page=",
        "https://www.olx.com.pk/items/q-Phone?page=",
        'https://www.olx.com.pk/computers-accessories_c443?page=',
        "https://www.olx.com.pk/bikes_c1898?page="
    ]

    for url in urls:
        for i in range(1, 75):
            # Send a GET request to the URL
            full_url = url + str(i)
            response = requests.get(full_url)
            print(response)
            # Parse the HTML content
            soup = BeautifulSoup(response.text, "html.parser")
            print(soup)
            # Find all divs with class="_9bea76df"
            divs = soup.find_all("div", class_="_9bea76df")
            print(divs)
            # Iterate over each div and extract desired information
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

print("Data has been written to Aswan.csv file.")
