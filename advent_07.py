file1 = open("data_07.txt", "r")
Lines = file1.readlines()
inbag = {}
the_ones = []
finish = [] 
search = ["shiny gold"]
for line in Lines: 
    if "no other bags." in line:
        continue
    
    list_bags =line.split(" contain ")
    container = list_bags[0].split(' bag')[0]
    children=[]
    for child in list_bags[1].split(","):
        child = child.strip()
        children.append(' '.join(child.split(' bag')[0].split(' ')[1:]))
        if children[-1] not in inbag:
            inbag[children[-1]]=[]
        inbag[children[-1]].append(container)
#print(inbag)

while len(search) > 0 : 
    item = search.pop() #bunu search ediyoruz 
    finish.append(item)
    if item not in inbag:
        continue
    for eleman in inbag[item]:
        if eleman not in search : 
            if eleman not in finish :
                search.append(eleman)
        the_ones.append(eleman)
print(len(set(the_ones)))
