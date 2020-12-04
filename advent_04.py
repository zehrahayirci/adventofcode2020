import numpy as np
file1 = open("data_04.txt", "r")
Lines = file1.read() 
myarray = Lines.split("\n\n")
print(len(myarray))

valids = np.zeros((len(myarray)))
print(valids)
for counter, passport in enumerate(myarray):
    passport_noline=passport.replace('\n'," ")
    small = passport_noline.split(" ")
    print(small)
    value=0
    keywords={"byr":1,"iyr":1,"eyr":1,"hgt":1,"hcl":1,"ecl":1,"pid":1,"cid":0}
    eye_color={"amb":1 ,"blu":1 ,"brn":1 ,"gry":1, "grn":1, "hzl":1 ,"oth":1}
    for item in small:
        #value+=keywords[item[0:3]]
        print(item[0:3])
        #print(value)
        if item[0:3] =="byr":
            byr=int(item.split(":")[1])
            if byr <=2002 and byr >= 1920 :
                value+= 1
        if item[0:3] =="iyr":
            iyr=int(item.split(":")[1])
            if iyr <=2020 and iyr >= 2010 :
                value+= 1
        if item[0:3] =="eyr":
            eyr=int(item.split(":")[1])
            if eyr <=2030 and eyr >= 2020 :
                value+= 1
        if item[0:3] =="ecl":
            ecl=item.split(":")[1]
            if ecl in eye_color: 
                value+= 1
        if item[0:3] =="pid":
            pid=item.split(":")[1]
            if len(pid) == 9 :
                value+= 1
        if item[0:3] =="hcl":
            hcl=item.split(":")[1]
            if len(hcl) == 7 and hcl[0]=="#":
                value+= 1  
        if item[0:3] =="hgt":
            hgt=item.split(":")[1]
            if len(hgt) >2 :
                if hgt[-2:]=="cm" and len(hgt) == 5:
                    boy = int(hgt[:3])
                    if boy <= 193 and boy >= 150:
                        value+= 1 
                elif hgt[-2:]=="in"and len(hgt) == 4:
                    boy = int(hgt[:2])
                    if boy <= 76 and boy >= 59:
                        value+= 1  
        print(value)  
    if value == 7:
        valids[counter] = 1
            
print(valids)
print(sum(valids))