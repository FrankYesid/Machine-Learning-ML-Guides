# Descriptive Statistics

Descriptive statistics are used to summarize and describe the main features of a dataset. They provide simple summaries about the sample and the measures. These summaries may be either quantitative (numerical) or visual (graphical).

## Key Concepts in Descriptive Statistics

### Measures of Central Tendency
Central tendency measures describe the center of a dataset.

- **Mean (Average):** The sum of all values divided by the number of values.
  \[ \text{Mean} = \frac{\sum_{i=1}^{n} x_i}{n} \]
  
- **Median:** The middle value when the data is ordered. If the number of observations is even, the median is the average of the two middle numbers.
  
- **Mode:** The value that appears most frequently in the dataset. A dataset may have one mode, more than one mode, or no mode at all.

### Measures of Dispersion
Dispersion measures describe the spread of the data.

- **Range:** The difference between the maximum and minimum values.
  \[ \text{Range} = \text{Max} - \text{Min} \]

- **Variance:** The average of the squared differences from the mean.
  \[ \text{Variance} = \frac{\sum_{i=1}^{n} (x_i - \text{Mean})^2}{n} \]

- **Standard Deviation:** The square root of the variance, representing the average distance of each data point from the mean.
  \[ \text{Standard Deviation} = \sqrt{\text{Variance}} \]

- **Interquartile Range (IQR):** The range between the first quartile (Q1) and the third quartile (Q3), representing the middle 50% of the data.
  \[ \text{IQR} = Q3 - Q1 \]

### Measures of Position
Position measures indicate the relative standing of data points within the dataset.

- **Percentiles:** Values below which a certain percentage of the data falls.
  - The 25th percentile (Q1) is the value below which 25% of the data falls.
  - The 50th percentile (Median) is the value below which 50% of the data falls.
  - The 75th percentile (Q3) is the value below which 75% of the data falls.

- **Z-Score:** The number of standard deviations a data point is from the mean.
  \[ Z = \frac{x - \text{Mean}}{\text{Standard Deviation}} \]

## Graphical Representations

### Histograms
A histogram is a graphical representation of the distribution of numerical data, showing the frequency of data within certain ranges (bins).

### Box Plots
A box plot displays the distribution of data based on a five-number summary: minimum, first quartile (Q1), median, third quartile (Q3), and maximum. It highlights the IQR and potential outliers.

### Scatter Plots
A scatter plot displays values for typically two variables for a set of data, showing how one variable is affected by another. It can indicate relationships or correlations between the variables.

### Bar Charts
A bar chart represents categorical data with rectangular bars, showing the frequency or proportion of categories.

### Pie Charts
A pie chart is a circular statistical graphic, which is divided into slices to illustrate numerical proportions. Each slice represents a category's contribution to the whole.

## Examples

### Example 1: Calculating Measures of Central Tendency
Given the dataset: \[ \{2, 4, 4, 4, 5, 5, 7, 9\} \]
- **Mean:** 
  \[ \text{Mean} = \frac{2 + 4 + 4 + 4 + 5 + 5 + 7 + 9}{8} = 5 \]
- **Median:** 
  Since the dataset has an even number of observations, the median is the average of the 4th and 5th values:
  \[ \text{Median} = \frac{4 + 5}{2} = 4.5 \]
- **Mode:** 
  The most frequent value is 4.

### Example 2: Calculating Measures of Dispersion
Using the same dataset: \[ \{2, 4, 4, 4, 5, 5, 7, 9\} \]
- **Range:**
  \[ \text{Range} = 9 - 2 = 7 \]
- **Variance:**
  \[ \text{Variance} = \frac{(2-5)^2 + (4-5)^2 + (4-5)^2 + (4-5)^2 + (5-5)^2 + (5-5)^2 + (7-5)^2 + (9-5)^2}{8} = \frac{9 + 1 + 1 + 1 + 0 + 0 + 4 + 16}{8} = 4 \ \]
- **Standard Deviation:**
  \[ \text{Standard Deviation} = \sqrt{4} = 2 \]

### Example 3: Creating a Box Plot
Using the same dataset: \[ \{2, 4, 4, 4, 5, 5, 7, 9\} \]
- **Minimum:** 2
- **Q1:** 4
- **Median:** 4.5
- **Q3:** 5.5
- **Maximum:** 9

These measures and representations help in understanding the underlying patterns and characteristics of the data, enabling better decision-making and data interpretation.
