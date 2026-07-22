import pandas as pd
import os
print(os.getcwd())   # Shows the folder Python is running from

df = pd.read_excel('week4\capstone.xlsx')

# overview
print(df.head())
print(df.info())
print(df.describe())

# check for missing values
print(df.isnull().sum()) #53 missing discount band values
df.loc[df['Discounts'] == 0, 'Discount Band'] = 'None'
print(df.isnull().sum()) #0

# duplicates
df = df.drop_duplicates()

# after cleaning, check the data again
print(df.head())
print(df.info())
print(df.describe())

# save cleaned data
df.to_csv('week4\capstone_cleaned.csv', index=False)