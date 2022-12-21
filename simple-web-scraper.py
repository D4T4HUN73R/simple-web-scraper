import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the website and retrieve the response
response = requests.get('http://www.example.com')

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the <p> elements on the page
paragraphs = soup.find_all('p')

# Print the text of each paragraph
for p in paragraphs:
    print(p.text)
