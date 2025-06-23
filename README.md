# Weather Forecast Project
This project is a machine learning pipeline for weather forecasting. It includes data extraction, transformation, model training, and prediction modules. The pipeline is designed to process raw weather data, train predictive models, and generate weather forecasts based on new input data.

## Project Structure
- extract/: Scripts for extracting and preparing training and prediction data.
- transform/: Notebooks and scripts for data transformation.
- training/: Scripts for training machine learning models.
- predict/: Scripts and models for making weather predictions.
- data/: Contains raw and processed weather data.

## How to run
1. Clone the repository
    git clone https://github.com/TerryNguyen1403/ML-Pipeline.git
    cd ML-Pipleline
2. Install dependencies
    pip install -r requirements.txt
3. Run extraction scripts in the extract/ directory to get a dataset from Open-meteo by calling its API.
4. Transform data
    Use the notebook script in transform/ directory to preprocess the data.
5. Train the model
    Rung the Training.py script in traning/ directory to feed the transformed dataset into GaussianNB, Random Forest Classifier, Support Vector Classifier (SVC) for training, evaluating and selecting a best model for predict new observations. The best model will be saved as a file name 'best_model.pkl' in predict/ directory.
6. Make predictions
    Run the script in predict/ directory to predict new observations.
