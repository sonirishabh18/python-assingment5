import matplotlib.pyplot as plt

x = [10,20,30,40,50]

fig, ax = plt.subplots(2,2)

ax[0,0].plot(x)
ax[0,0].set_title("Line Plot")

ax[0,1].scatter([1,2,3,4,5], x)
ax[0,1].set_title("Scatter Plot")

ax[1,0].bar([1,2,3,4,5], x)
ax[1,0].set_title("Bar Chart")

ax[1,1].hist(x)
ax[1,1].set_title("Histogram")

plt.suptitle("Data Visualization")
plt.show()
