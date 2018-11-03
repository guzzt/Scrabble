# -*- coding: utf8 -*-
import numpy   as np
from Square    import Square
from letterbag import letterbag

global TP; 
global TL;
global DL;
global DP;
global ST;

TP = 10;
TL = 11;
DL = 12;
DP = 13;
ST = 14;

class Board(object):
	""""""
	def __init__(self,dimension=15):
		self.dimension = dimension;
		self.matrix    = np.array([Square() for i in xrange(self.dimension*self.dimension)]).reshape(self.dimension,self.dimension);

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
		if (coord_y < 0) or (coord_y > 14) or (coord_x < 0) or (coord_x > 14):
			return False;
		elif self.matrix[coord_y,coord_x] == None:
			return True;
		elif self.matrix[coord_y,coord_x] == letter:
			return True;
		else
			return False;

	def CalculePoints(self,char,coord_y,coord_x):
		#Calcular atributos ...
		#...

		points += letterbag.GetLetterValue(l);
		return points;

def main():
	b = Board()
	print b.matrix

if __name__ == '__main__':
	main()
