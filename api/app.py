from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model (placeholder path)
model = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    amount = data.get('amount', 0)
    velocity = data.get('velocity', 0)

    features = np.array([[amount, velocity]])
    prediction = model.predict(features)[0]

    return jsonify({
        "fraud_prediction": int(prediction)
    })

if __name__ == '__main__':
    app.run(debug=True)
