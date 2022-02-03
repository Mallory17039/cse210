class Parachute:
    def __init__(self):
        self.head = "  O"
        self.parachute = [" ___", "/___\\", "\\   /", " \\ /", self.head, " /|\\", " / \\"]
    def display(self, misses):
        for i in range(misses, len(self.parachute)):
            print(self.parachute[i])