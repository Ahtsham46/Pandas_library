import pandas as pd 
import numpy as np

#create data
data = {
    'name' : ['Ali', 'Ahtsham', 'Khurram', 'Ayesha'],
    'age' :[23, 22, 26, 21],
    'City' : ['Lahore', 'Multan', 'Lahore', 'Multan']
}
df = pd.DataFrame(data) # DataFrame word is used to give a shape to data like excel sheet.
print("Original DataFrame:")
print(df)

# Reading and Writing Data
df.to_csv('student.csv', index=False)  # convert data into csv file
df_read = pd.read_csv('student.csv') # read from file
print("\nDataFrame read from CSV:")
print(df_read)

# Selecting Data
print("\nSelecting 'Name' and 'Age' columns:")
print(df[['name', 'age']])
print("\nSelecting rows where Age > 22:")
print(df[df['age'] > 22])

# Adding a new column
df['salary'] = [70000, 90000, 70000, 85000]
print("\nDataFrame with salary column added:")
print(df)

# Updating Data
df.loc[df['name'] == 'Ali', 'City'] = 'Islamabad'
print("\nDataFrame after updating Ali's city:")
print(df)

# Deleting Data
df = df.drop(columns=['salary'])
print("\nDataFrame after dropping salary column:")
print(df)

# Handle mising Data
df.loc[2, 'age'] = np.nan
print("\nDataFrame with missing value in Age column:")
print(df)
print("\nDataFrame after filling missing value in Age column with mean:")
df['age'] = df['age'].fillna(df['age'].mean())
print(df)