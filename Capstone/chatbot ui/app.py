import logging
from flask import Flask, render_template, request, jsonify
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import requests
from transformers import pipeline
import spacy
import json
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Enable detailed logging
logging.basicConfig(level=logging.DEBUG)

# Load models and setup
try:
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    app.logger.debug("Sentence Transformer model loaded successfully.")
except Exception as e:
    app.logger.error(f"Error loading Sentence Transformer model: {e}")

try:
    intent_model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    app.logger.debug("Intent model loaded successfully.")
except Exception as e:
    app.logger.error(f"Error loading Intent Detection model: {e}")

try:
    nlp = spacy.load("en_core_web_sm")
    app.logger.debug("Spacy NLP model loaded successfully.")
except Exception as e:
    app.logger.error(f"Error loading Spacy NLP model: {e}")

# Load and process dataset from the Excel file
try:
    df = pd.read_excel("./kolorist_chatbot_dataset.xlsx")
    app.logger.debug(f"Dataset loaded successfully: {df.shape[0]} rows.")
except Exception as e:
    app.logger.error(f"Error loading Excel dataset: {e}")

#organize and format the chatbot response in a clear manner
# Organize and format the chatbot response in a clean, styled HTML-friendly manner
def format_bot_response(raw_response):
    # Replace Markdown-style line breaks with <br>
    message = raw_response.replace("\n", "<br>")

    # Convert bullet points into list items if any
    if "-" in message:
        lines = message.split("<br>")
        list_items = ""
        for line in lines:
            if line.strip().startswith("-"):
                list_items += f"<li>{line.strip()[1:].strip()}</li>"
            elif line.strip():
                list_items += f"<p>{line.strip()}</p>"

        message_html = f"<ul>{list_items}</ul>"
    else:
        message_html = message

    # Wrap it with a heading
    response_html = f"""
    <strong>Serphia AI 🔮:</strong> {message_html}
    """
    return response_html
# Ensure the expected column exists
if 'User Input Example' not in df.columns:
    app.logger.error("Column 'User Input Example' not found in the dataset.")
    raise ValueError("Column 'User Input Example' not found in the dataset.")

documents = df['User Input Example'].dropna().tolist()

# Encode documents using SentenceTransformer
try:
    doc_embeddings = embedder.encode(documents)
    faiss_index = faiss.IndexFlatL2(doc_embeddings.shape[1])
    faiss_index.add(np.array(doc_embeddings, dtype=np.float32))
    app.logger.debug("Document embeddings created and FAISS index populated.")
except Exception as e:
    app.logger.error(f"Error encoding documents: {e}")

@app.route("/")
def ui():
    try:
        app.logger.debug("Rendering index.html")
        return render_template("index.html")
    except Exception as e:
        app.logger.error(f"Error rendering index.html: {e}")
        return jsonify({"error": "Error rendering the home page."})

@app.route('/ollama-chat', methods=['POST'])
def ollama_chat():
    try:
        user_message = request.json.get('message')
        app.logger.debug(f"Received message: {user_message}")

        # Intent Detection
        intents = ["weather inquiry", "color info", "greeting"]
        intent_result = intent_model(user_message, candidate_labels=intents)
        intent = intent_result["labels"][0]
        app.logger.debug(f"Intent detected: {intent}")

        # Entity Extraction
        doc = nlp(user_message)
        entities = [ent.text for ent in doc.ents]
        app.logger.debug(f"Entities extracted: {entities}")

        # FAISS Search for context
        query_embedding = embedder.encode([user_message])
        query_embedding = np.array(query_embedding, dtype=np.float32)
        D, I = faiss_index.search(query_embedding, 2)
        retrieved_docs = [documents[i] for i in I[0]]
        app.logger.debug(f"Retrieved documents: {retrieved_docs}")

        context = "\n".join(retrieved_docs)

        # Modify the response with actual contact details
        contact_info = """
        Here are the ways you can contact Kolorist SG Salon:
        
        • **Phone**: You can reach us at +65 6294 8888. Our friendly staff will be more than happy to attend to your queries and concerns.
        • **Email**: Send us an email at info@koloristsg.com, and we'll respond promptly. Please provide as much detail as possible so that we can better assist you.
        • **Online Form**: You can also submit a contact form on our website, and we'll get back to you within 24 hours.
        • **Social Media**: Follow us on social media platforms like Facebook, Instagram, or Twitter, and send us a direct message. We're always available to help!
        
        Remember, at Kolorist SG Salon, your satisfaction is our top priority. If you have any questions or concerns about our services, don't hesitate to reach out.
        """

        # Build a clean, AI-friendly prompt
        prompt = f"""
You are Serphia AI 🔮, a helpful assistant for Kolorist SG Salon.

Please answer the user's question politely, clearly, and concisely. If relevant, include key information from the provided context. Format your response in neat bullet points or organized short paragraphs as appropriate.

Context:
{context if context else 'No relevant documents found.'}

User's Question:
{user_message}

Your Response:
{contact_info}
"""

        app.logger.debug(f"Prompt sent to Ollama: {prompt}")

        # Call Ollama API
        ollama_response = requests.post(
            'http://localhost:11434/api/generate',
            json={'model': 'llama3', 'prompt': prompt},
            stream=True
        )

        response_text = ""
        for line in ollama_response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8').strip()
                try:
                    response_json = json.loads(decoded_line)
                    if 'response' in response_json:
                        response_text += response_json['response']
                except json.JSONDecodeError:
                    app.logger.debug(f"Non-JSON line from Ollama: {decoded_line}")
                    continue

        response_text = response_text.strip() if response_text else 'Sorry, no response from Serphia AI 🔮.'
        bot_reply = format_bot_response(response_text)

        app.logger.debug(f"Ollama AI reply: {bot_reply}")

        return jsonify({'response': bot_reply})

    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error connecting to Ollama: {e}")
        return jsonify({'response': "Error: Could not connect to the Ollama server."})

    except Exception as e:
        app.logger.error(f"Error in ollama-chat: {e}")
        return jsonify({'response': "Sorry, an error occurred while processing your request."})
    
if __name__ == '__main__':
    app.run(debug=True)