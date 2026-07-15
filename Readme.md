# OptiCrop: Smart Agricultural Production Optimization Engine

OptiCrop is a machine learning-based crop recommendation system. Given soil and climate
readings (nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall), it
predicts the most suitable crop to grow, and includes exploratory analysis to group crops
by season and by soil/climate profile.

## Overview

- **Problem**: Recommend the best crop for a given set of soil and environmental
  conditions, to support data-driven farming decisions.
- **Approach**: A Logistic Regression classifier trained on standardized soil/climate
  features, evaluated against 22 crop classes.
- **Extras**: Rule-based seasonal grouping (Kharif / Rabi / Summer), and K-Means clustering
  to uncover natural soil/climate groupings independent of crop labels.
- **Deployment**: A simple Flask web app (`app.py`) serves the trained model for real-time
  predictions through a form-based UI.

## Results

| Metric | Score |
|---|---|
| Accuracy | 97.27% |
| Precision | 97.42% |
| Recall | 97.27% |
| F1-Score | 97.25% |
| ROC-AUC | 0.9998 |

K-Means (k=4, chosen via the elbow method) revealed four natural soil/climate clusters
independent of crop label, described further in the notebook's conclusion.

## Entity Relationship Diagram

The system's data model separates users, soil readings, crops, datasets, trained models,
predictions, and generated reports into distinct entities to reduce redundancy and support
scalable prediction tracking. See `docs/ERD.png` (or the ER Diagram section in the project
workspace) for the full diagram.

## Repository structure

```
OptiCrop/
├── app.py                     # Flask web app for serving predictions
├── Crop_recommendation.csv    # Dataset (soil/climate features + crop label)
├── model/
│   ├── model.pkl               # Trained Logistic Regression model
│   ├── scaler.pkl              # Fitted StandardScaler
│   └── label_encoder.pkl       # Fitted LabelEncoder for crop names
├── notebook/
│   └── OptiCrop_Model.ipynb    # Full EDA, modeling, clustering, and conclusion
├── static/
│   └── style.css               # Frontend styling
├── templates/
│   ├── index.html              # Input form
│   └── result.html             # Prediction result page
└── requirements.txt
```

## Setup and run

**1. Clone the repository**
```bash
git clone https://github.com/sriramakanthpendikatla/OptiCrop.git
cd OptiCrop
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the web app**
```bash
python app.py
```
Then open `http://127.0.0.1:5000` in your browser, enter soil/climate values, and get a
crop recommendation.

**5. (Optional) Explore the notebook**
```bash
jupyter notebook notebook/OptiCrop_Model.ipynb
```
This walks through data cleaning, EDA, outlier handling, seasonal grouping, model
training/evaluation, K-Means clustering, and the project conclusion.

## Tech stack

Python · Flask · pandas · NumPy · scikit-learn · matplotlib · seaborn

## Future improvements

- Compare Logistic Regression against ensemble models (Random Forest, XGBoost)
- Incorporate soil type or geographic region as additional features
- Deploy the model behind a REST API for integration with other tools
