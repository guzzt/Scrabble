# -*- coding: utf8 -*-
import numpy   as np
from Square    import Square
from letterbag import LetterBag

global TP; 
global TL;
global DL;
global DP;
global ST;
global TL_FACTOR;
global DL_FACTOR;
global TP_FACTOR;
global DP_FACTOR;
global ST_FACTOR;
global HORIZONTAL;
global VERTICAL;

TP = 100;
TL = 110;
DL = 120;
DP = 130;
ST = 140;
TL_FACTOR  = TP_FACTOR = 3; 
DP_FACTOR  = DL_FACTOR = ST_FACTOR = 2;
HORIZONTAL = 'h';
VERTICAL   = 'v';

class Board(object):
	""""""
	def __init__(self,dimension=15):
		self.__dimension = dimension;
		self.__matrix    = np.array([Square() for i in xrange(self.dimension*self.dimension)]).reshape(self.dimension,self.dimension);
		self.__letterbag = LetterBag();
		self.__words     = [];

	@property
	def dimension(self):
		return self.__dimension;
        
	@dimension.setter
	def dimension(self,value):
		self.__dimension = value;

	@property
	def matrix(self):
		return self.__matrix;
        
	@matrix.setter
	def matrix(self,value):
		self.__matrix = value;

	@property
	def letterbag(self):
		return self.__letterbag;
        
	@letterbag.setter
	def letterbag(self,value):
		self.__letterbag = value;

	@property
	def words(self):
		return self.__words;
        
	@words.setter
	def words(self,value):
		self.__words = value;

	def LoadSquares(self):
		self.matrix[0,0].atribute   = TP;
		self.matrix[0,3].atribute   = DL;
		self.matrix[0,7].atribute   = TP;
		self.matrix[0,11].atribute  = DL;
		self.matrix[0,14].atribute  = TP;
		self.matrix[1,1].atribute   = DP;
		self.matrix[1,5].atribute   = TL;
		self.matrix[1,9].atribute   = TL;
		self.matrix[1,13].atribute  = DP;
		self.matrix[2,2].atribute   = DP;
		self.matrix[2,6].atribute   = DL;
		self.matrix[2,8].atribute   = DL;
		self.matrix[2,12].atribute  = DP;
		self.matrix[3,0].atribute   = DL;
		self.matrix[3,3].atribute   = DP;
		self.matrix[3,7].atribute   = DL;
		self.matrix[3,11].atribute  = DP;
		self.matrix[3,14].atribute  = DL;
		self.matrix[4,4].atribute   = DP;
		self.matrix[4,10].atribute  = DP;
		self.matrix[5,1].atribute   = TL;
		self.matrix[5,5].atribute   = TL;
		self.matrix[5,9].atribute   = TL;
		self.matrix[5,13].atribute  = TL;
		self.matrix[6,2].atribute   = DL;
		self.matrix[6,6].atribute   = DL;
		self.matrix[6,8].atribute   = DL;
		self.matrix[6,12].atribute  = DL;
		self.matrix[7,0].atribute   = TP;
		self.matrix[7,3].atribute   = DL;
		self.matrix[7,7].atribute   = ST;
		self.matrix[7,11].atribute  = DL;
		self.matrix[7,14].atribute  = TP;
		self.matrix[8,2].atribute   = DL;
		self.matrix[8,6].atribute   = DL;
		self.matrix[8,8].atribute   = DL;
		self.matrix[8,12].atribute  = DL;
		self.matrix[9,1].atribute   = TL;
		self.matrix[9,5].atribute   = TL;
		self.matrix[9,9].atribute   = TL;
		self.matrix[9,13].atribute  = TL;
		self.matrix[10,4].atribute  = DP;
		self.matrix[10,10].atribute = DP;
		self.matrix[11,0].atribute  = DL;
		self.matrix[11,3].atribute  = DP;
		self.matrix[11,7].atribute  = DL;
		self.matrix[11,11].atribute = DP;
		self.matrix[11,14].atribute = DL;
		self.matrix[12,2].atribute  = DP;
		self.matrix[12,6].atribute  = DL;
		self.matrix[12,8].atribute  = DL;
		self.matrix[12,12].atribute = DP;
		self.matrix[13,1].atribute  = DP;
		self.matrix[13,5].atribute  = TL;
		self.matrix[13,9].atribute  = TL;
		self.matrix[13,13].atribute = DP;
		self.matrix[14,0].atribute  = TP;
		self.matrix[14,3].atribute  = DL;
		self.matrix[14,7].atribute  = TP;
		self.matrix[14,11].atribute = DL;
		self.matrix[14,14].atribute = TP;		

	def isValid(self,letter,coord_y,coord_x):
		if ((coord_y < 0) or (coord_y > 14)) or ((coord_x < 0) or (coord_x > 14)):
			return False;
		elif self.matrix[coord_y,coord_x].letter == None:
			return True;
		elif self.matrix[coord_y,coord_x].letter == letter:
			return True;
		else:
			return False;

	def Anchors(self,coord_y,coord_x,direction):
		if(direction == HORIZONTAL):
			return self.matrix[coord_y];
		else:
			return self.matrix[0:,coord_x]
			
	def isHook(self,row,col):
		
		if(self.matrix[row,col].letter != None):
			return True;
		elif((row != 0) and (self.matrix[row-1,col].letter != None)):
			return True;
		elif((row != 14) and (self.matrix[row+1,col].letter != None)):
			return True;
		elif((col != 0) and (self.matrix[row,col-1].letter != None)):
			return True;
		elif((col != 14) and (self.matrix[row,col+1].letter != None)):
			return True;
		else:
			return False;

	def CalculePoints(self,char,coord_y,coord_x):
		#Calcula atributos 
		if self.matrix[coord_y,coord_x].atribute == None:
			points = self.letterbag.GetLetterValue(char);
		elif self.matrix[coord_y,coord_x].atribute == TL:
			points = self.letterbag.GetLetterValue(char,TL_FACTOR);
		elif self.matrix[coord_y,coord_x].atribute == DL:
			points = self.letterbag.GetLetterValue(char,TL_FACTOR);
		elif self.matrix[coord_y,coord_x].atribute == TP:
			points = TP;
		else:
			points = DP;
		return points;

def main():
	b = Board()
	print b.matrix

if __name__ == '__main__':
	main()
