# -*- coding: utf8 -*-
import Board
import gaddag
from   Player import Player
from   AI import StrategyMoveGeneration
from   Interface import Iface

def main():
	b = Board.Board()
	b.LoadSquares()
	p1 = Player();
	p2 = Player();
	s  = StrategyMoveGeneration();
	iface = Iface(player1=p1,player2=p2);
	s.board = iface.board = p1.board = p2.board = b;
	#p1.gamble('teste',"5","7",'v');
	#p2.gamble('ele','6','7','h');	
	#p2.gamble('massa','7','5','h');
	gdg = gaddag.gaddag_from_wordlist('../dict.txt');
	print '[carregou]'
	s.gdg = gdg;
	s.FindAnchors(6,7,'h')
	p1.rack = p1.board.letterbag.PlayerLetters(7);
	s.generate(['m','a','n','d','i','o','c','a']);
	for move in s.moves:
		w = move.word;
		if gdg.has_word(w):
			print w +' '+'true';
		else:
			print w +' '+'false';
	print p1.rack
	#p1.gamble('testsdmh',"1","6",'v');
	iface.Draw();

if __name__ == '__main__':
	main()