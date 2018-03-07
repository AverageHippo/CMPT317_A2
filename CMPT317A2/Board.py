from copy import deepcopy


class Board:
    def __init__(self):
        self.p1p1 = "Q"
        self.p1p2 = "D1"
        self.p1p3 = "D2"
        self.p1p4 = "D3"
        self.p2p1 = "W1"
        self.p2p2 = "W2"
        self.p2p3 = "W3"
        self.p2p4 = "W4"
        self.p2p5 = "W5"

        # self.board = [0,0,0, self.p1p1, 0,0, 0,self.p1p2,self.p1p3,self.p1p4,0,0,0,0,0,0, 0,0,0,0,0, self.p2p1, self.p2p2, self.p2p3,
        #                                                                            self.p2p4, self.p2p5,]


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



    def printboard(self):
        print(self.board)


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

        if (positionX or positionY) < 0:
            print("Position out of bound")
            return False
        elif (positionX or positionY) > 4:
            print("Position out of bound")
            return False
        elif ( p == "W1" or "W2" or "W3" or "W4" or "w5") :
            if (positionX == i + 1 or positionX == i-1 or positionX == i) \
                    and (positionY == j-1 or positionY == j+1 or positionY ==j)\
                    and not (positionX == i + 1 and positionY == j+1)\
                    and not (positionX == i - 1 and positionY == j-1)\
                    and not (positionX == i + 1 and positionY == j-1)\
                    and not (positionX == i - 1 and positionY == j+1):
                return True
            else:
                return False
        elif ( p == "Q" ) :
            print(i,j)
            if (positionX == i + 1 or positionX == i-1 or positionX == i ) \
                    and (positionY == j-1 or positionY == j+1 or positionY ==j):
                return True
            else:
                return False
        elif ( p == "D1" or "D2" or "D3" ) :
            print(i,j)
            if (positionX == i + 1 or positionX == i-1 or positionX == i ) \
                    and (positionY == j-1 or positionY == j+1 or positionY ==j):
                return True
            else:
                return False
        else:
            return False


    def getIndex(self, p):
        for i, e in enumerate(self.board):
                for j, ee in enumerate(e):
                    if p in ee:
                        return i, j


    def move(self, piecee, positionX, positionY):
        p = self.translate(piecee)
        i ,j = self.getIndex(p)

        if self.isPossibleMove(p,positionX,positionY) == True:
            print("Move is possible, Moving :", p, "to index : ", positionX,positionY )
            self.board[i][j] = "*"
            self.board[positionX][positionY] = p
        else:
            print("The Move you requested is not possible")




if __name__ == '__main__':
    B = Board()
    B.printboard()
    print(B.translate("W2"))
    B.move("W2", 3 , 1)
    B.printboard()
    B.move("W2", 2 , 1)
    B.printboard()



