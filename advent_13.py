
file1 = open("data_13.txt", "r")
number = int(file1.readline())
line = file1.readline()
liste = line.split(',')

print(liste)
plusminutes=[]
for i,n in enumerate(liste):
    if n != 'x':
        plusminutes.append(i)

while 'x' in liste:
    liste.remove('x')

liste = list(map(int, liste))
print(liste)
print(plusminutes)

minutes=[]
for eleman in liste:
    minutes.append(eleman-((number + eleman)%eleman))
    print(minutes)

min_index = minutes.index(min(minutes))
print(min_index)
print(minutes[min_index]*liste[min_index])

print("%%%%%Part Two%%%%%%%%%%%%%%")
a=1
for i,eleman in enumerate(liste):
    plusminutes[i] = (eleman - plusminutes[i]) % eleman

a = liste[0]
x = 0 
for i in range(1, len(liste)):
    k = 1 
    while True:
        if (k * a + x )%liste[i]==plusminutes[i]:
            x = k * a + x
            a = a * liste[i]
            break 
        k+=1
print(x)
