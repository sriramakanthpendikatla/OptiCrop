from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model, scaler, label encoder
model = pickle.load(open('model/model.pkl', 'rb'))
scaler = pickle.load(open('model/scaler.pkl', 'rb'))
label_encoder = pickle.load(open('model/label_encoder.pkl', 'rb'))

FEATURE_NAMES = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

@app.route('/')
def home():
    return render_template('index.html')

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

    # Prepare input as DataFrame (fixes feature-name warning)
    input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                               columns=FEATURE_NAMES)
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)
    predicted_crop = label_encoder.inverse_transform(prediction)[0]

    return render_template('result.html', crop=predicted_crop)

if __name__ == '__main__':
    app.run(debug=True)