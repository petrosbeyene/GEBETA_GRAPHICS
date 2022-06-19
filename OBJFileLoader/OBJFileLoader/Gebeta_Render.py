import sys
import pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time
import tkinter
from objloader import *
import logic

game = logic.Game()
brown = (210, 105, 30, 0)
blue = (0, 0, 128, 0)

def render(angle, zpos, board):
    glTranslate(0, 0, - zpos)
    glRotate(90, 0, 0, 1)
    glRotate(angle, 0, 1, 0)
    board.render()
    glTranslate(0, 0, zpos)

def renderText(value, pos, i):
    font = pygame.font.SysFont('freesansbold.ttf', 40)
    player_name  = font.render("Player" + str(i) + value, True, brown, blue)
    text_data = pygame.image.tostring(player_name, "RGBA", True)
    x, y = pos
    glWindowPos2d(x, y)
    glDrawPixels(player_name.get_width(), player_name.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
    pygame.display.flip()


def main():
    angle = 0
    pygame.init()
    viewport = (900,600)
    srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
    glClearColor(0.1, 0.1, 0.1, 0.0)
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
    board = OBJ('../../GebetaData/gebeta_board.obj', swapyz=True)
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
    data = logic.Data()
    beadPositionDict = data.getBeads()

    is_starting = True
    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

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
                    game.isValidMove(pos)
                    beadPositionDict = game.dataObj.getBeads()

                elif e.button == 3:
                    move = True
            elif e.type == MOUSEBUTTONUP:
                if e.button == 1:
                    rotate = False
                elif e.button == 3:
                    move = False

        if is_starting:
            render(angle, zpos, board)
            if angle == 360:
                is_starting = False
            angle += 1

        elif game.isEndGame == True:
            end_text = endGame()
            font = pygame.font.SysFont('freesansbold.ttf', 40)
            print(end_text)
            if end_text == "Draw":
                result_text = font.render("Draw", True, brown, blue)
            else:
                result_text = font.render("Winner : " + end_text, True, brown, blue)
            text_data = pygame.image.tostring(result_text, "RGBA", True)
            glWindowPos2d(300, 300)
            glDrawPixels(result_text.get_width(), result_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
            pygame.display.flip()
            time.sleep(5)
            break

        else:
            render(angle, zpos, board)


        for location in beadPositionDict.values():
            glTranslate(location[0], location[1], - zpos + location[2])
            bead.render()
            glTranslate(-location[0], -location[1], zpos - location[2])


        pygame.display.flip()



def endGame():
    if game.player1.getBank() > game.player2.getBank():
        return game.player1.name
    elif game.player2.getBank() > game.player1.getBank():
        return game.player2.name
    elif game.player1.getBank() == game.player2.getBank():
        return 'Draw'

if __name__ == "__main__":
    main()
