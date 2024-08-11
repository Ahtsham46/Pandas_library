import pandas as pd
df = pd.read_csv("student.csv", index_col=0)
print(f'File Data is:\n {df}')
print(f'Maximum age in file is :', max(df['age']))
print(f'Minimum age in file is :', min(df['age']))