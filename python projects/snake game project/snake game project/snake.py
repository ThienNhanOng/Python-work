import random

class Snake:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake_segments = [(width // 2, height // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def move(self):
        x, y = self.snake_segments[0]
        if self.direction == "UP":
            y -= 1
        elif self.direction == "DOWN":
            y += 1
        elif self.direction == "LEFT":
            x -= 1
        elif self.direction == "RIGHT":
            x += 1
        self.snake_segments.insert(0, (x, y))
        
        # Remove the last segment of the tail
        if len(self.snake_segments) > 1:
            self.snake_segments.pop()

    def change_direction(self, new_direction):
        opposite_directions = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if new_direction != opposite_directions[self.direction]:
            self.direction = new_direction

    def get_head(self):
        return self.snake_segments[0]

    def is_collision(self):
        head = self.get_head()
        return (
            head[0] < 0
            or head[0] >= self.width
            or head[1] < 0
            or head[1] >= self.height
            or len(set(self.snake_segments)) < len(self.snake_segments)
        )
