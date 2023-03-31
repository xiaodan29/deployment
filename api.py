# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse, request
import pandas as pd
import numpy
import pickle
import joblib

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


# load our model (from pickle).
model = pickle.load(open("rf_model.pkl", "rb" ))


# define API resources
class Predict(Resource):
    def post(self):
        json_data = request.get_json()
        
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        # getting predictions from our model.
        # it is much simpler because we used pipelines during development
        result = list(model.predict(df))
        # result is a numpy array, jsonify it.
        return jsonify({
               "Loan Approved: ":str(result) })
               


# assign endpoint
api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)