import random

#TODO: Create a Card Class
class Card:
    def __init__(self):
        """
        Constructs a card
        """
        self.value = random.randint(1, 13)

    def card_value(self):
        """
        basic card_value function
        returns vale of card
        """
        return self.value





