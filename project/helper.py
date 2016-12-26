#!/usr/bin/env python
# -*- coding: utf-8 -*-


import copy


def breadthFirstSearch(puzzle,target):

 	search_space = []
 	all_puzzles = []
 	search_space.append(puzzle)
 	all_puzzles.append(puzzle)

 	step = 0

 	while target not in all_puzzles and len(search_space) > 0:

 		tmp_puzzle = search_space.pop(0)

 		moves = createMoves(tmp_puzzle)
 		for move in moves:
 			copy_puzzle = copy.deepcopy(tmp_puzzle)
 			swap_result = swap(copy_puzzle,move[0],move[1])
 			if swap_result not in all_puzzles:
 				search_space.append(swap_result)
 				all_puzzles.append(swap_result)
		step +=1

	print "Breadth First Search Result : Puzzle Pool: %s Step Size:%s"%(len(all_puzzles),step)
 	if not len(search_space) > 0:
 		print "Result cannot Find"

def depthFirstSearch(puzzle,target):

	search_space = []
 	all_puzzles = []
 	search_space.append(puzzle)
 	all_puzzles.append(puzzle)
 	step = 0

 	depth = 0
 	while target not in all_puzzles and len(search_space) > 0 :

 		tmp_puzzle = search_space.pop(0)
 		moves = createMoves(tmp_puzzle)
 		for move in reversed(moves):
 			copy_puzzle = copy.deepcopy(tmp_puzzle)
 			swap_result = swap(copy_puzzle,move[0],move[1])
 			if swap_result not in all_puzzles:
 				search_space.insert(0,swap_result)
 				all_puzzles.insert(0,swap_result)
		step+=1
	print "depthFirst Search Result :Puzzle Pool: %s Step: %s"%(len(all_puzzles),step)

def bestFirstSearch(puzzle,target):
	distance = calculateManhattanDistance(puzzle,target)
	puzzle_values = {'puzzle':puzzle,
					 'distance': None}
	queue = [puzzle_values]
	path = []
	search_space = []
	find = False
	step = 0
	puzzle_pool = 1
	while find == False and len(queue) > 0:
		queue.sort(key=lambda x: x['distance'])
		current_puzzle = queue.pop(0)
		path.append(current_puzzle)
		search_space.append(current_puzzle)
		if current_puzzle['puzzle'] == target :
			find = True
		else:
			moves = createMoves(current_puzzle['puzzle'])
			for move in moves:
				copy_puzzle = copy.deepcopy(current_puzzle['puzzle'])
				swap_result = swap(copy_puzzle,move[0],move[1])
				distance = calculateManhattanDistance(swap_result,target)
				tmp_puzzle = {'puzzle':swap_result, 'distance':distance}
				if filter(lambda x: x['puzzle'] == tmp_puzzle['puzzle'], queue) == [] and tmp_puzzle not in search_space:
					queue.append(tmp_puzzle)
					#print tmp_puzzle
					puzzle_pool+=1
		step+=1

	
	print "Best First Search Result : Puzzle Pool Size:%s, Step Size: %s" %(puzzle_pool,step)
	# for puzzle in path:
	# 	print puzzle

def aStar(root,target):
	distance_t = calculateManhattanDistance(root,target)
	puzzle_values = {'puzzle':root,
					 'distance': distance_t}
	queue = [puzzle_values]
	path = []
	search_space = []
	find = False
	step = 0
	puzzle_pool = 1
	distance_r= 0
	while find == False and len(queue) > 0:
		queue.sort(key=lambda x: x['distance'])
		current_puzzle = queue.pop(0)
		search_space.append(current_puzzle)
		path.append(current_puzzle)
		if current_puzzle['puzzle'] == target :
			find = True
		else:
			moves = createMoves(current_puzzle['puzzle'])
			for move in moves:
				copy_puzzle = copy.deepcopy(current_puzzle['puzzle'])
				swap_result = swap(copy_puzzle,move[0],move[1])
				distance_t = calculateManhattanDistance(swap_result,target)
				distance_r = calculateManhattanDistance(swap_result,root)
				distance = distance_r + distance_t
				tmp_puzzle = {'puzzle':swap_result, 'distance':distance}
				if filter(lambda x: x['puzzle'] == tmp_puzzle['puzzle'], queue) == [] and tmp_puzzle not in search_space:
					queue.append(tmp_puzzle)
					#print tmp_puzzle
					puzzle_pool+=1
		step+=1

	print "AStar Result :Puzzle Pool Size:%s, Step Size: %s" %(puzzle_pool,step)
	# for puzzle in path:
	# 	print puzzle
def calculateManhattanDistance(puzzle,target):
	manhattan_distance = 0

	for (row_p,i) in enumerate(puzzle):
		for (col_p,j) in enumerate(i):
			if j == 0 :
				continue
			row_t,col_t = findIndex(target,j)
			manhattan_distance += abs(row_t - row_p) + abs(col_t - col_p)
			
	return manhattan_distance 


def createMoves(puzzle):

	row,col = findIndex(puzzle,0)
	moves = []

	if row > 0:
		moves.append((row-1,col))
	if col > 0:
		moves.append((row,col-1))
	if row < 3:
		moves.append((row+1,col))
	if col < 3:
		moves.append((row,col+1))

	return moves

def findIndex(puzzle,value):


	for (row,i) in enumerate(puzzle):
		for (col,j) in enumerate(i):
			if j == value:
				return row,col
def printPuzzle(puzzle):

	for i in puzzle:
		print i
def swap(puzzle,row_2,col_2):

	row_1, col_1 = findIndex(puzzle,0)

	tmp = puzzle[row_1][col_1]
	puzzle[row_1][col_1] = puzzle[row_2][col_2] 
	puzzle[row_2][col_2] = tmp

	return puzzle

