import pygame
import random
import time
pygame.init()

win = pygame.display.set_mode((360,740))

pygame.display.set_caption("Piano Tiles Bootleg 4k")

"""
NOTES ON WHERE IM TAKING THIS !!!
IM THINKING OF A TXT BASED FILE SYSTEM
ITS PROLLY GON BE RLLY INEFFICIENT BUT IDGAF
ONE CHARACTER/LINE ====== ONE FRAME
EACH CHARACTER/LINE WOULD BE SOME KIND OF CODE FOR A NOTE OR SMTH IDFK
LETS GOOOOOOO  FUTURE ME U GOT THIS MY GUY
"""

screenX = 360
screenY = 740
tileW = 90
tileH = 135
tilespeed = 20
BACKDROP_COLOR =(255, 255, 255)

keypress_switcher = {
    # CheckForKeypress() which key to check for???
    1:pygame.K_d,
    2:pygame.K_f,
    3:pygame.K_j,
    4:pygame.K_k
}

class Column:
    def __init__(self, order, moving=True):
        #order = how many from da left (start from 0)
        self.order = order
        self.moving = moving
        self.button_color = (255, 255, 255) #draw it last my guyyyy
        self.tileYlist = [-135] #list of Y val
        self.isKeyPressed = False
        self.time = time.time() #idfk one of those last_time - now_time = 250ms

    def CheckForKeypress(self):
        keys = pygame.key.get_pressed()
        if keys[keypress_switcher.get(self.order)]:
            #check switcher if keypressed
            self.button_color = (150, 150, 150)
            self.isKeyPressed = True
        else:
            self.button_color = (BACKDROP_COLOR)
            self.isKeyPressed = False

    def UpdateColumn(self):
        randomthing = random.randint(0, 2)# i change dthis KLJ HSDLIF HJSDKRFGHAERSF
        current_time = time.time()
        popzero = False

        self.CheckForKeypress()

        if current_time - self.time >= 0.25:
            self.time = current_time
            if randomthing == 0: #fix this pls
                self.tileYlist.append(-135)

        pygame.draw.rect(win, (self.button_color), (self.order * (screenX / 4) - 90, screenY - tileH, tileW, tileH)) #draw button

        for idx, valY in enumerate(self.tileYlist):
            self.tileYlist[idx] += tilespeed
            if self.isKeyPressed and valY + tileH > screenY - tileH: #if key pressed and tile overlaps with button
                popzero = True
            else:
                pygame.draw.rect(win, (0, 0, 0), (self.order * (screenX / 4) - 90, valY, tileW, tileH)) #draw tile

        if popzero:
            self.tileYlist.pop(0)


column1 = Column(1)
column2 = Column(2)
column3 = Column(3)
column4 = Column(4)

columnlist = [column1, column2, column3, column4]

run = True
while run:
    pygame.time.delay(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255,255,255))
    for column in columnlist:
        column.UpdateColumn()
    pygame.draw.line(win, (0,0,0), (90, 0), (90, 740)) # guide lines
    pygame.draw.line(win, (0, 0, 0), (180, 0), (180, 740))
    pygame.draw.line(win, (0, 0, 0), (270, 0), (270, 740))
    pygame.draw.line(win,(0, 0, 0),(0, screenY - tileH), (screenX, screenY - tileH))
    pygame.display.update()

pygame.quit()
