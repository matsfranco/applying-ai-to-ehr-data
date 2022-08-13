import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt

processed_cleveland_path = "./data/processed.cleveland.data"
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
processed_cleveland_df = pd.read_csv(processed_cleveland_path, names=column_header_list)
print(processed_cleveland_df.head())

