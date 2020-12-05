def F(min,max):
    rowmax = int((min+max)/2)
    return rowmax

def B(min,max):
    rowmin = int((min+max)/2)+1
    return rowmin


def findRow(Lines):
    maxid = 0
    minid = 1008
    all_seats = list(range(89,990))
    for line in Lines: 
        rowmin = 0 
        rowmax =127
        seatmin=0
        seatmax=7
        seatid=0
        for item in line:
            if item == 'B':
                rowmin = B(rowmin,rowmax)
            if item == 'F':
                rowmax = F(rowmin,rowmax)
            if item == 'L':
                seatmax = F(seatmin,seatmax)            
            if item == 'R':
                seatmin = B(seatmin,seatmax)
        #print(rowmin,rowmax,seatmin,seatmax)
        seatid = rowmin * 8 + seatmin
        print(seatid)
        print(all_seats[seatid-89])
        all_seats[seatid-89] = 0 
        if seatid > maxid:
                maxid = seatid
        if seatid < minid:
                minid= seatid
    print(maxid,minid)
    print(sum(all_seats))




if __name__ == '__main__':
    file1 = open("data_05.txt", "r")
    Lines = file1.readlines()
    findRow(Lines)
