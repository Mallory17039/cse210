from hilo.card import card

#TODO: fix some functions and maybe use tuple for card 1 and card 2?
# There is Zach's code in the bottom
class score:
    """ This will calculate score.
    Attributes:

    
    """

    def _init_(self):
        """
        constructs scores
        Args:
            self(score): an instance of score
        """
        self.is_playing = True
        self.score = 0
        self.total_score = 0

    def start_game(self):
        """Starts the game by running the main game loop
        Args:
            self(score): an instance of score        
        """
        while self.is_playing:
            pass

        #### DISPLAY CARD 1

    def get_guess(self):
        """Ask Higher or Lower to the user
        Args:
            self(score): an instance of score 
        """
        guess = input("Higher or Lower? [h/l] ")
        return guess

        #### DISPLAY CARD 2

    def cal_score(self):
        """Updates the player's score

        Args:
            self(score): an instance of score 
        """
        self.score = 0
        if (self.get_guess == "h"):
            ### GOTTA FIX HERE
            if(cardA.value > cardB.value):
                self.score = -75
                self.total_score += self.score
            elif(cardA.value < cardB.value):
               self.score = 100
               self.total_score += self.score
            else:
                self.score = 0
                self.total_score += self.score

        elif (guess == "l"):
            if(cardA.value < cardB.value):
                self.score = -75
                self.total_score += self.score
            elif(cardA.value > cardB.value):
               self.score = 100
               self.total_score += self.score
            else:
                self.score = 0
                self.total_score += self.score

    def display(self):
        """display the card and the score (not sure about card yet)
        Args:
            self(score): an instance of score 
        """
        if not self.is_playing:
            return 
        cards = ""


    def play_again(self):
        """Ask the user if they want to play
        Args:
            self(score): an instance of score  
        """
        if not self.is_playing:
            return 
        new_round = input("Do you want to play again? [y/n] ")
        self.is_playing = (new_round == "y")

# def main():
#     gamePlay = True
#     self.score = Score()

#     while (gamePlay):
#         cardA = Card()
#         cardB = Card()
#         print("")
#         cardA.firstDisplay()
#         guess = input("Higher or lower? [h/l] ")
#         cardB.secondDisplay()

        
#         if (guess == "h"):
#             if(cardA.value > cardB.value):
#                 self.score.subtract(75)
#             elif(cardA.value < cardB.value):
#                self.score.add(100)
#             else:
#                 self.score.add(0)
        
#         elif (guess == "l"):
#             if(cardA.value < cardB.value):
#                 self.score.subtract(75)
#             elif(cardA.value > cardB.value):
#                self.score.add(100)
#             else:
#                 self.score.add(0)


#         self.score.display()

#         again = input("Play again? [y/n] ")

#         if (again == "n"):
#             gamePlay = False
  
          
        




# if __name__ == "__main__":
#     main()