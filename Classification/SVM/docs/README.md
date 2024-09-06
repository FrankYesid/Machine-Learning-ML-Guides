# Support Vector Machine (SVM) Classification Project

This README file provides an overview of the Support Vector Machine (SVM) algorithm, instructions on how the model is implemented, and details of the directory structure, including data, documentation, and results.

## 1. Overview of Support Vector Machines (SVM)

### What is SVM?

Support Vector Machines (SVM) are a powerful and widely used supervised learning algorithm primarily applied to classification tasks. SVMs aim to find the optimal hyperplane that best separates the data points of different classes in the feature space.

### Key Concepts:

- **Hyperplane**: In an SVM model, the goal is to find the hyperplane that best divides the dataset into classes. The hyperplane is a decision boundary that separates data points based on their class labels.
  
- **Support Vectors**: The data points closest to the hyperplane are called support vectors. These points are critical in defining the hyperplane's position and orientation.
  
- **Maximizing Margin**: SVM works by maximizing the margin, which is the distance between the hyperplane and the closest support vectors. This helps the model generalize better to unseen data.

- **Kernel Trick**: SVM can be extended to handle non-linearly separable data by using kernel functions, such as the polynomial kernel or radial basis function (RBF) kernel, to map the data into higher-dimensional spaces where a linear hyperplane can be applied.

### Advantages of SVM:

- **Effective in High-Dimensional Spaces**: SVM is particularly powerful when working with high-dimensional data, as the margin optimization helps handle complex feature spaces.
  
- **Robust to Overfitting**: By maximizing the margin between classes, SVM avoids overfitting, especially in smaller datasets.

- **Kernel Flexibility**: The kernel trick allows SVM to handle both linear and non-linear relationships in data.

### Disadvantages of SVM:

- **Computationally Expensive**: SVM can be slow and memory-intensive, especially with large datasets.
  
- **Choosing the Right Kernel**: The choice of kernel and parameters can significantly impact performance, requiring careful tuning.

## 2. Directory Structure

### `data/`
This folder contains the dataset files used for training and testing the SVM model. In this project, we use a subset of the MNIST dataset (handwritten digits). The dataset is stored in CSV format.

- `mnist_train_small.csv`: Contains the training data, including pixel values and labels.
- `mnist_test.csv`: Contains the test data for evaluating the trained model.

### `docs/`
The `docs/` folder contains detailed documentation on the SVM algorithm, references for further study, and a bibliography of related research.

- **docs/svm_overview.md**: Explains the theoretical foundation of SVM.
- **docs/svm_references.md**: Provides useful links, tutorials, and external resources on SVM.

### `results/`
The `results/` folder stores output files from running the SVM model, including accuracy reports, confusion matrices, and classification results.

- `confusion_matrix.png`: A visual representation of the classification performance.
- `classification_report.txt`: Detailed metrics such as precision, recall, F1-score for each class.
- `test_predictions.csv`: CSV file containing predictions on the test set.

## 3. Steps to Run the SVM Model

### 1. Data Preprocessing:
Before training the SVM model, the data needs to be loaded and normalized. We will use the `utils.py` module to handle the preprocessing.

### 2. Model Training:
We use the `SVC` class from `scikit-learn` to train the SVM model. The kernel type and parameters (C, gamma) are configurable based on the dataset's characteristics.

```python
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import utils

# Load and preprocess data
train_path = 'data/mnist_train_small.csv'
test_path = 'data/mnist_test.csv'
X_train, y_train, X_test = utils.load_data(train_path, test_path)

# Initialize and train the SVM model
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')
svm_model.fit(X_train, y_train)

# Predict on the test data
y_test_pred = svm_model.predict(X_test)
```

### 3. Model Evaluation:
Evaluate the model by generating a confusion matrix and classification report. Save the evaluation metrics for analysis.

```python
# Evaluate the model
conf_matrix = confusion_matrix(y_test, y_test_pred)
class_report = classification_report(y_test, y_test_pred)

# Save results
utils.save_confusion_matrix(conf_matrix, 'results/confusion_matrix.png')
utils.save_classification_report(class_report, 'results/classification_report.txt')
```

### 4. Hyperparameter Tuning:
You can experiment with different kernel types (linear, polynomial, RBF) and adjust parameters such as `C` (regularization) and `gamma` to improve performance.

```python
# Experiment with different kernel types and parameters
svm_poly = SVC(kernel='poly', degree=3, C=1.0)
svm_rbf = SVC(kernel='rbf', C=1.0, gamma=0.001)
```

## 4. Further Reading and Resources

### Articles and Tutorials:
- [SVM Algorithm - Towards Data Science](https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47)
- [Understanding SVM in Python - Real Python](https://realpython.com/python-machine-learning-svm/)

### Courses:
- **Coursera: Machine Learning by Andrew Ng**: This popular course includes sections on SVM, including linear and non-linear classification using kernel methods.
- **Udacity: Intro to Machine Learning with TensorFlow**: A course that covers the SVM algorithm as part of its supervised learning section.

### Research Papers and Bibliography:
- **Cortes, C., & Vapnik, V. (1995)**. Support-Vector Networks. *Machine Learning*, 20(3), 273-297. This seminal paper introduced the SVM algorithm and laid the foundation for its development.
- **Boser, B. E., Guyon, I. M., & Vapnik, V. N. (1992)**. A Training Algorithm for Optimal Margin Classifiers. In *Proceedings of the Fifth Annual Workshop on Computational Learning Theory* (pp. 144-152). An important work that discusses the theory behind SVM and optimal margin classifiers.

---

This `README.md` provides a detailed overview of the SVM classification project, guiding you through the directory structure, code implementation, and useful resources for understanding and applying the Support Vector Machine algorithm.