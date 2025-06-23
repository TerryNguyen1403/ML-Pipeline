# Import libraries
import pandas as pd

# Import models
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# Import metrics
from sklearn.metrics import accuracy_score

# Import joblib for saving and loading models
import joblib

# Access dataframe
df = pd.read_csv('data/transformed_data.csv')

# Split into X and y
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Encoding categorical data
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# y = le.fit_transform(y)

#Split data into train set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define models
models = {
    'Naive Bayes': GaussianNB(),
    'Random Forest': RandomForestClassifier(n_estimators=10, criterion='gini', random_state=0),
    'Support Vector Classifier': SVC(random_state=0)
}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy

best_model_name = max(results, key=results.get)
best_model = models[best_model_name]

best_model.fit(X_train, y_train)

joblib.dump(best_model, 'predict/best_model.pkl')
joblib.dump(scaler, 'predict/standard_scaler.pkl')
