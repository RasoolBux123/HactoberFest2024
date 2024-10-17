import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# Create a folder to save the scraped images
folder_name = "downloaded_images"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# URL of the website to scrape
url = "https://example.com"  # Replace with the target website

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all image tags
img_tags = soup.find_all('img')

# Loop through the image tags and download them
for img in img_tags:
    # Get the image source URL
    img_url = img.get('src')
    
    # Join the base URL with the image URL in case the image URL is relative
    img_url = urljoin(url, img_url)

    # Get the image name from the URL
    img_name = os.path.basename(img_url)

    # Download and save the image
    img_response = requests.get(img_url)
    
    # Save the image to the folder
    with open(os.path.join(folder_name, img_name), 'wb') as img_file:
        img_file.write(img_response.content)
        print(f"Downloaded {img_name}")

print("Image scraping completed!")
