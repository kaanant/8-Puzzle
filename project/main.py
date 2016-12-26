#!/usr/bin/env python
# -*- coding: utf-8 -*-

from helper import findIndex
from helper import createMoves
from helper import breadthFirstSearch
from helper import depthFirstSearch
from helper import bestFirstSearch
from helper import aStar
import datetime

def main():
	target_puzzle = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]	

	rand_puzzle = [[1,2,4,8],[5,7,3,12],[0,9,6,11],[13,10,14,15]]

	
 	#depthFirstSearch(rand_puzzle,target_puzzle)
 	
 	a = datetime.datetime.now()
	bestFirstSearch(rand_puzzle,target_puzzle)
	b = datetime.datetime.now()
	print "Time BestFirstSearch:%s"%(b-a)

	a = datetime.datetime.now()
	aStar(rand_puzzle,target_puzzle)
	b = datetime.datetime.now()
	print "Time AStar:%s"%(b-a)

	a = datetime.datetime.now()
	breadthFirstSearch(rand_puzzle,target_puzzle)
	b = datetime.datetime.now()
	print "Time breadthFirstSearch:%s"%(b-a)

if __name__ == '__main__':
	main();