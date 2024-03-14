# notes from quiz, course one, week 3, shallow neural networks:

import numpy as np

x = np.random.rand(3,2)
# print(x)



y = np.sum(x, axis=0, keepdims=True)  

print(x, '\n\n', y)

print() 

print(x.shape, y.shape)  # (3,2) (3,2)

print()

a = np.random.rand(3,2)
y = np.sum(x, axis=1, keepdims=True)
print(x, '\n\n', y, y.shape)  # y.shape is (3, 1) since we summed over the rows and kept the dimensions 

# received 100% on the quiz clear

