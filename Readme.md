<div align="center">

# 🌾 OptiCrop
### Smart Agricultural Production Optimization Engine

*A machine learning system that recommends the best crop to grow based on soil and climate conditions.*

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/status-active-success?style=for-the-badge)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Results](#-results)
- [Entity Relationship Diagram](#-entity-relationship-diagram)
- [Repository Structure](#-repository-structure)
- [Setup and Run](#-setup-and-run)
- [Tech Stack](#-tech-stack)
- [Future Improvements](#-future-improvements)

---

## 🌱 Overview

OptiCrop takes seven soil and climate readings — **nitrogen, phosphorus, potassium,
temperature, humidity, pH, and rainfall** — and predicts the most suitable crop to grow,
helping turn raw field data into a confident, data-driven planting decision.

| | |
|---|---|
| 🎯 **Problem** | Recommend the best crop for a given set of soil and environmental conditions, to support data-driven farming decisions. |
| 🧠 **Approach** | A Logistic Regression classifier trained on standardized soil/climate features, evaluated against **22 crop classes**. |
| ✨ **Extras** | Rule-based seasonal grouping (*Kharif / Rabi / Summer*) and K-Means clustering to uncover natural soil/climate groupings independent of crop labels. |
| 🚀 **Deployment** | A Flask web app (`app.py`) serves the trained model for real-time predictions through a simple form-based UI. |

---

## 📊 Results

<div align="center">

| Metric | Score |
|:---|:---:|
| 🎯 Accuracy | **97.27%** |
| 🎯 Precision | **97.42%** |
| 🎯 Recall | **97.27%** |
| 🎯 F1-Score | **97.25%** |
| 🎯 ROC-AUC | **0.9998** |

</div>

> 🔍 **Clustering insight:** K-Means (k=4, chosen via the elbow method) revealed four
> natural soil/climate clusters, independent of crop label — explored further in the
> notebook's conclusion.

---

## 🗺️ Entity Relationship Diagram

The system's data model separates **users, soil readings, crops, datasets, trained
models, predictions, and generated reports** into distinct entities — reducing
redundancy and supporting scalable prediction tracking.

📎 Full diagram: [`7.Project Documentation/entity relationship diagram/opticrop_erd.png`](<7.Project Documentation/entity relationship diagram/opticrop_erd.png>)

---

## 📂 Repository Structure

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
│   ├── Flask/                          # 🚀 Deployable Flask web app
│   │   ├── app.py                      # Flask app for serving predictions
│   │   ├── model.pkl                   # Trained Logistic Regression model
│   │   ├── scaler.pkl                  # Fitted StandardScaler
│   │   ├── label_encoder.pkl           # Fitted LabelEncoder for crop names
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
│   ├── screenshot_home.png             # Home page screenshot
│   ├── screenshot_result.png           # Prediction result screenshot
│   ├── requirements.txt
│   ├── .env.example
│   ├── Project Executable Files.pdf
│   └── Sample Project Documentation.pdf
├── 8.Project Demonstration/
│   ├── Communication.md
│   ├── Project Demo Planning.md
│   ├── Scalability & Future Plan.md
│   └── Team Involvement in Demonstration.md
└── notebook/
    └── OptiCrop_Model.ipynb            # Full EDA, modeling, clustering, and conclusion
```

---

## ⚙️ Setup and Run

**1️⃣ Clone the repository**

```bash
git clone https://github.com/sriramakanthpendikatla/OptiCrop.git
cd OptiCrop
```

**2️⃣ Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

**3️⃣ Install dependencies**

```bash
pip install -r "7.Project Documentation/requirements.txt"
```

**4️⃣ Run the web app**

The Flask app lives inside `7.Project Documentation/Flask/`:

```bash
cd "7.Project Documentation/Flask"
python app.py
```

Then open **`http://127.0.0.1:5000`** in your browser, enter soil/climate values, and get
your crop recommendation. 🌾

**5️⃣ (Optional) Explore the notebooks**

```bash
jupyter notebook notebook/OptiCrop_Model.ipynb
```

This walks through data cleaning, EDA, outlier handling, seasonal grouping, model
training/evaluation, K-Means clustering, and the project conclusion. The split
`data_preprocessing/preprocessing.ipynb` and `visualization_analisys/visualization.ipynb`
under `7.Project Documentation/` cover the corresponding sections individually.

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat-square)

</div>

---

## 🔮 Future Improvements

- 🌲 Compare Logistic Regression against ensemble models (Random Forest, XGBoost)
- 🗺️ Incorporate soil type or geographic region as additional features
- 🌐 Deploy the model behind a REST API for integration with other tools

---

<div align="center">

Made with 🌾 for smarter, data-driven farming.

</div>
