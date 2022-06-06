"""Gebeta

Traditional Ethiopian Game.
"""

# Import necessary modules
import pygame
from pygame.locals import *
from OpenGL.GL import *

def init():
    """Initializes a pygame window."""
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Demo")
    glClearColor(1.0, 1.0, 1.0, 1.0)

def clear():
    """clears the window with the colors in glClearColor."""
    glClear(GL_COLOR_BUFFER_BIT)

def main():
    """Main entry of the program."""
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        clear()
        pygame.display.flip()
        pygame.time.wait(10)

main()