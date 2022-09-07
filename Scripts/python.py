### import packages
import pandas as pd
import datetime as dt
import uuid
import numpy as np

### load data into python 
df = pd.read_csv('data/School_Learning_Modalities.csv')

### get count of rows and columns
df.shape

### list names of columns 
list(df)

### clean column names
# remove special characters and white space ' ' from column names
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')
list(df)
# replace whitespace ' ' with underscore '_'
df.columns = df.columns.str.replace(' ', '_')
list(df)
# change column names to all lowercase
df.columns = df.columns.str.lower()
list(df)

### cleaning strings within each column
# get list of column types
df.dtypes
# identify columns with strings 
df_strings = df.select_dtypes('object').columns
df_strings
# remove special characters & whitespace ' ' 
df['district_name'] = df['district_name'].str.replace('[^A-Za-z0-9]+', '_')
df['week'] = df['week'].str.replace('[^A-Za-z0-9]+', '_')
df['learning_modality'] = df['learning_modality'].str.replace('[^A-Za-z0-9]+', '_')
df['city'] = df['city'].str.replace('[^A-Za-z0-9]+', '_')
df['state'] = df['state'].str.replace('[^A-Za-z0-9]+', '_')

### convert columns to appropriate types
df['week'] = pd.to_datetime(df['week'])

### Identify duplicates and remove
df.duplicated(keep='first')
df.drop_duplicates(keep='first')

### Assess missingness
# count of missing values from each column
df.isnull().sum()
# relace blank '' or whitespace ' ' cells with NaN
df.replace(to_replace='', value=np.nan, inplace=True)
df.replace(to_replace=' ', value=np.nan, inplace=True)

### Create new column called modality_inperson based on old column learning-modality, where true is in person and false is remote or hybrid
df['modality_inperson'] = (df['learning_modality'].apply(lambda x: 'true' if x == 'in_person' else 'false'))


### upload clean data
df.to_csv('data/School_Learning_Modalities_Clean.csv')