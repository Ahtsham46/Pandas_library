import pandas as pd
import numpy as np
dict  = {
    "name":["Ali","Usman","Sana","Mariya"],
    "marks": [67,78,98,44],
    "city": ["lahore", "Multan", "Karachi", "Lahore"]
}
df = pd.DataFrame(dict)
print(df.head(2))
print(df.tail(2))
print(df.describe())