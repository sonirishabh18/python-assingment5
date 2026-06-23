import pandas as pd
import numpy as np

data = {
    "Name":["A","B","C","D"],
    "Marks":[80,np.nan,70,np.nan],
    "City":["Jaipur",np.nan,"Delhi",np.nan]
}

df = pd.DataFrame(data)

print(df.isnull())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df = df.dropna(subset=["City"])

print(df)
