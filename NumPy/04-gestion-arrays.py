import numpy as np

arr = np.arange(5, 50, 5)

print(arr[0])
print(arr[-1])
print(arr[::-1])
print(arr[-5:])
print(arr[:3])
arr[-1]=99

print(arr)


arr = np.arange(0, 30, 3)

print("-----------------")
print(arr)
sub_arr=arr[0:4]
print(sub_arr)
sub_arr[:4]=55
print(arr)
arr = np.arange(0, 30, 3)

print("-----------------")
print(arr)
sub_arr=arr[0:4].copy()
print(sub_arr)
sub_arr[:4]=55
print(arr)
print(sub_arr)
