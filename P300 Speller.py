import pygame as pg
import random as r
import time as t
import sys

pg.init()

width, height = 500, 600

window = pg.display.set_mode((width, height))
pg.display.set_caption("P300 Speller")

characters = "abcdefghijklmnopqrstuvwxyz0123456789".upper()

# Variables
turn = 0
black = (0, 0, 0)
grey = (125, 125, 125)
white = (255, 255, 255)
rNum = r.randint(0, 6)
speed1 = 1
speed2 = 1

# Text
font = pg.font.SysFont("times", 40, False, False)

onTime = t.time()
checkOn = False
offTime = t.time()
checkOff = True

flash = False

running = True

while running:

    window.fill(black)

    # If flash on duration has exceeded on time turn flash off
    if t.time() - onTime >= speed1 and checkOn == True:
        flash = False
        offTime = t.time()
        checkOff = True
        checkOn = False

    # If flash off duration has exceeded on time turn flash on
    if t.time() - offTime >= speed2 and checkOff == True:
        flash = True
        rNum = r.randint(1, 6)
        turn += 1
        if turn > 1:
            turn = 0
        onTime = t.time()
        checkOn = True
        checkOff = False
    
    x, y = 50, 50
    col = 1
    row = 1
    # Set coordinates for letters
    for item in characters:
        if col > 6:
            x = 50
            y += 75
            col = 1
            row += 1
        colour = grey
        # Set colour to white for row or column of the random number
        if flash == True:
            if turn == 0:
                if row == rNum:
                    colour = white
            else:
                if col == rNum:
                    colour = white
        text = font.render(item, False, colour)
        window.blit(text, (x, y))
        x += 75
        col += 1

    # Speed contols
    lArrow = font.render("<", False, grey)
    rArrow = font.render(">", False, grey)
    speedText = font.render(f"{round(speed1, 2)} sec", False, grey)
    speed2Text = font.render("On", False, grey)
    lArrowRect = lArrow.get_rect(center=(width/4 - 75, 510))
    rArrowRect = rArrow.get_rect(center=(width/4 + 75, 510))
    speedRect = speedText.get_rect(center=(width/4, 510))
    speed2Rect = speed2Text.get_rect(center=(width/4, 560))
    window.blit(lArrow, lArrowRect)
    window.blit(rArrow, rArrowRect)
    window.blit(speedText, speedRect)
    window.blit(speed2Text, speed2Rect)

    lArrow2 = font.render("<", False, grey)
    rArrow2 = font.render(">", False, grey)
    speedText2 = font.render(f"{round(speed2, 2)} sec", False, grey)
    speed2Text2 = font.render("Off", False, grey)
    lArrowRect2 = lArrow2.get_rect(center=((width/2) + width/4 - 75, 510))
    rArrowRect2 = rArrow2.get_rect(center=((width/2) + width/4 + 75, 510))
    speedRect2 = speedText2.get_rect(center=((width/2) + width/4, 510))
    speed2Rect2 = speed2Text2.get_rect(center=((width/2) + width/4, 560))
    window.blit(lArrow2, lArrowRect2)
    window.blit(rArrow2, rArrowRect2)
    window.blit(speedText2, speedRect2)
    window.blit(speed2Text2, speed2Rect2)
    
    pg.display.flip()
         
    # Inpu manager
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mPos = pg.mouse.get_pos()
            if lArrowRect.collidepoint(mPos):
                if speed1 > 0.1:
                    speed1 -= 0.15
            elif rArrowRect.collidepoint(mPos):
                if speed1 < 1:
                    speed1 += 0.15
            if lArrowRect2.collidepoint(mPos):
                if speed2 > 0.1:
                    speed2 -= 0.15
            elif rArrowRect2.collidepoint(mPos):
                if speed2 < 1:
                    speed2 += 0.15


    
    pg.display.update()
