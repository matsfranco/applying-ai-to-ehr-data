import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_distributions(df, c, chartType):
    df[c].value_counts().plot(kind=chartType)
    plt.show()
    plt.close()

def check_null_values(df):
    null_df = pd.DataFrame({'columns': df.columns, 
                            'percent_null': df.isnull().sum() * 100 / len(df), 
                           'percent_zero': df.isin([0]).sum() * 100 / len(df),
                           'percent_miss': df.isin(['?']).sum() * 100 / len(df)
                           } )
    return null_df 

def create_cardinality_feature(df):
    num_rows = len(df)
    random_code_list = np.arange(100, 1000, 1)
    return np.random.choice(random_code_list, num_rows)
    

numerical_feature_list = ['age',  'trestbps', 'chol', 'thalach', 'oldpeak' ]
categorical_feature_list = [ 'sex', 'cp', 'restecg', 'exang', 'slope', 'ca', 'thal']

processed_switzerland_path = "./data/processed.switzerland.data"
column_header_list = [
    'age',
    'sex',
    'cp',
    'trestbps',
    'chol',
    'fbs',
    'restecg',
    'thalach',
    'exang',
    'oldpeak',
    'slope',
    'ca',
    'thal', 
    'num_label'
]
processed_switzerland_df = pd.read_csv(processed_switzerland_path, names=column_header_list)

print('Head of file content: ')
print(processed_switzerland_df.head())

################################
# ANALIZING VALUE DISTRIBUTION #
################################

## A.
numerical_feature_list = ['age',  'trestbps', 'chol', 'thalach', 'oldpeak' ]

## B.

null_df = check_null_values(processed_switzerland_df)
print('Missing Values:')
print(null_df)
#chol may be zero due to a pipeline problem or problems in acquire this data

## C. 

example_column2 = "cp"
print("Distribution for {} feature".format(example_column2))
visualize_distributions(processed_switzerland_df, example_column2, 'bar')
sns.countplot(processed_switzerland_df['cp'])

## D
sns.boxplot(y=processed_switzerland_df['age'])
plt.show()

## E

def count_unique_values(df, cat_col_list):
    cat_df = df[cat_col_list]
    val_df = pd.DataFrame({'columns': cat_df.columns, 
                       'cardinality': cat_df.nunique() } )
    return val_df

categorical_feature_list = [ 'sex', 'cp', 'restecg', 'exang', 'slope', 'ca', 'thal']
val_df = count_unique_values(processed_switzerland_df, categorical_feature_list) 
print(val_df)