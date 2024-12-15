# Happiness Dataset Analysis

## Overview

This repository contains an analysis of a dataset focused on various factors influencing happiness across different countries and years. The dataset consists of 2,363 entries and 11 columns, encompassing a range of metrics such as life satisfaction (Life Ladder), economic indicators (Log GDP per capita), social support, and perceptions of corruption, among others. The primary goal of this analysis is to explore the relationships within these variables and to provide insights into what drives happiness in different contexts.

## Dataset Summary

- **Shape**: The dataset contains 2,363 rows and 11 columns.
- **Columns**: The following variables are included:
  - **Country name**: The name of the country (categorical).
  - **Year**: The year of the record (integer).
  - **Life Ladder**: A measure of life satisfaction (float).
  - **Log GDP per capita**: The logarithm of GDP per capita (float).
  - **Social Support**: A measure of social support available to individuals (float).
  - **Healthy Life Expectancy at Birth**: Average years an individual is expected to live in good health (float).
  - **Freedom to Make Life Choices**: Measure of freedom individuals feel they have (float).
  - **Generosity**: A measure of generosity in society (float).
  - **Perceptions of Corruption**: How corrupt a society is perceived to be (float).
  - **Positive Affect**: Measure of positive feelings (float).
  - **Negative Affect**: Measure of negative feelings (float).

### Missing Values

The analysis identified missing values in several key variables:
- **Log GDP per capita**: 28 missing values.
- **Social support**: 13 missing values.
- **Healthy life expectancy at birth**: 63 missing values.
- **Freedom to make life choices**: 36 missing values.
- **Generosity**: 81 missing values.
- **Perceptions of corruption**: 125 missing values.
- **Positive affect**: 24 missing values.
- **Negative affect**: 16 missing values.

Handling these missing values is essential to ensure the robustness of further analyses.

### Summary Statistics

- **Life Ladder**: The mean score is approximately 5.48, with a standard deviation of 1.12, indicating variability in happiness levels across countries.
- **Log GDP per capita**: The average is around 9.40, suggesting a relationship between economic status and happiness.
- **Social Support**: The average score is 0.81, highlighting the importance of social networks in contributing to happiness.
- **Healthy Life Expectancy**: The average is about 63.40 years, underlining the relevance of health to overall well-being.
- **Freedom to Make Life Choices**: The mean score is 0.75, indicating that personal freedoms may significantly influence happiness.
- **Generosity**: The average is very low (9.77e-05), which may suggest a need for exploring cultural or societal factors influencing generosity.
- **Perceptions of Corruption**: The average score is 0.74, reflecting the impact of governance and trust on happiness.
- **Positive Affect**: The mean score is around 0.65, while the negative affect score averages at 0.27, indicating more prevalent positive feelings.

## Visualizations

The analysis includes several visualizations that provide further insights:

1. **Correlation Heatmap**: This visualization illustrates the relationships between different variables in the dataset. Strong correlations may indicate potential causal relationships worthy of further exploration.
2. **Histograms**: Histograms for each key variable (e.g., Life Ladder, Log GDP per capita, Social Support) provide a distribution view, revealing how these metrics are spread across the dataset.

## Key Insights

- **Economic Factors**: The analysis suggests a positive relationship between log GDP per capita and life satisfaction, indicating that wealthier countries tend to report higher happiness levels.
- **Social Support**: A high level of social support correlates with increased happiness, emphasizing the significance of community and interpersonal relationships in enhancing well-being.
- **Health and Life Expectancy**: Healthy life expectancy is a critical factor; countries with higher life expectancy often report better happiness metrics.
- **Freedom and Autonomy**: The perception of freedom to make life choices is linked to higher life satisfaction, underscoring the role of personal agency in happiness.
- **Corruption and Trust**: The perception of corruption inversely relates to happiness levels, suggesting that trust in governance can significantly impact societal well-being.

## Implications

The findings from this analysis can inform policymakers, social scientists, and NGOs focused on improving quality of life. Emphasizing economic development, enhancing social support systems, promoting health initiatives, and fostering environments of trust and freedom can lead to improved happiness outcomes across populations. Further research could delve into the causal mechanisms behind these relationships, utilizing longitudinal data to track changes over time.

---

This README.md serves as a comprehensive guide to understanding the analysis performed on the happiness dataset, the insights drawn from it, and its potential implications for societal well-being.
