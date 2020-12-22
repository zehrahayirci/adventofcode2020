def calculateScore(liste):
    number = len(liste)
    score=0
    while number>0:
        score += number * liste.pop(0)
        number-=1
    print(score)

def classicGame(player1,player2):
    while len(player1)>0 and len(player2)>0:
        number_1=player1.pop(0)
        number_2=player2.pop(0)
        if number_1 > number_2:
            player1.append(number_1)
            player1.append(number_2)
        elif number_2 > number_1:
            player2.append(number_2)
            player2.append(number_1)
        print(number_1,number_2)
        print(player1)
        print(player2)
    if len(player1) == 0:
        return 2
    else:
        return 1

def new_game(player1, player2, deep):
    history = []
    while len(player1)>0 and len(player2)>0:
        state1 = "_".join(map(str,player1))
        state2 = "_".join(map(str,player2))
        state = (state1, state2)
        #print(player1, player2)
        if state in history:
            # player1 wins
            return 1
        else:
            history.append(state)
            n1 = player1[0]
            n2 = player2[0]
            if len(player1[1:]) >= n1 and len(player2[1:]) >= n2:
                winner = new_game(player1[1:n1+1], player2[1:n2+1], deep+1)
            else:
                if n1>n2:
                    winner = 1
                else:
                    winner = 2
        
        if winner == 1:
            player1.append(n1)
            player1.append(n2)
            player1 = player1[1:]
            player2 = player2[1:]
        else:
            player2.append(n2)
            player2.append(n1)
            player1 = player1[1:]
            player2 = player2[1:]

    if deep<1:
        if len(player1) == 0:
            calculateScore(player2)
        else:
            calculateScore(player1)
    else:
        if len(player1) == 0:
            return 2
        else:
            return 1

file1=open("data_22.txt","r")
Lines = file1.read()
print(Lines)
a=Lines.split("\n\n")
p_1=a[0].split("\n")
p_2=a[1].split("\n")
print(p_1)
print(p_2)
player1 = []
player2 = []
for item in p_1[1:]:
    player1.append(int(item))
for item in p_2[1:]:
    player2.append(int(item))


#classicGame(player1,player2)
new_game(player1,player2,0)


