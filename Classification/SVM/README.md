# Support Vector Machine (SVM) Classification

This folder contains resources, scripts, and documentation for performing classification using Support Vector Machines (SVM) on the MNIST dataset. The SVM algorithm is a powerful tool for classification tasks, and this project demonstrates how to apply it, evaluate its performance, and save the results for further analysis.

## 1. Project Structure

The project is organized into the following key folders and files:

```
SVM/
├── data/
│   └── mnist_train_small.csv
│   └── mnist_test.csv
├── docs/
│   └── SVM_overview.md
│   └── bibliography.md
├── results/
│   └── confusion_matrix.png
│   └── classification_report.txt
│   └── test_predictions.csv
│   └── validation_accuracy.txt
├── utils.py
├── SVM_classification.ipynb
├── LICENSE
└── README.md
```

### Explanation of Directories:

- **data/**: Contains the training and test datasets in CSV format. The dataset used is a subset of MNIST for digit classification.
- **docs/**: Contains documentation and references, including a detailed explanation of the SVM algorithm and links to additional resources and literature.
- **results/**: Stores output files generated from the SVM model, such as the confusion matrix, classification report, test predictions, and validation accuracy.
- **utils.py**: Contains utility functions for loading the dataset, saving results, and handling data preprocessing tasks.
- **SVM_classification.ipynb**: A Jupyter Notebook that implements the SVM classification, loads data, trains the model, and generates performance metrics.

## 2. Dataset

The MNIST dataset used in this project is stored in the `data/` folder and consists of:

- `mnist_train_small.csv`: A small subset of the MNIST training set (60,000 images).
- `mnist_test.csv`: The test set (10,000 images).

Each CSV file contains:

- **Features**: Pixel values of 28x28 grayscale images (flattened into a vector of size 784).
- **Labels**: The corresponding digit (0-9) for each image.

## 3. Key Functions (utils.py)

The `utils.py` file contains functions used throughout the project:

- **`load_data(train_path, test_path)`**: Loads the training and test data from CSV files.
- **`save_classification_report(report, filename)`**: Saves the classification report (precision, recall, F1-score) to a text file.
- **`save_confusion_matrix(conf_matrix, filename)`**: Saves the confusion matrix as a heatmap image.
- **`save_predictions(predictions, filename)`**: Saves the predicted and true labels to a CSV file.
  
## 4. SVM Classification Workflow

The `SVM_classification.ipynb` notebook contains the complete workflow for training and testing the SVM model:

### Steps in the Notebook:

1. **Load Data**: The notebook loads the training and test datasets from the `data/` folder using the `utils.load_data()` function.
  
2. **Train the SVM Model**:
   - The notebook initializes an SVM classifier using the `rbf` kernel with the `SVC` class from `scikit-learn`.
   - The model is trained on the training dataset.

3. **Test the Model**:
   - After training, the model is tested on the test dataset.
   - Predictions are generated for the test images.

4. **Evaluation**:
   - A confusion matrix is generated to visualize how well the model performs on each digit class.
   - A classification report is created with metrics such as precision, recall, and F1-score.
   - The validation accuracy is calculated and displayed.

5. **Save Results**:
   - The confusion matrix is saved as `confusion_matrix.png`.
   - The classification report is saved as `classification_report.txt`.
   - The test predictions (true labels vs predicted labels) are saved as `test_predictions.csv`.
   - The validation accuracy is saved in `validation_accuracy.txt`.

### Example Code Snippet:

```python
# Train the SVM model
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')
svm_model.fit(X_train, y_train)

# Predict on the test set
y_pred = svm_model.predict(X_test)

# Generate confusion matrix and classification report
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Save results
utils.save_classification_report(class_report, 'results/classification_report.txt')
utils.save_confusion_matrix(conf_matrix, 'results/confusion_matrix.png')

# Save predictions
utils.save_predictions(y_test, y_pred, 'results/test_predictions.csv')
```

## 5. Results

Once the model has been tested, the results are stored in the `results/` folder. The key outputs include:

- **`confusion_matrix.png`**: A heatmap of the confusion matrix showing the performance of the SVM on each digit class.
- **`classification_report.txt`**: A detailed report of precision, recall, F1-score, and support for each class.
- **`test_predictions.csv`**: A CSV file containing the true labels and the predicted labels for each sample in the test set.
- **`validation_accuracy.txt`**: A text file with the overall accuracy of the model on the test set.

## 6. Documentation

Further details on the SVM algorithm and its theoretical background can be found in the `docs/` folder:

- **`SVM_overview.md`**: Provides a detailed explanation of the SVM algorithm, how it works, and its applications in machine learning.
- **`bibliography.md`**: Lists the sources and references used for studying SVMs, including books, research papers, and online tutorials.

## 7. License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

This `README.md` provides a comprehensive overview of the folder structure, datasets, code, and workflow involved in training and testing an SVM model on the MNIST dataset. The structure is designed to be modular and scalable, allowing you to easily experiment with different models and datasets.