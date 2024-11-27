import torch
from flask import Flask, jsonify

app = Flask(__name__)

# Load the model (example: a simple model)
model = torch.nn.Linear(10, 1)

@app.route('/')
def home():
    return "PyTorch Model Server"

@app.route('/predict', methods=['POST'])
def predict():
    return jsonify({"message": "Prediction endpoint"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
