# The search space is a tree, but the state space is a graph: there may be several different ways to
# reach a given game state.
#
# The transposition table is a dictionary (hash table) that remembers if
# a game state was seen before, and it it was, what its minimax value is.
# Warning: The transposition table can fill up quickly!

from Board import Board as B

def minimax(start):
    """
    MINIMAX returns VALUE,MOVE,STATE
    with TRANSPOSITION TABLE

    :param start:  a Game object responding to the following methods:
        str(): return a unique string describing the state of the game (for use in hash table)
        isTerminal(): checks if the game is at a terminal state
        utility(): obtain the value of a terminal node
        successors(): returns a list of all legal game states that extend this one by one move
                      in this version, the list consists of a move,state pair
        isMinNode(): returns True if the node represents a state in which Min is to move
        isMaxNode(): returns True if the node represents a state in which Max is to move
    :return: a pair, u,m consisting of the minimax utility, and a move that obtains it
    """

    transpositionTable = dict()
    depth = 10

    def do_minimax(node, depth):

        s = node.str()
        if s in transpositionTable:
            return transpositionTable[s]
        elif node.isTerminal() or depth < 0:
            val = node.utility()
            my_move = None
            res_state = None
        else:
            possibilities = node.successors()

            values = []
            for my_move,res_state in possibilities:
                val, _, _ = do_minimax(res_state, depth-1)
                depth = depth -1
                values.append( (val, my_move, res_state) )

            if node.isMaxNode():
                val,my_move,res_state = argmax(values)
            elif node.isMinNode():
                val,my_move,res_state = argmin(values)
            else:
                print("Something went horribly wrong")
                return None

        transpositionTable[s] = val, my_move, res_state  # store the move and the utility in the tpt
        return val,my_move,res_state

    return do_minimax(start, 10)


def argmax(ns):
    """
    find the highest utility,move pair
    :param ns: a list of utility,move pairs
    :return:  the utility,move pair with the highest utility
    """

    maxv,maxm,maxs = ns[0]
    for v,m,s in ns:
        if v > maxv:
            maxv,maxm,maxs = v,m,s
    return maxv,maxm,maxs


def argmin(ns):
    """
    find the lowest utility,move pair
    :param ns: a list of utility,move pairs
    :return:  the utility,move pair with the lowest utility
    """

    minv,minm,mins = ns[0]
    for v,m,s in ns:
        if v < minv:
            minv,minm,mins = v,m,s
    return minv,minm,mins



# we need a evaluation finction that evaluates the moves per state
# to make sure that we are in the right place, we need to make sure that the utility function is working,
# that means that everything should work perfectly.
# this is not the working copy, sorry
