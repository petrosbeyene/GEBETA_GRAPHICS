import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *

# IMPORT OBJECT LOADER
from objloader import *

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
glShadeModel(GL_SMOOTH)

# LOAD OBJECT AFTER PYGAME INIT
board = OBJ('../../Gebeta_data/gebeta_board.obj', swapyz=True)
board.loadTexture('../../Texture_Images/timber_light.jpg')
board.generate()

clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = viewport
gluPerspective(90.0, width/float(height), 1, 100.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)

# rx, ry = (0,0)
# tx, ty = (0,0)
# rotate = move = False
zpos = 10
pos = (0, 0)
while 1:
    # srf.fill(white)
    clock.tick(30)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            sys.exit()
        elif e.type == MOUSEBUTTONDOWN:
            # if e.button == 4: zpos = max(1, zpos-1)
            # elif e.button == 5: zpos += 1
            if e.button == 1:
                rotate = True
                pos = pygame.mouse.get_pos()
                print(pos)
                # h.main(pos)

                f = open("holes2.txt", "a")
                f.write(str(pos) + '\n')
                f.close()

            elif e.button == 3: move = True
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        # elif e.type == MOUSEMOTION:
        #     i, j = e.rel
        #     if rotate:
        #         rx += i
        #         ry += j
        #     if move:
        #         tx += i
        #         ty -= j


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslate(0, 0, - zpos)
    glRotate(90, 0, 0, 1)
    glRotate(45, 0, 1, 0)
    board.render()
    glTranslate(0, 0, zpos)
    pygame.display.flip()



