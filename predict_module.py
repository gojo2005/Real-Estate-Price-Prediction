import pickle
import joblib
import pandas as pd
import os

# Folder path
folder_path = r"C:\Users\LENOVO\Desktop\HousePriceApp"

# Load model, scaler, and columns
with open(os.path.join(folder_path, "xgb_house_price_model.pkl"), "rb") as f:
    model = pickle.load(f)

scaler = joblib.load(os.path.join(folder_path, "scaler.pkl"))

with open(os.path.join(folder_path, "columns.pkl"), "rb") as f:
    columns = pickle.load(f)

def predict_price(input_data):
    """
    input_data: dict with keys like bedrooms, bathrooms, sqft_living, city, statezip, etc.
    """
    df = pd.DataFrame([input_data])
    
    # Feature Engineering
    df['house_age'] = 2025 - df['yr_built']
    df['renovated'] = df['yr_renovated'].apply(lambda x: 1 if x > 0 else 0)
    df['has_basement'] = df['sqft_basement'].apply(lambda x: 1 if x > 0 else 0)
    df["area_per_bedroom"] = df["sqft_living"] / df["bedrooms"]
    df["bathroom_to_bedroom_ratio"] = df["bathrooms"] / df["bedrooms"]

    df = df.drop(['yr_built', 'yr_renovated'], axis=1)
    
    # One-hot encode categorical variables
    df = pd.get_dummies(df, columns=['city', 'statezip'], drop_first=True)
    
    # Align columns with training data
    df = df.reindex(columns=columns, fill_value=0)
    
    # Scale numeric features
    num_cols = ['sqft_living','sqft_lot','sqft_above','sqft_basement','bedrooms','bathrooms','floors']
    df[num_cols] = scaler.transform(df[num_cols])
    
    # Predict
    return model.predict(df)[0]
