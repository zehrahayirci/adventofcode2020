import numpy as np
file1 = open("data_06.txt", "r")
Lines = file1.read() 
myarray = Lines.split("\n\n")
print(len(myarray))

bigsum = 0 
for counter, passport in enumerate(myarray):
    #answers_noline=passport.replace('\n'," ")
    small = passport.split("\n")
    all_yesno = np.zeros((26))
    print(small)
    print(sum(all_yesno))
    alist = []
    for item in small:
        alist.append(set(item))
    interr = set.intersection(*alist)
    bigsum+=len(interr) 
print(bigsum)

