#!/usr/bin/env python
# Basic OBJ file viewer. needs objloader from:
#  http://www.pygame.org/wiki/OBJFileLoader
# LMB + move: rotate
# RMB + move: pan
# Scroll wheel: zoom in/out
import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *

# IMPORT OBJECT LOADER
from objloader import *
import logic as l

import holes as h


def main():
    pygame.init()
    viewport = (900,600)
    hx = viewport[0]/2
    hy = viewport[1]/2
    srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glViewport(0, 0, 900, 600)

    glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)           # most obj files expect to be smooth-shaded

    # LOAD OBJECT AFTER PYGAME INIT
    board = OBJ('../../Gebeta_data/gebeta_board.obj', swapyz=True)
    board.loadTexture('../../Texture_Images/timber_light.jpg')
    board.generate()

    # LOAD BEAD IN PYGAME WINDOW
    bead = OBJ('../../BeadData/bead.obj', swapyz=True)
    bead.generate()



    clock = pygame.time.Clock()

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    width, height = viewport
    gluPerspective(90.0, width/float(height), 1, 100.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)

    zpos = 10
    rotate = False
    move = False

    beadPositionDict = {'b1': (-0.8, 8.0, 1.0), 'b2': (-0.5333333333333334, 8.333333333333334, 1.0), 'b3': (-0.2666666666666667, 8.666666666666666, 1.0), 'b4': (0.0, 9.0, 1.0), 'b5': (-0.7, 4.7, 1.0), 'b6': (-0.4666666666666667, 5.133333333333334, 1.0), 'b7': (-0.23333333333333334, 5.566666666666666, 1.0), 'b8': (0.0, 6.0, 1.0), 'b9': (-0.8, 1.5, 1.0), 'b10': (-0.5333333333333334, 1.9000000000000001, 1.0), 'b11': (-0.2666666666666667, 2.3000000000000003, 1.0), 'b12': (0.0, 2.7, 1.0), 'b13': (-0.7, -1.7, 1.0), 'b14': (-0.4666666666666667, -1.3, 1.0), 'b15': (-0.23333333333333334, -0.9, 1.0), 'b16': (0.0, -0.5, 1.0), 'b17': (-0.7, -4.8, 1.0), 'b18': (-0.4666666666666667, -4.366666666666666, 1.0), 'b19': (-0.23333333333333334, -3.933333333333333, 1.0), 'b20': (0.0, -3.5, 1.0), 'b21': (-0.8, -8.2, 1.0), 'b22': (-0.5333333333333334, -7.866666666666666, 1.0), 'b23': (-0.2666666666666667, -7.533333333333333, 1.0), 'b24': (0.0, -7.2, 1.0), 'b25': (2.5, 8.0, 1.0), 'b26': (2.7333333333333334, 8.333333333333334, 1.0), 'b27': (2.966666666666667, 8.666666666666666, 1.0), 'b28': (3.2, 9.0, 1.0), 'b29': (2.5, 4.8, 1.0), 'b30': (2.7333333333333334, 5.133333333333333, 1.0), 'b31': (2.966666666666667, 5.466666666666667, 1.0), 'b32': (3.2, 5.8, 1.0), 'b33': (2.5, 1.5, 1.0), 'b34': (2.7333333333333334, 1.8333333333333333, 1.0), 'b35': (2.966666666666667, 2.1666666666666665, 1.0), 'b36': (3.2, 2.5, 1.0), 'b37': (2.5, -1.8, 1.0), 'b38': (2.7333333333333334, -1.4, 1.0), 'b39': (2.966666666666667, -0.9999999999999999, 1.0), 'b40': (3.2, -0.5999999999999999, 1.0), 'b41': (2.5, -4.9, 1.0), 'b42': (2.7333333333333334, -4.533333333333333, 1.0), 'b43': (2.966666666666667, -4.166666666666667, 1.0), 'b44': (3.2, -3.8, 1.0), 'b45': (2.3, -8.0, 1.0), 'b46': (2.6, -7.733333333333333, 1.0), 'b47': (2.9, -7.466666666666667, 1.0), 'b48': (3.2, -7.2, 1.0)}

    while 1:
        # srf.fill(white)
        clock.tick(30)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            elif e.type == KEYDOWN and e.key == K_ESCAPE:
                sys.exit()
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 4: zpos = max(1, zpos-1)
                elif e.button == 5: zpos += 1
                elif e.button == 1:
                    rotate = True
                    pos = pygame.mouse.get_pos()
                    # if 112 <= pos[0] <= 211:
                    #     if 163 <= pos[1] <= 239:
                    #         ypos -= 2

                    # f = open("holes2.txt", "a")
                    # f.write(str(pos) + '\n')
                    # f.close()

                elif e.button == 3: move = True
            elif e.type == MOUSEBUTTONUP:
                if e.button == 1: rotate = False
                elif e.button == 3: move = False


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslate(0, 0, - zpos)
        glRotate(90, 0, 0, 1)
        glRotate(0, 0, 1, 0)
        board.render()
        glTranslate(0, 0, zpos)

        for location in beadPositionDict.values():
            glTranslate(location[0], location[1], - zpos + location[2])
            bead.render()
            glTranslate(-location[0], -location[1], zpos - location[2])
        pygame.display.flip()


main()


