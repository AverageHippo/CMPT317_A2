from Board import Board as B
from copy import deepcopy


def successor(state, player):

    player1 = ["W1", "W2", "W3", "W4", "W5"]

    succssor = []

    if (player==1):

        for i in player1:
            isA, x, y = B.isAlive(state, i)
            if (isA == True):
                for r in 0,1,-1:
                    for c in 0,1,-1:

                        if ( (x+r) > 4 or (y+c) > 4) or ((x+r) <0  or (y+c) <0):
                            continue
                        else:

                            possible = B.isPossibleMove(state, i, x+r,y+c )
                            # print(possible)
                            if possible == True:
                                print("The player - ", i,  x+r,y+c)
                                newState = deepcopy(state)
                                newMove = B.move(newState, i,x+r,y+c)
                                if newMove == True:
                                    succssor.append(newState)
        #
        print("Printing -- ", succssor)


    elif(player==2):
        return 2


    else:
        return 0


if __name__ == '__main__':

    New = B.create()
    B.move(New, "W1", 3,0)
    successor(New, 1)


