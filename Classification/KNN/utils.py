import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(train_path, test_path):
    """
    Load the MNIST dataset from CSV files.

    Parameters:
    - train_path (str): Path to the training data CSV file.
    - test_path (str): Path to the test data CSV file.

    Returns:
    - X_train (numpy.ndarray): Training images data.
    - y_train (numpy.ndarray): Training labels.
    - X_test (numpy.ndarray): Test images data.
    """
    # Load training data
    train_df = pd.read_csv(train_path)
    X_train = train_df.iloc[:, 1:].values  # Pixel values
    y_train = train_df.iloc[:, 0].values   # Labels

    # Load test data
    test_df = pd.read_csv(test_path)
    X_test = test_df.values  # Pixel values

    return X_train, y_train, X_test

def normalize_data(X):
    """
    Normalize pixel values to the range [0, 1].

    Parameters:
    - X (numpy.ndarray): The data to normalize.

    Returns:
    - X_normalized (numpy.ndarray): Normalized data.
    """
    return X / 255.0

def plot_sample(X, y, index):
    """
    Plot a single image from the dataset.

    Parameters:
    - X (numpy.ndarray): The image data.
    - y (numpy.ndarray): The labels corresponding to the image data.
    - index (int): The index of the image to plot.

    Returns:
    - None: Displays the image with its label.
    """
    plt.imshow(X[index].reshape(28, 28), cmap='gray')
    plt.title(f'Label: {y[index]}')
    plt.axis('off')
    plt.show()

def plot_multiple_samples(X, y, indices):
    """
    Plot multiple images from the dataset.

    Parameters:
    - X (numpy.ndarray): The image data.
    - y (numpy.ndarray): The labels corresponding to the image data.
    - indices (list of int): A list of indices of the images to plot.

    Returns:
    - None: Displays the images with their labels.
    """
    plt.figure(figsize=(10, 5))
    for i, index in enumerate(indices):
        plt.subplot(1, len(indices), i + 1)
        plt.imshow(X[index].reshape(28, 28), cmap='gray')
        plt.title(f'Label: {y[index]}')
        plt.axis('off')
    plt.show()

def reshape_data(X):
    """
    Reshape the data to its original 28x28 image format for use in convolutional neural networks.

    Parameters:
    - X (numpy.ndarray): The data to reshape.

    Returns:
    - X_reshaped (numpy.ndarray): Reshaped data with dimensions suitable for CNNs.
    """
    return X.reshape(-1, 28, 28, 1)
