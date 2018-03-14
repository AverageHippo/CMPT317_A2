from Board import Board as B
import Successor as S

def Minimax(start):

    transpositionTable = dict()
    player = B.whoseTurn(start)

    def do_minimax(node, counter):
        if counter > 0:
            counter -= 1
            s = B.str(node)
            if s in transpositionTable:
                return transpositionTable[s]
            elif B.isTerminal(node):
                u = B.utility(node, player)
            else:
                vs = [do_minimax(c, counter-1) for c in S.successor(node)]
                if B.isMaxNode(node):
                    u = max(vs)
                elif B.isMinNode(node):
                    u = min(vs)
                else:
                    print("something went wrong")
                    return None
            transpositionTable[s] = u
            print(transpositionTable[s])
            return u
        else:
            return 0

    # result = do_minimax(start, 10)
    # print(result)
    return do_minimax(start, 10)


# def playGame(New):
#
#     player = B.whoseTurn(New)
#     B.selectPlayer(New)
#     while B.utility(New, player) != (1 or 0 or -1):
#         print("Player", B.whoseTurn(New), "Move")
#         if B.getHuman(New) == B.whoseTurn(New):
#             player = B.inputMove(New)
#         m = Minimax(player)
#         # print(m)
#

if __name__ == '__main__':
    New = B.create()
    # print(B.whoseTurn(New))
    # playGame(New)
    Minimax(New)


