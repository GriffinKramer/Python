'''
Griffin Kramer
4/16/2019
9.9 code practice
'''
def findIt (array, num):
    for i in range (len(array)):
        if (array[i] == num):
            return i
    return -1

listofnums = [24, 20, 29, 32, 34, 29, 49, 46, 39, 23, 42, 24, 38]
num_guess = int(input("Enter the number you're looking for: "))
if (findIt(listofnums,num_guess)) == -1:
    print("The number " + str(num_guess) + " was not found.")
else:
    print("The number: " + str(num_guess) + " was found at index: " + str(findIt(listofnums,num_guess)))
