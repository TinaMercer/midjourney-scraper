import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the website to scrape
url = "http://www.midjourney.com"

# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Scrape text data
text_data = soup.get_text()

# Scrape image links
image_links = []
for img in soup.find_all("img"):
  image_links.append(img["src"])

# Save text data to a text file
with open("text_data.txt", "w") as file:
  file.write(text_data)

# Save image links to a CSV file
with open("image_links.csv", "w", newline="") as file:
  writer = csv.writer(file)
  writer.writerow(["Image Links"])
  writer.writerows([[link] for link in image_links])

print("Scraping completed successfully!")

