import pygame as pg
import numpy as np

WINDOW_W = 960
WINDOW_H = 540
SCREEN_W, SCREEN_H = WINDOW_W / 2, WINDOW_H / 2


def main():
    pg.init()

    window = pg.display.set_mode((WINDOW_W, WINDOW_H), vsync=True)
    screen = pg.Surface((SCREEN_W, SCREEN_H))
    clock = pg.time.Clock()
    running = True
    data = [pos * [SCREEN_W, SCREEN_H] for pos in np.random.rand(100, 2)]
    centroids = [pos * [SCREEN_W, SCREEN_H] for pos in np.random.rand(3, 2)]

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill("black")

        for x, y in data:
            pg.draw.circle(screen, "white", (x, y), 2)

        for x, y in centroids:
            pg.draw.circle(screen, "green", (x, y), 3)

        resized = pg.transform.scale(screen, (WINDOW_W, WINDOW_H))
        window.blit(resized, (0, 0))

        pg.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
