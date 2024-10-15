########################################
# Name: Matteo Alemany
# Collaborators:
# Estimated time spent (hrs): 1
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15


def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """
    w = BRICK_WIDTH
    h = BRICK_HEIGHT
    b = BRICKS_IN_BASE
    gw = GWindow(WIDTH, HEIGHT)

    n=0
    g=600-h
    # You got it from here
    while b > 0:
        for i in range(b):
            gw.add(GRect(n+(w*i),g,w,h))
        g+=(-BRICK_HEIGHT)
        b+=(-1)
        n+=w/2

















if __name__ == '__main__':
    draw_pyramid()

















