# Matrices and Vectors

In linear algebra, matrices and vectors are fundamental objects that are used to represent and solve linear equations, transformations, and more. Understanding the properties and operations of matrices and vectors is essential for many applications in mathematics, physics, computer science, and engineering.

## Vectors

### Definition
A vector is an ordered list of numbers, which can represent points in space, directions, or other quantities.

- **Notation:** Vectors are typically written in bold (e.g., **v**) or with an arrow on top (e.g., \(\vec{v}\)).
- **Column Vector:**
  \[
  \mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}
  \]
- **Row Vector:**
  \[
  \mathbf{v} = \begin{bmatrix} v_1 & v_2 & \cdots & v_n \end{bmatrix}
  \]

### Operations
- **Vector Addition:**
  \[
  \mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1 \\ u_2 \\ \vdots \\ u_n \end{bmatrix} + \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} = \begin{bmatrix} u_1 + v_1 \\ u_2 + v_2 \\ \vdots \\ u_n + v_n \end{bmatrix}
  \]

- **Scalar Multiplication:**
  \[
  c \mathbf{v} = c \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} = \begin{bmatrix} c v_1 \\ c v_2 \\ \vdots \\ c v_n \end{bmatrix}
  \]

- **Dot Product:**
  \[
  \mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + \ldots + u_n v_n
  \]

- **Norm (Magnitude):**
  \[
  \|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2}
  \]

## Matrices

### Definition
A matrix is a rectangular array of numbers arranged in rows and columns.

- **Notation:** Matrices are typically written in uppercase bold (e.g., **A**) or with brackets.
- **Matrix:**
  \[
  \mathbf{A} = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}
  \]

### Operations
- **Matrix Addition:**
  \[
  \mathbf{A} + \mathbf{B} = \begin{bmatrix} a_{ij} \end{bmatrix} + \begin{bmatrix} b_{ij} \end{bmatrix} = \begin{bmatrix} a_{ij} + b_{ij} \end{bmatrix}
  \]

- **Scalar Multiplication:**
  \[
  c \mathbf{A} = c \begin{bmatrix} a_{ij} \end{bmatrix} = \begin{bmatrix} c a_{ij} \end{bmatrix}
  \]

- **Matrix Multiplication:**
  \[
  (\mathbf{A} \mathbf{B})_{ij} = \sum_{k} a_{ik} b_{kj}
  \]
  where \( \mathbf{A} \) is an \( m \times n \) matrix and \( \mathbf{B} \) is an \( n \times p \) matrix.

- **Transpose:**
  The transpose of a matrix \( \mathbf{A} \), denoted by \( \mathbf{A}^T \), is obtained by swapping its rows and columns.
  \[
  \mathbf{A}^T = \begin{bmatrix} a_{11} & a_{21} & \cdots & a_{m1} \\ a_{12} & a_{22} & \cdots & a_{m2} \\ \vdots & \vdots & \ddots & \vdots \\ a_{1n} & a_{2n} & \cdots & a_{mn} \end{bmatrix}
  \]

- **Determinant:**
  The determinant is a scalar value that can be computed from the elements of a square matrix and encodes certain properties of the matrix.
  For a \( 2 \times 2 \) matrix:
  \[
  \det(\mathbf{A}) = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc
  \]

- **Inverse:**
  The inverse of a square matrix \( \mathbf{A} \), denoted by \( \mathbf{A}^{-1} \), is the matrix such that:
  \[
  \mathbf{A} \mathbf{A}^{-1} = \mathbf{A}^{-1} \mathbf{A} = \mathbf{I}
  \]
  where \( \mathbf{I} \) is the identity matrix.

## Special Types of Matrices

- **Identity Matrix:** A square matrix with ones on the diagonal and zeros elsewhere.
  \[
  \mathbf{I} = \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{bmatrix}
  \]

- **Zero Matrix:** A matrix with all elements equal to zero.
  \[
  \mathbf{0} = \begin{bmatrix} 0 & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 \end{bmatrix}
  \]

- **Diagonal Matrix:** A matrix where all off-diagonal elements are zero.
  \[
  \mathbf{D} = \begin{bmatrix} d_1 & 0 & \cdots & 0 \\ 0 & d_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & d_n \end{bmatrix}
  \]

- **Symmetric Matrix:** A matrix that is equal to its transpose.
  \[
  \mathbf{A} = \mathbf{A}^T
  \]

## Applications of Matrices and Vectors

- **Solving Systems of Linear Equations:**
  Represent a system of linear equations as \( \mathbf{A} \mathbf{x} = \mathbf{b} \) and use matrix operations to find \( \mathbf{x} \).

- **Linear Transformations:**
  Matrices represent linear transformations from one vector space to another.

- **Computer Graphics:**
  Matrices are used to perform transformations such as translation, rotation, and scaling on graphical objects.

- **Machine Learning:**
  Vectors and matrices are used to represent data, parameters, and transformations in algorithms such as linear regression, neural networks, and more.

Understanding matrices and vectors is crucial for many fields, including mathematics, physics, computer science, and engineering, as they provide a powerful framework for modeling and solving complex problems.
