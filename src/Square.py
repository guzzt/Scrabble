# -*- coding: utf8 -*-
class Square(object):
	"""Quadrados do tabuleiro"""
	def __init__(self, coord,atribute):
		self.coord    = coord; #Tupla x y
		self.atribute = atribute;
		self.letter   = None;