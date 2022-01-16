import pygame
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

GRID_SIZE = 40
GRID_WIDTH = SCREEN_WIDTH/GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT/GRID_SIZE

CHRIMSON = (215, 38, 61)

class Apple():
    def __init__(self, segments):
        self.coordinates = (0,0)
        self.color = CHRIMSON
        self.randomize_coordinates(segments)

    def randomize_coordinates(self, segments):
        """Spawns apple to new free location"""
        self.coordinates = (random.randint(0, GRID_WIDTH-1) * GRID_SIZE, random.randint(0, GRID_HEIGHT-1) * GRID_SIZE )
        while self.coordinates in segments:
            self.coordinates = (random.randint(0, GRID_WIDTH-1) * GRID_SIZE, random.randint(0, GRID_HEIGHT-1) * GRID_SIZE )

    def draw(self,surface):
        """Renders the Apple"""
        rect = pygame.Rect((self.coordinates[0], self.coordinates[1]), (GRID_SIZE,GRID_SIZE))
        pygame.draw.rect(surface=surface,color=self.color, rect=rect)

