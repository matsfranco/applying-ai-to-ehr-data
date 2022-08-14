import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt

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
processed_swiss_df = pd.read_csv(processed_switzerland_path, names=column_header_list)
print(processed_swiss_df.head())

demo_features = ['sex',  'age', 'num_label' ]
demo_df = processed_swiss_df[demo_features]


## Convert age to bins
age_bins = [0, 18, 25, 39, 54, 65, 90]
a_bin = [str(x) for x in age_bins]
age_labels = ["".join(x) for x in zip( [x + " - " for x in a_bin[:-1]], a_bin[1:])]
demo_df['age_bins'] = pd.cut(demo_df['age'], bins=age_bins, labels=age_labels)
print(demo_df)

# Age Bin Grouping
ax = sns.countplot(x="age_bins", data=demo_df)
plt.show()

# Age Bin and Gender Grouping
ax = sns.countplot(x="age_bins", hue="sex", data=demo_df)
plt.show()

#

g = sns.catplot(x="age_bins", hue="sex", col="num_label", data=demo_df, kind="count", height=4,aspect=1.9)
plt.show()
