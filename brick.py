# Nikolei Advani, 11/29/16
# This python file creates a class
import pygame


class Brick:
    """This class is a blueprint to create and draw bricks within a pygame window"""
    def __init__(self, surface, height, width, color):
        self.surface = surface
        self.height = height
        self.width = width
        self.color = color

    def draw(self, x, y):
        """This method draws the bricks on the pygame window"""
        pygame.draw.rect(self.surface, self.color, (x, y, self.width, self.height), 0)

