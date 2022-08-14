import pandas as pd
import numpy as np

# Data from https://www.hcup-us.ahrq.gov/toolssoftware/ccs10/ccs10.jsp#download

columnList = [
    'ICD-10-PCS_CODE',
    'CCS_CATEGORY',
    'ICD-10-PCS_CODE_DESCRIPTION',
    'CCS_CATEGORY_DESCRIPTION',
    'MULTI_CCS_LVL_1',
    'MULTI_CCS_LVL_1_LABEL',
    'MULTI_CCS_LVL_2',
    'MULTI_CCS_LVL_2_LABEL'
]

dataPath = "./data/ccs/ccs_pr_icd10pcs_2020_1.csv"

proceduresDF = pd.read_csv(dataPath, names=columnList).fillna(0)[:-1]
print(proceduresDF.head())

# 1. If you search the CCS_CATEGORY_DESCRIPTION for "coronary", what are the two 
# single level categories that you find? What is/are the label(s) for the multi-level 1 categories?
coronaryProcs = proceduresDF[proceduresDF['CCS_CATEGORY_DESCRIPTION'].str.contains('coronary')]
print('\n1. MULTI_CCS_LVL_1 which contains \'coronary\' in CCS_CATEGORY_DESCRIPTION: ')
print('Single level categories: '+ str(coronaryProcs.CCS_CATEGORY.unique()))
print('Single level categories description: '+ str(coronaryProcs.CCS_CATEGORY_DESCRIPTION.unique()))
print('Label for Multi-Level 1 Category: '+ str(coronaryProcs.MULTI_CCS_LVL_1_LABEL.unique()))

# 2. Given CCS single level category 45, what do you notice about the ICD10 PCS Codes? 
# Do they all have a similar character pattern?
cat45Procs = proceduresDF[proceduresDF['CCS_CATEGORY'].str.contains('45')]
cat45ProcsICD10CodesOneDig = set(cat45Procs['ICD-10-PCS_CODE'].str[1:2])
cat45ProcsICD10CodesTwoDig = set(cat45Procs['ICD-10-PCS_CODE'].str[1:3])
cat45ProcsICD10CodesThreeDig = set(cat45Procs['ICD-10-PCS_CODE'].str[1:4])
cat45ProcsICD10CodesFourDig = set(cat45Procs['ICD-10-PCS_CODE'].str[1:5])
print('One Digit: '+str(cat45ProcsICD10CodesOneDig))
print('Two Digit: '+str(cat45ProcsICD10CodesTwoDig))
print('Three Digit: '+str(cat45ProcsICD10CodesThreeDig))
print('Four Digit: '+str(cat45ProcsICD10CodesFourDig))
# All of them start with Zero