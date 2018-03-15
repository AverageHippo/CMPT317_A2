from Board import Board as B
import Successor as S
import sys

infinity = float('inf')
def Minimax(start):

    transpositionTable = dict()
    player = B.whoseTurn(start)

    def do_minimax(node, counter):
        s = B.str(node)
        if s in transpositionTable:
            return transpositionTable[s]
        elif B.isTerminal(node) or counter <= 0:
            #val= B.utility(node, player)
            val = B.queenDistanceHeuristic(node)
            res_state = None
        else:
            possibilities = S.successor(node)
            values = []
            for res_state in possibilities:
                val, _ = do_minimax(res_state, counter-1)
                values.append( (val, res_state) )
                # B.printboard(res_state)
            if B.isMaxNode(node):
                val,res_state = argmax(values)
            elif B.isMinNode(node):
                val,res_state = argmin(values)
            else:
                print("Something went horribly wrong")
                return None

        transpositionTable[s] = val, res_state  # store the move and the utility in the tpt
        return val, res_state

    return do_minimax(start, 5)



def argmax(ns):
    """
    find the highest utility,move pair
    :param ns: a list of utility,move pairs
    :return:  the utility,move pair with the highest utility
    """
    maxv,maxs = ns[0]
    for v,s in ns:
        if v > maxv:
            maxv,maxs = v,s
    return maxv,maxs


def argmin(ns):
    """
    find the lowest utility,move pair
    :param ns: a list of utility,move pairs
    :return:  the utility,move pair with the lowest utility
    """
    minv,mins = ns[0]
    for v,s in ns:
        if v < minv:
            minv,mins = v,s
    return minv,mins


def playGame(New):

    player = B.whoseTurn(New)
    B.selectPlayer(New)
    while B.utility(New, player) != (1 or 0 or -1):
        print("Player", B.whoseTurn(New), "Move")
        if B.getHuman(New) == B.whoseTurn(New):
            player = B.inputMove(New)
        m = Minimax(player)
        # print(m)

def AlphaBeta(node, counter):
    def Max(alpha, beta, counter):
        v = None
        if B.isTerminal(node) or counter <= 0:
            v = B.util(node)
        possibleMoves = S.successor(node)
        v = -infinity
        for i in possibleMoves:
            v = max(v, Min(alpha, beta, counter-1))
            if beta <= v:
                return v
            alpha = max(alpha, v)
        return v

    def Min(alpha, beta, counter):
        if B.isTerminal(node) or counter <= 0:
           v = B.util(node)
        possibleMoves = S.successor(node)
        v = infinity
        for i in possibleMoves:
            v = min(v, Max(alpha, beta, counter-1))
            if alpha >= v:
                return v
            else:
                alpha = min(beta, v, counter)
        return v
    score = -infinity
    beta = infinity
    bestMove = None
    for i in S.successor(node):
        v = (Min(score, beta, counter-1))
        if v > score:
            score = v
            bestMove = i
    return bestMove





if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    New = B.create()
    # B.togglePlayer(New)
    # print(B.whoseTurn(New))
    # playGame(New)
    for i in range(1):
        x,y = AlphaBeta(New, 2)
        # B.printboard(y)
        #B.togglePlayer(New)
        x1,New = AlphaBeta(y, 2)
        B.printboard(New)


