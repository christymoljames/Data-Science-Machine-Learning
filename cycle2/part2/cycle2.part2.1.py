import numpy as np  
import random
t = np.random.randint(low = 0, high = 10, size = (4,3))
print("The randint square matrix")
print(t)
cube = np.power(t, 3)
print("the power cube")
print(cube)
multiply = np.multiply(t,(t*t))
print("the multiply cube")
print(multiply)
print("single star")
star = t*t*t
print(star)
doublestar = t**3
print("double star printing")
print(doublestar)