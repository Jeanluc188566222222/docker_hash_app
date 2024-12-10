from flask import Flask, request, jsonify, render_template
import hashlib

app = Flask(__name__)

# Stockage des hachages calculés en mémoire
history = []

# Route pour afficher la page HTML
@app.route('/')
def index():
    return render_template('index.html')

# Route pour calculer le hachage
@app.route('/hash', methods=['POST'])
def calculate_hash():
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({'error': 'Missing input field'}), 400

    input_str = data.get('input', '')
    algorithm = data.get('algorithm', 'sha256')  # Par défaut SHA256

    try:
        hash_function = getattr(hashlib, algorithm)
        hash_value = hash_function(input_str.encode()).hexdigest()

        history.append({'input': input_str, 'algorithm': algorithm, 'hash': hash_value})

        return jsonify({'input': input_str, 'algorithm': algorithm, 'hash': hash_value})

    except AttributeError:
        return jsonify({'error': 'Unsupported hash algorithm'}), 400

# Route pour récupérer l'historique
@app.route('/history', methods=['GET'])
def get_history():
    if not history:
        return jsonify({"message": "No history available"}), 200
    return jsonify(history), 200

if __name__ == '__main__':
    app.run(debug=True)
