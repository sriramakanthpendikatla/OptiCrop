from pathlib import Path
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent


def load_pickle(filename):
    path = BASE_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f'Required file not found: {path}')
    with path.open('rb') as f:
        return pickle.load(f)


# Load model, scaler, and label encoder from the Flask app folder only
model = load_pickle('model.pkl')
scaler = load_pickle('scaler.pkl')
label_encoder = load_pickle('label_encoder.pkl')

FEATURE_NAMES = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/find-your-crop')
def find_crop():
    return render_template('find_crop.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form values
    N = float(request.form['N'])
    P = float(request.form['P'])
    K = float(request.form['K'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])

    # Prepare input as DataFrame (match the training preprocessing)
    input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                               columns=FEATURE_NAMES)

    # Match the training notebook: log-transform K before scaling
    input_data['K'] = np.log1p(input_data['K'])

    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)
    predicted_crop = label_encoder.inverse_transform(prediction)[0]
    with open(BASE_DIR / 'prediction_debug.txt', 'w', encoding='utf-8') as f:
        f.write(f'INPUT: {input_data.to_dict(orient="records")[0]}\nPREDICTED_CROP: {predicted_crop}\n')

    return render_template('result.html', crop=predicted_crop)

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))