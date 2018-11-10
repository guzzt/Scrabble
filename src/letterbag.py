# -*- coding: utf8 -*-
import random

global NUM_LETTERS_PLAYER
NUM_LETTERS_PLAYER = 7;

class LetterBag(object):
	"""Saco de letras """
	def __init__(self):
		#removido ['ç']*2 
		self.__bag = ['a']*14 + ['e']*11 + ['i']*10 + ['o']*10 + ['s']*8 + ['u']*7 + ['m']*6 + ['r']*6 + ['t']*5 \
				   + ['d']*5  + ['l']*5  + ['c']*4  + ['p']*4  + ['n']*4 + ['b']*3 + ['f']*2 + ['g']*2 \
				   + ['h']*2  + ['v']*2  + ['j']*2  + ['q']    + ['x']   + ['z']   + [' ']*3;
	@property
	def bag(self):
		return self.__bag;
        
	@bag.setter
	def bag(self,value):
		self.__bag = value;

	def PlayerLetters(self,num=NUM_LETTERS_PLAYER):
		letters = random.sample(self.bag,num);
		for letter in letters:
			self.bag.remove(letter);
		return letters
	def GetLetterValue(self,c,factor=1):
		if c == ' ':
			return 0;
		elif((c == 'a') or (c == 'e') or (c == 'i') or (c == 'o') or (c == 'u') or (c == 's') or (c == 'm') or (c == 'r') or (c == 't')):
			return factor;
		elif((c == 'd') or (c == 'l') or (c == 'p') or (c == 'c')):
			return 2*factor;
		elif((c == 'n') or (c == 'b')): #removido  (c == 'ç')
			return 3*factor;
		elif((c == 'f') or (c == 'g') or (c == 'h') or (c == 'v')):
			return 4*factor;
		elif(c == 'j'):
			return 5*factor; 
		elif(c == 'q'):
			return 6*factor;
		elif((c == 'x') or (c == 'z')):
			return 8*factor;  
		else:
			raise Exception('[-]Caractere Inválido');

def main():
	l = LetterBag();
	print(l.bag)			 

if __name__ == '__main__':
	main()


		