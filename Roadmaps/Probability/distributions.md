# Probability Distributions

Probability distributions describe how the values of a random variable are distributed. They provide a way to understand the likelihood of different outcomes. Distributions can be discrete or continuous, depending on the nature of the random variable.

## Discrete Probability Distributions

Discrete probability distributions apply to scenarios where the random variable can take on a finite or countable number of values.

### Binomial Distribution
The binomial distribution represents the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success.

- **Parameters:** \( n \) (number of trials), \( p \) (probability of success)
- **Probability Mass Function (PMF):**
  \[ P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} \]
  where \( \binom{n}{k} \) is the binomial coefficient.

### Poisson Distribution
The Poisson distribution represents the number of events occurring in a fixed interval of time or space, given that these events occur with a known constant mean rate and independently of the time since the last event.

- **Parameter:** \( \lambda \) (average rate of occurrence)
- **Probability Mass Function (PMF):**
  \[ P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!} \]

### Geometric Distribution
The geometric distribution represents the number of trials needed to get the first success in a sequence of independent Bernoulli trials.

- **Parameter:** \( p \) (probability of success)
- **Probability Mass Function (PMF):**
  \[ P(X = k) = (1-p)^{k-1} p \]

### Hypergeometric Distribution
The hypergeometric distribution describes the number of successes in a sequence of draws from a finite population without replacement.

- **Parameters:** \( N \) (population size), \( K \) (number of successes in the population), \( n \) (number of draws)
- **Probability Mass Function (PMF):**
  \[ P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}} \]

## Continuous Probability Distributions

Continuous probability distributions apply to scenarios where the random variable can take on an infinite number of values within a given range.

### Normal Distribution
The normal distribution, also known as the Gaussian distribution, is a continuous distribution characterized by its bell-shaped curve. It is defined by its mean \( \mu \) and standard deviation \( \sigma \).

- **Probability Density Function (PDF):**
  \[ f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2} \]

### Exponential Distribution
The exponential distribution represents the time between events in a Poisson process. It is often used to model waiting times.

- **Parameter:** \( \lambda \) (rate parameter)
- **Probability Density Function (PDF):**
  \[ f(x) = \lambda e^{-\lambda x} \]
  for \( x \geq 0 \).

### Uniform Distribution
The uniform distribution represents a situation where all outcomes are equally likely within a given range \([a, b]\).

- **Probability Density Function (PDF):**
  \[ f(x) = \frac{1}{b-a} \]
  for \( a \leq x \leq b \).

### Gamma Distribution
The gamma distribution is a two-parameter family of continuous probability distributions often used to model waiting times for multiple events.

- **Parameters:** \( \alpha \) (shape parameter), \( \beta \) (rate parameter)
- **Probability Density Function (PDF):**
  \[ f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x} \]
  for \( x \geq 0 \).

### Beta Distribution
The beta distribution is a family of continuous probability distributions defined on the interval \([0, 1]\) and parameterized by two positive shape parameters \( \alpha \) and \( \beta \).

- **Probability Density Function (PDF):**
  \[ f(x) = \frac{x^{\alpha-1} (1-x)^{\beta-1}}{B(\alpha, \beta)} \]
  for \( 0 \leq x \leq 1 \), where \( B(\alpha, \beta) \) is the beta function.

## Key Properties of Distributions

### Expected Value
The expected value (mean) of a random variable gives a measure of the central tendency of the distribution.

- **Discrete Random Variable:** 
  \[ E(X) = \sum_{x} x P(X = x) \]
- **Continuous Random Variable:** 
  \[ E(X) = \int_{-\infty}^{\infty} x f(x) \, dx \]

### Variance
The variance measures the spread or dispersion of the distribution around the mean.

- **Discrete Random Variable:** 
  \[ \text{Var}(X) = \sum_{x} (x - E(X))^2 P(X = x) \]
- **Continuous Random Variable:** 
  \[ \text{Var}(X) = \int_{-\infty}^{\infty} (x - E(X))^2 f(x) \, dx \]

### Standard Deviation
The standard deviation is the square root of the variance and provides a measure of the average distance of the values from the mean.

## Applications of Probability Distributions

Probability distributions are used in a wide range of applications, including:
- **Quality Control:** Modeling defects and failures in manufacturing.
- **Finance:** Analyzing returns on investments and risk management.
- **Medicine:** Modeling the spread of diseases and the effectiveness of treatments.
- **Engineering:** Reliability analysis and risk assessment.
- **Natural Sciences:** Modeling physical phenomena and experimental data.

Understanding the characteristics and applications of different probability distributions is essential for analyzing data and making informed decisions based on probabilistic models.
