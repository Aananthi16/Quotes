from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "The best way to predict the future is to invent it.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "An unexamined life is not worth living."
]

@app.route('/')
def home():
    return f"<h1>{random.choice(quotes)}</h1>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Use Render's PORT env var
    app.run(host='0.0.0.0', port=port)     
    
