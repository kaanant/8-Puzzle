#!/usr/bin/env python
# -*- coding: utf-8 -*-


import copy


def breadthFirstSearch(puzzle,target):

 	search_space = []
 	all_puzzles = []
 	search_space.append(puzzle)
 	all_puzzles.append(puzzle)

 	iteration = 0

 	while target not in all_puzzles and len(search_space) > 0:

 		tmp_puzzle = search_space.pop(0)

 		moves = createMoves(tmp_puzzle)
 		for move in moves:
 			copy_puzzle = copy.deepcopy(tmp_puzzle)
 			swap_result = swap(copy_puzzle,move[0],move[1])
 			if swap_result not in all_puzzles:
 				search_space.append(swap_result)
 				all_puzzles.append(swap_result)
		
 	if not len(search_space) > 0:
 		print "Result cannot Find"

def depthFirstSearch(puzzle,target):

	search_space = []
 	all_puzzles = []
 	search_space.append(puzzle)
 	all_puzzles.append(puzzle)
 	depth = 0

 	while target not in all_puzzles and len(search_space) > 0:

 		tmp_puzzle = search_space.pop(0)
 		depth += 1
 		print depth,tmp_puzzle
 		moves = createMoves(tmp_puzzle)
 		for move in reversed(moves):
 			copy_puzzle = copy.deepcopy(tmp_puzzle)
 			swap_result = swap(copy_puzzle,move[0],move[1])
 			if swap_result not in all_puzzles:
 				search_space.insert(0,swap_result)
 				all_puzzles.insert(0,swap_result)

def createMoves(puzzle):

	row,col = findBlankIndex(puzzle)
	moves = []

	if row > 0:
		moves.append((row-1,col))
	if col > 0:
		moves.append((row,col-1))
	if row < 2:
		moves.append((row+1,col))
	if col < 2:
		moves.append((row,col+1))

	return moves

def findBlankIndex(puzzle):


	for (row,i) in enumerate(puzzle):
		for (col,j) in enumerate(i):
			if j == 0:
				return row,col

def swap(puzzle,row_2,col_2):

	row_1, col_1 = findBlankIndex(puzzle)

	tmp = puzzle[row_1][col_1]
	puzzle[row_1][col_1] = puzzle[row_2][col_2] 
	puzzle[row_2][col_2] = tmp

	return puzzle

