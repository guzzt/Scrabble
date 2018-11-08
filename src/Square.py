# -*- coding: utf8 -*-
class Square(object):
	"""Quadrados do tabuleiro"""
	def __init__(self,atribute=None):
		self.__atribute = atribute;
		self.__letter   = None;

	@property
	def atribute(self):
		return self.__atribute;
        
	@atribute.setter
	def atribute(self,value):
		self.__atribute = value;

	@property
	def letter(self):
		return self.__letter;
        
	@letter.setter
	def letter(self,value):
		self.__letter = value;
