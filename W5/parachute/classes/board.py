class Board:

    def __init__(self):
        self.board = ["none"]

    def __init__(self, word):
        self.word = word
        self.board = ["_" for i in range(len(word))]
    
    def reveal_letter(self, letter):
        # update the board to reveal all instances of the letter in the word
        pass

    def display(self):
       print(" ".join(self.board))