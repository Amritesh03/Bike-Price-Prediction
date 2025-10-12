from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib
import os

app = Flask(__name__)
CORS(app)

pipeline = joblib.load("bike_price_pipeline.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_df = pd.DataFrame({
        'mileage_k':[float(data['mileage_k'])],
        'service_count':[int(data['service_count'])],
        'engine_size':[float(data['engine_size'])],
        'engine_power':[float(data['engine_power'])],
        'brand':[data['brand']],
        'fuel_type':[data['fuel_type']],
        'bike_type':[data['bike_type']],
    })

    log_price = pipeline.predict(input_df)[0]
    price = np.exp(log_price)
    return jsonify({'predicted_price': round(price, 2)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=True)