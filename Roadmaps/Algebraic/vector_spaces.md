# Vector Spaces

A vector space (or linear space) is a fundamental concept in linear algebra. It is a collection of vectors that can be added together and multiplied ("scaled") by numbers, called scalars. Scalars are often taken to be real numbers, but there are also vector spaces with scalar multiplication defined over other fields, such as complex numbers.

## Definition of a Vector Space

A vector space \( V \) over a field \( F \) is a set equipped with two operations:

1. **Vector Addition:** An operation that takes any two vectors \( \mathbf{u} \) and \( \mathbf{v} \) in \( V \) and produces another vector \( \mathbf{w} \) in \( V \).
   \[
   \mathbf{u} + \mathbf{v} = \mathbf{w}
   \]

2. **Scalar Multiplication:** An operation that takes any scalar \( c \) in \( F \) and any vector \( \mathbf{v} \) in \( V \) and produces another vector \( \mathbf{w} \) in \( V \).
   \[
   c \mathbf{v} = \mathbf{w}
   \]

These operations must satisfy eight axioms (properties):

### Axioms of Vector Spaces

1. **Closure under Addition:**
   \[
   \mathbf{u} + \mathbf{v} \in V \quad \text{for all } \mathbf{u}, \mathbf{v} \in V
   \]

2. **Commutativity of Addition:**
   \[
   \mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u} \quad \text{for all } \mathbf{u}, \mathbf{v} \in V
   \]

3. **Associativity of Addition:**
   \[
   (\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w}) \quad \text{for all } \mathbf{u}, \mathbf{v}, \mathbf{w} \in V
   \]

4. **Existence of Additive Identity:**
   There exists an element \( \mathbf{0} \in V \) such that:
   \[
   \mathbf{u} + \mathbf{0} = \mathbf{u} \quad \text{for all } \mathbf{u} \in V
   \]

5. **Existence of Additive Inverse:**
   For each \( \mathbf{u} \in V \), there exists an element \( -\mathbf{u} \in V \) such that:
   \[
   \mathbf{u} + (-\mathbf{u}) = \mathbf{0}
   \]

6. **Closure under Scalar Multiplication:**
   \[
   c \mathbf{u} \in V \quad \text{for all } c \in F \text{ and } \mathbf{u} \in V
   \]

7. **Distributivity of Scalar Multiplication with respect to Vector Addition:**
   \[
   c (\mathbf{u} + \mathbf{v}) = c \mathbf{u} + c \mathbf{v} \quad \text{for all } c \in F \text{ and } \mathbf{u}, \mathbf{v} \in V
   \]

8. **Distributivity of Scalar Multiplication with respect to Field Addition:**
   \[
   (c + d) \mathbf{u} = c \mathbf{u} + d \mathbf{u} \quad \text{for all } c, d \in F \text{ and } \mathbf{u} \in V
   \]

9. **Associativity of Scalar Multiplication:**
   \[
   c (d \mathbf{u}) = (cd) \mathbf{u} \quad \text{for all } c, d \in F \text{ and } \mathbf{u} \in V
   \]

10. **Existence of Multiplicative Identity:**
    There exists an element \( 1 \in F \) such that:
    \[
    1 \mathbf{u} = \mathbf{u} \quad \text{for all } \mathbf{u} \in V
    \]

## Examples of Vector Spaces

### Example 1: Euclidean Space
The set of all \( n \)-tuples of real numbers \( \mathbb{R}^n \) is a vector space. Vector addition and scalar multiplication are defined as:
\[
(x_1, x_2, \ldots, x_n) + (y_1, y_2, \ldots, y_n) = (x_1 + y_1, x_2 + y_2, \ldots, x_n + y_n)
\]
\[
c (x_1, x_2, \ldots, x_n) = (c x_1, c x_2, \ldots, c x_n)
\]

### Example 2: Polynomial Space
The set of all polynomials with real coefficients \( \mathbb{R}[x] \) is a vector space. Vector addition and scalar multiplication are defined as the usual addition and scalar multiplication of polynomials.

### Example 3: Function Space
The set of all continuous functions from a set \( S \) to the real numbers \( \mathbb{R} \), denoted by \( C(S, \mathbb{R}) \), is a vector space. Vector addition and scalar multiplication are defined pointwise:
\[
(f + g)(x) = f(x) + g(x)
\]
\[
(c f)(x) = c f(x)
\]

## Subspaces

A subspace is a subset of a vector space that is itself a vector space under the same operations.

### Definition
A subset \( W \) of a vector space \( V \) is a subspace if:
1. The zero vector of \( V \) is in \( W \).
2. \( W \) is closed under vector addition.
3. \( W \) is closed under scalar multiplication.

### Example: Line through the Origin
The set of all scalar multiples of a fixed vector \( \mathbf{v} \) in \( \mathbb{R}^n \) forms a subspace of \( \mathbb{R}^n \).

## Basis and Dimension

### Basis
A basis of a vector space \( V \) is a set of vectors in \( V \) that are linearly independent and span \( V \).

### Dimension
The dimension of a vector space \( V \) is the number of vectors in a basis of \( V \).

### Example
In \( \mathbb{R}^2 \), the vectors \( \mathbf{e_1} = (1, 0) \) and \( \mathbf{e_2} = (0, 1) \) form a basis. The dimension of \( \mathbb{R}^2 \) is 2.

## Linear Combinations and Span

### Linear Combination
A linear combination of vectors \( \mathbf{v_1}, \mathbf{v_2}, \ldots, \mathbf{v_k} \) is an expression of the form:
\[
c_1 \mathbf{v_1} + c_2 \mathbf{v_2} + \ldots + c_k \mathbf{v_k}
\]
where \( c_1, c_2, \ldots, c_k \) are scalars.

### Span
The span of a set of vectors \( \{\mathbf{v_1}, \mathbf{v_2}, \ldots, \mathbf{v_k}\} \) is the set of all linear combinations of these vectors. It is the smallest subspace that contains all the vectors in the set.

Understanding vector spaces is crucial for studying linear transformations, eigenvalues, eigenvectors, and many other advanced topics in linear algebra and its applications.
