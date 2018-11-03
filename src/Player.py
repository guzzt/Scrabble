# -*- coding: utf8 -*-
from Board import Board;
class Player(object):
	def __init__(self,name='Player'):
		self.__rack  = [];
		self.__score = 0; 
		self.__words = {};
		self.__name  = name;
		self.__board = None;

	@property
    def rack(self):
        return self.__rack;
        
    @rack.setter
    def rack(self,value):
        self.__rack = value;
    @property
    def score(self):
        return self.__score;
        
    @score.setter
    def score(self,value):
        self.__score = value;

    @property
    def words(self):
        return self.__words;
        
    @words.setter
    def words(self,value):
        self.__words = value;
    @property
    def name(self):
        return self.__name;
        
    @name.setter
    def name(self,value):
        self.__name = value;
    @property
    def board(self):
        return self.__board;
        
    @board.setter
    def board(self,value):
        self.__board = value;

	def Move(self,letter,row,col):
		if self.board.isValid(letter,row,col):
			self.board.matrix[row,col] = letter; 
			return True;
		else:
			return False;

	def gamble(self,word,coord_init,coord_final):
		init_y  = int(coord_init[0],16);
		init_x  = int(coord_init[1],16);
		final_y = int(coord_final[0],16);
		final_x = int(coord_final[1],16);

		#Verifica se as coordenadas que a palavra sera disposta são validas (horizontal,vertical)
		if( (init_x != final_x) and (init_y != final_y)):
			return False;

		#Verifica se é horizontal ou vertical
		if init_x == final_x:
			per_line = False;
		else:
			per_line = True;

		#Verifica se o tamanho da palavra condiz com as coordenadas informadas
		if per_line:
			if (init_x - final_x) != len(word):
				return False;
		else:
			if (init_y - final_y) != len(word):
				return False;

		for l in word:
			if per_line:
				if not self.Move(l,init_x,init_y,board):
					return False;
				init_y += 1;
			else:
				if not self.Move(l,init_x,init_y,board):
					return False;
				init_x += 1;

		return True;

