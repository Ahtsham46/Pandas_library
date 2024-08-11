import pandas as pd
def transpos(df):
    df_transposed = df.T
    return df_transposed
df = pd.DataFrame({
    'name': ['Ali', 'Usman', 'Ahtsham', 'Noor'],
    'age': [21, 23, 20, 19],
    'dpt': ['SE', 'LAW', 'CS', 'DNS']
})
print("Original DataFrame:")
print(df)
print("\nTransposed DataFrame:")
transposed = transpos(df)
print(transposed)
