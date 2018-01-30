import math
# 1 square root of 100
def task1():
    x = 300
    print(math.sqrt(x))
#task1()

# 2 grab 500 out of string SP500
def task2():
    sp_index = 'SP500'
    print(sp_index[2:])
#task2()

# 3
def task3():
    sp_index = 'S&P 500'
    value = 1500
    print('The {} is at {} today'.format(sp_index,value))
#task3()

# 4 use indexing and key calls to grab: SP price (250), number 365!

def task4():
    stock_info = {'sp500':{'today':300,'yesterday': 250}, 'info':['Time',[24,7,365]]}
    print(stock_info['sp500']['yesterday'])
    print(stock_info['info'][1][-1])
#task4()

# 5
def task5():
    my_str = ('price: 345.324: source -- QUANDL')
    my_str1 = my_str.split('--')
    print(my_str1)
    print(my_str1[-1])
#task5()

# 6 count number of times word 'price' occurs in string
def task6(string):
    count = 0
    for word in string.lower().split():
        if 'price' in string:
            count +=1
    print (count)

#task6('Wow that is a nice price, very nice Price! I said price 3 times.')

# 7
def task7():
    avg_price = [3,4,5]
    sum_ = 0
    for num in avg_price:
        sum_ = sum_ + num
    average = sum_/(len(avg_price))
    print(average)
task7()



