import pandas as pd
import numpy as np

# Data from https://data.chhs.ca.gov/dataset/hospital-inpatient-diagnosis-procedure-and-external-cause-codes
# 2018 Hospital Inpatient - Diagnosis Code Frequency

columnList = ['ProcedureCode','ProcedureDesc','TotalProc','PrimaryProc','SecondProc']
dataPath = "./data/IDC-10-PCS-Table.csv"

proceduresDF = pd.read_csv(dataPath, names=columnList,sep=';').fillna(0)[:-1]
print(proceduresDF.head())

def calculateGroupingPercetage(columnName,codeList,total,dataFrame) :
    percentages = []
    for code in codeList:
        groupingItems = dataFrame[dataFrame[columnName].str.startswith(code)]
        totalSumGroupingItems = sum(groupingItems['SecondProc'].astype(int))
        percentage = totalSumGroupingItems/total
        percentages.append(percentage)
    return percentages

def getGreaterPercentageGroup(codes, percentages):
    maxValue = max(percentages)
    maxIndex = percentages.index(maxValue)
    return list(codes)[maxIndex], maxValue


# 1. Give the codes that have 'CORONARY ARTERY' in the description
coronaryArteryProcs = proceduresDF[proceduresDF['ProcedureDesc'].str.contains('CORONARY ARTERY')]
print('\n1. ICD-10 PCS Codes which contains \'CORONARY ARTERY\' in description:')
print(coronaryArteryProcs['ProcedureCode'])

# 2. What percentage of cases that have 'CORONARY ARTERY' in their description have primary procedure 
# codes that could be grouped at the B category level?
totalCoronaryArteryProcsInFirstProc = sum(coronaryArteryProcs['PrimaryProc'].astype(int))
print('totalCoronaryArteryProcsInFirstProc: '+str(totalCoronaryArteryProcsInFirstProc))
coronaryArteryProcsStartingWithB = coronaryArteryProcs[coronaryArteryProcs['ProcedureCode'].str.startswith('B')]
totalCoronaryArteryProcsInFirstProcStartsWithB = sum(coronaryArteryProcsStartingWithB['PrimaryProc'].astype(int))
print('totalCoronaryArteryProcsInFirstProcStartsWithB: '+str(totalCoronaryArteryProcsInFirstProcStartsWithB))
precentStartsWithBOverTotal = totalCoronaryArteryProcsInFirstProcStartsWithB/totalCoronaryArteryProcsInFirstProc
print('Percent of Procs which starts with B in CORONARY ARTERY Procs: '+str(precentStartsWithBOverTotal))

# 3. What is the highest percentage grouping you can make with 3 characters for the secondary procedure code?
totalCoronaryArteryProcsInSecondProc = sum(coronaryArteryProcs['SecondProc'].astype(int))
threeCharsCodes = set(coronaryArteryProcs['ProcedureCode'].str[0:3])
groupingPercentages = calculateGroupingPercetage('ProcedureCode',threeCharsCodes,totalCoronaryArteryProcsInSecondProc,coronaryArteryProcs)
greaterPercentageGroup = getGreaterPercentageGroup(threeCharsCodes,groupingPercentages)
print('Greater percentage group: '+str(greaterPercentageGroup))