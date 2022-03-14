#!/usr/bin/env python
"""
The 8-puzzle will be represented by a one-dimensional array populated with numbers 0-15, with 0 representing the blank space
"""

import random 
import copy

class Node:
    def __init__(self, board, cost, parent, move):
        self.board = board
        self.cost = cost
        self.parent = parent
        self.move = move

    def __hash__(self):
        return hash(self.board, self.cost, self.parent, self.move)

    def __eq__(self, other):
        return (self.board) == (other.board)

def moveNorth(board, index):
    tempBoard = copy.copy(board)
    temp = tempBoard[index]
    tempBoard[index] = tempBoard[index - 4]
    tempBoard[index - 4] = temp
    return tempBoard

def moveSouth(board, index):
    tempBoard = copy.copy(board)
    temp = tempBoard[index]
    tempBoard[index] = tempBoard[index + 4]
    tempBoard[index + 4] = temp
    return tempBoard

def moveEast(board, index):
    tempBoard = copy.copy(board)
    temp = tempBoard[index]
    tempBoard[index] = tempBoard[index + 1]
    tempBoard[index + 1] = temp
    return tempBoard

def moveWest(board, index):
    tempBoard = copy.copy(board)
    temp = tempBoard[index]
    tempBoard[index] = tempBoard[index - 1]
    tempBoard[index - 1] = temp
    return tempBoard



solved = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

def generateStart(board):
    for i in range(5):
        index = board.index(0)
        move = random.randint(1, 4)
        if(move == 1):
            if(index > 3):
                board = moveNorth(board, index)
        if(move == 2):
            if(index < 12):
                board = moveSouth(board, index)
        if(move == 3):
            if(index % 4 < 3):
                board = moveEast(board, index)
        if(move == 4):
            if(index % 4 > 0):
                board = moveWest(board, index)
    return board



def getMoves(node):
    moves = []
    currentBoard = copy.copy(node.board)
    cost = copy.copy(node.cost)
    index = node.board.index(0)
    if(index > 3):
        north = Node(moveNorth(currentBoard, index), cost + 1, node, "N")
        moves.append(north)
    if(index < 12):
        south = Node(moveSouth(currentBoard, index), cost + 1, node, "S")
        moves.append(south)
    if(index % 4 < 3):
        east = Node(moveEast(currentBoard, index), cost + 1, node, "E")
        moves.append(east)
    if(index % 4 > 0):
        west = Node(moveWest(currentBoard, index), cost + 1, node, "W")
        moves.append(west)
    
    return moves

def bfs(start, solved):

    frontier = []
    visited = []

    root = Node(start, 0, None, None)
    frontier.append(root)
    

    while(frontier):
        
        node = frontier.pop(0)

        if(node.board == solved):
            printResults(node)
            return node

        if(node not in visited):
            visited.append(node)
            
            moves = getMoves(node)

            for move in moves:
                frontier.append(move)


def dfs(start, solved):
    frontier = []
    visited = []

    root = Node(start, 0, None, None)
    frontier.append(root)

    while(frontier):
        
        node = frontier.pop(len(frontier) - 1)
        visited.append(node)

        if(node.board == solved):
            printResults(node)
            return node
        
        moves = getMoves(node)
        for move in moves:
            if move not in visited:
                frontier.append(move)

def ids(start, solved):
    root = Node(start, 0, None, None)
    for i in range(0, 20):
        result = dls(root, solved, i)
        if(not isinstance(result, str)):
            printResults(result)
            return(result)
    return "FAILURE"


def dls(root, solved, depth):
    frontier = []
    frontier.append(root)

    while(frontier):
        node = frontier.pop(len(frontier) - 1)
        if(node.cost <= depth):
            moves = getMoves(node)
            for move in moves:
                frontier.append(move)

        if(node.board == solved):
            return(node)

    return "CUTOFF"
        



def printResults(node):
    results = []
    results.append(node)

    while(node.parent is not None):
        results.insert(0, node.parent)
        node = node.parent
        
    for node in results:
        if(node.move is not None):
            print(node.move, end=" ")
    
    print()

start = generateStart(solved)
for i in start:
    print(i, end=" ")
print()
print("Breadth-First Search:")
bfs(start, solved)
print("Depth-First Search:")
dfs(start, solved)
print("Iterative Deepening Search:")
ids(start, solved)
