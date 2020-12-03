def isTree(line,linecount,right,char):
    target = (right * linecount) % char
    if line[target] == '#':
        print("agac:satir:{}, kural{}".format(linecount,right))
        return 1
    else :
        return 0 


def countTrees(Lines):
    linecount = 0
    char = 31
    treecount_3_1=0
    treecount_1_1=0
    treecount_5_1=0
    treecount_7_1 = 0 
    treecount_1_2 = 0 
    for line in Lines: 
        treecount_3_1+= isTree(line,linecount,3,char)
        treecount_1_1+= isTree(line,linecount,1,char)
        treecount_5_1+= isTree(line,linecount,5,char)
        treecount_7_1+= isTree(line,linecount,7,char)
        if (linecount % 2) == 0:
            treecount_1_2+=isTree(line,int(linecount/2),1,char)
        
        linecount +=1
    print("1_1: {} 3_1:{} 5_1:{} 7_1:{} 1_2:{}".format(treecount_1_1,treecount_3_1,
        treecount_5_1,treecount_7_1,treecount_1_2))
    print(treecount_3_1 * treecount_1_1 * treecount_5_1 *
            treecount_7_1 *treecount_1_2)



if __name__ == '__main__':
	file1 = open("data_03.txt", "r")
	Lines = file1.readlines() 
	countTrees(Lines)