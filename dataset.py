import requests
from bs4 import BeautifulSoup

urls = [
    "https://kolorist.sg/",
    "https://kolorist.sg/pages/services",
    "https://api.whatsapp.com/send/?phone=6582184070&text=hello%20Kolorist,%20I%20would%20like%20to%20make%20an%20appointment",
    "https://kolorist.sg/pages/personal-colour-analysis",
    "https://kolorist.sg/blogs/blog",
    "https://kolorist.sg/blogs/news",
    "https://bookings.gettimely.com/koloristsg/book?uri=https%3A%2F%2Fbook.gettimely.com%2FBooking%2FLocation%2F176667%3Fmobile%3DTrue%26locationId%3D279343%26params%3D%25253fclient-login%25253dtrue%252526location%25253d279343",
    "https://maps.app.goo.gl/SaiSjcHX3ZEnBKLHA",
    "https://kolorist.sg/pages/kolorist-head-spa",
    "https://kolorist.sg/pages/korean-make-up-services",
    "https://kolorist.sg/pages/frizzy-lab",
    "https://kolorist.sg/pages/korean-headspa-training",
    "https://www.instagram.com/kolorist.sg",
    "https://www.tiktok.com/@salon.kolorist.sg",
    "https://www.facebook.com/kolorist.sg"
]

def scrape(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        content_type = response.headers.get('Content-Type', '')

        if "text/html" not in content_type:
            return f"\n--- {url} ---\n[Skipped: Non-HTML content]\n"

        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = "\n".join([p.get_text(strip=True) for p in soup.find_all('p')])
        return f"\n--- {url} ---\n{page_text.strip()}\n"

    except Exception as e:
        return f"\n--- {url} ---\n[Error scraping: {str(e)}]\n"

all_scraped_text = ""
for url in urls:
    print(f"Scraping: {url}")
    all_scraped_text += scrape(url)

with open("kolorist_dataset.txt", "w", encoding="utf-8") as file:
    file.write(all_scraped_text)

print("✅ All done! Dataset saved to kolorist_dataset.txt")
