def Calculate(sayilar,islemler):
    eldevar = int(sayilar[0])
    for i,islem in enumerate(islemler):
        if islem == "+":
            eldevar = eldevar + int(sayilar[i+1])
        elif islem == "*":
            eldevar = eldevar * int(sayilar[i+1])
    return eldevar

def CalculateAdvanced(sayilar,islemler):
    while '+' in islemler:
        for i,islem in enumerate(islemler):
            if islem == "+":
                eldevar = int(sayilar[i]) + int(sayilar[i+1])
                del islemler[i]
                sayilar = sayilar[0:i]+[str(eldevar)]+sayilar[i+2:]
                break
            else:
                continue
    return Calculate(sayilar,islemler)

def yesParanthese(exp):

    sayi = ""
    sayilar = [] 
    islemler = [] 
    for i, item in enumerate(exp):
        if item == "*":
            sayilar.append(sayi)
            sayi = ""
            islemler.append("*")
        elif item == "+":
            sayilar.append(sayi)
            sayi = ""
            islemler.append("+")
        else:
            sayi += item
    sayilar.append(sayi)

    a = CalculateAdvanced(sayilar,islemler)
    return a
        

def noParanthese(exp):
    if '(' not in exp:
        return yesParanthese(exp)
    
    for i,item in enumerate(exp):
        if item =="(":
            count =0
            for j in range(i+1,len(exp)):
                if exp[j]=="(":
                    count +=1
                if exp[j]==")":
                    if count ==0:
                        parantezin_ici = noParanthese(exp[i+1:j])
                        yeni_exp = exp[0:i]+str(parantezin_ici) + exp[j+1:]
                        return noParanthese(yeni_exp)
                    else: 
                        count -=1



file1 = open("data_18.txt", "r")
Lines = file1.readlines()


summ = 0
for line in Lines:
    summ += noParanthese(line)
print(summ)
