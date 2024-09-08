# Autoencoders for Dimensionality Reduction and Data Reconstruction

This folder contains resources, scripts, and documentation for training and evaluating Autoencoders, a type of neural network used for unsupervised learning tasks like dimensionality reduction and data reconstruction. The project applies Autoencoders to the MNIST dataset and demonstrates how to train the model, test it, and analyze the results.

## 1. Project Structure

The project is organized as follows:

```
Autoencoders/
├── data/
│   └── mnist_train.csv
│   └── mnist_test.csv
├── docs/
│   └── autoencoders_overview.md
│   └── bibliography.md
├── results/
│   └── reconstructed_images.png
│   └── loss_plot.png
│   └── encoded_data.csv
├── utils.py
├── autoencoder_model.py
├── autoencoder_training.ipynb
├── LICENSE
└── README.md
```

### Explanation of Directories:

- **data/**: Contains the training and test datasets in CSV format, used for training and evaluating the Autoencoder.
- **docs/**: Includes documentation that explains the theory behind Autoencoders and references for further reading.
- **results/**: Stores the outputs from training and testing the Autoencoder, such as the loss plot, reconstructed images, and encoded data.
- **utils.py**: Contains utility functions for loading data, saving results, and handling data preprocessing tasks.
- **autoencoder_model.py**: Python script containing the architecture of the Autoencoder neural network.
- **autoencoder_training.ipynb**: A Jupyter Notebook that demonstrates how to train the Autoencoder, visualize the training process, and evaluate the model's performance.

## 2. Dataset

The MNIST dataset is used for training and testing the Autoencoder. It is divided into:

- **mnist_train.csv**: The training set of handwritten digits.
- **mnist_test.csv**: The test set of handwritten digits.

Each CSV file contains:

- **Features**: Pixel values of 28x28 grayscale images, flattened into a vector of size 784.
- **Labels**: Although labels are not directly used in Autoencoders (since it's unsupervised), the test dataset includes labels for evaluation.

## 3. Key Functions (utils.py)

The `utils.py` file contains functions used throughout the project:

- **`load_data(train_path, test_path)`**: Loads the training and test data from CSV files.
- **`save_reconstructed_images(images, filename)`**: Saves a grid of original vs. reconstructed images to a PNG file.
- **`plot_loss(loss_history, filename)`**: Plots and saves the training loss over epochs.
- **`save_encoded_data(encoded_data, filename)`**: Saves the encoded (compressed) representations of the input data to a CSV file.

## 4. Autoencoder Model (autoencoder_model.py)

The Autoencoder model is implemented in `autoencoder_model.py`, which defines the encoder and decoder parts of the network.

- **Encoder**: Reduces the dimensionality of the input data by compressing it into a latent space representation.
- **Decoder**: Reconstructs the original data from the latent space representation.

The model is trained using the mean squared error (MSE) loss function, which measures the reconstruction error, and the Adam optimizer for training.

## 5. Training Workflow (autoencoder_training.ipynb)

The `autoencoder_training.ipynb` notebook contains the workflow for training the Autoencoder and evaluating its performance on the MNIST dataset.

### Steps in the Notebook:

1. **Load Data**: The notebook loads the training and test datasets using the `utils.load_data()` function.
  
2. **Build the Autoencoder**:
   - The Autoencoder is built with an encoder to compress the input and a decoder to reconstruct it.
   - The model is compiled with the Adam optimizer and mean squared error loss.

3. **Train the Model**:
   - The model is trained on the MNIST dataset over a defined number of epochs.
   - The training process outputs a loss plot that shows how well the model learns to reconstruct the input data over time.

4. **Evaluate the Model**:
   - After training, the model is tested on the test dataset to evaluate its reconstruction capability.
   - The reconstructed images are compared to the original images, and both are visualized.

5. **Save Results**:
   - The training loss is saved as a plot (`loss_plot.png`).
   - The reconstructed images are saved as a grid image (`reconstructed_images.png`).
   - The encoded (compressed) representations are saved as a CSV file (`encoded_data.csv`).

### Example Code Snippet:

```python
from autoencoder_model import Autoencoder
import utils

# Load training and test data
X_train, X_test = utils.load_data('data/mnist_train.csv', 'data/mnist_test.csv')

# Build and compile the Autoencoder model
autoencoder = Autoencoder(input_dim=784, encoding_dim=32)
autoencoder.compile(optimizer='adam', loss='mse')

# Train the Autoencoder
history = autoencoder.fit(X_train, X_train, epochs=50, batch_size=256, validation_data=(X_test, X_test))

# Plot and save the training loss
utils.plot_loss(history.history['loss'], history.history['val_loss'], 'results/loss_plot.png')

# Generate and save reconstructed images
reconstructed_images = autoencoder.predict(X_test)
utils.save_reconstructed_images(X_test, reconstructed_images, 'results/reconstructed_images.png')

# Save encoded representations
encoded_data = autoencoder.encoder.predict(X_test)
utils.save_encoded_data(encoded_data, 'results/encoded_data.csv')
```

## 6. Results

Once the Autoencoder has been trained and evaluated, the results are stored in the `results/` folder:

- **`loss_plot.png`**: A plot showing the training and validation loss over the epochs.
- **`reconstructed_images.png`**: A comparison between the original and reconstructed images from the test dataset.
- **`encoded_data.csv`**: A CSV file containing the encoded (compressed) representations of the test dataset in the latent space.

## 7. Documentation

Further documentation on Autoencoders and their applications can be found in the `docs/` folder:

- **`autoencoders_overview.md`**: Provides a detailed explanation of Autoencoders, their architecture, and how they can be used for tasks like dimensionality reduction and data compression.
- **`bibliography.md`**: Lists the sources and references used for studying Autoencoders, including research papers, online tutorials, and books.

## 8. License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

This `README.md` provides an overview of the Autoencoder project, explaining the folder structure, datasets, code, and workflow involved in training and testing an Autoencoder on the MNIST dataset. It is designed to be a flexible starting point for experimenting with Autoencoders on different datasets and use cases.