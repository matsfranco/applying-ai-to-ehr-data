import pandas as pd
import numpy as np

code_list = ["02C24ZZ", "02C33Z6", "D2C33ZZ", "Z2C34Z6", "D2C34ZZ", "4A020N6"]
description_list = ["Percutaneous transluminal angioplasty", "Percutaneous transluminal coronary angioplasty",
"Percutaneous transluminal angioplasty", "Percutaneous transluminal angioplasty", "Percutaneous transluminal angioplasty",
"Diagnostic cardiac catheterization; coronary" ]

sample_df = pd.DataFrame({"sample_code": code_list, "code_description": description_list})

print(sample_df)

# 1. Searching for codes with text pattern
print('\n1. Searching for codes with text pattern')
matched_string_df = sample_df[sample_df['code_description'].str.contains('angioplasty')]
print(matched_string_df)
print('Unmatched row:')
unmatched_string_df = sample_df[~sample_df['code_description'].str.contains('angioplasty')]
print(unmatched_string_df)

# 2. Grouping by Character
print('\n2. Grouping by Character')
print('Grouping by First Char: 4')
first_char_group_df = sample_df[sample_df['sample_code'].str.startswith('4')]
print(first_char_group_df)
print('Grouping by Two Firsts Char: D2')
two_char_group_df = sample_df[sample_df['sample_code'].str.startswith('D2')]
print(two_char_group_df)