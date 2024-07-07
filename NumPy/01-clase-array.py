import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
array = np.array([1,2,3,4,5])

print(array)

print(array.ndim)
print(array.shape)

array = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
])

print(array)

print(array.ndim)
print(array.shape)

array = np.array([1,2,3,4,5, 6.1234])
print(array.dtype)
print(array)

array = np.array(["Hola", "que", "tal"])
print(array.dtype)
array = np.array(["Hola", "que", "tal", 2])
print(array.dtype)
array = np.array(["Hola", "que", "tal", 2, 3.1234])
print(array.dtype)
print(array)


tabla = pd.DataFrame(
    np.random.randint(1,100, size=(4,3)),
    columns=['Pepe', 'María', 'Juan']
)

tabla.plot()
plt.show()