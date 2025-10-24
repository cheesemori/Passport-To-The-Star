import pygame as pg
import sys

pg.init()

game_version = "v0.1"
screen = pg.display.set_mode((1280, 720))
pg.display.set_caption(f'Passport To The Star {game_version}')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


