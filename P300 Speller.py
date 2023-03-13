import pygame as pg
import random as r
import time as t
import sys

pg.init()

width, height = 600, 750

window = pg.display.set_mode((width, height))
pg.display.set_caption("P300 Speller")

characters = "abcdefghijklmnopqrstuvwxyz0123456789".upper()

# Variables
turn = 0
black = (0, 0, 0)
grey = (125, 125, 125)
white = (255, 255, 255)
rNum = r.randint(0, 6)
speedUI = 1
multiplier = 0

# Text
font = pg.font.SysFont("times", 40, False, False)

time1 = t.time()

running = True

while running:

    window.fill(black)

    if t.time() - time1 >= (1 - multiplier):
        turn += 1
        rNum = r.randint(1, 6)
        if turn > 1:
            turn = 0
        time1 = t.time()
            
    x, y = 25, 50
    col = 1
    row = 1
    for item in characters:
        if col > 6:
            x = 25
            y += 100
            col = 1
            row += 1
        colour = grey
        if turn == 0:
            if row == rNum:
                colour = white
        else:
            if col == rNum:
                colour = white
        text = font.render(item, False, colour)
        window.blit(text, (x, y))
        x += 100
        col += 1

    # Speed contols
    lArrow = font.render("<", False, grey)
    rArrow = font.render(">", False, grey)
    speedText = font.render(str(speedUI), False, grey)
    speed2Text = font.render(f"{round(1 - multiplier, 2)} sec", False, grey)
    lArrowRect = lArrow.get_rect(center=(width/2 - 50, 650))
    rArrowRect = rArrow.get_rect(center=(width/2 + 50, 650))
    speedRect = speedText.get_rect(center=(width/2, 650))
    speed2Rect = speed2Text.get_rect(center=(width/2, 700))
    window.blit(lArrow, lArrowRect)
    window.blit(rArrow, rArrowRect)
    window.blit(speedText, speedRect)
    window.blit(speed2Text, speed2Rect)
    
    pg.display.flip()
         

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mPos = pg.mouse.get_pos()
            if lArrowRect.collidepoint(mPos):
                if speedUI > 1:
                    speedUI -= 1
                    multiplier -= 0.15
            elif rArrowRect.collidepoint(mPos):
                if speedUI < 5:
                    speedUI += 1
                    multiplier += 0.15

    
    pg.display.update()
