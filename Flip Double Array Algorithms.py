'''
Griffin Kramer
Unit 10 Project
'''
import random

def printArray(a):
    for r in range(len(a)):
        for c in range(len(a[0])):
            print(a[r][c], end = ' ')
        print(' ')
        
def flipHorizontal(a):
    for j in range ((len(a))):
        for i in range ((len(a[0])) // 2):
            temp = a[j][i]
            a[j][i] = a[j][len(a[0]) - 1 - i]
            a[j][len(a[0]) - 1 - i] = temp

def flipVertical(a):
        for i in range ((len(a)) // 2):
            temp = a[i]
            a[i] = a[len(a) - 1 - i]
            a[len(a) - 1 - i] = temp


array = []
array.append([0, 2, 0, 0, 0])
array.append([0, 2, 0, 0, 0])
array.append([0, 2, 2, 0, 0])
array.append([0, 2, 0, 2, 0])
array.append([0, 2, 0, 0, 2])

printArray(array)

print('')

flipVertical(array)

printArray(array)

print('')

flipVertical(array)

flipHorizontal(array)

printArray(array)

array2 = []
num = int(input('enter dimension for 2d array: '))
for i in range (num):
    array2.append([])
    for j in range (num):
        array2[i].append(random.randint(0, 5))
        
printArray(array2)
flipVertical(array2)

print('')
printArray(array2)
flipVertical(array2)
print('')

flipHorizontal(array2)
printArray(array2)









