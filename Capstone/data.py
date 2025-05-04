import requests
from bs4 import BeautifulSoup


url = 'https://kolorist.sg/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

paragraphs = [p.text for p in soup.find_all('p')]

website_content = "\n".join(paragraphs)

print(website_content)
