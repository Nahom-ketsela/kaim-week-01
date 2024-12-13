
# Sentiment and Stock Price Analysis

Welcome to the **Sentiment and Stock Price Analysis** project! This repository focuses on uncovering insights from financial news and stock price data by analyzing the relationship between sentiment and stock market performance.

---

## Project Overview

The project aims to analyze financial news sentiment and correlate it with stock price movements to:

- Quantify the tone and sentiment of financial news using Natural Language Processing (NLP) techniques.
- Discover patterns and relationships between news sentiment and stock market trends.
- Provide actionable insights for investment and trading strategies.

---

## Key Features

### Comprehensive Analysis
- **Sentiment Analysis**:
  - Used NLP techniques to quantify the tone (positive, negative, neutral) of financial news headlines.
  - Associated sentiment scores with stock ticker symbols to analyze emotional context around specific stocks.

- **Correlation Analysis**:
  - Tracked stock price changes around the publication date of financial news articles.
  - Identified statistical correlations between sentiment scores and stock price movements.

### Data Cleaning
- Ensured the dataset's integrity by:
  - Removing duplicates and irrelevant entries.
  - Normalizing timestamps to align news and stock price data.
  - Filling missing values using appropriate estimation techniques.

### Statistical Summaries
- Generated descriptive statistics for sentiment scores and stock price metrics.
- Analyzed sentiment trends over time and their impact on daily stock returns.

### Visualizations
- Visualized sentiment distribution across stocks and sectors.
- Created scatter plots and line charts to show relationships between sentiment and stock prices.
- Generated heatmaps to reveal correlation strengths between variables.

---

## Dataset Information

The dataset includes the following key variables:

- **Headline**: The title of financial news articles, often indicating significant events (e.g., earnings announcements, price target updates).
- **Stock**: Ticker symbols of publicly traded companies (e.g., `AAPL` for Apple).
- **Sentiment Score**: Numerical representation of sentiment derived from NLP techniques.
- **Close Price**: Daily closing price of the corresponding stock.
- **Date**: Publication date and time (UTC-4 timezone) of the news articles.

---

## Setup Instructions

To run the analysis locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Nahom-ketsela/kaim-week-01.git
   ```

2. Install the required dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn textblob
   ```

3. Open the Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

4. Run the analysis in the notebook file provided.

---

## Key Insights

- **Sentiment Trends**: Financial news sentiment fluctuates significantly, with spikes in negativity during market downturns.
- **Stock Performance Correlation**: Positive news sentiment is generally associated with stock price increases, while negative sentiment correlates with price declines.
- **Sector-Specific Sentiment**: Some sectors (e.g., technology) are more sensitive to news sentiment compared to others (e.g., utilities).
- **Data Integrity**: Addressed challenges such as missing data and timestamp misalignment to ensure high-quality analysis.

---

## Recommendations

- **For Investors**: Use sentiment analysis as a supplementary tool to identify potential stock movements.
- **For Analysts**: Focus on sectors or stocks with high sensitivity to sentiment for targeted analysis.
- **For Developers**: Extend the analysis by integrating real-time news sentiment to support predictive modeling.

