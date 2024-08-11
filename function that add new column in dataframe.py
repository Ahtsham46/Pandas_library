import pandas as pd
def new_dataFrame(df,column_name,calculted_fu):
    df[column_name] = calculted_fu(df)
    return df
def calculateed_fu(df):
    return df['age'] * 12
df = pd.DataFrame({
    'name': ['ALi', 'Usman', 'Ahtsham', 'Noor'],
    'age': [21, 23, 20, 19],
    'dpt': ['SE', 'LAW', 'CS', 'DNS']
})
new_dataFrame_with_column = new_dataFrame(df,'Age in months', calculateed_fu)
print(new_dataFrame_with_column)