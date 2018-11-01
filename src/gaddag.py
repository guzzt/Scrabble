# -*- coding: utf8 -*-
class StateGaddag(object):
    def __init__(self):
        self.__edges   = {}; #transicoes que levam aos proximos estados
        self.__letters = set(); #Cada estado é composto por um conjunto de letras, esse conjunto indica as letras que levam a uma possivel palavra valida 

    @property
    def edges(self):
        return self.__edges;
        
    @edges.setter
    def edges(self,value):
        self.__edges = value;

    @property
    def letters(self):
        return self.__letters;

    @letters.setter
    def letters(self,value):
        self.__letters = value;

    def add_edge(self,char):
        """Adiciona uma transição do estado atual para um caractere se não existir tal transicao
           retorna o estado que essa transição leva"""
        if ((not char.isalpha()) and (char != '@')): #Verifica se é um caractere valido se for tranforma para lowercase, senao levanta uma excecao
            raise Exception('Caractere Inválido ' + char);
        char = char.lower()

        if (char in self.edges): #Se existir a transicao retorna o estado referente a ela
            return self.edges[char];
        new_state = StateGaddag(); #caso contrario cria um estado e o atribui a uma transicao referente aquele caractere, retorna o novo estado
        self.edges[char] = new_state;
        return new_state;

    def add_final_edge(self,char1,char2):
        """Adiciona uma transicao do estado atual para char1 se não existir tal transicao.
           E adiciona char2 para o conjuto de letras desse estado.
           Retorna o novo estado."""
        new_state = self.add_edge(char1);
        new_state.letters.add(char2);
        return new_state;

    def force_edge(self,char,state):
        """Adiciona uma transicao do estado atual com char para o estado "forçado"
           levantando uma exceção se um arco para char já existir para qualquer outro estado."""
        if char in self.edges:
            if not self.edges[char] == state:
                raise Exception('A transição com o caractere forçado já existe');
        self.edges[char] = state

class GADDAG(object):
    def __init__(self):
        self.__root      = StateGaddag();
        self.__num_words = 0;

    @property
    def root(self):
        return self.__root;

    @root.setter
    def root(self,value):
        self.__root = value;

    @property
    def num_words(self):
        return self.__num_words;

    @num_words.setter
    def num_words(self,value):
        self.__num_words = num_words;

    def add_word(self,word):
        """Adiciona uma palavra ao GADDAG"""
        word_len = len(word);
        if(word_len < 2):
            raise Exception('Palavra muito pequena '+word);

        #print(word)
        state = self.root;
        for i in xrange(word_len-1,1,-1): #Adiciona um caminho a partir da ultima letra na palavra
            state = state.add_edge(word[i]);
        state.add_final_edge(word[1],word[0]);

        for i in xrange(word_len-2,-1,-1): #Cria um caminho a partir da penultima letra
            state = state.add_edge(word[i])
        state.add_final_edge('@',word[-1])

        for i in xrange(word_len-3,-1,-1): #Cria os caminhos restantes
            forced_state = state;
            state        = self.root;
            for j in xrange(i,-1,-1):
                state.add_edge(word[i]);
            state.add_edge('@');
            state.add_final_edge(word[i+1],forced_state);

    def has_word(self,word):
        """Verifica a existencia de determinada palavra"""
        state = self.root
        for l in word[:0:-1]: #Avalia todos os caracteres que estao no REV(w) execeto o primeiro
            if not l in state.edges:
                return False
            state = state.edges[l] # percorre todos os estados
        return word[0] in state.letters;  #O primeiro caractere é avaliado

    def words_with_prefix(self,prefix):
        """Retorna uma lista de palavras que possuem determinado prefixo"""
        pass;
    def words_contains(self,subword):
        """Retorna uma lista de palavras que possuem determinada subpalavra"""
        pass;
    def words_with_sufix(self,sufix):
        """Retorna uma lista de palavras que possuem determinado sufixo"""
        pass;

def save(path_file):
    pass;
def load_gaddag(path_file):
    """Carrega o gaddag de um arquivo serializado"""
    pass;
def gaddag_from_wordlist(path_file):
    """Le uma wordlist e adiciona todas as palavras e retorna um gaddag com todas as palavras"""
    gaddag = GADDAG()
    with open(path_file, 'r') as f:
        for word in f.readlines():
            stripped = word.rstrip()
            if len(stripped) > 1:
                gaddag.add_word(stripped)  # Chop the newline
    return gaddag

def compress_file(path_file):
    """Comprime um arquivo contendo a serializacao do gaddag"""
    pass;
def decompress_file(path_file):
    """descomprimie um arquivo contendo a serializacao do gaddag"""
    pass;

def main():
    g = GADDAG();
    g = gaddag_from_wordlist('../dict.txt')
    print(g.has_word('abaixem'))

if __name__ == '__main__':
    main()
		