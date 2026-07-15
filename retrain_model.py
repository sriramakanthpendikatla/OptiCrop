import pandas as pd
import numpy as np
import pickle
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

root = Path(r'C:\Users\Asus\OptiCrop')
csv_path = root / '7.Project Documentation' / 'Dataset' / 'Crop_recommendation.csv'
out_dir = root / '7.Project Documentation' / 'Flask'

df = pd.read_csv(csv_path)

feature_cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
X = df[feature_cols].copy()
y = df['label']

X['K'] = np.log1p(X['K'])

le = LabelEncoder()
y_encoded = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=5000, random_state=42)
model.fit(X_train_scaled, y_train)

with open(out_dir / 'model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open(out_dir / 'scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
with open(out_dir / 'label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

print('retrained and saved')
print('train accuracy', model.score(X_train_scaled, y_train))
print('test accuracy', model.score(X_test_scaled, y_test))
