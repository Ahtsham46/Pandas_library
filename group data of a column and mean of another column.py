import pandas as pd
df = pd.DataFrame({
    'name': ['ALi', 'Usman', 'Ahtsham', 'Noor'],
    'age': [21, 23, 20, 19],
    'dpt': ['SE', 'LAW', 'CS', 'DNS'],
    'score': [88, 92, 85, 78]
})
grouped = df.groupby('dpt').mean('score')
print(grouped)