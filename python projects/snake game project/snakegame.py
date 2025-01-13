import pygame,sys,random
from pygame.math import Vector2
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
  
    def draw_snake(self):
        for block in self.body:
            x_position = int(block.x * cell_size)
            y_position = int(block.y * cell_size)
            block_rect = pygame.Rect((x_position,y_position,cell_size,cell_size))
            pygame.draw.rect(screen,"blue",block_rect)








pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock() #control time in pygame
test_surface = pygame.Surface((50,200))
test_rect = test_surface.get_rect(center=(250,250)) #center the sprite (half the screen size)
leftright = 200
updown = 200
cell_size=40
varsnake = SNAKE()

while True: 
    # display our drawing and screen ui 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
    screen.fill(pygame.Color("Green"))
    
    varsnake.draw_snake()
    
    screen.blit(test_surface,(test_rect))
    pygame.display.update()
    clock.tick(60) #