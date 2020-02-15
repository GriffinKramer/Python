def printit(a):
    for r in range(len(a)):
        for c in range(len(a[0])):
            print(a[r][c], end = ' ')
        print(' ')
        
def reverse(a):
    for j in range ((len(a)-1)):
        for i in range ((len(a[0])) // 2):
            temp = a[j][i]
            a[j][i] = a[j][len(a[0]) - 1 - i]
            a[j][len(a[0]) - 1 - i] = temp
        
    
array = []

array.append([' ', ' ', ' ', ' ', '*', ' '])
array.append([' ', ' ', '^', '^', '*', ' '])
array.append([' ', '^', ' ', ' ', '^', ' '])
array.append(['^', '_', '_', '_', '_', '^'])
array.append(['|', ' ', ' ', ' ', ' ', '|'])
array.append(['|', ' ', ' ', '□', ' ', '|'])
array.append(['|', ' ', ' ', '□', ' ', '|'])
array.append(['|', '_', '_', '_', '_', '|'])

printit(array)
reverse(array)
print('')
printit(array)
