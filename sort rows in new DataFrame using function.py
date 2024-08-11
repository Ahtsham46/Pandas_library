import pandas as pd
def sort_dataframe(df,column_name):
    sorted_df = df.sort_values(by=column_name, ascending = True)
    return sorted_df
df = pd.DataFrame({
    'name': ['ALi', 'Usman', 'Ahtsham', 'Noor'],
    'age': [21, 23, 20, 19],
    'dpt': ['SE', 'LAW', 'CS', 'DNS']
})
sorted_df = sort_dataframe(df, 'age')
print(f'Original DataFrame:\n{df.to_string(index=False)}\n')
print(f'Sorted DataFrame:\n{sorted_df.to_string(index=False)}')
    