# Calculus

Calculus is a branch of mathematics that studies continuous change. It is divided into two main parts: Differential Calculus and Integral Calculus. Differential Calculus deals with the concept of a derivative, while Integral Calculus focuses on the concept of an integral.

## Key Concepts

### Limits
Limits describe the behavior of a function as its input approaches a certain value.

- **Formal Definition:** \( \lim_{{x \to c}} f(x) = L \) means that as \( x \) approaches \( c \), \( f(x) \) approaches \( L \).

### Continuity
A function is continuous if it has no breaks, jumps, or holes at a point or over an interval.

- **Definition:** A function \( f(x) \) is continuous at \( x = c \) if \( \lim_{{x \to c}} f(x) = f(c) \).

## Differential Calculus

### Derivatives
A derivative represents the rate of change of a function with respect to a variable.

- **Notation:** \( f'(x) \) or \( \frac{d}{dx}f(x) \)
- **Definition:** \( f'(x) = \lim_{{h \to 0}} \frac{f(x+h) - f(x)}{h} \)

### Rules of Differentiation
- **Power Rule:** \( \frac{d}{dx}x^n = nx^{n-1} \)
- **Product Rule:** \( \frac{d}{dx} [u(x)v(x)] = u'(x)v(x) + u(x)v'(x) \)
- **Quotient Rule:** \( \frac{d}{dx} \left[ \frac{u(x)}{v(x)} \right] = \frac{u'(x)v(x) - u(x)v'(x)}{[v(x)]^2} \)
- **Chain Rule:** \( \frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x) \)

### Applications of Derivatives
- **Finding Tangents:** The slope of the tangent line to the curve \( y = f(x) \) at \( x = a \) is \( f'(a) \).
- **Optimization:** Finding local maxima and minima by setting the derivative \( f'(x) = 0 \) and solving for \( x \).
- **Related Rates:** Solving problems where multiple quantities change with respect to time.

## Integral Calculus

### Integrals
An integral represents the accumulation of quantities and can be interpreted as the area under a curve.

- **Definite Integral:** Represents the area under \( f(x) \) from \( a \) to \( b \), denoted as \( \int_{a}^{b} f(x) \, dx \).
- **Indefinite Integral:** Represents the family of all antiderivatives of \( f(x) \), denoted as \( \int f(x) \, dx \).

### Fundamental Theorem of Calculus
- **Part 1:** If \( F(x) \) is an antiderivative of \( f(x) \), then \( \int_{a}^{b} f(x) \, dx = F(b) - F(a) \).
- **Part 2:** If \( F(x) \) is defined as \( F(x) = \int_{a}^{x} f(t) \, dt \), then \( F'(x) = f(x) \).

### Techniques of Integration
- **Substitution:** \( \int f(g(x))g'(x) \, dx = \int f(u) \, du \), where \( u = g(x) \).
- **Integration by Parts:** \( \int u \, dv = uv - \int v \, du \).
- **Partial Fractions:** Decomposing a rational function into simpler fractions that can be integrated individually.

### Applications of Integrals
- **Area Under a Curve:** The area between the curve \( y = f(x) \) and the x-axis from \( x = a \) to \( x = b \) is \( \int_{a}^{b} f(x) \, dx \).
- **Volume of Solids of Revolution:** Using the disk/washer method or the shell method to find the volume of a solid formed by rotating a region around an axis.
- **Work and Energy:** Calculating the work done by a force over a distance, or the energy stored in a system.

## Differential Equations
Differential equations involve derivatives and are used to model various phenomena.

- **First-Order Differential Equations:** Equations involving the first derivative of the function (e.g., \( \frac{dy}{dx} = ky \)).
- **Second-Order Differential Equations:** Equations involving the second derivative of the function (e.g., \( \frac{d^2y}{dx^2} + p(x)\frac{dy}{dx} + q(x)y = 0 \)).

Calculus is a fundamental tool in mathematics, providing the framework for modeling and understanding change. Mastering the concepts of limits, derivatives, integrals, and differential equations is essential for further study in mathematics, physics, engineering, and many other fields.
