

def isLoop(Lines,flip):
    nummer = 0 
    index = 0 
    visited = []

    while index not in visited:
        if index > len(Lines)-1:
            print("nummer:{}".format(nummer))
            return True
        line = Lines[index]
        visited.append(index)
        
        if line[:3] == "acc":
            if line[4] == "-":
                minus = int(line.split("-")[1])
                nummer = nummer - minus
            elif line[4] == "+":
                add = int(line.split("+")[1])
                nummer = nummer + add
            index+=1 

        if line[:3] == "nop":
            if index == flip:
                if line[4] == "-":
                    minus = int(line.split("-")[1])
                    index = index - minus

                elif line[4] == "+":
                    add = int(line.split("+")[1])
                    index = index + add
            else:
                index+=1 

        if line[:3] == "jmp":
            if index == flip:
                index+=1 
                continue

            if line[4] == "-":
                minus = int(line.split("-")[1])
                index = index - minus

            elif line[4] == "+":
                add = int(line.split("+")[1])
                index = index + add
    return False 

    
if __name__ == "__main__":
    file8 = open("data_08.txt","r")
    Lines = file8.readlines()
    for i in range(len(Lines)):
        if(isLoop(Lines,i)):
            print(i)

