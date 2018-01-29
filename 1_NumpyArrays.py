import numpy as np
'''
vectors = 1d arrays
matrix = 2d + arrays (but it can have only one)
'''
def convertArrays():
    my_list = [1,2,3]
    x = np.array(my_list)
    print(type(x))

    print('=' * 40)

    my_matrix = [[1,2,3], [4,5,6], [7,8,9]]
    y = np.array(my_matrix)
    print(type(y))
    print(y)
#convertArrays()

def createArrays():
    # in finance you rarely need more than 2d arrays
    print('=' * 40)
    # create random arrays:
    z = np.arange(0,11,2)    # numpy version of range() function!
    zeros = np.zeros((3,5))  # 3-rows, 5 columns of zeros #float is default type in np and pandas!
    ones = np.ones(5)
    lspace = np.linspace(0,10,30)   # evenly spaced numbers over specified interval
    identity_matrix = np.eye(4)     # identity = equal rows and columns, ones at diagonal!
    print(zeros)
    print(ones)
    print(lspace)
    print(identity_matrix)
#createArrays()

def randomArrays():
    print(np.random.rand(1))    # same prob for random 0-1 to get picked-> uniform distribution
    print(np.random.rand(5,5))  # 5x5 matrix of random 0-1 nos
    print(np.random.randn(5))   # standard normal distribution -> closer to = zero bigger prob to be picked!
    print(np.random.randint(1, 100)) #rand integer from 1 - 99

#randomArrays()

def arrayMethods():
    arr = np.arange(25)
    ranarr = np.random.randint(0,50,10)
    print(arr)
    print(ranarr)
    print('=' * 40)
    print(arr.reshape(5,5))     # quickly create matrix!
    print(arr.shape)            # tells you dimensions!
    print(arr.dtype)            # data types (int32 = 32 bit integers)
    print(ranarr.max())
    print(ranarr.argmax())         # index where max value is
    print(ranarr.sum())

#arrayMethods()








