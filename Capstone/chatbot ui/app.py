from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

# Initialize the Flask app
app = Flask(__name__)

def scrape_website_content():
    url = 'https://kolorist.sg/'  # Replace with your actual target URL
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = [p.text for p in soup.find_all('p')]
        website_content = "\n".join(paragraphs)
        return website_content
    except Exception as e:
        print(f"Error scraping website: {e}")
        return "Sorry, could not fetch website data."
    
@app.route("/")  # Index route to serve the homepage
def index():
    return render_template("index.html")

# Basic dummy chatbot logic
def get_chatbot_response(user_input):
    if "color" in user_input.lower():
        return "I see you're interested in colors. I'm Kolorist, after all 🎨"
    return "Tell me more about what you're thinking."

# Route to handle Ollama AI chat
@app.route('/ollama-chat', methods=['POST'])
def ollama_chat():
    user_message = request.json.get('message')

    try:
        ollama_response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': 'llama3',
                'prompt': user_message,
                'stream': False,
                'options': {
                    'temperature': 0.9,
                    'top_p': 0.95,
                    'top_k': 50
                }
            }
        )
        result = ollama_response.json()
        bot_reply = result.get('response', 'Sorry, no response from Ollama.')

    except requests.exceptions.ConnectionError:
        bot_reply = "Error: Could not connect to the Ollama server. Is it running?"

    return jsonify({'response': bot_reply})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
