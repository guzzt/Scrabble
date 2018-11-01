# -*- coding: utf8 -*-
class LetterBag(object):
	"""Saco de letras """
	def __init__(self):
		self.bag = ['a']*14 + ['e']*11 + ['i']*10 + ['o']*10 + ['s']*8 + ['u']*7 + ['m']*6 + ['r']*6 + ['t']*5 \
				 + ['d']*5  + ['l']*5  + ['c']*4  + ['p']*4  + ['n']*4 + ['b']*3 + ['ç']*2 + ['f']*2 + ['g']*2 \
				 + ['h']*2  + ['v']*2  + ['j']*2  + ['q']    + ['x']   + ['z']

def main():
	l = LetterBag();
	print(l.bag)			 

if __name__ == '__main__':
	main()


		