from random import random, randrange, sample
import os.path

# import the file, not class (YET)
from classes import word
from classes import board
from classes import parachute
Word = word.Word
Board = board.Board
Parachute = parachute.Parachute


class Game:
    def __init__(self):
        self.misses = 0        
        self.words_list = self._load_words()

    def guess(self):
        return input("Guess a letter a-z: ")
    
    def _load_words(self):
        # my_path is an abspath for the current dir
        my_path = os.path.abspath(os.path.dirname(__file__))
        # path = abspath + file name = abspath for the file
        # we got the first hundred five-letter words from words-by-frequency and created a new file
        # \n is 1 character - strip before comparison to find words of x length
        path = os.path.join(my_path, "./first_hundred_five_letter_words.txt")
        output = []
        with open(path, "r") as f:
            for each_ln in f:
                output.append(each_ln.strip())
        return output

    def miss(self):
        # TODO: remove print?
        print('missed')
        self.misses += 1

    def start(self):
        our_parachute = Parachute()
        gameplay = True

        random_word = sample(self.words_list, 1)[0]
        print('random_word', random_word)

        # Passing the random word to our new instance of Word
        our_word = Word(random_word)
        our_board = Board(our_word.value)
        while gameplay:
            our_board.display()
            our_parachute.display(self.misses)
            playerGuess = self.guess()
            if playerGuess in our_word.value:
                our_board.reveal_letter(playerGuess)
            else:
                self.miss()