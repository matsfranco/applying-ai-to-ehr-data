# Applying AI to EHR Data

## The Dataset
Dataset: Heart Disease Dataset donated to [UCI ML Dataset Repository](https://archive.ics.uci.edu/ml/datasets/heart+Disease).

Authors:
Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
V.A. Medical Center, Long Beach and Cleveland Clinic Foundation:Robert Detrano, M.D., Ph.D.

## 1. Basic Concepts

### 1.8 Value Distribution
#### Gaussian/Normal
#### Uniform
All values with the same or similar frequency. Usually represents a problem.
#### Skewed/Unbalanced
A small subset have high values

### 1.9 Missing Values and Outliers
#### Missing Completly at Random (MCAR)
Data missing due to something unrelated and there is no systematic reason.
Example: "White cell value Data is missing because a testing machine was improperly calibrated."
#### Missing at Random (MAR)
There is some systematic reason for the missing.
Example: "Women could be less likely to give their weight on a survey."
#### Missing Not at Random (MNAR)
There is a relationship between a value in the dataset and the missing values.
Example: "Those with low education are not accounted for in a study."

### 1.10 Analysing Dataset for High Cardinality
Cardinality is the number of unique values that a feature has aind is relevant to EHR datasets because there are code sets such as diagnosis codes in the order of tens of thousands of unique codes. This only applies to categorical features and the reason this is a problem is that it can increase dimensionality and makes training models much more difficult and time-consuming.

### 2. EHR Code Sets
#### 2.1 Code Sets Overview

Diagnose codes: ICD10-CM
Procedure Codes: ICD10-PCS, CPT, HCPCS
Medication Codes: NDC Codes, RXNorm
Grouping/Categorizing: CCS

#### 2.2 Code Sets Background
Medical Encounter: interaction between a patient and healthcare provider(s) to provide healthcare service(s) or assessing the health status of a patient.

#### 2.3 Diagnosis Codes Part 1
Diagnosis is a key piece of information that connects so much of the encounter experience together.
ICD10: International Classification of Deseases 10
ICD10-CM: International Classification of Deseases 10 - Clinical Modification. Medical claims, disease epidemic and mortality tracking
Changing ICD9 (XXX.XX) -> ICD10 (XXX.XXX X).

ICD10-CM format

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

#### 2.8 Procedure Codes
Categorization of the medical codes during an encounter
- ICD-10-PCS (Procedure Code System) [Reference](https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2014-pcs-procedure-coding-system.pdf)
    - Only for Inpatient;
Focus on medical and surgical;
- Current Procedural Terminology (CPT) [Reference](https://www.aapc.com/resources/medical-coding/cpt.aspx)
    - Focus in Outpatient but applicable to physician visits in ambulatory settings;
    - Focus on professional services by physician;
- Healthcare Common Procedure Coding System (HCPCS) [Reference](https://en.wikipedia.org/wiki/Healthcare_Common_Procedure_Coding_System)
    - Inpatient and Outpatient;
    - Three levels: L1 is the CPT codes, L2 Non-physician services and L3 Medicare/Medicadin related

The ICD10-PCS Codes
- 7 alphanumeric characters
- 1st character is the Section
- Subsequent characters relate to the Section and give: Body System, Body Part, Approach, Device used for a procedure

Example: 027004Z
- 0 = Medical
- 2 = Heart and Great Vessels
- 7 = Dilatation
- 0 = Coronay Artery, One Site
- 0 = Open approach
- 4 = Drug-eluting Intraluminal Device
- Z = No Qualifier

The CPT Codes 
- Up to 5 numbers
- 3 Categories: 
    - Category 1: Billable Codes
    - Category 2:
        - Five digits ending in F
        - Non-billable
        - Performance measure focused on physicals and patient history
    - Category 3:
        - Services and procedures using emerging technology

Generally focusing in first two categories

#### 2.9 and 2.10
Exercises

#### 2.11 Medication Codes

National Drug Code (NDC), maintained by FDA [Reference](https://ndclist.com/)

NDC Structure
- 10 or 11 digits
- Three parts
    - Labeler: Drug Manufacturer;
    - Product Code: drug details;
    - Package Code: form and size of medication;

Example: 50242-917-01
- 50242 = Genentech, Inc
- 917 = Non-proprietary name and formulation: ATEZOLIZUMAB 1200 mg/20mL
- 01 = 1 vial, single-use in 1 carton: 14 ml in 1 vial, single-use of Tecentriq

Crosswalk: connection betwwen two different code sets or versions of drugs in the same code set
NDC codes can be connected to HCPCS codes.
A common challenge with NDC is to group codes by common types of drugs.

NXNorm [Reference](https://www.nlm.nih.gov/research/umls/rxnorm/overview.html)
Normalized naming system to solve NDC problems. 

#### 2.12 Grouping/Categorizing Systems

Clinical Cassifications Software (CCS)
Created to meaningful categorize ICD10 PCS codes. Maps diagnosis or procedure codes from ICD code sets.
- Single-Level Categories
    - Mutually exclusive categories;
    - 285 categories for diagnoses
    - 231 categories for procedures
    - Examples:
        - Operations on the cardiovascular system are codes 43-63
        - Heart valve procedure is code 43
- Multi-Level Categories
    - Helpful for more detailed analysis and more granular level grouping. 
    - 4 level for diagnosis codes and 3 levels for procedures
    - Example:
        - 7.1.2.1 = Hypertensive heart and/or renal disease

- CCS ICD10-PCS Category Mapping File
    - CCS presents and overview, description, guidance and downloading information such as the [CCS ICD10-PCS Category Mapping File in csv](https://www.hcup-us.ahrq.gov/toolssoftware/ccs10/ccs10.jsp#download)
        - .csv is the CCS IDC10-PCS Category Mapping File
        - .sas is an ASCII file to be used in Statistical Analysis Software (SAS)
        - .pdf is an guide that explains how to download and apply the CCS to ICD10-PCS
    - Mapping has 8 columns
        - ICD-10-PCS CODE: Procedure Code
        - CCS CATEGORY
        - ICD-10-PCS CODE DESCRIPTION
        - CCS CATEGORY DESCRIPTION
        - MULTI CCS LVL 1: Multi-level 1 Category 
        - MULTI CCS LVL 1 LABEL: Multi-level 1 Category Description 
        - MULTI CCS LVL 2: Multi-level 2 Category 
        - MULTI CCS LVL 2 LABEL: Multi-level 2 Category Description  