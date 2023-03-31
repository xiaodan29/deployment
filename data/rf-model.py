from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse, request
import pandas as pd
import numpy
import pickle
import joblib

app = Flask(__name__)
api=Api(app)

# Load the model
model = pickle.load(opem('rf_model.pkl','rb')

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.json

    # Convert JSON data to a DataFrame
    input_data = pd.DataFrame([data])

    # Make predictions using the model
    predictions = model.predict(input_data)

    # Convert the predictions to a JSON response
    response = {'predictions': predictions.tolist()}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)
