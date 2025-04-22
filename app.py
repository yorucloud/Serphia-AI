from flask import Flask, render_template, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Your chatbot logic goes here
def get_chatbot_response(user_input):
    # For now, this is dummy logic — replace with your AI later
    if "color" in user_input.lower():
        return "I see you're interested in colors. I'm Kolorist, after all 🎨"
    return "Tell me more about what you're thinking."

@app.route("/")  # Ensure the app is initialized before routes are defined
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = get_chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
