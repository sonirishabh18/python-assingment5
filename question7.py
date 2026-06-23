import pandas as pd

df = pd.read_csv("sales.csv")

print(df.groupby("Category")["Sales"].sum())

print(df.sort_values("Sales",ascending=False).head(3))
