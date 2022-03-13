#!/usr/bin/env python
"""
The 8-puzzle will be represented by a one-dimensional array populated with numbers 0-15, with 0 representing the blank space
"""

import random 
import copy

class Node:
    def setDistance(board):
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        dist = 0
        for i in range(1, 16):
            b = board.index(i)
            g = goal.index(i)
            dist += abs((b % 4) - (g % 4)) + abs((b // 4) - (g // 4))
        return dist

    def __init__(self, board, cost, parent, move, dist):
        self.board = board
        self.cost = cost
        self.parent = parent
        self.move = move
        self.dist = dist

    def __hash__(self):
        return hash(self.board, self.cost, self.parent, self.move)

    def __eq__(self, other):
        return (self.board) == (other.board)




class PriorityQueue:
    def __init__(self, queue):
        self.queue = queue
    
    def __hash__(self):
        return hash(self.queue)

    def __eq__(self, other):
        return (self.queue) == (other.queue)

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    

    def siftUp(self):
        if(len(self.queue) == 1):
            return

        p = len(self.queue) - 1

        while(p != 0):
            parent = (p - 1) // 2
            if(self.queue[parent].dist < self.queue[p].dist):
                return

            temp = self.queue[parent]
            self.queue[parent] = self.queue[p]
            self.queue[p] = temp

            p = parent
    
    def siftDown(self):
        p = 0
        while(2 * p + 1 < len(self.queue)):
            leftChild = 2 * p + 1
            rightChild = leftChild + 1
            minChild = leftChild

            if(rightChild < len(self.queue)):
                if(self.queue[rightChild].dist < self.queue[leftChild].dist):
                    minChild = rightChild

            if(self.queue[minChild].dist > self.queue[p].dist):
                return

            temp = self.queue[minChild]
            self.queue[minChild] = self.queue[p]
            self.queue[p] = temp

            p = minChild


    def add(self, node):
        self.queue.append(node)
        self.siftUp()

    def pop(self):
        queue = self.queue

        node = self.queue[0]
        last = len(self.queue) - 1
        self.queue[0] = self.queue[last]
        
        self.queue.pop(last)
        self.siftDown()
        return node


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




def generateStart(board):
    for i in range(500):
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


def setDistance(board):
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    dist = 0
    for i in range(1, 16):
        b = board.index(i)
        g = goal.index(i)
        dist += abs((b % 4) - (g % 4)) + abs((b // 4) - (g // 4))
    return dist


def getMoves(node):
    moves = []
    currentBoard = copy.copy(node.board)
    cost = copy.copy(node.cost)
    index = node.board.index(0)
    if(index > 3):
        north = Node(moveNorth(currentBoard, index), cost + 1, node, "N", setDistance(moveNorth(currentBoard, index)))
        moves.append(north)
    if(index < 12):
        south = Node(moveSouth(currentBoard, index), cost + 1, node, "S", setDistance(moveSouth(currentBoard, index)))
        moves.append(south)
    if(index % 4 < 3):
        east = Node(moveEast(currentBoard, index), cost + 1, node, "E", setDistance(moveEast(currentBoard, index)))
        moves.append(east)
    if(index % 4 > 0):
        west = Node(moveWest(currentBoard, index), cost + 1, node, "W", setDistance(moveWest(currentBoard, index)))
        moves.append(west)
    
    return moves

def aStarSearch(start, solved):
    frontier = PriorityQueue([])
    visited = []
    
    root = Node(start, 0, None, None, setDistance(start))
    frontier.add(root)

    while(frontier):
        node = frontier.pop()

        if(node.board == solved):
            printResults(node)
            return(node)

        if(node not in visited):
            visited.append(node)
            moves = getMoves(node)

            for move in moves:
                frontier.add(move)

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


solved = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
start = generateStart(solved)
for i in start:
    print(i, end=" ")
print()
print("A* Search")
aStarSearch(start, solved)
