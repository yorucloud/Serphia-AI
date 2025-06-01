import requests
from bs4 import BeautifulSoup
import openpyxl
import time

# Define target URLs
pages = {
    "Home": "https://kolorist.sg/",
    "Services": "https://kolorist.sg/pages/services",
    "Booking": "https://kolorist.sg/pages/book",
    "Contact": "https://kolorist.sg/pages/book",
    "About": "https://kolorist.sg/pages/about",
    "Shop": "https://kolorist.sg/pages/about",
    "Personal Colour Analysis": "https://kolorist.sg/pages/personal-colour-analysis",
    "Blog": "https://kolorist.sg/blogs/blog",
    "News": "https://kolorist.sg/blogs/news"
}

# Initialize workbook
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Kolorist Dataset"
ws.append(["Intent", "User Input Example", "Bot Response", "Source Page"])

# Function to determine intent based on page title
def determine_intent(title):
    title = title.lower()
    if "service" in title:
        return "service_info"
    elif "book" in title:
        return "booking_info"
    elif "contact" in title:
        return "contact_info"
    elif "about" in title:
        return "about_info"
    elif "shop" in title or "collection" in title:
        return "product_info"
    elif "personal colour analysis" in title:
        return "personal_colour_info"
    elif "blog" in title or "news" in title:
        return "blog_info"
    else:
        return "general_info"

# Scrape content
for page_name, url in pages.items():
    print(f"Scraping {page_name} page...")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Get all paragraph and heading text
        texts = []
        for tag in soup.find_all(['p', 'h1', 'h2', 'h3']):
            text = tag.get_text(strip=True)
            if text:
                texts.append(text)

        # Combine and write entries
        if texts:
            intent = determine_intent(page_name)
            for i in range(min(10, len(texts))):  # Adjust the number as needed
                ws.append([
                    intent,
                    f"What can you tell me about {page_name.lower()}?",
                    texts[i],
                    url
                ])
        time.sleep(1)  # Respectful scraping
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# Save workbook
wb.save("kolorist_chatbot_dataset.xlsx")
print("Scraping and dataset generation complete!")
