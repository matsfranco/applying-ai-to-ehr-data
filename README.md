# Applying AI to EHR Data

## The Dataset
Dataset: Heart Disease Dataset donated to [UCI ML Dataset Repository](https://archive.ics.uci.edu/ml/datasets/heart+Disease).

Authors:
Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
V.A. Medical Center, Long Beach and Cleveland Clinic Foundation:Robert Detrano, M.D., Ph.D.

## Basic Concepts

### 8. Value Distribution
#### Gaussian/Normal
#### Uniform
All values with the same or similar frequency. Usually represents a problem.
#### Skewed/Unbalanced
A small subset have high values

### 9. Missing Values and Outliers
#### Missing Completly at Random (MCAR)
Data missing due to something unrelated and there is no systematic reason.
Example: "White cell value Data is missing because a testing machine was improperly calibrated."
#### Missing at Random (MAR)
There is some systematic reason for the missing.
Example: "Women could be less likely to give their weight on a survey."
#### Missing Not at Random (MNAR)
There is a relationship between a value in the dataset and the missing values.
Example: "Those with low education are not accounted for in a study."

### 10. Analysing Dataset for High Cardinality
Cardinality is the number of unique values that a feature has aind is relevant to EHR datasets because there are code sets such as diagnosis codes in the order of tens of thousands of unique codes. This only applies to categorical features and the reason this is a problem is that it can increase dimensionality and makes training models much more difficult and time-consuming.


## File descriptions
### dataset-schema-analysis.py
Some examples of analysis on a dataset to understand properties such as value distributions, missing values, outliers, cardinality and demographic analysis using Numpy, Pandas and Matplotlib