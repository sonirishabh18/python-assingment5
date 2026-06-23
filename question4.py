import numpy as np

a = np.linspace(1,10,5)
b = np.zeros((1,5))
c = np.ones((1,5))

d = np.vstack((a,b,c))

print(d)
