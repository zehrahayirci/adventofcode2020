import re

file1 = open("data_21.txt", "r")
Lines = file1.readlines()
english_set=[]
foreign_set=[]
main_set=set("")
dicti={}
for line in Lines:
    my_set=set("")
    eng_set=set("")
    words= line.split("(contains ")
    items = words[0].split(" ")
    #print(items)
    for item in items:
        if item !="":
            my_set.add(item)
    foreign_set.append(my_set)

    eng = words[1].split(",")
    for eng_item in eng:
        eng_item=eng_item.strip()
        eng_item=re.sub('[\)\\n]','', eng_item)
        eng_set.add(eng_item)
        main_set.add(eng_item)
    english_set.append(eng_set)

#print(foreign_set)
#print(english_set)
#print(main_set)
while(len(dicti)<len(main_set)):
    for item in main_set:
        junc_id=[]
        for i, eng in enumerate(english_set):
            if item in eng:
                junc_id.append(i)
        setlist = (foreign_set[a] for a in junc_id)
        u = set.intersection(*setlist)
        if len(u) == 1:
            for uu in u:
                dicti[item]=uu
                for jab in foreign_set:
                    jab.discard(uu) 
print(dicti)
count=0
for a in foreign_set:
    if len(a)>=1:
        count+=len(a)
print(count)

sol = ""
for k in sorted(dicti.keys()):
    sol += dicti[k] +","
print(sol)