#!/usr/bin/env python
#-*-coding: utf-8-*-


class Node:

	def __init__(self,puzzle,distance = None,heuristic = None,moves = [],blank_index = None):

		self.puzzle = puzzle # puzzle -> 4*4 matris
		self.distance = distance # distance -> kök dügüme olan uzaklık
		self.heuristic = None # h -> sonuca olan sezgisel uzaklık
		self.moves = []
		self.blank_index = {"row": None,
							"col": None}
		self.total_distance = heuristic + distance

	def setHeuristic(self,value):
		self.heuristic = value

	def getHeuristic(self):
		return self.heuristic

	def setDistance(self,value):
		self.distance = value

	def getDistance(self):
		return self.distance

	def setPuzzle(self,puzzle):

		self.puzzle = puzzle

	def getPuzzle(self):
		return self.puzzle

	def setBlankIndex(self,row,col):
		self.blank_index["row"] = row
		self.blank_index["col"] = col

	def getBlankIndex(self):
		return self.blank_index["row"],self.blank_index["col"]

	def setMoves(self,moves):
		self.moves = moves[:]

	def getMoves(self):
		return self.moves

		