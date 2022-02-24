"""
The 8-puzzle will be represented by a one-dimensional array populated with numbers 1-9, with 9 representing the blank space
"""

class Node:
    def __init__(self, board, cost):
        self.board = board
        self.cost = cost

    def __hash__(self):
        return hash(self.board, self.cost)

    def __eq__(self, other):
        return (self.board, self.cost) == (other.board, other.cost)



