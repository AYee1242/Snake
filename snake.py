import random
import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
GRID_SIZE = 40

ZOMP = (50, 162, 135)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake():
    def __init__(self):
        self.score = 0
        self.length = 1
        self.direction = random.choice([UP,DOWN,LEFT,RIGHT])
        self.segments = [(int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))]
        self.color = ZOMP

    def user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def turn(self,direction):
        """Sets direction of the snake"""
        if (direction[0] + self.direction[0] != 0 and direction[1] + self.direction[1] != 0) or len(self.segments) == 1:
            self.direction = direction

    def move(self):
        """Moves snake 
        Returns False if the snake hit itself or the wall
        Retruns True if the move is valid
        """
        cur_x,cur_y = self.segments[0][0], self.segments[0][1]
        dir_x,dir_y = self.direction

        new_segment = (cur_x + dir_x*GRID_SIZE, cur_y + dir_y*GRID_SIZE)

        #Snake can only hit itself if its length is greater than 2
        if (len(self.segments) > 2 and new_segment in self.segments[2:]) or new_segment[0] < 0 or new_segment[0] >= SCREEN_WIDTH or new_segment[1] < 0 or new_segment[1] >= SCREEN_HEIGHT:
            return False

        self.segments.insert(0,new_segment)
        if (len(self.segments) > self.length):
            self.segments.pop()

        return True
    
    def draw(self, surface):
        """Renders the Snake"""
        for segment in self.segments:
            rect = pygame.Rect((segment[0], segment[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface=surface,color=self.color, rect=rect)