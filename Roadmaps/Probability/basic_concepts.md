# Basic Probability Concepts

Probability is a measure of the likelihood that an event will occur. It quantifies uncertainty and is used extensively in fields such as mathematics, statistics, science, engineering, and everyday decision making.

## Key Concepts

### Experiment and Outcomes
- **Experiment:** A process or action that results in one or several outcomes (e.g., flipping a coin, rolling a die).
- **Outcome:** A possible result of an experiment (e.g., heads or tails in a coin flip).

### Sample Space
- **Sample Space (S):** The set of all possible outcomes of an experiment.
  - Example: For a coin flip, \( S = \{ \text{Heads}, \text{Tails} \} \).
  - Example: For rolling a six-sided die, \( S = \{ 1, 2, 3, 4, 5, 6 \} \).

### Events
- **Event:** A subset of the sample space. An event can consist of one or more outcomes.
  - Example: Rolling an even number on a die is an event, \( E = \{ 2, 4, 6 \} \).

### Probability of an Event
The probability of an event \( A \) is a number between 0 and 1 that indicates how likely the event is to occur. It is defined as:
\[ P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}} \]

### Probability Rules
1. **Non-Negativity:** The probability of any event \( A \) is non-negative, \( P(A) \geq 0 \).
2. **Normalization:** The sum of the probabilities of all possible outcomes in the sample space is 1, \( \sum_{i} P(E_i) = 1 \).
3. **Additivity:** For any two mutually exclusive events \( A \) and \( B \), the probability that \( A \) or \( B \) occurs is \( P(A \cup B) = P(A) + P(B) \).

### Complementary Events
The complement of an event \( A \) is the event that \( A \) does not occur, denoted by \( A' \). The probability of the complement is:
\[ P(A') = 1 - P(A) \]

### Union and Intersection of Events
- **Union (A or B):** The event that either \( A \) or \( B \) or both occur. Denoted by \( A \cup B \).
  \[ P(A \cup B) = P(A) + P(B) - P(A \cap B) \]
- **Intersection (A and B):** The event that both \( A \) and \( B \) occur. Denoted by \( A \cap B \).
  \[ P(A \cap B) = P(B) \cdot P(A|B) \]

### Independent Events
Two events \( A \) and \( B \) are independent if the occurrence of one does not affect the occurrence of the other.
\[ P(A \cap B) = P(A) \cdot P(B) \]

### Conditional Probability
The probability of event \( A \) given that event \( B \) has occurred is called the conditional probability and is denoted by \( P(A|B) \):
\[ P(A|B) = \frac{P(A \cap B)}{P(B)} \]
provided that \( P(B) > 0 \).

### Bayes' Theorem
Bayes' Theorem relates the conditional probability of events:
\[ P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)} \]
This theorem is useful for updating probabilities based on new information.

## Examples

### Example 1: Rolling a Die
- **Sample Space:** \( S = \{1, 2, 3, 4, 5, 6\} \)
- **Event \( A \):** Rolling an even number \( A = \{2, 4, 6\} \)
- **Probability \( P(A) \):** \( P(A) = \frac{3}{6} = 0.5 \)

### Example 2: Drawing a Card from a Deck
- **Sample Space:** A standard deck has 52 cards.
- **Event \( B \):** Drawing a heart \( B = \{\text{13 hearts}\} \)
- **Probability \( P(B) \):** \( P(B) = \frac{13}{52} = 0.25 \)

### Example 3: Coin Toss
- **Sample Space:** \( S = \{\text{Heads, Tails}\} \)
- **Event \( C \):** Getting a head \( C = \{\text{Heads}\} \)
- **Probability \( P(C) \):** \( P(C) = \frac{1}{2} = 0.5 \)

Understanding these basic concepts is crucial for delving deeper into the study of probability and its applications in various fields.
