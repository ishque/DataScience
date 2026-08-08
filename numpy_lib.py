import numpy as np
a = np.array([1,3,4,5,6])
print(a)
#2D
b = np.array([[1,2,3,4],[5,6,7,8]])
print(b)

c = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(c)
print(a.shape)
d=np.array([1,0,3,4], dtype=bool)
print(d)

#np.arange
a1=np.arange(1,11)
print(a1)

#======>with reshape
a2 = np.arange(24).reshape(6,4)
print(a2)
a3 = np.array([1,2,3,4,5,6,7,8,9, 10])
print(a3)

a4 = np.zeros(20)
print(a4)

a5 = np.ones(16).reshape(4,4)
print(a5)
even_arr = np.arange(2,51)
print(even_arr[even_arr % 2 == 0])

arr = np.array([15,25,35,45,55])


arr = np.array([5, 10, 15, 20, 25, 30])
print(arr*2)
arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
np.put(arr1,[arr1 % 2==0],[0])
print(arr1)

arr5 = np.arange(1, 17).reshape(4,4)
print(arr5)
#print(arr5[:,:,1])
print(np.flipud(arr5).diagonal())


arr = np.array([12, 5, 8, 20, 15, 30])

result = np.where((arr > 10) & (arr % 2 == 0), arr * 10, arr)
print(result)
#print(arr > 10 )
#print(arr[arr % 2 == 0])
arr = np.array([10, 15, 20, 25, 30, 35, 40])

arr[arr%2 == 1] = -1
print(arr)

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

arr1 = np.array([[100]])
print(arr+arr1)
import matplotlib.pyplot as plt
x = np.linspace(-10,10, 100)
y = x
plt.plot(x,y)
def sigmoid(array):
    return 1/(1+np.exp(-(array)))
a = np.arange(10)
print(sigmoid(a))