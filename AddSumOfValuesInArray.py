#Griffin Kramer
#9.6 Q2

import random
def randadd(a_list, num):
    for i in range (num):
        a_list.append(random.randint(10, 99))

def sumitup(a_list):
    sum = 0
    for i in range (len(a_list)):
        sum += a_list[i]
    return sum
        
array = []
ask = int(input('how many values'))
randadd(array, ask)
print(array)
print('Total: ' + str(sumitup(array)))
