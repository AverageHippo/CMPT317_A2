from Board import Board as B

def Minimax(start):

    def commenceMinimax(node):
        if S in transpose:
            return transpose[S]
        elif isLeaf(node):
            val = node.win()
            move = None
            res = None
        else:
            possiblemoves = node.successor(b, player)
            value = []

            for move, res in possiblemoves:
                val, _, _, = commenceMinimax(res)
                value.append((val, move, res))

            if node.isMaxNode():
                val, move, res = maxValue(value)
            elif node.isMinNode():
                val, move, res = minValue(value)
            else:
                print("Fatal error occurred, something isn't collecting values")
                return None
        transpose[S] = val, move, res
        return val, move, res

    def maxValue(node):
        print("we're in here, that's a relief")
        maxValue, maxMove, maxState = ns[0]
        for v,m,s in ns:
            if v > maxValue:
                maxValue, maxMove, maxState = v, m, s
        return maxValue, maxMove, maxState

    def minValue(node):
        print("We're in here, thank cthulu")
        minValue, minMove, minState = ns[0]
        for v, m, s in ns:
            if v < minValue:
                minValue, minMove, minState = v, m, s
        return minValue, minMove, minState


    def isLeaf(node):
        assert node is not None
        return len(node.children) == 0



