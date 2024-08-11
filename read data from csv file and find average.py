import pandas as pd
import csv
average = pd.read_csv('student.csv',)
average_age = average['age'].mean()
print(f'Data is\n{average}')
print(f'Average of age is: {average_age}')