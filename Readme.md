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
scalable prediction tracking. See
[`7.Project Documentation/entity relationship diagram/opticrop_erd.png`](<7.Project Documentation/entity relationship diagram/opticrop_erd.png>)
for the full diagram.

## Repository structure

```
OptiCrop/
├── 1. Brainstorming & Ideation/
│   ├── Brainstorming & Idea Prioritization.pdf
│   ├── Define Problem Statements.pdf
│   └── Empathy Map.pdf
├── 2.Requirement Analysis/
│   ├── Customer Journey Map.pdf
│   ├── Data Flow Diagram.pdf
│   ├── Solution Requirements.pdf
│   └── Technology Stack.pdf
├── 3. Project Design Phase/
│   ├── Problem-Solution Fit.pdf
│   ├── Proposed Solution.pdf
│   └── Solution Architecture.pdf
├── 4. Project Planning Phase/
│   └── Project Planning.pdf
├── 5. Project Development Phase/
│   └── Coding & Solution.pdf
├── 6.Project Testing/
│   └── Performance Testing.pdf
├── 7.Project Documentation/
│   ├── Dataset/
│   │   └── Crop_recommendation.csv    # Dataset (soil/climate features + crop label)
│   ├── Flask/                          # Deployable Flask web app
│   │   ├── app.py                      # Flask app for serving predictions
│   │   ├── model.pkl                   # Trained Logistic Regression model
│   │   ├── scaler.pkl                  # Fitted StandardScaler
│   │   ├── label_encoder.pkl           # Fitted LabelEncoder for crop names
│   │   ├── requirements.txt
│   │   ├── static/
│   │   │   └── style.css               # Frontend styling
│   │   └── templates/
│   │       ├── base.html               # Shared layout
│   │       ├── index.html              # Input form
│   │       ├── find_crop.html          # Prediction form page
│   │       ├── result.html             # Prediction result page
│   │       └── about.html              # About page
│   ├── data_preprocessing/
│   │   └── preprocessing.ipynb         # Data cleaning & preprocessing steps
│   ├── entity relationship diagram/
│   │   └── opticrop_erd.png            # ER diagram image
│   ├── visualization_analisys/
│   │   └── visualization.ipynb         # EDA & visualization notebook
│   ├── opticrop_architecture.png       # System architecture diagram
│   ├── Project Executable Files.pdf
│   └── Sample Project Documentation.pdf
├── 8.Project Demonstration/
│   ├── Communication_TEMPLATE.md
│   ├── Project_Demo_Planning_TEMPLATE.md
│   ├── Scalability_Future_Plan_TEMPLATE.md
│   └── Team_Involvement_TEMPLATE.md
├── notebook/
│   └── OptiCrop_Model.ipynb            # Full EDA, modeling, clustering, and conclusion
└── requirements.txt                     # Root-level dependencies for running the app
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

The Flask app lives inside `7.Project Documentation/Flask/`:

```bash
cd "7.Project Documentation/Flask"
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
