# Applying AI to EHR Data

## The Dataset
Dataset: Heart Disease Dataset donated to [UCI ML Dataset Repository](https://archive.ics.uci.edu/ml/datasets/heart+Disease).

Authors:
Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
V.A. Medical Center, Long Beach and Cleveland Clinic Foundation:Robert Detrano, M.D., Ph.D.

## 1. Basic Concepts

### 1.8. Value Distribution
#### Gaussian/Normal
#### Uniform
All values with the same or similar frequency. Usually represents a problem.
#### Skewed/Unbalanced
A small subset have high values

### 1.9. Missing Values and Outliers
#### Missing Completly at Random (MCAR)
Data missing due to something unrelated and there is no systematic reason.
Example: "White cell value Data is missing because a testing machine was improperly calibrated."
#### Missing at Random (MAR)
There is some systematic reason for the missing.
Example: "Women could be less likely to give their weight on a survey."
#### Missing Not at Random (MNAR)
There is a relationship between a value in the dataset and the missing values.
Example: "Those with low education are not accounted for in a study."

### 1.10. Analysing Dataset for High Cardinality
Cardinality is the number of unique values that a feature has aind is relevant to EHR datasets because there are code sets such as diagnosis codes in the order of tens of thousands of unique codes. This only applies to categorical features and the reason this is a problem is that it can increase dimensionality and makes training models much more difficult and time-consuming.

### 2. EHR Code Sets
#### 2.1 Code Sets Overview

Diagnose codes: IDC10-CM
Procedure Codes: IDC10-PCS, CPT, HCPCS
Medication Codes: NDC Codes, RXNorm
Grouping/Categorizing: CCS

#### 2.2 Code Sets Background
Medical Encounter: interaction between a patient and healthcare provider(s) to provide healthcare service(s) or assessing the health status of a patient.

#### 2.3 Diagnosis Codes Part 1
Diagnosis is a key piece of information that connects so much of the encounter experience together.
IDC10: International Classification of Deseases 10
IDC10-CM: International Classification of Deseases 10 - Clinical Modification. Medical claims, disease epidemic and mortality tracking
Changing IDC9 (XXX.XX) -> IDC10 (XXX.XXX X).

IDC10-CM format

AAA.BBB C
A - Category of the diagnosis. 21 different categories
B - Etiology, anatomic site and manifestation part, the cause for a condition or desease or the local of the condition
C - Often wised tiwh injunry-related codes referring to the episode of care

#### 2.4 Diagnosis Codes Part 2
To receive a diganoses can be necessary several encounters.
Diagnose codes should never be repeated in the same encounter.
Diagnosis would carry accros different encounters.
Prioritization of Diagnosis Codes:
 - Primary Diagnosis: most resource intensive diagnosis code;
 - Princial Diagnosis: that condition established after study to be chiefly responsible for occasioning the admission of the patient to the hospital for care;
 - Secondary Diagnosis: other diagnoses codes;



## File descriptions
### dataset-schema-analysis.py
Some examples of analysis on a dataset to understand properties such as value distributions, missing values, outliers, cardinality and demographic analysis using Numpy, Pandas and Matplotlib