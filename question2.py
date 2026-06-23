import numpy as np

a = np.arange(1,17).reshape(4,4)

print(a)

print("Diagonal Elements:")
print(np.diag(a))

a[a%2==0] = 0
print("Even numbers replaced with 0:")
print(a)

print("Index of Maximum Value:")
print(np.argmax(a))
