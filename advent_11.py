import numpy as np

def is_outside(_num, _min, _max):
    if _num < _min:
        return True
    if _num >_max:
        return True 
    return False

def countAdjacents(array, y, x, MAX_X, MAX_Y):
    count = 0 
    for x_inc in [-1,0,1]:
        for y_inc in [-1,0,1]:
            if is_outside(x+x_inc,0,MAX_X) or is_outside(y+y_inc, 0, MAX_Y):
                continue
            if x_inc==0 and y_inc == 0:
                continue 
            if array[y+y_inc,x+x_inc] == 1:
                count+=1
    return count

def countAdjacents2(array, y, x, MAX_X, MAX_Y):
    count = 0 
    for x_inc in [-1,0,1]:
        for y_inc in [-1,0,1]:
            if x_inc==0 and y_inc == 0:
                continue
            curr_x = x + x_inc 
            curr_y = y + y_inc 
            while True:
                if is_outside(curr_x,0,MAX_X) or is_outside(curr_y, 0, MAX_Y):
                    break
                if array[curr_y,curr_x] == 1:
                    count+=1
                    break
                if array[curr_y,curr_x] == 0:
                    break
                curr_x +=x_inc 
                curr_y +=y_inc 
    return count 


            

def update(array):
    new_array = np.copy(array)
    for y in range(new_array.shape[0]):
        for x in range(new_array.shape[1]):
            cnt = countAdjacents(array, y,x, new_array.shape[1]-1,new_array.shape[0]-1)
            if array[y,x] == 0: # empty
                if cnt == 0:
                    new_array[y,x] = 1
            elif array[y,x] == 1:
                if cnt >= 4:
                    new_array[y,x] = 0
    return new_array

def update2(array):
    new_array = np.copy(array)
    for y in range(new_array.shape[0]):
        for x in range(new_array.shape[1]):
            cnt = countAdjacents2(array, y,x, new_array.shape[1]-1,new_array.shape[0]-1)
            if array[y,x] == 0: # empty
                if cnt == 0:
                    new_array[y,x] = 1
            elif array[y,x] == 1:
                if cnt >= 5:
                    new_array[y,x] = 0
    return new_array



file1 = open("data_11.txt", "r")
Lines = file1.readlines() 
occupied= 0
Lines = list(map(lambda x:list(x.split()[0]), Lines))
for y in range(len(Lines)):
    for x in range(len(Lines[y])):
        if Lines[y][x] == '.':
            Lines[y][x] = -1
        elif Lines[y][x] == 'L':
            Lines[y][x] = 0
larray = np.array(Lines)

while True:
    larray_up = update2(larray)
    if np.all(larray==larray_up):
        break 
    else:
        larray = larray_up
print(np.sum(larray[larray==1]))


'''
for lineindex,line in enumerate(Lines): 
    if lineindex != 0:
        beforeline = Lines[index-1]
    else :
        beforeline = ""

    if lineindex != len(Lines):
        afterline = Lines[index+1]
    else :
        afterline = ""    
    i = 0 
    while i < 10
        adjacents = 0
        if c == 'L':
            countAdjacents(line,beforeline,afterline,index)

'''

  