def openDoor(loop_number,subject_number):
    number = 1 
    for i in range(loop_number):
        number *= subject_number
        number= number % 20201227
    return number

def getLoopNumber(puzzle_input):
    number = 1 
    for i in range(5000000):
        number *=7 
        number = number % 20201227
        if number == puzzle_input:
            return i+1

loopnumber_door = getLoopNumber(1614360)
loopnumber_key = getLoopNumber(7734663)
print(loopnumber_door)
print(loopnumber_key)
a = openDoor(loopnumber_key,1614360)
print(a)
