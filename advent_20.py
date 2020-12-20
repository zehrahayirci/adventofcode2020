import numpy as np
import matplotlib.pyplot as plt 

def process_tile(tile):
    up = tile[0,:]
    down = tile[-1,:]
    left = tile[:,0]
    right = tile[:,-1]

    mulp = np.arange(up.shape[0])
    mulp = np.power(2, mulp)
    mulp2 = mulp[::-1]

    up_num = np.sum(mulp * up)
    down_num = np.sum(mulp * down)
    left_num = np.sum(mulp * left)
    right_num = np.sum(mulp * right)

    up_num2 = np.sum(mulp2 * up)
    down_num2 = np.sum(mulp2 * down)
    left_num2 = np.sum(mulp2 * left)
    right_num2 = np.sum(mulp2 * right)

    return up_num,down_num,left_num,right_num, up_num2,down_num2,left_num2,right_num2

def give_me_border(x,y, fpic, N):
    komsular = []
    for xinc in [-1,0,1]:
        for yinc in [-1,0,1]:
            if not xinc * yinc == 0:
                continue
            if xinc == 0 and yinc == 0:
                continue 
            if x+xinc < 0 or x+xinc > N-1:
                continue
            if y+yinc < 0 or y+yinc > N-1:
                continue
            if fpic[x+xinc, y+yinc] > 0 :
                komsular.append(fpic[x+xinc, y+yinc])
    return komsular

def solve_from_left_to_right(row,full_pic, all_dats, big_picture):
    for sx in range(1,12):
        #print(sx)
        right_of_left = process_tile(big_picture[row*10:(row+1)*10,(sx-1)*10:(sx)*10])[3]
        my_nums = processed_dat[all_dats[full_pic[row,sx]-1][0]]
        for i,num in enumerate(my_nums):
            if num == right_of_left:
                tttt = all_dats[full_pic[row,sx]-1][1]
                if i == 2:
                    big_picture[row*10:(row+1)*10,sx*10:(sx+1)*10] = tttt
                elif i==4:
                    big_picture[row*10:(row+1)*10,sx*10:(sx+1)*10] = np.rot90(tttt)
                elif i==7:
                    big_picture[row*10:(row+1)*10,sx*10:(sx+1)*10] = np.flip(np.flip(tttt, axis=0), axis=1)
                elif i==6:
                    big_picture[row*10:(row+1)*10,sx*10:(sx+1)*10] = np.flip(tttt, axis=0)
                elif i==5:
                    big_picture[row*10:(row+1)*10,sx*10:(sx+1)*10] = np.flip(np.rot90(tttt,k=3),axis=0)
                elif i==3:
                    big_picture[row*10:(row+1)*10,sx*10:(sx+1)*10] = np.flip(tttt,axis=1)
                elif i==1:
                    big_picture[row*10:(row+1)*10,sx*10:(sx+1)*10] = np.rot90(tttt,k=3)
                else:
                    print('Error {} is not recognized'.format(i))

def solve_from_up_to_down(col, full_pic, all_dats, big_picture):
    for sy in range(1,12):
        down_of_up = process_tile(big_picture[(sy-1)*10:sy*10, col*10:(col+1)*10])[1]
        my_nums = processed_dat[all_dats[full_pic[sy,col]-1][0]]
        for i,num in enumerate(my_nums):
            if num == down_of_up:
                tttt = all_dats[full_pic[sy, col]-1][1]
                if i ==6:
                    big_picture[sy*10:(sy+1)*10,col*10:(col+1)*10] = np.rot90(tttt,k=3)
                elif i==5:
                    big_picture[sy*10:(sy+1)*10,col*10:(col+1)*10] = np.flip(np.flip(tttt,axis=0), axis=1)
                elif i==7:
                    big_picture[sy*10:(sy+1)*10,col*10:(col+1)*10] = np.flip(np.rot90(tttt),axis=1)
                elif i==0:
                    big_picture[sy*10:(sy+1)*10,col*10:(col+1)*10] = tttt
                elif i==4:
                    big_picture[sy*10:(sy+1)*10,col*10:(col+1)*10] = np.flip(tttt, axis=1)
                else:
                    print('ozan',i)

data = open('data_20.txt').read().split('\n')


all_dats = []
i = 0
for l in data:
    if 'Tile' in l:
        if i == 10:
            all_dats.append((nextt,new_array.copy()))
        nextt = int(l.split(' ')[1][:-1])
        new_array = np.zeros((10,10), dtype=int)
        i = 0
    elif '.' in l or '#' in l:
        line = list(map(lambda x:1 if x=='#' else 0, l))
        new_array[i,:] = np.array(line)
        i+=1
all_dats.append((nextt,new_array.copy()))


processed_dat = {}
for dat in all_dats:
    processed_dat[dat[0]] = process_tile(dat[1])

matches = np.zeros((144,144), dtype=int)
for i in range(144):
    for j in range(144):
        if i == j:
            continue
        key_left =  processed_dat[all_dats[i][0]]
        key_right =  processed_dat[all_dats[j][0]]
        for si in range(8):
            for sj in range(8):
                if key_left[si] == key_right[sj]:
                    matches[i,j] = 1

aa = np.sum(matches, axis=1)

full_pic = np.zeros((12,12), dtype=int)
b = 1
jx = 0
jy = 0

for i in range(144):
    if  aa[i] == 2:
        full_pic[jy,jx] = i+1
        
        # next coord
        if jy == 11:
            jx = 11
        elif jx==11:
            jx = 0
            jy = 11 
        else:
            jx = 11
        b*=int(all_dats[i][0])

print("solution for part 1", b)

for jx in [0,11]:
    for jy in [0,11]:
        corner_id = full_pic[jx,jy] - 1
        neigh = np.where(matches[corner_id,:]==1)[0]
        # search for neighboors

        nx1 = 10 if jx == 11 else 1
        ny1 = 10 if jy == 11 else 1

        n1  = neigh[0] + 1
        n2  = neigh[1] + 1

        full_pic[nx1,jy] = n1
        full_pic[jx,ny1] = n2


max_iter = 0
while np.any(full_pic==0):
    max_iter+=1
    if max_iter > 15000:
        break

    for sx in range(12):
        for sy in range(12):
            if full_pic[sx,sy] == 0:
                komsular = give_me_border(sx,sy, full_pic, 12)
                if len(komsular) > 0 :
                    #print(sx, sy, komsular)
                    matchler = np.ones((144),dtype=int)
                    for i in komsular:
                        matchler = matchler * matches[i-1,:]
                    cozumler = np.where(matchler==1)[0]
                    gercek_cozumler = []
                    for cozum in cozumler:
                        if not np.any(full_pic==cozum+1):
                            gercek_cozumler.append(cozum+1)
                    if len(gercek_cozumler) == 1:
                        full_pic[sx,sy] = gercek_cozumler[0]
    
#print(full_pic)

#print('o')
for nextt in [73,12]:
    corn_nums = processed_dat[all_dats[5][0]]
    nnums = processed_dat[all_dats[nextt][0]]
    #print(5, corn_nums)
    #print(nextt, nnums)

big_picture = np.zeros((10*12,10*12), dtype = int)
big_picture[0:10,0:10] = np.flip(all_dats[full_pic[0,0]-1][1], axis=1)

solve_from_left_to_right(0, full_pic, all_dats, big_picture)
solve_from_up_to_down(0, full_pic, all_dats, big_picture)
for i in range(1,12):
    solve_from_left_to_right(i, full_pic, all_dats, big_picture)

real_big_picture = np.zeros((12*8,12*8),dtype=int)
for xr in range(12):
    for yr in range(12):
        real_big_picture[yr*8:(yr+1)*8,xr*8:(xr+1)*8] = big_picture[yr*10+1:(yr+1)*10-1,xr*10+1:(xr+1)*10-1]

canavar = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
[1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1], 
[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]],dtype=int)


found = False
for xf in [True, False]:
    for yf in [True, False]:
        for rot in [-1,1,2,3]:
            if found:
                break
            new_real_pic = np.copy(real_big_picture)
            only_canavar = np.zeros((8*12,8*12), dtype=int)

            if xf:
                new_real_pic = np.flip(new_real_pic, axis=1)
            if yf:
                new_real_pic = np.flip(new_real_pic, axis=0)
            if rot > 0:
                new_real_pic = np.rot90(new_real_pic, k=rot)
            canavar_counter = 0
            for xs in range(8*12-20):
                for ys in range(8*12-3):
                    ism = new_real_pic[ys:ys+3,xs:xs+20]
                    if np.all(ism[canavar==1]==1):
                        canavar_counter +=1
                        only_canavar[ys:ys+3,xs:xs+20] = canavar
            if canavar_counter>0:
                plt.imshow(only_canavar)
                plt.savefig('canavars.png')
                print('solution for part 2:{}'.format(np.sum(new_real_pic)- canavar_counter*np.sum(canavar)))
                found = True
