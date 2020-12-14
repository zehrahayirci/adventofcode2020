import numpy as np
import ast
import copy

def masked2(mask,decimal):
    binary = bin(decimal)
    string_bin=str(binary).split('b')[1]
    new = np.zeros(36,dtype=int)
    for i,index in enumerate(reversed(mask)):
        if i >= len(string_bin):
            if index == "X":
                new[-1*i-1] = 2
            elif index == "1":
                new[-1*i-1] = 1 
            elif index == "0":
                new[-1*i-1] = 0
        else:
            if index == "X":
                new[-1*i-1] = 2
            elif index == "1":
                new[-1*i-1] = 1 
            elif index == "0":
                new[-1*i-1] = string_bin[-1*i-1]

    new = list(new)
    new = list(map(str, new))

    new_list = [new]
    for i in range(36):
        if new[i] == '2':
            cand_list = []
            for new_cand in new_list:
                new_cand[i] = '0'
                cand_list.append(copy.deepcopy(new_cand))
                new_cand[i] = '1'
                cand_list.append(copy.deepcopy(new_cand))
            new_list = cand_list        

    numbers=[]
    for l in new_list:
        new_Str = ''.join(l)
        new_decimal = int(new_Str,2)
        numbers.append(new_decimal)
    return numbers


def masked(mask,decimal):
    binary = bin(decimal)
    string_bin=str(binary).split('b')[1]
    new = np.zeros(36,dtype=int)
    for i,index in enumerate(reversed(mask)):
        if i >= len(string_bin):
            if index == "X":
                new[-1*i-1] = 0
            elif index == "1":
                new[-1*i-1] = 1 
            elif index == "0":
                new[-1*i-1] = 0
        else:
            if index == "X":
                new[-1*i-1] = string_bin[-1*i-1]
            elif index == "1":
                new[-1*i-1] = 1 
            elif index == "0":
                new[-1*i-1] = 0

    new = list(new)
    new = list(map(str, new))
    new_Str = ''.join(new)
    new_decimal = int(new_Str,2)
    return new_decimal


'''
file1 = open("data_14.txt", "r")
Lines = file1.readlines()
global_mem={}
for line in Lines:
    if "mask" in line:
        mask = line.split(" = ")[1]
        mask=mask.split()[0]
    else:
        mem = {}
        exec(line)
        for eleman in mem:
            global_mem[eleman] = masked(mask,mem[eleman])

print(global_mem)
summ=0
for eleman in global_mem.values():
    summ+=eleman
print(summ)
'''



file1 = open("data_14.txt", "r")
Lines = file1.readlines()
global_mem={}
for line in Lines:
    if "mask" in line:
        mask = line.split(" = ")[1]
        mask=mask.split()[0]
    else:
        mem = {}
        exec(line)
        for eleman in mem:
            adresses = masked2(mask, eleman)
            for k in adresses:
                global_mem[k] = mem[eleman]

print(global_mem)
summ=0
for eleman in global_mem.values():
    summ+=eleman
print(summ)
