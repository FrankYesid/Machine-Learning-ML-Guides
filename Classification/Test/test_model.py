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
