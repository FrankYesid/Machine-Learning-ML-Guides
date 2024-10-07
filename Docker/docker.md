# Churn Prediction Project

This project implements a churn prediction system using machine learning techniques. Docker is used to automate and standardize the execution environment. Streamlit and FastAPI are integrated for visualization and prediction API.

## Steps and Considerations

### 1. Install Dependencies

**Instruction:**
```bash
pip install -r requirements.txt
```
**Details:**
- Before running any script, you need to install the dependencies listed in `requirements.txt`. This includes necessary libraries like `pandas`, `catboost`, `scikit-learn`, among others.

### 2. Build the Model in `train_model.py`

- This script contains the preprocessing logic and model development.
- **Key Point:** The model should be saved in a file for future predictions.

### 3. Create the `predict.py` Script

This file contains the same preprocessing flow as `train_model.py`, but with an additional section for making predictions.

- **Prediction Instruction:**
```bash
python src/predict.py
```
- **Model File:** Ensure that the trained model is in the correct path. Example: `model/cat_model.cbm`.

### 4. Configure the `Dockerfile`

The `Dockerfile` is a configuration file that creates a standardized container environment where your application will run. Here are the steps to create it:

1. **Select a base image:**
    ```Dockerfile
    FROM python:3.9-slim
    ```
    This provides the minimal Python 3.9 environment for execution.

2. **Install dependencies:**
    ```Dockerfile
    COPY requirements.txt requirements.txt
    RUN pip install --no-cache-dir -r requirements.txt
    ```
    Copies the `requirements.txt` file to the container and installs the dependencies.

3. **Specify the working directory and copy the code:**
    ```Dockerfile
    WORKDIR /app
    COPY . .
    ```

4. **Run the prediction script:**
    ```Dockerfile
    CMD ["python", "src/predict.py"]
    ```

### 5. Build the Docker Container

**Instruction:**
```bash
docker build -t churn-prediction-app .
```

- **Key Point:** This command builds the Docker container based on the `Dockerfile`. Ensure that all necessary files, including scripts and the model, are present.

### 6. Run the Docker Container

**Instruction:**
```bash
docker run -it churn-prediction-app
```
This command runs the container and launches the prediction application. Enter the customer information as prompted to predict their likelihood of churn.

### 7. Visualization with Streamlit and FastAPI

You can integrate the prediction with Streamlit and FastAPI to provide a user-friendly graphical interface and an API.

- **Streamlit:** Displays the churn probability in a web application.
- **FastAPI:** Allows other users to interact with the model via an API.

### 8. Docker Build and Run Commands

- **Build the Docker image:**
    ```bash
    docker build -t churn-prediction-app .
    ```

- **Run the Docker image:**
    ```bash
    docker run -it churn-prediction-app
    ```

### 9. Future Tasks

- Optimize the model's accuracy by adjusting hyperparameters.
- Develop a complete user interface for real-time prediction.

---