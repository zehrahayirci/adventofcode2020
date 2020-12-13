file1 = open("data_10.txt", "r")
numbers = file1.readlines()
numbers = list(map(int, numbers))
print(numbers)

currrent_jolt = 0
difference_one = 0 
difference_three = 0 
count_difference = 0

while numbers:
    #print(numbers)
    if (currrent_jolt+1) in numbers :
        currrent_jolt+=1
        numbers.remove(currrent_jolt)
        difference_one+=1
    elif (currrent_jolt+2) in numbers :
        currrent_jolt+=2
        numbers.remove(currrent_jolt)
    elif (currrent_jolt+3) in numbers :
        currrent_jolt+=3
        numbers.remove(currrent_jolt)
        difference_three+=1
difference_three+=1
print(difference_one*difference_three) 

atlanan = 0 
numbers = sorted(numbers)

print(numbers)


caxhe = {}
def count_jolt(current, mylist):
    if current in caxhe:
        return caxhe[current]
    cnt = 0
    if current == mylist[-1]:
        return 1
    flag = True
    if current+1 in mylist:
        cnt += count_jolt(current+1, mylist)
        flag = False
    if current+2 in mylist:
        cnt += count_jolt(current+2, mylist)
        flag = False
    if current+3 in mylist:
        cnt += count_jolt(current+3, mylist)
        flag = False
    if flag:
        return 0
    caxhe[current]=cnt
    return cnt

myn = count_jolt(0,numbers)
print(myn)

