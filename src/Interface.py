# -*- coding: utf8 -*-
import Board
from   Player import Player
from   AI import StrategyMoveGeneration

class Iface(object):
	"""docstring for Iface"""
	def __init__(self,board=None,player1=None,player2=None):
		self.__board   = board;
		self.__player1 = player1;
		self.__player2 = player2;

	@property
	def board(self):
		return self.__board;
        
	@board.setter
	def board(self,value):
		self.__board = value;

	@property
	def player1(self):
		return self.__player1;
        
	@player1.setter
	def player1(self,value):
		self.__player1 = value;

	@property
	def player2(self):
		return self.__player2;
        
	@player2.setter
	def player2(self,value):
		self.__player2 = value;
	def PrintPlayerWords(self,player,msg):
		print "   [+]"+msg,
		for w in player.words:
			print w.string + '(%d)' % w.score,
		print
	def Draw(self):
		lineCoord = '    0 1 2 3 4 5 6 7 8 9 A B C D E';
		line = '   ' + '- '*self.board.dimension;
		print lineCoord
		print ' '+line
		for i in xrange(self.board.dimension):
			print format(i,'X'),'|',
			for j in xrange(self.board.dimension):
				if (self.board.matrix[i,j].atribute == None) and (self.board.matrix[i,j].letter == None):
					print ' ',
				elif (self.board.matrix[i,j].atribute == Board.TP) and (self.board.matrix[i,j].letter == None):
					print '@',
				elif (self.board.matrix[i,j].atribute == Board.DL) and (self.board.matrix[i,j].letter == None):
					print '-',
				elif (self.board.matrix[i,j].atribute == Board.DP) and (self.board.matrix[i,j].letter == None):
					print '*',
				elif (self.board.matrix[i,j].atribute == Board.TL) and (self.board.matrix[i,j].letter == None):
					print '+',
				elif (self.board.matrix[i,j].atribute == Board.ST) and (self.board.matrix[i,j].letter == None):
					print '#',
				else:
					print self.board.matrix[i,j].letter.upper(),
			print '|',format(i,'X'),
			if(i == 0):
				self.PrintPlayerWords(self.player1,"My words:");
			elif(i == 13):
				self.PrintPlayerWords(self.player2,"Your words:");
			else:
				print
		print ' ' + line
		print lineCoord

	def MensageInfo(self,msg):
		print '   [+]'+msg;
	def MensageError(self,msg):
		print '   [-]'+msg;

if __name__ == '__main__':
	main()