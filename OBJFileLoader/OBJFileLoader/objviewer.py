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

angle = 0
def main():
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
    board = OBJ('../../Gebeta_Board_data/gebeta_board.obj', swapyz=True)
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

    brown = (210, 105, 30, 0)
    blue = (0, 0, 128, 0)

    # initialState()
    while True:
        if game.isEndGame == True:
            end_text = endGame()
            font = pygame.font.SysFont('freesansbold.ttf', 40)
            if end_text == "Draw":
                result_text = font.render("Draw", True, brown, blue)
            else:
                result_text = font.render("Winner : " + end_text, True, brown, blue)
            text_data = pygame.image.tostring(result_text, "RGBA", True)
            glWindowPos2d(300, 300)
            glDrawPixels(result_text.get_width(), result_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
            pygame.display.flip()
            time.sleep(5)
            popWindow()
            break
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

                elif e.button == 3: move = True
            elif e.type == MOUSEBUTTONUP:
                if e.button == 1: rotate = False
                elif e.button == 3: move = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslate(0, 0, - zpos)
        glRotate(90, 0, 0, 1)
        glRotate(angle, 0, 1, 0)
        board.render()
        glTranslate(0, 0, zpos)

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

def popWindow():
    popWin = tkinter.Tk()
    popWin.geometry("300x200")

    play_button = tkinter.Button(popWin, text = "Play again", command=mainCaller())
    play_button.pack(side = tkinter.RIGHT)
    quit_button = tkinter.Button(popWin, text = "Quit", command = sys.quit())
    quit_button.pack(side = tkinter.LEFT)
    popWin.mainloop()

def mainCaller():
    main()

# def initialState():
#     start = tkinter.Tk()
#     start.geometry("100X100")
#     start_button = tkinter.Button(start, text = "Start", command = callMain())
#     start_button.pack()
#
# def callMain():
#     global angle
#     angle = 0
#
main()
# initialState()

