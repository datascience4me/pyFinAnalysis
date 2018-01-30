import numpy as np

arr = np.arange(0,11)
#print(arr[8])

# Broadcasting!! -> different from indexing, unique to arrays

arr[0:5] = 100      #broadcasting! cant be done with lists!
#print(arr)

# indexing 2-d arrays = matrices
# mat [row, column] or mat[row][column]

mat = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(mat)
print('=' * 40)
print(mat[0])   # row with index 0!
print(mat[1,1]) # 25!!!
print(mat[0:2, 1:])

# you will using pandas indexing more -> conditional selection (<>)!!
print('=' * 40)
arr2 = np.arange(1,11)
bool_arr = arr > 4
print(bool_arr)
arr2 = arr2>4
print(arr2)
