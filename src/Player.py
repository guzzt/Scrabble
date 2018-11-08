# -*- coding: utf8 -*-
import Board;
from   Word  import Word;

class Player(object):
	def __init__(self,name='Player'):
		self.__rack  = [];
		self.__score = 0; 
		self.__words = [];
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

	def isValidMove(self,word,row,col,direction):
		if(len(self.board.words) == 0):
			Valid = False;
		if direction == Board.VERTICAL:
			for letter in word:
				if((not Valid) and ((row,col) == (7,7))):
					Valid = True;
				if not self.board.isValid(letter,row,col): 
					return False;
				row += 1
		else:
			for letter in word:
				if((not Valid) and ((row,col) == (7,7))):
					Valid = True;
				if not self.board.isValid(letter,row,col): 
					return False;
				col += 1

		return Valid;


	def gamble(self,word,coord_y,coord_x,direction):

		"""TODO verificar se todos os movimentos são validos antes de adicionar uma palavra"""

		y  = int(coord_y,16);
		x  = int(coord_x,16);

		#Verifica se o tamanho da palavra cabe no tabuleiro a partir das coordenadas informadas
		if per_line:
			if x + len(word) > 14:
				return False;
		else:
			if y + len(word) > 14:
				return False;

		#Verifica se a insercão é valida, calcula os pontos de cada letra
		if not isValidMove(word,coord_y,coord_x,direction):
			return False;
			
		w = Word(word);
		for l in word:
			if direction == Board.HORIZONTAL:
				self.board[y,x].letter = l;
				points = self.board.CalculePoints(l,y,x);
				x += 1;
			else:
				self.board[y,x].letter = l;
				points = self.board.CalculePoints(l,y,x);
				y += 1;
			
			if(points == Board.TP):
				w.factors.append(Board.TP_FACTOR);
			elif(points == Board.DP):
				w.factors.append(Board.DP_FACTOR);
			elif(points == Board.ST):
				w.factors.append(Board.ST_FACTOR);
			else:
				w.score += points;


		for f in w.factors:
			w.score *= f;

		self.words.append(w);
		self.score += w.score; 

		return True;


def printBoard(p1):
	for i in xrange(14):
		for j in xrange(14):
			print p1.board.matrix[i,j].letter, 
		print

def main():
	b  = Board.Board();
	b.LoadSquares()
	p1 = Player();
	p1.board = b;
	p1.gamble('teste',"0","0",'v')
	printBoard(p1);
	print p1.score
	
if __name__ == '__main__':
	main()