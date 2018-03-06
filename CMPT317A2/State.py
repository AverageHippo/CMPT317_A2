from tkinter import Tk, Button
from tkinter.font import Font
from copy import deepcopy

class State:
    def __init__(self, other = None):
        self.player1
        self.player2
        self.piece1 = pieces.Queen
        self.piece2, self.piece3, self.piece4 = 'D'
        self.piece5, self.piece6, self.piece7, self.piece8, self.piece9 = 'W'
        self.size = 5
        self.spaces = '.'
        self.board = {}
        for y in range(self.size):
            for x in range(self.size):
                self.board[x, y] = self.spaces
                self.board[0, 2] = self.piece1
                self.board[1, 1] = self.piece2
                self.board[1, 2] = self.piece3
                self.board[1, 3] = self.piece4
                self.board[4, 0] = self.piece5
                self.board[4, 1] = self.piece6
                self.board[4, 2] = self.piece7
                self.board[4, 3] = self.piece8
                self.board[4, 4] = self.piece9
                print(self.board)
        if other:
            self.__dict__ = deepcopy(other.__dict__)

    def pieces(self):
        Queen = 'Q'
        Dragon = 'D'
        Wight = 'W'

    def moves(self, x, y):
        board = State(self)

class GUI:
    def __init__(self):
        self.app = Tk()
        self.app.title('Wights and Dragons')
        self.app.resizable(height=False, width=False)
        self.board = State()
        self.font = Font(family="Arial", size=24)
        self.buttons = {}
        for x,y in self.board.spaces:
            listener = lambda x=x, y=y: self.move(x,y)
            button = Button(self.app, command=listener, font=self.font, width=2, height=2)
            button.grid(row=y, column=x)
            self.buttons[x,y] = button
        listener = lambda: self.reset()
        button = Button(self.app, text='reset', command=listener)
        button.grid(row=self.board.size + 1, column=0, columnspan=self.board.size, sticky="Hello")
        self.update()

    def mainloop(self):
        self.app.mainloop()

if __name__ == '__main__':
  GUI().mainloop()





