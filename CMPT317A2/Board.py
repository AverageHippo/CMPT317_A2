from copy import deepcopy
from operator import eq
from random import randint



class Board:

    def __init__(self, player=1):
        self.p1p1 = "Q"
        self.p1p2 = "D1"
        self.p1p3 = "D2"
        self.p1p4 = "D3"
        self.p2p1 = "W1"
        self.p2p2 = "W2"
        self.p2p3 = "W3"
        self.p2p4 = "W4"
        self.p2p5 = "W5"

        row , col = 5,5

        self.board = [["*" for row in range(row)] for col in range(col)]
        self.board[0][2] = self.p1p1
        self.board[1][1] = self.p1p2
        self.board[1][2] = self.p1p3
        self.board[1][3] = self.p1p4
        self.board[4][0] = self.p2p1
        self.board[4][1] = self.p2p2
        self.board[4][2] = self.p2p3
        self.board[4][3] = self.p2p4
        self.board[4][4] = self.p2p5
        self.turn = player
        self.human = None
        self.AI = None



    def selectPlayer(self):

        player = input("Select P1 or P2: ")
        if player == "P1":
            self.human = 1
            self.AI = 2
        elif player == "P2":
            self.human = 2
            self.AI = 1


    def getHuman(self):
        return self.human

    def create():
        return Board()

    def printboard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end='  ')
            print()





    def translate(self, piece):
        p = ""

        if piece=="Q":
            p = self.p1p1
        elif piece=="D1":
            p = self.p1p2
        elif piece=="D2":
            p = self.p1p3
        elif piece=="D3":
            p = self.p1p4
        elif piece=="W1":
            p = self.p2p1
        elif piece=="W2":
            p = self.p2p2
        elif piece=="W3":
            p = self.p2p3
        elif piece=="W4":
            p = self.p2p4
        elif piece=="W5":
            p = self.p2p5
        return p


    def isPossibleMove(self, p, positionX, positionY):
        i ,j = self.getIndex(p)

        currentPlace , opening = self.checkOpening(positionX, positionY)


        # This is the boundary exceptation check for both the X and Y axis.
        if (positionX or positionY) < 0:
            print("Position out of bound")
            return False
        elif (positionX or positionY) > 4:
            print("Position out of bound")
            return False

        # Possible moves or Whites
        elif p =='W2' or p =='W1' or p =='W3' or p =='W4' or p =='W5' or p == 'W' :

            if (positionX == i + 1 or positionX == i-1 or positionX == i) \
                    and (opening==True) \
                    and (positionY == j-1 or positionY == j+1 or positionY ==j)\
                    and (( not (positionX == i + 1 and positionY == j+1)
                    and not (positionX == i - 1 and positionY == j-1)
                    and not (positionX == i + 1 and positionY == j-1)
                    and not (positionX == i - 1 and positionY == j+1))):

                return True

            elif opening ==False:

                # If the position we want to move is already taken, So capture time
                # Cannot capture the same side pawns, Thats canibilism
                if (currentPlace == "W" or  currentPlace == "W1" or  currentPlace == "W2" or  currentPlace == "W3" or  currentPlace == "W4" or  currentPlace == "W5"):
                    # print("-- Want to capture your own pawn ( Whites ) -- LOLOLOL")

                    return False

                # only when the position we ant to move is diagional and not whites and there is a pawn
                elif  (positionX == i + 1 and positionY == j+1)\
                        or (positionX == i - 1 and positionY == j-1)\
                        or (positionX == i + 1 and positionY == j-1)\
                        or (positionX == i - 1 and positionY == j+1)\
                        and ((currentPlace is "Q")  or (currentPlace is "D1") or (currentPlace is "D2") or (currentPlace is "D3")):
                    self.capture(p, positionX, positionY, currentPlace)
                    # print("eating Q or D")
                    return True
                else:
                    return False

            return False

        # Posible matches for Queens
        elif ( p == "Q" ) :

            if (positionX == i + 1 or positionX == i-1 or positionX == i ) \
                    and (positionY == j-1 or positionY == j+1 or positionY ==j)\
                    and opening == True\
                    and (currentPlace is not "Q" or currentPlace is not  "D1" or currentPlace is not "D2" or\
                         currentPlace is not "D3" or currentPlace is not  "D"):
                return True
            elif opening == False and (currentPlace is "Q" or currentPlace is "D1" or currentPlace is "D2" or
                                       currentPlace is  "D3" or currentPlace is  "D"):
                # print("Q is trying to eat other pawns in same player. ")
                return False

            elif opening==False and (currentPlace is "W" or currentPlace is "W1" or currentPlace is "W2" or
                                       currentPlace is  "W3" or currentPlace is  "W4" or currentPlace is "W5"):
                self.capture(p, positionX, positionY, currentPlace)
                # print("eating W")
                return True
            else:
                return False
        # Possible moves for Dragon
        elif p == "D1" or  "D2" or "D3"  :

            if (positionX == i + 1 or positionX == i-1 or positionX == i ) \
                    and (positionY == j-1 or positionY == j+1 or positionY ==j)\
                    and opening == True\
                    and (currentPlace is not "Q" or currentPlace is not "D1" or currentPlace is not  "D2" or
                    currentPlace is not "D3" or currentPlace is not "D"):
                return True
            elif opening == False and currentPlace is "Q" or currentPlace is "D1" or currentPlace is "D2" or currentPlace is "D3" or\
                    currentPlace is "D":
                # print("Dragon is trying to eat other pawns in same player. ")
                return False
            elif opening==False and (currentPlace is "W" or currentPlace is "W1" or currentPlace is "W2" or
                                       currentPlace is  "W3" or currentPlace is  "W4" or currentPlace is "W5"):
                self.capture(p, positionX, positionY, currentPlace)
                # print("eating W")
                return True
            else:
                return False

        else:
            return False



    def capture(self, attacker, positionX, positionY, enemny):
        captured = {}

        print("Attack with : ", attacker, "Capture : ", enemny, "In position :", positionX, positionY)
        return True


    def checkOpening(self, positionX, positionY):

        if (positionX or positionY) < 0:
            print("Position out of bound")
            return "", True
        elif (positionX or positionY) > 4:
            print("Position out of bound")
            return "", True
        else:
            if self.board[positionX][positionY] == "W1":
                return "W1" , False
            elif self.board[positionX][positionY] == "W2":
                return "W2" , False
            elif self.board[positionX][positionY] == "W3":
                return "W3" , False
            elif self.board[positionX][positionY] == "W4":
                return "W4" , False
            elif self.board[positionX][positionY] == "W5":
                return "W5" , False
            elif self.board[positionX][positionY] is 'Q':
                return "Q", False
            elif self.board[positionX][positionY] is 'D1':
                return "D1", False
            elif self.board[positionX][positionY] is 'D2':
                return "D2", False
            elif self.board[positionX][positionY] is 'D3':
                return "D3", False
            else:
                return "" , True




    def getIndex(self, p):

        for i, e in enumerate(self.board):
                for j, ee in enumerate(e):
                    if p in ee:
                        return i, j

    def inputMove(self):
        flag = False
        while flag == False:
            who = input("Who ")
            X = int(input("Where in X cordinate"))
            Y = int(input("Where in Y cordinate"))
            flag = self.move(who,X,Y)
        self.togglePlayer()
        return self



    def str(self):
        s = ''
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                s += str(self.board[j][i])
        return s


    def move(self, piecee, positionX, positionY):
        p = self.translate(piecee)
        i ,j = self.getIndex(p)
        alive , _,_ = self.isAlive(p)

        if self.isPossibleMove(p,positionX,positionY) == True and (alive== True):
            # print("Move is possible, Moving :", p, "to index : ", positionX,positionY )
            self.board[i][j] = "*"
            self.board[positionX][positionY] = p
            return True

        else:
            # print("The Move you requested is not possible")
            return False


    def player1(self, p):
        if p =='W2' or p =='W1' or p =='W3' or p =='W4' or p =='W5' or p == 'W':
            return True
        else:
            return False

    def player2(self, p):
        if p =='D1' or p =='D2' or p =='D3' or p =='D' or p =='Q':
            return True
        else:
            return False



    def isAlive(self, player1):
        try:
            x,y = self.getIndex(player1)
            return True, x, y

        except TypeError:
            print("No such pawn exists")
            return False



    def utility(self,player):
        # if player == "Q" :
        #     return 1
        # if (player == "W1" or player == "W2" or player == "W3" or player == "W4" or player == "W5") :
        #     return -1
        # else:
        #     return 0
        return randint(0, 9)


    def isTerminal(self):
        if(self.board[4][0] or self.board[4][1] or self.board[4][2] or self.board[4][3] or self.board[4][4]) == "Q":
            return True
        elif (self.board[0][0] or self.board[0][1] or self.board[0][2] or self.board[0][3] or self.board[0][4]) == "W1":
            return True
        elif (self.board[0][0] or self.board[0][1] or self.board[0][2] or self.board[0][3] or self.board[0][4]) == "W2":
            return True
        elif (self.board[0][0] or self.board[0][1] or self.board[0][2] or self.board[0][3] or self.board[0][4]) == "W3":
            return True
        elif (self.board[0][0] or self.board[0][1] or self.board[0][2] or self.board[0][3] or self.board[0][4]) == "W4":
            return True
        elif (self.board[0][0] or self.board[0][1] or self.board[0][2] or self.board[0][3] or self.board[0][4]) == "W5":
            return True
        else:
            return False


    def togglePlayer(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

        return self.turn


    def isMinNode(self):
        if self.turn == 2:
            return True
        else:
            return False

    def isMaxNode(self):
        if self.turn == 1:
            return True
        else:
            return False

    def whoseTurn(self):
        return self.turn



if __name__ == '__main__':


    # # Movement for Dragon Test
    B = Board()
    B.printboard()
    B.inputMove()

    # Possible moves for D1
    # print("the check", B.checkOpening(3,3))
    # B.move("W5", 3,3)
    # B.move("D1", 1,0)
    # B.move("D1", 1,1)
    # B.move("D1", 0,2) #cannot
    # B.move("D3", 1,4)
    # B.move("D2", 0,2)
    # B.move("D2", 2,2)
    # B.move("D2", 1,2)
    # B.move("D2", 1,3)
    # Not possible moves
    # B.move("Q", 1,1)
    # B.move("Q", 1,2)
    # B.move("Q", 1,3)
    # x = B.win()
    # print(x)
    # B = Board()
    # B.printboard()
    # print("the check", B.checkOpening(3,1))
    # B.move("W2", 3 , 1)
    # print(B.checkOpening(3,1))
    # B.printboard()
    # B.move("W2", 2, 1)
    # B.printboard()
    # print("---",B.checkOpening(1,2))
    # B.move("Q", 1, 2)
    # B.printboard()
    # print(B.checkOpening(1,2))
    # B.move("Q", 1, 1)
    # B.printboard()
    # print(B.checkOpening(1,1))

    # Check to see if the checkOpening method is working or not
    # print(B.checkOpening(0,2))
    # print(B.checkOpening(1,1))
    # print(B.checkOpening(1,2))
    # print(B.checkOpening(1,3))
    # print(B.checkOpening(4,0))
    # print(B.checkOpening(4,3))
    # print(B.checkOpening(4,4))

    # Movement for Queen Test
    # B = Board()
    # B.printboard()
    # # Possible moves
    # B.move("Q", 0,1)
    # B.move("Q", 0,2)
    # B.move("Q", 0,3)
    # B.move("Q", 0,2)
    # # Not possible moves
    # B.move("Q", 1,1)
    # B.move("Q", 1,2)
    # B.move("Q", 1,3)

    # checking to see if Wight is working or not
    # B.move("W1", 3,0)
    # B.move("W2", 3,1)
    # B.move("W3", 3,2)
    # B.move("W4", 3,3)
    # B.move("W5", 3,4)
    # B.printboard()
    # B.move("W1", 2, 0)
    # B.move("W2", 2, 1)
    # B.move("W3", 2, 2)
    # B.move("W4", 2, 3)
    # B.move("W5", 2, 4)
    # B.printboard()
    # print(B.checkOpening(1,1))
    # B.move("W1", 1, 1)
    # B.move("W4", 1, 2)
    # B.printboard()

    # B.move("W3", 1,4)
    # B.move("D", 0,2)
    # B.move("D2", 2,2)
    # B.move("D2", 1,2)
    # B.move("D2", 1,3)








