#!/usr/bin/env python
#-*-coding: utf-8-*-

import sys, os
from Node import Node
import random
import numpy as np
import copy

def main():

	target = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
	tree = []
	distance = 1

	tree = generateRootPuzzle(target,tree)

	findMoves(tree[0])

	tree = generateNewPuzzle(tree[0],tree,distance,target)	

	result = aStar(tree[0],target)

def generateRootPuzzle(target,tree):

	root_puzzle = []
	while len(root_puzzle) < len(target):
		rand = random.randint(0,15)
		if rand not in root_puzzle:
			root_puzzle.append(rand)

	heuristic = calculateManhattanDistance(root_puzzle,target)
	tree.append((Node(puzzle =root_puzzle,distance =0,heuristic = heuristic)))

	findBlankIndex(tree[0].getPuzzle(),tree[0])

	return tree

def findBlankIndex(puzzle,node):

	for (index,i) in enumerate(puzzle):
		if i == 0:
			col =  index % 4  
			row =  (index - col) / 4

	node.setBlankIndex(row=row,col=col)

def findMoves(node):

	row,col = node.getBlankIndex()
	moves = []

	if row < 3:
		moves.append((row+1,col))
	if row > 0:
		moves.append((row-1,col))
	if col > 0:
		moves.append((row,col-1))
	if col < 3:
		moves.append((row,col+1))

	node.setMoves(moves)

def calculateManhattanDistance(puzzle,target):
	manhattan_distance = 0

	for (index_1,i) in enumerate(target):
		for (index_2,j) in enumerate(puzzle):
			if i == j:
				row_1,col_1 = findIndex(index_1)
				row_2,col_2 = findIndex(index_2)
				manhattan_distance += abs(row_2 - row_1) + abs(col_2 - col_1)

	return manhattan_distance 

def findIndex(index):
	
	col = index % 4
	row = (index - col) / 4
		
	return row,col

def printPuzzle(puzzle):

	print puzzle[:4]
	print puzzle[4:8]
	print puzzle[8:12]
	print puzzle[12:16]

def generateNewPuzzle(node,tree,distance,target):

	puzzle = node.getPuzzle()
	moves = node.getMoves()
	b_row,b_col = node.getBlankIndex()
	index1 = (4*b_row) + b_col

	while(len(moves)):
		mv = moves.pop()
		
		index2 = (4*mv[0]) + mv[1]
		new_puzzle = swap(puzzle,index1,index2)
		heuristic = calculateManhattanDistance(new_puzzle,target)
		tmp_node = Node(puzzle=new_puzzle,distance = distance,heuristic=heuristic)
		findBlankIndex(tmp_node.getPuzzle(),tmp_node)
		tree.append(tmp_node)

	return tree

def swap(puzzle,index1,index2):

	tmp_puzzle = puzzle[:]

	tmp = tmp_puzzle[index2]
	tmp_puzzle[index2]= tmp_puzzle[index1]
	tmp_puzzle[index1] = tmp

	return tmp_puzzle

def findMinNode(tree):

	minimum = 999
	for (index,node) in enumerate(tree):

		if node.total_distance < minimum:
			minimum = node.total_distance
			min_index = index

	return tree[min_index]

def aStar(start,target):
	paths = []
	path = []


	path.append(start)
	paths.append(path)

	while len(paths):
		
		minPathLength = 9999999999

		for path in paths:
			if minPathLength > path[-1].total_distance:
				minPathLength = path[-1].total_distance
				minPathElement = path

		if not minPathElement[-1].getHeuristic:
			return minPathElement

		findMoves(minPathElement[-1])
		moves = generateNewPuzzle(minPathElement[-1], [], path[-1].getDistance() + 1, target)
		
		for move in moves:
			tmp = copy.deepcopy(minPathElement)
			tmp.append(move)

			if tmp not in paths:
				paths.append(tmp)

		paths.remove(minPathElement)







if __name__ == '__main__':
	main();