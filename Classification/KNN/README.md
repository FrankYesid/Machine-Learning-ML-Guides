# KNN Classification Project

This project implements a K-Nearest Neighbors (KNN) classification model using a dataset, with a focus on evaluating its performance in terms of accuracy and other metrics. The project is organized into several key components, including data loading, model training, evaluation, and result visualization.

## Folder Structure

- **`data/`**: Contains the dataset used for training and testing the KNN model. Data should be in `.csv` format, with separate files for training and testing (e.g., `train.csv` and `test.csv`).

- **`docs/`**: Documentation for the project, including instructions, explanations of the methodology, and references for further reading on KNN.

- **`results/`**: This folder stores the outputs generated during the project, including evaluation metrics, confusion matrix plots, classification reports, and test set predictions.

## Key Files

### 1. **`utils.py`**x

This file contains utility functions to assist in various stages of the project, such as data loading, normalization, and visualization. Below is an overview of the key functions:

- **`load_data(train_path, test_path)`**: Loads the training and test datasets from CSV files, returning the features and labels for the train set, and features for the test set.
  
- **`normalize_data(data)`**: Normalizes the feature data by scaling values to a range of [0, 1], which is essential for KNN performance.

- **`plot_confusion_matrix(conf_matrix)`**: Visualizes the confusion matrix using a heatmap to represent classification results.

- **`plot_sample(X, y, index)`**: Plots a sample image from the dataset, useful for data exploration.

### 2. **`knn_classification.ipynb`**

This Jupyter notebook walks through the process of building, training, and evaluating the KNN model. The steps are organized as follows:

1. **Data Loading**:
   - Load the training and test datasets using the `load_data` function from `utils.py`.
   - Print dataset shapes to verify successful loading.

2. **Data Preprocessing**:
   - Normalize the pixel values of the images to ensure consistent scale for KNN, using `normalize_data`.

3. **Model Training**:
   - Split the training dataset into training and validation sets.
   - Train a KNN model with different values of `k` (number of neighbors) and select the optimal `k` based on validation accuracy.

4. **Model Evaluation**:
   - Evaluate the KNN model's accuracy on the validation set.
   - Generate and save a confusion matrix plot, classification report, and overall accuracy to the `results/` folder.

5. **Test Set Prediction**:
   - Use the trained model to make predictions on the test set.
   - Save the test predictions to a CSV file for further evaluation.

6. **Result Visualization**:
   - Plot key metrics such as the confusion matrix and save visualizations to the `results/` folder.

## Results and Outputs

The `results/` folder contains the following outputs:

- **`confusion_matrix.png`**: A heatmap plot of the confusion matrix showing the performance of the KNN model on the validation set.
  
- **`classification_report.txt`**: A text file containing the precision, recall, F1-score, and support for each class (digit).
  
- **`test_predictions.csv`**: A CSV file containing the predicted labels for the test set.
  
- **`validation_accuracy.txt`**: A text file containing the overall accuracy of the model on the validation set, along with the optimal value of `k`.

## How to Run the Project
1. Place the dataset files (`train.csv` and `test.csv`) in the `data/` folder.
2. Open and run the steps in the `knn_classification.ipynb` notebook.
3. The results will be automatically saved in the `results/` folder after running the notebook.

## Conclusion

This project demonstrates how to implement and evaluate a K-Nearest Neighbors classification model. The results help in understanding the strengths and limitations of KNN, particularly when applied to image-based datasets like MNIST. For further improvements, one could explore different distance metrics, scaling techniques, or alternative models.