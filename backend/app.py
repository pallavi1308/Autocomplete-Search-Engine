from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from backend.trie import Trie  
import os

app = Flask(__name__, template_folder='../templates')
app = Flask(__name__)   # ✅ This was missing
CORS(app)
# Load dictionary into Trie
trie = Trie()
with open('backend/words.txt', 'r') as f:
    for word in f:
        trie.insert(word.strip().lower())

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/suggestions', methods=['GET'])
def get_suggestions():
    query = request.args.get('query', '').lower()
    if not query:
        return jsonify([])
    suggestions = trie.starts_with(query)
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)
