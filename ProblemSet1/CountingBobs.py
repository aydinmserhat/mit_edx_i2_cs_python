s = "itcanbeanyStringofbob"
numbob = 0
for i in range(len(s)):
    if s[i:].startswith('bob'):
        numbob = numbob + 1
print ("Number of times bob occurs is: ") + str(numbob)