# Unsupervised Learning Algorithms

Unsupervised Learning is a type of Machine Learning where the model is trained on unlabeled data. The goal is to find hidden patterns or intrinsic structures in the input data. Unsupervised learning is commonly used for clustering, dimensionality reduction, and anomaly detection tasks.

## Key Concepts
- **Unlabeled Data:** Data that does not have predefined labels or outputs.
- **Clusters:** Groups of similar data points identified by the algorithm.
- **Dimensionality Reduction:** The process of reducing the number of input variables in a dataset.

## Common Unsupervised Learning Algorithms

### 1. K-Means Clustering
K-Means is a popular clustering algorithm that partitions the data into K clusters. Each data point belongs to the cluster with the nearest mean.

- **Steps:**
  1. Initialize K centroids randomly.
  2. Assign each data point to the nearest centroid.
  3. Update the centroids based on the mean of the assigned points.
  4. Repeat steps 2 and 3 until convergence.

- **Use Cases:** Customer segmentation, image compression, etc.

### 2. Hierarchical Clustering
Hierarchical Clustering builds a hierarchy of clusters by either merging smaller clusters into larger ones (agglomerative) or splitting larger clusters into smaller ones (divisive).

- **Steps (Agglomerative):**
  1. Treat each data point as a single cluster.
  2. Merge the two closest clusters.
  3. Repeat step 2 until all points are merged into a single cluster.

- **Use Cases:** Gene expression data analysis, social network analysis, etc.

### 3. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
DBSCAN is a clustering algorithm that groups together points that are closely packed, marking points in low-density regions as outliers.

- **Key Parameters:**
  - **eps:** The maximum distance between two points to be considered neighbors.
  - **minPts:** The minimum number of points to form a dense region.

- **Use Cases:** Geographic data analysis, image segmentation, etc.

### 4. Principal Component Analysis (PCA)
PCA is a dimensionality reduction technique that transforms the data into a new coordinate system where the greatest variance lies on the first principal component, the second greatest variance on the second component, and so on.

- **Steps:**
  1. Standardize the data.
  2. Compute the covariance matrix.
  3. Calculate the eigenvalues and eigenvectors of the covariance matrix.
  4. Project the data onto the eigenvectors.

- **Use Cases:** Data visualization, noise reduction, feature extraction, etc.

### 5. Independent Component Analysis (ICA)
ICA is a computational technique for separating a multivariate signal into additive, independent non-Gaussian components.

- **Use Cases:** Signal processing, image separation, etc.

### 6. t-Distributed Stochastic Neighbor Embedding (t-SNE)
t-SNE is a dimensionality reduction technique particularly well-suited for visualizing high-dimensional data.

- **Steps:**
  1. Compute pairwise similarities of the input data points.
  2. Define a probability distribution over pairs of high-dimensional objects.
  3. Define a similar distribution for the points in the low-dimensional map.
  4. Minimize the Kullback-Leibler divergence between the two distributions.

- **Use Cases:** Data visualization, clustering validation, etc.

## Evaluation Metrics
- **Silhouette Score:** Measures how similar a data point is to its own cluster compared to other clusters.
- **Davies-Bouldin Index:** Measures the average similarity ratio of each cluster with the one that is most similar to it.
- **Calinski-Harabasz Index:** The ratio of the sum of between-clusters dispersion and of within-cluster dispersion.

## Applications of Unsupervised Learning
Unsupervised Learning algorithms are used in various applications, including:
- **Market Basket Analysis:** Identifying associations between products.
- **Anomaly Detection:** Detecting unusual patterns that do not conform to expected behavior.
- **Customer Segmentation:** Grouping customers based on purchasing behavior.
- **Image Segmentation:** Dividing an image into multiple segments to simplify or change its representation.

Unsupervised Learning provides valuable insights into data by uncovering hidden structures and patterns without the need for labeled data. Understanding the different algorithms and their applications is essential for leveraging the power of unsupervised learning.
