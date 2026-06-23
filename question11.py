import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = {
    "Age": np.random.randint(22,50,50),
    "Salary": np.random.randint(20000,100000,50),
    "Experience": np.random.randint(1,20,50),
    "Department": np.random.choice(["AI","CSE","ECE"],50)
}

df = pd.DataFrame(data)

sns.scatterplot(x="Age", y="Salary", hue="Department", data=df)
plt.show()

sns.heatmap(df[["Age","Salary","Experience"]].corr(), annot=True)
plt.show()

sns.barplot(x="Department", y="Salary", data=df)
plt.show()
