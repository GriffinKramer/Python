#Griffin Kramer
#Random Joke Generator
#3rd Period Comp-Sci
 
ctr = 0
infile = open("jokes.txt", "r")
linenum = infile.readline()
while linenum:
    ctr = ctr + 1
    linenum = infile.readline()
print(str(ctr) + " jokes total")
infile.close()
#infile = open("jokes.txt", "r")
#infile2 = open("answers.txt", "r")
l = True
while l == True:
    jokenum = int(input("enter a joke number, 0 to stop: "))
    while jokenum != 0:
        if jokenum <= 0 or jokenum > ctr:
            print("please pick a proper joke number")
        else:
            infile = open("jokes.txt", "r")
            infile2 = open("answers.txt", "r")
            for i in range (jokenum):
                 line = infile.readline()
                 line2 = infile2.readline()
            print("Joke #" + str(jokenum))
            print(line)
            print(line2)
        jokenum = int(input("enter a joke number, 0 to stop: "))
        infile.close()
    l = False



