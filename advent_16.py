import numpy as np


def matches(rules_dict,number):
    match_l=[]
    for eleman in rules_dict:
        if ((number >= rules_dict[eleman][0][0]) and (number <= rules_dict[eleman][0][1])) or\
            ((number >= rules_dict[eleman][1][0]) and (number <= rules_dict[eleman][1][1])):
            match_l.append(1)
        else:
            match_l.append(0)                
    return match_l


file1 = open("data_16.txt", "r")
Lines = file1.readlines()

rules_dict = {}
for i in range(20):
    line = Lines[i].split(" ")
    numbers_1 = line[1].split("-")
    numbers_1 = list(map(int, numbers_1))    
    numbers_2 = line[3].split("-")
    numbers_2 = list(map(int, numbers_2))
    tup=(numbers_1,numbers_2)
    rules_dict[i]=tup
    #print(rules_dict)

ticket = Lines[22].split(",")
ticket = list(map(int, ticket))


summ=0
trueLines = []
for i in range(25,262):
    line = Lines[i].split(",")
    line = list(map(int, line))
    wrongLine=False
    for number in line:
        flag = True 
        for eleman in rules_dict:
            if ((number >= rules_dict[eleman][0][0]) and (number <= rules_dict[eleman][0][1])) or\
                ((number >= rules_dict[eleman][1][0]) and (number <= rules_dict[eleman][1][1])):
                    flag =False
                    break
        if flag:
            wrongLine=True
            summ+=number
    if not wrongLine:
        trueLines.append(line)

Deduced = np.ones((20,20),dtype=int)
for ln in trueLines:
    for i in range(20):
        ml= matches(rules_dict,ln[i])
        for j  in range(20):
            if ml[j] == 0:
                Deduced[i,j] = 0 
print(Deduced)

used=[]
while len(used) <20 : 
    xs = np.sum(Deduced,axis=0) #col sum
    ys = np.sum(Deduced,axis=1) #row sum
    if np.any(xs==1):
        col = np.where(xs==1)[0][0]
        row = np.where(Deduced[:,col]==1)[0][0]
        if (row,col) not in used:
            used.append((row,col))
            Deduced[row,:] = 0
            Deduced[:,col] = 0
    if np.any(ys==1):
        row = np.where(ys==1)[0][0]
        col = np.where(Deduced[row,:]==1)[0][0]
        if (row,col) not in used:
            used.append((row,col))
            Deduced[row,:] = 0
            Deduced[:,col] = 0

myrules = []
for rul in used:
    if rul[1]<6:
        myrules.append(rul[0])

a=1
for i in myrules:
    a*=ticket[i]

print(a)