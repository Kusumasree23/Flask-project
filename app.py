from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Route to return student number
@app.route('/')
def student_number():
    return jsonify({"student_number": "200600636"})  # Replace with your actual student number

# Route for Dialogflow webhook fulfillment
@app.route('/webhook', methods=['POST'])
def webhook():
    # Extract JSON data from Dialogflow request
    req = request.get_json()
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName')

    # Handle "Daily Self-Care Tip" intent
    if intent == "Daily Self-Care Tip":
        tips = [
            "Take a 10-minute break to meditate and breathe deeply.",
            "Enjoy a warm cup of tea while listening to your favorite music.",
            "Go for a short walk to refresh your mind and body.",
            "Write down three things you're grateful for today.",
            "Ask for help when you need it—you're doing an amazing job!"
        ]
        tip = random.choice(tips)
        response = {
            "fulfillmentText": tip
        }
        return jsonify(response)

    # Default response if no matching intent
    return jsonify({"fulfillmentText": "No matching intent found."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
