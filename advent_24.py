import numpy as np

def modifyTiles2(grid):
    new_grid = np.copy(grid)

    black_cnt = np.zeros(grid.shape)
    black_cnt[0:900,0:898] += grid[0:900,2:900]
    black_cnt[0:900,2:900] += grid[0:900,0:898]
    black_cnt[0:899,0:899] += grid[1:900,1:900]
    black_cnt[0:899,1:900] += grid[1:900,0:899]
    black_cnt[1:900,0:899] += grid[0:899,1:900]
    black_cnt[1:900,1:900] += grid[0:899,0:899]
    
    white_to_black = np.zeros(grid.shape)
    white_to_black[black_cnt==2] = 1

    black_to_white = np.zeros(grid.shape)
    black_to_white[black_cnt==0] = 1
    black_to_white[black_cnt>2] = 1

    new_grid[grid==1] = new_grid[grid==1] - black_to_white[grid==1]
    new_grid[grid==0] = new_grid[grid==0] + white_to_black[grid==0]
    
    return new_grid


def checkCase(d,directions):
    if d == directions[0]:
        return (0,2)
    elif d == directions[1]:
        return (1,1)
    elif d == directions[2]:
        return (1,-1)
    elif d == directions[3]:
        return (0,-2)
    elif d == directions[4]:
        return (-1,-1)
    elif d == directions[5]:
        return (-1,1)


dat = open('data_24.txt','r')
Lines = dat.readlines()

directions=["e","se", "sw", "w", "nw", "ne"]

grid = np.zeros((900,900))
pos = np.array([451,451])
for line in Lines:
    d = ""
    pos = np.array([451,451])
    for i in range(len(line)):
        d+=line[i]
        if d in directions:
            case = checkCase(d,directions)
            d = ""
            pos += np.array(case)
    grid[pos[0], pos[1]] = 1-grid[pos[0], pos[1]]
    print(pos)
print(np.sum(grid))

for i in range(100):
    grid = modifyTiles2(grid)
    if i % 10 == 9:
        print(i,np.sum(grid))
