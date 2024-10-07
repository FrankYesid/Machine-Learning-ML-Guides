import uvicorn
import pandas as pd
from fastapi import FastAPI
from catboost import CatBoostClassifier
from pydantic import BaseModel, constr 

# Path to the model
MODEL_PATH = "src/model/catboost_model.cbm" 

# Function to load the trained model
def load_model():  
    model = CatBoostClassifier()  
    model.load_model(MODEL_PATH)  
    print("Modelo cargado correctamente!") # ¡Nuevo mensaje para confirmar la carga!  
    return model

# Function to predict churn probability from data in DataFrame format
def get_churn_probability(data, model):
    # Convert incoming data into a DataFrame
    print(data)
    dataframe = pd.DataFrame.from_dict(data)
    # dataframe = pd.DataFrame([data.to_dict()])
    
    # Ensure numeric columns are converted to integers or floats
    # Asegurar que las columnas numéricas sean convertidas a enteros si es posible
    for col in dataframe.columns:
        if pd.api.types.is_numeric_dtype(dataframe[col]):
            # Convertir a numérico, convirtiendo NaNs a un valor específico (por ejemplo, 0) si es necesario
            dataframe[col] = pd.to_numeric(dataframe[col], errors='coerce').fillna(0).astype(int)

    print(dataframe)
    # Make the prediction
    churn_probability = model.predict_proba(dataframe)[0][1]
    return churn_probability

# Load the model
model = load_model()
print(model)
# Create the FastAPI application
app = FastAPI(title="Churn Prediction API", version="1.0")

@app.get('/')
def index():
    return {'message': 'CHURN Prediction API'}

# Define the API endpoint
@app.post('/predict/')
def predict_churn(data: dict):
    # Get the prediction
    churn_probability = get_churn_probability(data, model)
    # Return the prediction
    return {'Churn Probability': churn_probability}

# Run the application
if __name__ == '__main__':
    uvicorn.run("fast-api:app", host='127.0.0.1', port=8000)
