file1 = open("data_15.txt", "r")
Lines = file1.readline()
numbers = Lines.split(',')
numbers = list(map(int, numbers))
history={}
last_number=0
last_new=0
for i, item in enumerate(numbers):
    history[item]=[i+1,0]
    last_number=item
    last_new=1

for j in range(i+2,30000001):
    if last_new == 1:
        if 0 in history:
            before_that = history[0][0]
            history[0]=[j,before_that]
            last_new = 0
        else:
            history[0]=[j,0]
            last_new = 1
        last_number=0
    else:
        loc = history[last_number][0] - history[last_number][1]
        if loc in history:
            last_new = 0
            before_that = history[loc][0]
            history[loc]=[j,before_that]
        else:
            history[loc]=[j,0]
            last_new = 1
        last_number=loc
print(j,last_number,last_new)
        

    