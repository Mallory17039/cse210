import random

#TODO: Create a Card Class
class Card:
    def __init__(self):
        """
        Constructs a card
        """
        self.value = random.randint(1, 13)

    def display(self):
        """
        basic display function
        returns vale of card
        """
        return self.value

    def firstDisplay(self):
        """
        Display function
        """
        print(f"The card is: {self.value}")

    def secondDisplay(self):
        """
        Second Display
        
        """
        print(f"Next card was: {self.value}")

#TODO: Create a Score Class
class Score:
    def __init__(self):
        self.points = 300

    def display(self):
        print(f"your score is: {self.points}")


    def subtract(self, int):
        self.points -= int
        
    def add(self, int):
        self.points += int


