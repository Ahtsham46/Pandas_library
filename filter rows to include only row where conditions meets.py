import pandas as pd

def filter_dataframe(df, column_name, condition):
    filtered_df = df[condition(df[column_name])]
    return filtered_df
df = pd.DataFrame({
    'name': ['ALi', 'Usman', 'Ahtsham', 'Noor'],
    'age': [21, 23, 20, 19],
    'dpt': ['SE', 'LAW', 'CS', 'DNS']
})
filtered_df = filter_dataframe(df, 'age', lambda x: x > 19)
print(f'Original DataFrame:\n{df.to_string(index=False)}\n')
print(f'Filtered DataFrame (age > 20):\n{filtered_df.to_string(index=False)}')
