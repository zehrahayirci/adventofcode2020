inbag = {}
file1 = open("data_07.txt", "r")
Lines = file1.readlines()
for line in Lines: 
    list_bags =line.split(" contain ")
    container = list_bags[0].split(' bag')[0]
    children=[]
    if "no other bags." in line:
        inbag[container] = children
        continue
    for child in list_bags[1].split(","):
        child = child.strip()
        ca = child.split(' ')
        nummer = ca[0]
        name =  ca[1] + ' ' + ca[2]
        tup = (name,nummer)
        children.append(tup)
    inbag[container] = children
print(inbag)

def countbags(inbag,item): #eleman = shiny gold 
    if len(inbag[item]) < 1:
        return 1
    else : 
        count = 1 
        for eleman in inbag[item]:
            count += int(eleman[1]) * countbags(inbag,eleman[0])
        return count 

print(countbags(inbag,"shiny gold")-1) 

        