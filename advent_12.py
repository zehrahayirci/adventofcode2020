def whichface(current,new_face,new_angle):
    directions={'N':0, 'E':1,'S':2,'W':3}
    revd=dict([reversed(i) for i in directions.items()])
    directions.update(revd)
    angles={90:1, 180:2, 270:3, 360:0}
    angle=angles[new_angle]
    if new_face == 'L':
        dir = directions[current]-angle
    if new_face == 'R':
        dir = directions[current]+angle

    return directions[dir%4]


def whichfacewaypoint(current_waypoint, new_face,new_angle):
    new_waypoint=[0,0,0,0]
    directions={'N':0, 'E':1,'S':2,'W':3}
    revd=dict([reversed(i) for i in directions.items()])
    directions.update(revd)

    angles={90:1, 180:2, 270:3, 360:0}
    angle=angles[new_angle]
    if new_face == 'L':
        for i in range(4):
            new_waypoint[i] = current_waypoint[(i+angle)%4]
    if new_face == 'R':

        for i in range(4):
            a = (i-angle)%4
            new_waypoint[i] = current_waypoint[(i-angle)%4]
    return new_waypoint



file1 = open("data_12.txt", "r")
Lines = file1.readlines()
directions={'N':0, 'E':1,'S':2,'W':3}
face ='E'
position=[0,0,0,0]
waypoint=[1,10,0,0]
for line in Lines:
    print(line)
    number = int(line[1:])
    if line[0] == 'F':
        for i in range(4):
            position[i] += number * waypoint[i]
            #position[directions[face]]+=int(line[1:])
    elif line[0] == 'L' or line[0] == 'R':
            waypoint =whichfacewaypoint(waypoint,line[0],number)
            #face =whichface(face,line[0],int(line[1:]))
    else:
        waypoint[directions[line[0]]]+=number
        #position[directions[line[0]]]+=int(line[1:])
    #print(position)
    #print(waypoint)
print( abs(position[0]-position[2]) + abs(position[1]-position[3]) )
    #print(position)
    #print(face)
    
