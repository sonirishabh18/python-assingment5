import pandas as pd

data = {
    "Name":["A","B","C","D","E","F","G","H","I","J"],
    "Age":[18,19,20,18,21,19,20,18,22,19],
    "Marks":[78,65,89,45,91,72,85,66,95,80],
    "City":["Jaipur","Jodhpur","Pilani","Delhi","Ajmer","Kota","Pune","Mumbai","Jalore","Udaipur"]
}

df = pd.DataFrame(data)

print(df.describe())

print(df[df["Marks"]>75])

print(df.sort_values("Marks",ascending=False))
