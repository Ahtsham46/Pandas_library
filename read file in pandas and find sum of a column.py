import pandas as pd
df = pd.read_csv("student.csv", index_col=0)
print(f'File Data is:\n {df}')
print(f'Sum of  age column in file is :', sum(df['age']))