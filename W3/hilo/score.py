from hilo.card import Card

class score:
    """ This will calculate score.
    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def _init_(self):
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
            self.display1()
            Card.get_guess
            self.display2()
            self.cal_score()
            self.play_again()

    def cal_score(self):
        """Updates the player's score

        Args:
            self(score): an instance of score 
        """
        self.score = 0
        self.score += Card.points
        self.total_score += self.score
        print(f"Your Score is: {self.total_score}\n")

    def display1(self):
        """display the card
        Args:
            self(score): an instance of score 
        """
        print(f"The card is: {Card.card_value.card1}")

    def display2(self):
        """display the card
        Args:
            self(score): an instance of score 
        """
        print(f"The card is: {Card.card_value.card2}")

    def play_again(self):
        """Ask the user if they want to play
        Args:
            self(score): an instance of score  
        """
        if not self.is_playing:
            return 
        new_round = input("Do you want to play again? [y/n] ")
        self.is_playing = (new_round == "y")

