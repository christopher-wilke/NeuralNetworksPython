import numpy as np

# Row Vector
a = [1, 2, 3]
print(np.array([a]))

# Column Vector
b = [2, 3, 4]
b = np.array([b]).T
print(b)

print(np.dot(a, b))
