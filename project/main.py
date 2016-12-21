#!/usr/bin/env python
# -*- coding: utf-8 -*-

from helper import findBlankIndex
from helper import createMoves
from helper import breadthFirstSearch
from helper import depthFirstSearch

def main():
	target_puzzle = [[1,2,3],[4,5,6],[7,8,0]]	

	rand_puzzle = [[1,2,3],[8,0,4],[7,6,5]]

	breadthFirstSearch(rand_puzzle,target_puzzle)
	depthFirstSearch(rand_puzzle,target_puzzle)

if __name__ == '__main__':
	main();