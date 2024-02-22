
# Sentiment Analysis Preprocessing Tool

## Introduction

This project provides a comprehensive tool for preprocessing textual data for sentiment analysis. It includes functionalities for data cleaning, text preprocessing, and visualization to aid in understanding the distribution of sentiments within a dataset.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)

## Installation

No installation is required beyond the Python environment. Ensure you have Python installed, and then install the necessary libraries using pip:

```bash
pip install pandas matplotlib wordcloud nltk beautifulsoup4
```

## Usage

To use this tool, simply run the script `sentiment_preprocess.py` with Python, providing the path to your dataset file as an argument:

```bash
python sentiment_preprocess.py <path_to_your_dataset.csv>
```

## Features

- **Data Loading**: Load textual data from CSV files.
- **Duplicate Removal**: Identifies and removes duplicate entries in the dataset.
- **Text Cleaning**: Includes contraction fixing, HTML tag removal, special character removal, case normalization, and tokenization.
- **Stopwords Removal and Lemmatization**: Further cleans the text by removing stopwords and applying lemmatization.
- **Visualization**: Generates word clouds to visualize the most frequent words in positive and negative sentiments.

## Dependencies

- pandas
- matplotlib
- WordCloud
- NLTK
- BeautifulSoup

## Examples

To process a dataset named `reviews.csv` located in your current directory:

```bash
python sentiment_preprocess.py reviews.csv
```

This will preprocess the text data and show visualizations of the word frequencies for different sentiments.

## Troubleshooting

- Ensure all dependencies are installed and up-to-date.
- Verify the dataset path is correct and accessible.
- Check for any typos in the script or command line.

```
