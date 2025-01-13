import random

class Food:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = self.generate_food_position()
        self.color = random.choice(["red", "blue", "green"])

    def generate_food_position(self):
        return random.randrange(self.width), random.randrange(self.height)

    def respawn_food(self):
        self.position = self.generate_food_position()
        self.color = random.choice(["red", "blue", "green"])
