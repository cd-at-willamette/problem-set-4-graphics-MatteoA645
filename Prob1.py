############################################################
# Name: Matteo
# Name(s) of anyone worked with:
# Est time spent (hr): 1 hour
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel


def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    gw = GWindow(500, 500)
    w = 500
    o = GOval(w//5,w//5,200,200)
    o.set_filled(True)
    o.set_fill_color("yellow")
    gw.add(o)
    o2=GOval(125,125,150,150)
    o2.set_filled(True)
    o2.set_fill_color("blue")
    gw.add(o2)
    l=GLine(129,129,271,271)
    l2=GLine(129,271,271,129) #hated finding these coordinates with a passion
    gw.add(l)
    gw.add(l2)
    t=GLabel("Uncanny X-Men",w//5+30,w//10)
    r=GRect(100,100,200,200)
    r.set_filled(False)
    r.set_color("blue")
    gw.add(t)
    gw.add(r)





if __name__ == '__main__':
    draw_image()
