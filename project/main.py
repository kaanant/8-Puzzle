#!/usr/bin/env python
# -*- coding: utf-8 -*-

from helper import findBlankIndex
from helper import createMoves
from helper import createAllSituation

def main():
	target_puzzle = [[1,2,3],[4,5,6],[7,8,0]]	

	rand_puzlle = [[1,4,3],[7,0,6],[5,8,2]]
	createAllSituation(rand_puzlle)


if __name__ == '__main__':
	main();