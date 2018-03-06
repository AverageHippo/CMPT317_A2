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

        self.board = [[0,0,0, self.p1p1, 0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]



    def printboard(self):
        print(self.board)


if __name__ == '__main__':
    B = Board()
    B.printboard()

