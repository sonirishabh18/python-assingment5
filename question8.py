import pandas as pd

df1 = pd.DataFrame({
    "StudentID":[1,2,3],
    "Name":["A","B","C"],
    "Department":["AI","CSE","ECE"]
})

df2 = pd.DataFrame({
    "StudentID":[1,2,3],
    "Grade":["A","B","A"]
})

result = pd.merge(df1,df2,on="StudentID")

print(result[result["Grade"]=="A"])
