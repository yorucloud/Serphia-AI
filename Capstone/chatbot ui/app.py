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

        # Build a clean, AI-friendly prompt
        prompt = f"""
You are Serphia AI 🔮, a helpful assistant for Kolorist SG Salon.

Please answer the user's question politely, clearly, and concisely. If relevant, include key information from the provided context. Format your response in neat bullet points or organized short paragraphs as appropriate.

Context:
{context if context else 'No relevant documents found.'}

User's Question:
{user_message}

Your Response:
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

        bot_reply = response_text.strip() if response_text else 'Sorry, no response from Serphia AI 🔮.'
        app.logger.debug(f"Ollama AI reply: {bot_reply}")

        return jsonify({'response': bot_reply})

    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error connecting to Ollama: {e}")
        return jsonify({'response': "Error: Could not connect to the Ollama server."})

    except Exception as e:
        app.logger.error(f"Error in ollama-chat: {e}")
        return jsonify({'response': "Sorry, an error occurred while processing your request."})

if __name__ == "__main__":
    try:
        app.run(debug=True, host='0.0.0.0', port=5001)
        app.logger.debug("Flask app running on http://127.0.0.1:5001/")
    except Exception as e:
        app.logger.error(f"Error starting Flask app: {e}")
