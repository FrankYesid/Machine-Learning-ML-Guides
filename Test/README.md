# Test Folder

This folder contains scripts and resources related to testing the performance of machine learning models. The testing process involves evaluating the trained models on a test dataset and generating various performance metrics, including accuracy, precision, recall, confusion matrices, and other evaluation reports.

## 1. Purpose of the Test Folder

The main goal of this folder is to ensure that the trained models are thoroughly tested on unseen data (test set) to evaluate their generalization ability. The following steps outline how the testing process is conducted:

- Load the trained model and the test dataset.
- Generate predictions on the test dataset.
- Calculate performance metrics, such as accuracy, precision, recall, and F1-score.
- Visualize results with confusion matrices and save them for further analysis.

## 2. Directory Structure

- `test_model.py`: Script to load a trained model, run predictions on the test set, and generate evaluation metrics.
- `test_results/`: A folder where the results of the tests (such as confusion matrices, classification reports, and test predictions) are stored.

## 3. How to Test a Model

### Step 1: Load the Test Dataset

You need to have a test dataset available in CSV format (e.g., `mnist_test.csv`), which should be located in the `data/` folder. The test dataset will be used to evaluate the model.

### Step 2: Run the Test Script

Run the `test_model.py` script to load the trained model, process the test data, and generate predictions. The script will calculate and output the following metrics:

- **Confusion Matrix**: Visualizes the true vs predicted labels.
- **Classification Report**: Displays precision, recall, and F1-score for each class.
- **Test Predictions**: Saves the predicted values and corresponding true values for the test set into a CSV file.

Example usage:

```bash
python test_model.py --model_path models/svm_model.pkl --test_data data/mnist_test.csv
```

### Step 3: Generate and Save Results

Once the script is run, the results will be saved in the `test_results/` folder, which includes:

- `confusion_matrix.png`: A heatmap visualization of the confusion matrix.
- `classification_report.txt`: A text file containing precision, recall, and F1-score for each class.
- `test_predictions.csv`: A CSV file containing the true labels and predicted labels for each sample in the test set.

### Example Test Script: `test_model.py`

```python
import utils
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
import pickle
import pandas as pd
import argparse

# Argument parser for model and test data paths
parser = argparse.ArgumentParser(description='Test a trained model on a test dataset')
parser.add_argument('--model_path', type=str, required=True, help='Path to the trained model (e.g., svm_model.pkl)')
parser.add_argument('--test_data', type=str, required=True, help='Path to the test dataset (e.g., mnist_test.csv)')
args = parser.parse_args()

# Load the trained model
with open(args.model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Load test data
X_test, y_test = utils.load_test_data(args.test_data)

# Make predictions
y_pred = model.predict(X_test)

# Generate classification report and confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Save classification report
with open('test_results/classification_report.txt', 'w') as f:
    f.write(class_report)

# Save confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.savefig('test_results/confusion_matrix.png')
plt.show()

# Save test predictions
predictions_df = pd.DataFrame({'True Label': y_test, 'Predicted Label': y_pred})
predictions_df.to_csv('test_results/test_predictions.csv', index=False)
```

## 4. Notes on Testing

- **Model Path**: Ensure that the path to the trained model (e.g., SVM or KNN) is correctly provided when running the test script.
- **Test Data**: Make sure the test data file is properly formatted and stored in the `data/` fol der.
- **Performance Metrics**: The classification report and confusion matrix provide insights into how well the model is performing on the test data.

## 5. Example Results

Once the test is completed, you should expect to find the following files in the `test_results/` folder:

- `classification_report.txt`: Example output from the SVM model could look like:

  ```
               precision    recall  f1-score   support

           0       0.98      0.97      0.97      1000
           1       0.97      0.98      0.97      1000
           ...
  
      accuracy                           0.98     10000
     macro avg       0.98      0.98      0.98     10000
  weighted avg       0.98      0.98      0.98     10000
  ```

- `confusion_matrix.png`: This file will contain a visual confusion matrix with the true and predicted labels.

---

This `README.md` explains how to set up and run the test process for machine learning models, detailing how the model's performance is measured and how the results are saved. Make sure to follow these steps for evaluating any model you are working with.