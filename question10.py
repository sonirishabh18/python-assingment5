import matplotlib.pyplot as plt

marks = [80,75,90,85,70,60,95,88]

plt.hist(marks)
plt.show()

plt.boxplot(marks)
plt.show()

x = [40,35,25]

plt.pie(x,labels=["A","B","C"])
plt.show()
