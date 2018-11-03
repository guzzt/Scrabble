# -*- coding: utf8 -*-
import random

global NUM_LETTERS_PLAYER
NUM_LETTERS_PLAYER = 7;

class LetterBag(object):
	"""Saco de letras """
	def __init__(self):
		self.bag = ['a']*14 + ['e']*11 + ['i']*10 + ['o']*10 + ['s']*8 + ['u']*7 + ['m']*6 + ['r']*6 + ['t']*5 \
				 + ['d']*5  + ['l']*5  + ['c']*4  + ['p']*4  + ['n']*4 + ['b']*3 + ['ç']*2 + ['f']*2 + ['g']*2 \
				 + ['h']*2  + ['v']*2  + ['j']*2  + ['q']    + ['x']   + ['z']   + [' ']*3;

	def PlayerLetters(self,num):
		random.shuffle(self.bag);
		len(len(self.bag));
		letters = random.sample(self.bag,NUM_LETTERS_PLAYER);
		for letter in letters:
			self.bag.remove(letter);
			
	def GetLetterValue(char):
		if char == ' ':
			return 0;
		elif((char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u') or (char == 's') or (char == 'm') or (char == 'r') or (char == 't')):
			return 1;
		elif((char == 'd') or (char == 'l') or (char == 'p') or (char == 'c')):
			return 2;
		elif((char == 'n') or (char == 'b') or (char == 'ç')):
			return 3;
		elif((char == 'f') or (char == 'g') or (char == 'h') or (char == 'v')):
			return 4;
		elif(char == 'j'):
			return 5; 
		elif(char == 'q'):
			return 6;
		elif((char == 'x') or (char == 'z')):
			return 8;  

def main():
	l = LetterBag();
	print(l.bag)			 

if __name__ == '__main__':
	main()


		