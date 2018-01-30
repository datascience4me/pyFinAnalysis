import numpy as np

# 1) array of ten zeos
zeros = np.zeros(10)
#print(zeros)

# 2) array of ten ones
ones = np.ones(10)
#print(ones)

# 3) ten fives
fives = np.ones(10) * 5
#print(fives)

# 4) integers from 10 to 50
ten_to_fifty = np.arange(10, 51)
#print(ten_to_fifty)

# 5) integers from 10 to 50 evens
ten_to_fifty_even = np.arange(10, 51, 2)
#print(ten_to_fifty_even)

# 6) 3 X 3 Matrix
mat = np.arange(0,9).reshape(3,3)
#print(mat)

# 7) 3X3 identical mat
mat_id = np.eye(3, 3)
#print(mat_id)

# 8) random no 0-1
x = np.random.rand(1)
#print(x)

# 9) 25 random nos from st.normal distribution

rand_ = np.random.rand(25)
#print(rand_)

# 10) matrix  from 0.01 to 1 by 0.01 increments
matrix = np.arange(1, 101).reshape(10,10)/100
# or
#print(matrix)

#11) 20 nos lineary space 0-1:
lnspace = np.linspace(0,1,10)
#print(lnspace)

# 12) indexing
mat_ind = np.arange(1,26).reshape(5,5)
# print(mat_ind)
# print('=' * 40)
# print(mat_ind[2:, 1:])
# print(mat_ind[-2,-1])
# print(mat_ind[0:3, 1])
# print(mat_ind[0:3, 1:2])    #notice the different formatting
# print(mat_ind[-1])
# print(mat_ind[3:])
# print(np.sum(mat_ind))
# print(np.std(mat_ind))
# print(np.sum(mat_ind, axis=0))  # 0 = rows; 1 = columns!

# bonus = same no
seed_no = np.random.seed(101)
seed_no = np.random.rand(1)
print(seed_no)
