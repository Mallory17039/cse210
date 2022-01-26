import random

#TODO: Create a Card Class
class Card:
    def __init__(self):
        """
        Constructs a card
        """
        self.card1 = random.randint(1, 13)
        self.card2 = random.randint(1, 13)
        self.point = 0

    def card_value(self):
        """
        basic card_value function
        returns vale of card
        """
        return self.card1, self.card2

    def get_guess(self):
        """Ask Higher or Lower to the user
        Args:
            self(point): an instance of point 
        """
        guess = input("Higher or Lower? [h/l] ")
        if (self.get_guess == "h"):
            if(self.card1 > self.card2):
                self.point = -75
            elif(self.card1 < self.card2):
                self.point = 100
            else:
                self.point = 0
        elif (guess == "l"):
            if(self.card1 < self.card2):
                self.point = -75
            elif(self.card1 > self.card2):
                self.point = 100
            else:
                self.point = 0




