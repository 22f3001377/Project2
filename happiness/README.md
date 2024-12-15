# README.md

## Overview

This dataset provides a comprehensive analysis of various factors influencing happiness and well-being across different countries over a period of time. The dataset consists of 2,363 records and 11 columns, including key metrics such as life satisfaction, GDP per capita, social support, and perceptions of corruption. The analysis aims to uncover patterns and correlations between these variables, offering valuable insights into the determinants of happiness.

## Dataset Summary

- **Shape**: (2363, 11)
- **Columns**:
  - `Country name`: Name of the country.
  - `year`: The year of the data entry.
  - `Life Ladder`: A measure of subjective well-being (happiness).
  - `Log GDP per capita`: The natural logarithm of GDP per capita, indicating economic prosperity.
  - `Social support`: A measure of perceived social support.
  - `Healthy life expectancy at birth`: Average life expectancy adjusted for health.
  - `Freedom to make life choices`: A measure of personal freedom.
  - `Generosity`: A measure of altruistic behavior.
  - `Perceptions of corruption`: The perceived level of corruption in the country.
  - `Positive affect`: The presence of positive feelings.
  - `Negative affect`: The presence of negative feelings.

### Missing Values

The dataset contains missing values in several columns, which may affect the analysis:

- `Log GDP per capita`: 28 missing values
- `Social support`: 13 missing values
- `Healthy life expectancy at birth`: 63 missing values
- `Freedom to make life choices`: 36 missing values
- `Generosity`: 81 missing values
- `Perceptions of corruption`: 125 missing values
- `Positive affect`: 24 missing values
- `Negative affect`: 16 missing values

### Summary Statistics

Key summary statistics reveal the central tendencies and variations in the data:

- **Life Ladder**: Mean = 5.48, with a range from 1.28 to 8.02.
- **Log GDP per capita**: Mean = 9.40, indicating varying levels of economic prosperity.
- **Social support**: Mean = 0.81, suggesting a generally high level of social support across the dataset.
- **Healthy life expectancy**: Mean = 63.40 years, indicating a broad range of health outcomes.
- **Freedom to make life choices**: Mean = 0.75, indicating a moderate to high level of perceived freedom.
- **Generosity**: Mean = 0.0001, suggesting low levels of measured generosity across the dataset.
- **Perceptions of corruption**: Mean = 0.74, indicating a general perception of corruption in many countries.
- **Positive affect**: Mean = 0.65, suggesting a prevalence of positive feelings.
- **Negative affect**: Mean = 0.27, indicating lower levels of negative feelings.

## Visualizations

The following visualizations have been created to aid in understanding the dataset and the relationships between the variables:

1. **Correlation Heatmap**: This visualization provides insights into how different variables are correlated with one another, helping to identify potential relationships and areas for further analysis.
   
   ![Correlation Heatmap](C:\\Users\\SUMEDHA\\Downloads\\happiness\\correlation_heatmap.png)

2. **Histograms**: Several histograms display the distribution of key variables, including:
   - Year Distribution
   - Life Ladder Distribution
   - Log GDP per capita Distribution
   - Social Support Distribution
   - Healthy Life Expectancy Distribution
   - Freedom to Make Life Choices Distribution
   - Generosity Distribution
   - Perceptions of Corruption Distribution
   - Positive Affect Distribution
   - Negative Affect Distribution

   ![Year Histogram](C:\\Users\\SUMEDHA\\Downloads\\happiness\\year_histogram.png)
   ![Life Ladder Histogram](C:\\Users\\SUMEDHA\\Downloads\\happiness\\Life Ladder_histogram.png)
   ![Log GDP per capita Histogram](C:\\Users\\SUMEDHA\\Downloads\\happiness\\Log GDP per capita_histogram.png)
   ![Social Support Histogram](C:\\Users\\SUMEDHA\\Downloads\\happiness\\Social support_histogram.png)
   ![Healthy Life Expectancy Histogram](C:\\Users\\SUMEDHA\\Downloads\\happiness\\Healthy life expectancy at birth_histogram.png)
   ![Freedom to Make Life Choices Histogram](C:\\Users\\SUMEDHA\\Downloads\\happiness\\Freedom to make life choices_histogram.png)
   ![Generosity Histogram](C:\\Users\\SUMEDHA\\Downloads\\happiness\\Generosity_histogram.png)
   ![Perceptions of Corruption Histogram](C:\\Users\\SUMEDHA\\Downloads\\happiness\\Perceptions of corruption_histogram.png)
   ![Positive Affect Histogram](C:\\Users\\SUMEDHA\\Downloads\\happiness\\Positive affect_histogram.png)
   ![Negative Affect Histogram](C:\\Users\\SUMEDHA\\Downloads\\happiness\\Negative affect_histogram.png)

## Key Insights

1. **Economic Factors**: There is a positive correlation between Log GDP per capita and Life Ladder, suggesting that higher economic prosperity often correlates with greater happiness.

2. **Social Support**: The high average score for social support indicates that countries with strong social networks tend to have higher happiness scores.

3. **Freedom and Happiness**: The perceived freedom to make life choices also shows a positive relationship with life satisfaction, highlighting the importance of autonomy in enhancing well-being.

4. **Corruption Perception**: The relatively high perception of corruption may negatively impact happiness, indicating that governance and trust in institutions are crucial for societal well-being.

5. **Generosity**: The low average score for generosity suggests a need for further exploration into the societal factors that influence altruistic behavior.

## Implications

These insights underscore the importance of economic development, social support networks, individual freedoms, and governance in promoting happiness and well-being. Policymakers and stakeholders can use this information to design targeted interventions that foster a happier society by addressing economic and social inequalities, enhancing freedom of choice, and improving governance.

This analysis serves as a foundation for further research and discussions on the multifaceted nature of happiness and well-being on a global scale.