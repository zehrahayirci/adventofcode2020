def isTotal(numbers,target):
    for i in range(25):
        for j in range(24):
            if (numbers[i] + numbers[j]) == target:
                return True
    else:
        return False

def weakXMAS(target,index,List):
    summ = 0 
    lisr = []
    print(target)
    print(lisr)
    #print(numbers)
    i = index 
    for i in range(0,index):
        summ = int(List[i])
        lisr.append( int(List[i]) )
        j = i+1
        while(summ <target):       
            summ += int(List[j])
            lisr.append(int(List[j]))
            if summ == target:
                print(lisr)
                sorted = lisr.sort()
                print(lisr[0]+lisr[-1])
            j+=1
        lisr = []


file1 = open("data_09.txt", "r")
Lines = file1.readlines() 
nums = []
bitti = 0 
for pre in range(25):
    nums.append(int(Lines[pre]))
print(nums)
for i in range(25,len(Lines)):
    targetnum = int(Lines[i])
    if isTotal(nums,targetnum):
        nums.pop(0)
        nums.append(targetnum)
        #print(nums)
    elif(bitti==0) : 
        weakXMAS(targetnum,i,Lines)
        bitti = 1
    if bitti == 1:
        i = len(Lines)+2




