# Basic Linear Algebra

Linear algebra is a branch of mathematics that deals with vectors, vector spaces (also called linear spaces), linear transformations, and systems of linear equations. It is fundamental for many areas of mathematics and its applications, particularly in computer science and machine learning.

## Vectors

### Definition
A vector is an ordered list of numbers. Vectors can be thought of as points in space or as directions with magnitude.

- **Notation:** Vectors are typically written in bold (e.g., **v**) or with an arrow on top (e.g., \(\vec{v}\)).

### Operations
- **Addition:** The sum of two vectors **u** and **v** is another vector obtained by adding the corresponding components.
  \[
  \mathbf{u} + \mathbf{v} = (u_1 + v_1, u_2 + v_2, \ldots, u_n + v_n)
  \]

- **Scalar Multiplication:** The product of a scalar \( c \) and a vector **v** is obtained by multiplying each component of **v** by \( c \).
  \[
  c\mathbf{v} = (cv_1, cv_2, \ldots, cv_n)
  \]

- **Dot Product:** The dot product (or inner product) of two vectors **u** and **v** is a scalar defined as the sum of the products of their corresponding components.
  \[
  \mathbf{u} \cdot \mathbf{v} = u_1v_1 + u_2v_2 + \ldots + u_nv_n
  \]

- **Norm (Magnitude):** The norm (or length) of a vector **v** is a measure of its length.
  \[
  \|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2}
  \]

## Matrices

### Definition
A matrix is a rectangular array of numbers arranged in rows and columns. 

- **Notation:** Matrices are typically written in uppercase bold (e.g., **A**) or with brackets.

### Operations
- **Addition:** The sum of two matrices **A** and **B** of the same size is obtained by adding their corresponding elements.
  \[
  \mathbf{A} + \mathbf{B} = [a_{ij} + b_{ij}]
  \]

- **Scalar Multiplication:** The product of a scalar \( c \) and a matrix **A** is obtained by multiplying each element of **A** by \( c \).
  \[
  c\mathbf{A} = [ca_{ij}]
  \]

- **Matrix Multiplication:** The product of two matrices **A** and **B** is defined if the number of columns in **A** equals the number of rows in **B**. The element in the \(i\)-th row and \(j\)-th column of the product matrix is the dot product of the \(i\)-th row of **A** and the \(j\)-th column of **B**.
  \[
  (\mathbf{A} \mathbf{B})_{ij} = \sum_{k} a_{ik} b_{kj}
  \]

### Special Matrices
- **Identity Matrix:** A square matrix with ones on the diagonal and zeros elsewhere.
  \[
  \mathbf{I} = \begin{bmatrix}
  1 & 0 & \cdots & 0 \\
  0 & 1 & \cdots & 0 \\
  \vdots & \vdots & \ddots & \vdots \\
  0 & 0 & \cdots & 1
  \end{bmatrix}
  \]

- **Zero Matrix:** A matrix with all elements equal to zero.
  \[
  \mathbf{0} = \begin{bmatrix}
  0 & 0 & \cdots & 0 \\
  0 & 0 & \cdots & 0 \\
  \vdots & \vdots & \ddots & \vdots \\
  0 & 0 & \cdots & 0
  \end{bmatrix}
  \]

## Linear Transformations

### Definition
A linear transformation is a function between two vector spaces that preserves vector addition and scalar multiplication.

- **Notation:** If **T** is a linear transformation from vector space **V** to vector space **W**, it is written as \( T: V \to W \).

### Properties
- **Linearity:** 
  \[
  T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})
  \]
  \[
  T(c\mathbf{v}) = cT(\mathbf{v})
  \]

### Matrix Representation
Every linear transformation can be represented by a matrix. If **T** is a linear transformation, then there exists a matrix **A** such that:
  \[
  T(\mathbf{v}) = \mathbf{A} \mathbf{v}
  \]

## Systems of Linear Equations

### Definition
A system of linear equations is a collection of one or more linear equations involving the same set of variables.

### Matrix Form
A system of linear equations can be written in matrix form as:
  \[
  \mathbf{A} \mathbf{x} = \mathbf{b}
  \]
where **A** is the coefficient matrix, **x** is the vector of variables, and **b** is the vector of constants.

### Solution Methods
- **Gaussian Elimination:** A method for solving a system of linear equations by transforming the system's augmented matrix to row echelon form using row operations.
  
- **Matrix Inversion:** If **A** is an invertible matrix, the system can be solved by multiplying both sides by the inverse of **A**:
  \[
  \mathbf{x} = \mathbf{A}^{-1} \mathbf{b}
  \]

## Applications of Linear Algebra

Linear algebra has a wide range of applications, including:
- **Computer Graphics:** Transformations, rotations, and scaling of objects.
- **Machine Learning:** Algorithms such as linear regression, support vector machines, and neural networks.
- **Engineering:** Systems of equations in circuit analysis, structural analysis.
- **Economics:** Input-output models, optimization problems.

Understanding basic linear algebra is crucial for advancing in many fields of science, engineering, and technology.
