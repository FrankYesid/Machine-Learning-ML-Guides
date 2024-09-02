# Importar las bibliotecas necesarias
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd


# Pendiente agregar verificador de función
def load_data(file_path):
    """
    Carga un archivo de datos en formato CSV.
    
    :param file_path: Ruta al archivo CSV que contiene los datos.
    :return: DataFrame de pandas con los datos cargados.
    """
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data, target_column):
    """
    Preprocesa los datos dividiéndolos en características y la variable objetivo.
    
    :param data: DataFrame que contiene los datos.
    :param target_column: Columna del DataFrame que será la variable objetivo.
    :return: X (características) y y (variable objetivo).
    """
    X = data.drop(columns=[target_column])
    y = data[target_column]
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Divide los datos en conjuntos de entrenamiento y prueba.
    
    :param X: Características del dataset.
    :param y: Variable objetivo del dataset.
    :param test_size: Proporción del conjunto de prueba.
    :param random_state: Semilla para reproducibilidad.
    :return: X_train, X_test, y_train, y_test.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Entrena un modelo de clasificación usando RandomForest.
    
    X_train: Características del conjunto de entrenamiento.
    y_train: Variable objetivo del conjunto de entrenamiento.
    return: Modelo entrenado.
    """
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evalúa el modelo utilizando el conjunto de prueba.
    
    model: Modelo entrenado.
    X_test: Características del conjunto de prueba.
    y_test: Variable objetivo del conjunto de prueba.
    return: Precisión y reporte de clasificación.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report

def classify_new_data(model, new_data):
    """
    Clasifica nuevos datos utilizando el modelo entrenado.
    
    model: Modelo entrenado.
    new_data: Nuevos datos a clasificar.
    return: Predicciones para los nuevos datos.
    """
    predictions = model.predict(new_data)
    return predictions

# Ejemplo de uso:
if __name__ == "__main__":
    # Cargar y preprocesar los datos
    data = load_data("data.csv")
    X, y = preprocess_data(data, target_column="label")

    # Dividir los datos
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Entrenar el modelo
    model = train_model(X_train, y_train)

    # Evaluar el modelo
    accuracy, report = evaluate_model(model, X_test, y_test)
    print(f"Accuracy: {accuracy}")
    print(f"Classification Report:\n{report}")

    # Clasificar nuevos datos (suponiendo que 'new_data.csv' contiene datos nuevos sin la columna de etiqueta)
    new_data = pd.read_csv("new_data.csv")
    predictions = classify_new_data(model, new_data)
    print(f"Predictions: {predictions}")