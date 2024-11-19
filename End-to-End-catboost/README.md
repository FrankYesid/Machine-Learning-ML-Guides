# Proyecto de End-to-End en Python

## Descripción

Este proyecto es una solución de extremo a extremo (End-to-End) en Python. El proyecto abarca desde la recopilación y limpieza de datos, hasta el análisis, modelado y despliegue de un modelo de Machine Learning.

## Características

- **Recopilación de datos**: Scripts para la extracción y recopilación de datos desde diversas fuentes.
- **Preprocesamiento**: Limpieza y transformación de los datos.
- **Análisis exploratorio**: Herramientas y notebooks para la exploración y visualización de datos.
- **Modelado**: Implementación de varios algoritmos de Machine Learning.
- **Evaluación**: Evaluación y validación de los modelos.
- **Despliegue**: Despliegue del modelo en un entorno de producción.

## Requisitos 

Python 3.11.+
pip (Python package manager)
Git (Version control tool)

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/FrankYesid/Machine Learning (ML) Guides/End-to-End.git
    cd Machine Learning (ML) Guides/End-to-End
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `.\.venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso 
Para ejecutar el proyecto, sigue los siguientes pasos:

1. **Recopilación de datos**:
    ```bash
    python scripts/recopilacion_datos.py # esto se encuentra analizado en el cuaderno en src/notebooks/END-To-END Machine Learning
    ```

2. **Preprocesamiento**:
    ```bash
    python scripts/preprocesamiento.py # esto se encuentra analizado en el cuaderno en src/notebooks/END-To-END Machine Learning
    ```

3. **Análisis exploratorio**:
    Abre y ejecuta los notebooks en la carpeta `src/notebooks`:
    ```bash
    jupyter notebook notebooks/END-To-END Machine Learning.ipynb
    ```

4. **Modelado**:
    ```bash
    python src/train_model.py
    ```

5. **Evaluación**:
    ```bash
    python src/predict.py
    ```

6. **Despliegue**:
    Sigue las instrucciones en `README.md` para desplegar el modelo.

## Contribución

¡Las contribuciones son bienvenidas! Por favor sigue los siguientes pasos para contribuir:

1. Haz un fork de este repositorio.
2. Crea una nueva rama:
    ```bash
    git checkout -b feature/nueva-funcionalidad
    ```
3. Realiza tus cambios y haz commits:
    ```bash
    git commit -m "Añadir nueva funcionalidad"
    ```
4. Envía tus cambios al repositorio remoto:
    ```bash
    git push origin feature/nueva-funcionalidad
    ```
5. Abre una Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.


# Actualización del Proyecto: Predicción de Churn

## Descripción del Proyecto:

Este proyecto es una implementación completa de un sistema de predicción de churn (abandono de clientes) utilizando técnicas de aprendizaje automático. El objetivo es predecir si un cliente dejará de usar un servicio basándose en datos históricos y características del cliente.

## Cambios en esta Actualización:

- **Análisis Exploratorio de Datos (EDA)**: Se añadieron scripts para la limpieza de datos y visualización.
- **Ingeniería de Características**: Se implementaron nuevas técnicas para la creación de características a partir de datos brutos.
- **Modelado**: Se integraron múltiples modelos de machine learning, incluyendo Random Forest, Gradient Boosting y XGBoost.
- **Evaluación de Modelos**: Se añadieron métricas de evaluación detalladas para comparar el rendimiento de los modelos.
- **Despliegue**: Se proporcionaron scripts y configuraciones para desplegar el modelo en un entorno de producción.

## Instrucciones:

### Instalar Dependencias:

```bash
pip install -r requirements.txt
```

### Ejecutar el Script de Entrenamiento:

```bash
python train_model.py
```

### Evaluar el Modelo:

```bash
python predict.py
```

## Próximos Pasos:

- Mejorar la precisión del modelo a través del ajuste de hiperparámetros.
- Implementar técnicas avanzadas de ingeniería de características.
- Desarrollar una interfaz de usuario para facilitar la predicción de churn en tiempo real.

Para el proceso tener presente lo siguiente: [**Instructivo**](instructivo.md)

Este resumen proporciona una visión general de las mejoras y actualizaciones realizadas al proyecto, así como instrucciones claras para que otros desarrolladores repliquen el trabajo y contribuyan.

