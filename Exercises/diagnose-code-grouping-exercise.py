import pandas as pd
import numpy as np

# Data from https://data.chhs.ca.gov/dataset/hospital-inpatient-diagnosis-procedure-and-external-cause-codes
# 2018 Hospital Inpatient - Diagnosis Code Frequency


columnList = ['ICD10CMCODE','DiagnosisDesc','TotalDiag','PrimaryDiag','SecondDiag']
dataPath = "./data/IDC-10-CM-Table.csv"

diagnosisDF = pd.read_csv(dataPath, names=columnList,sep=';').fillna(0)[:-1]
print(diagnosisDF.head())

# 1. Give the codes that have 'SEPSIS" in the description
sepseDiagnosis = diagnosisDF[diagnosisDF['DiagnosisDesc'].str.contains('SEPSIS')]
print('ICD10-CM CODE which contains SEPSE:')
print(sepseDiagnosis['ICD10CMCODE'])

# 2. What percentage of primary diagnosis can be grouped at the category level with A41?
diagnosesWithA41 = diagnosisDF[diagnosisDF['ICD10CMCODE'].str.startswith('A41')]
print(diagnosesWithA41['ICD10CMCODE'])
totalA41AsPrimaryDiag = sum(diagnosesWithA41['PrimaryDiag'].astype(int))
print('Total A41 Starting Code as primary diagnosis: '+str(totalA41AsPrimaryDiag))
totalSepsisPrimaryDiag = sum(sepseDiagnosis['PrimaryDiag'].astype(int))
print('Total SEPSIS as primary diagnosis: '+str(totalSepsisPrimaryDiag))
percentA41OverSepsis = totalA41AsPrimaryDiag/totalSepsisPrimaryDiag
print('Percentage of A41 over SEPSIS: '+str(percentA41OverSepsis))

# 3. If you were to create a metacategory for sepsis, what percentage of secondary diagnosis 
# codes would be grouped with using just the first character?
secondaryDiagnosisGroupingByA = sepseDiagnosis[sepseDiagnosis['ICD10CMCODE'].str.startswith('A')]
totalASecDiagGroup = sum(secondaryDiagnosisGroupingByA['SecondDiag'].astype(int))
print(str(totalASecDiagGroup))
totalSepsisSecDiagGroup = sum(sepseDiagnosis['SecondDiag'].astype(int))
print(str(totalSepsisSecDiagGroup))
percentAOverSepsisSecDiag = totalASecDiagGroup/totalSepsisSecDiagGroup
print('Percentage of \'A\' over SEPSIS: '+str(percentAOverSepsisSecDiag))
