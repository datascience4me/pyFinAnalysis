'''
Lambda expressions/functions
when you don't want to define function you use lambda functions = anonymous functions
use case = map and filter functions!
used one time in a script and without name
useful when used with other functions (used a lot with pandas)
'''

#lambda expressions:

lambda var: var * 2

seq = [1,2,3,4,5]
print(list(map(lambda var: var*2, seq)))

def isEven(num):
    return num % 2 == 0

#lambda num: num % 2 == 0

print(list(filter(isEven, seq)))
print('='*40)
print((list(filter(lambda num: num % 2 == 0, seq))))

print('='*40)

# strip method

myVar = 'go sports #volleyball'
print(myVar.split())
print(myVar.split('#'))     # makes a list on #!

# string formatting


