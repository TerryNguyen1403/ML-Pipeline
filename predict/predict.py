# Import pandas for data manipulation
import pandas as pd

# Import joblib for loading models
import joblib

#Load model and standard scaler
classification_model = joblib.load('predict/best_model.pkl')
scaler = joblib.load('predict/standard_scaler.pkl')

#Load dataset
df = pd.read_csv('data/sample_data_for_prediction.csv')
df = df.drop('date', axis=1)

X_pred = df.iloc[:,:].values
X_pred = scaler.transform(X_pred)

y_pred = classification_model.predict(X_pred)

print(y_pred.reshape(-1,1))
