'''
Griffin Kramer
4/19/19
3rd Comp Sci
9.10 Q3
'''

#Swap word1 and word2
def swaps(terms, i, smallest):
    word = terms[i]
    terms[i] = terms[smallest]
    terms[smallest] = word

terms = ["Bandwidth", "Hierarchy", "IPv6", "Software", "Firewall", "Cybersecurity", "Lists", "Program", "Logic", "Reliability"]
print(terms)
for i in range (len(terms)-1):
    #word = terms[i]
    smallest = i + 1
    for j in range (i, len(terms)):
        if terms[smallest] > terms[j]:
            smallest = j
    #terms[i] = temrm[smallest]
    #terms[smallest] = word
    swaps(terms, i, smallest)
print(terms)
