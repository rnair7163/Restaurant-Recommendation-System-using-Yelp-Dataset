# Dependencies
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"

@app.route('/predict', methods=['POST'])
def predict():
    if mod:
        try:
            json_ = request.json
            print(json_)
            query = str(json_)

            prediction = list(mod.text_process(query))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    mod = joblib.load("D:/DPA Data/dpa_project/recommender_model.pk") # Load "model.pkl"
    print ('Model loaded')

    app.run(port=port, debug=True)
