import numpy as np 


def giveNeightbors(x,y,z,w):
    maxx = 26
    neighborlar=[]
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    if i == 0 and  j == 0 and k == 0 and l == 0:
                        continue
                    komsu_x = x+i
                    komsu_y = y+j
                    komsu_z = z+k
                    komsu_w = w+l
                    if komsu_x < 0 or komsu_y < 0 or komsu_z < 0 or komsu_x > maxx or komsu_y > maxx \
                        or komsu_z > maxx or komsu_w > maxx or komsu_w < 0 : 
                        continue
                    neighborlar.append([komsu_x,komsu_y,komsu_z,komsu_w])
    return neighborlar

def regel(neighbors, cube, state):
    count = 0 
    for i in neighbors:
        if cube[i[0],i[1],i[2],i[3] ]== 1:
            count+=1
    if state == 1:
        if count ==2 or count ==3: 
            new_state = 1 
        else :
            new_state = 0
    if state == 0 :
        if count == 3:
            new_state = 1 
        else : 
            new_state =0 

    return new_state,count

def isActive(cube):
    new_cube =  np.zeros((27,27,27,27),dtype =int)
    for i in range(cube.shape[0]):
        for j in range(cube.shape[1]):
            for k in range(cube.shape[2]):
                for l in range(cube.shape[3]):
                    neighbors = giveNeightbors(i,j,k,l)
                    new_cube[i,j,k,l],c= regel(neighbors,cube,cube[i,j,k,l])
    return new_cube

cube = np.zeros((27,27,27,27),dtype =int)
cube[9,12,12, 12] = 1 
cube[9,15,12, 12] = 1 

cube[10,14,12, 12] = 1 
cube[10,15,12, 12] = 1 

cube[11,9,12, 12] = 1 
cube[11,10,12, 12] = 1 
cube[11,13,12, 12] = 1 
cube[11,14,12, 12] = 1 
cube[11,16,12, 12] = 1 

cube[12,9,12, 12] = 1 
cube[12,11,12, 12] = 1 
cube[12,13,12, 12] = 1 
cube[12,14,12, 12] = 1 

cube[13,9,12, 12] = 1 
cube[13,12,12, 12] = 1 
cube[13,14,12, 12] = 1 
cube[13,15,12, 12] = 1 
cube[13,16,12, 12] = 1 

cube[14,12,12, 12] = 1 
cube[14,13,12, 12] = 1 
cube[14,15,12, 12] = 1 

cube[15,12,12, 12] = 1 
cube[15,9,12, 12] = 1 
cube[15,13,12, 12] = 1 
cube[15,16,12, 12] = 1 

cube[16,10,12, 12] = 1 
cube[16,12,12, 12] = 1 
cube[16,15,12, 12] = 1 





for i in range(6):
    print(i)
    cube = isActive(cube)

print(np.sum(cube))
