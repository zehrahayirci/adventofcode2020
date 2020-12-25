
inp = "974618352" 
numbers = []
for i in inp:
    numbers.append(int(i))
print(numbers)

current=0
for round in range(100):
    #print("\n step", round)
    #print("current_loc",current)
    #print("current_value",numbers[current])
    current_value = numbers[current]
    destination = numbers[current] -1 
    pick_up = []
    pick_up.append(numbers[(current+1)%9] )
    pick_up.append(numbers[(current+2)%9] )
    pick_up.append(numbers[(current+3)%9] )
    
    for i in range(3):
        numbers.remove(pick_up[i])

    #print("numbers",numbers)
    
    #print("pick_up",pick_up)
    if destination < 1: 
            destination = 9 
    while destination in pick_up:
        destination-=1
        if destination < 1: 
            destination = 9 
    #print("destination",destination)
    destination_loc = numbers.index(destination)
    numbers.insert((destination_loc+1) % 7, pick_up[2])
    numbers.insert((destination_loc+1) % 8, pick_up[1])
    numbers.insert((destination_loc+1) % 9, pick_up[0])
    #print("new_numbers",numbers)

    current = numbers.index(current_value)
    #print("current_loc",current)
    current = (current+1) % 9
    #print("next_current",current)

    loc_1 = numbers.index(1)
    res = ""
    for i in range(1,9):
        res+=str(numbers[(loc_1+i)%9])
    print(res)


