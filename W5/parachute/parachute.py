from random import random, randrange


import random

#Possible Word List(~14k words)
#PossibleWordsList = open("words-by-frequency.txt", "r").read().split()

wordList = ["secret", "house", "hedgehog"]
#head = "O"
#parachute = ["___", "/___\\", "\\   /", "\\/", head, "/|\\", "/ \\"]


class Word:
    def __init__(self):
        self.value = "none"
        self.words_list = self._load_words()

    def random(self):
        self.value = self.words_list([randrange(0, len(self.words_list))])

    def _load_words(self):
        with open("words-by-frequency", "r") as f:
            for each_ln in f:
                if len(each_ln) >= 6 and len(each_ln) <= 12:
                    self.words_list.append(each_ln.strip())

class Board:
    def __init__(self):
        self.board = ["none"]
    def __init__(self, length):
        self.board = ["", "", "", "", "", "", "", "", "", "", "", ""]
        for i in range(length):
            self.board[i] = "_"
    def display(self):
       print(" ".join(self.board))


class Parachute:
    def __init__(self):
        self.head = "  O"
        self.parachute = [" ___", "/___\\", "\\   /", " \\ /", self.head, " /|\\", " / \\"]
    def display(self, misses):
        for i in range(misses, len(self.parachute)):
            print(self.parachute[i])



class Game:
    def __init__(self):
        self.misses = 0        

    def guess(self):
        return input("Guess a letter a-z: ")
    def miss(self):
        self.misses += 1
    

def main():
    game = Game()
    parachute = Parachute()
    gameplay = True
    randomWord = Word()
    randomWord.random()
    board = Board(len(randomWord.value))
    while (gameplay):
        board.display()
        parachute.display(game.misses)
        playerGuess = game.guess()
        if(playerGuess == randomWord.value):
            print("You guessed the word")
        else:
            game.miss()

if __name__ == "__main__":
    main()