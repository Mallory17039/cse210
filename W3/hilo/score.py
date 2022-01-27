from hilo.card import Card

# Class should start with Capital
class Score:
    """ This will calculate score.
    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """
    #Constructor should be with __ (two under scores) -> Dunder
    def __init__(self):
        """
        constructs scores
        Args:
            self(score): an instance of score
        """
        self.is_playing = True
        self.score = 300
        self.total_score = 300

    def start_game(self):
        """Starts the game by running the main game loop
        Args:
            self(score): an instance of score        
        """
        while self.is_playing:
            self.card1 = Card()
            self.card2 = Card()
            self.display(self.card1)
            self.get_guess()
            self.display(self.card2)
            self.cal_score()
            self.play_again()

    def get_guess(self):
        """Ask Higher or Lower to the user
        Args:
            self(point): an instance of point 
        """
        guess = input("Higher or Lower? [h/l] ")
        if (self.get_guess == "h"):
            if(self.card1.card_value() > self.card2.card_value()):
                self.point = -75
            elif(self.card1.card_value() < self.card2.card_value()):
                self.point = 100
            else:
                self.point = 0
        elif (guess == "l"):
            if(self.card1.card_value() < self.card2.card_value()):
                self.point = -75
            elif(self.card1.card_value() > self.card2.card_value()):
                self.point = 100
            else:
                self.point = 0

    def cal_score(self):
        """Updates the player's score

        Args:
            self(score): an instance of score 
        """
        self.score = 0
        self.score += self.point
        self.total_score += self.score
        print(f"Your Score is: {self.total_score}\n")

    def display(self, card):
        # calling something in this file, Card is calling from Class
        """display the card
        Args:
            self(score): an instance of score 
        """
        print(f"The card is: {card.card_value()}")

    def play_again(self):
        """Ask the user if they want to play
        Args:
            self(score): an instance of score  
        """
        if not self.is_playing:
            return 
        new_round = input("Do you want to play again? [y/n] ")
        self.is_playing = (new_round == "y")

