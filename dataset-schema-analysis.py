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
                           'percent_zero': df.isin([0]).sum() * 100 / len(df)
                           } )
    return null_df 

def create_cardinality_feature(df):
    num_rows = len(df)
    random_code_list = np.arange(100, 1000, 1)
    return np.random.choice(random_code_list, num_rows)
    
def count_unique_values(df, cat_col_list):
    cat_df = df[cat_col_list]
    cat_df['principal_diagnosis_code'] = create_cardinality_feature(cat_df)
    #add feature with high cardinality
    val_df = pd.DataFrame({'columns': cat_df.columns, 
                       'cardinality': cat_df.nunique() } )
    return val_df


numerical_feature_list = ['age',  'trestbps', 'chol', 'thalach', 'oldpeak' ]
categorical_feature_list = [ 'sex', 'cp', 'restecg', 'exang', 'slope', 'ca', 'thal']

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

print('Head of file content: ')
print(processed_cleveland_df.head())

################################
# ANALIZING VALUE DISTRIBUTION #
################################

## Sex Distribution
example_column1 = 'sex'
print("Distribution for {} feature".format(example_column1))
print('Replacing 0\'s and 1\'s by female and male, respectively ')
processed_cleveland_df[example_column1] = processed_cleveland_df[example_column1].replace({1:"Male",0:"Female"})
#visualize_distributions(processed_cleveland_df, example_column1, 'bar')

## Type Distribution
example_column2 = "cp"
print("Distribution for {} feature".format(example_column2))
print('Replacing values... 1: \"Typical Angina\", 2: \"Atypical Angina\", 3: \"Non-anginal Pain\", 4: \"Asymptomatic\"')
processed_cleveland_df[example_column2] = processed_cleveland_df[example_column2].replace({1: "Typical Angina",
2: "Atypical Angina",
3: "Non-anginal Pain",
4: "Asymptomatic" })
#visualize_distributions(processed_cleveland_df, example_column2, 'barh')

##############################################
# REVIEW OF NORMAL AND UNIFORM DISTRIBUTIONS #
##############################################

## Normal Distribution
mu, sigma = 100, 17.0 #mean and standard deviation
norm_dist = np.random.normal(mu,sigma, 100) 
norm_ax = sns.displot(norm_dist,kde=False)
#plt.show()

## Uniform Distribution
uniform_dist = np.random.uniform(-1,0,1000)
uniform_ax = sns.displot(uniform_dist, kde=False )
#plt.show()

############################
# SCALING & MISSING VALUES #
############################

## Scaling of numerical features

#print(processed_cleveland_df[numerical_feature_list].describe())

# Missing Values
null_df = check_null_values(processed_cleveland_df)
#print(null_df)
plt.show()

############
# OUTLIERS #
############
sns.boxplot(y=processed_cleveland_df['age'])
plt.show()
sns.boxplot(y=processed_cleveland_df['chol'])
plt.show()

####################
# HIGH CARDINALITY #
####################
val_df = count_unique_values(processed_cleveland_df, categorical_feature_list) 
#print(val_df)

########################
# DEMOGRAPHIC ANALYSIS #
########################

demo_features = ['sex',  'age' ]
demo_df = processed_cleveland_df[demo_features].replace({1:"male", 0:"female"})
#convert age to bins
age_bins = np.arange(0, 90, 10)
a_bin = [str(x) for x in np.arange(0, 90, 10) ]
age_labels = ["".join(x) for x in zip( [x + " - " for x in a_bin[:-1]], a_bin[1:])]
demo_df['age_bins'] = pd.cut(demo_df['age'], bins=age_bins, labels=age_labels)
print(demo_df)
ax = sns.countplot(x="age_bins", data=demo_df)
plt.show()
ax = sns.countplot(x="age_bins", hue="sex", data=demo_df)
plt.show()