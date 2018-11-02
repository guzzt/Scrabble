# -*- coding: utf8 -*-
import numpy as np
from Square  import Square

global TP; 
global TL;
global DL;
global DP;
global STAR;

TP   = 10;
TL   = 11;
DL   = 12;
DP   = 13;
STAR = 14;

class Board(object):
	""""""
	def __init__(self,dimension=15):
		self.dimension = dimension;
		self.matrix    = np.array([Square() for i in xrange(self.dimension*self.dimension)]).reshape(self.dimension,self.dimension);

	def LoadSquares(self):
		self.matrix[0,0].atribute  = TP;
		self.matrix[0,3].atribute  = DL;
		self.matrix[0,7].atribute  = TP;
		self.matrix[0,11].atribute = DL;
		self.matrix[0,14].atribute = TP;
		self.matrix[1,1].atribute  = DP;
		self.matrix[1,5].atribute  = TL;
		self.matrix[1,9].atribute  = TL;
		self.matrix[1,13].atribute = DP;
		self.matrix[2,2].atribute  = DP;
		self.matrix[2,6].atribute  = DL;
		self.matrix[2,8].atribute  = DL;
		self.matrix[2,12].atribute = DP;
		self.matrix[0,0].atribute = TP
		self.matrix[0,0].atribute = TP
		self.matrix[0,0].atribute = TP
		self.matrix[0,0].atribute = TP
		self.matrix[0,0].atribute = TP
		self.matrix[0,0].atribute = TP
		self.matrix[0,0].atribute = TP
		self.matrix[0,0].atribute = TP
		self.matrix[0,0].atribute = TP
		self.matrix[0,0].atribute  = TP;
		

def main():
	b = Board()
	print b.matrix

if __name__ == '__main__':
	main()
