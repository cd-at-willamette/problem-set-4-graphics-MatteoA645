########################################
# Name: Matteo Alemany
# Collaborators:
# Estimate time spent (hrs):
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 50                       # Distance from left of window to origin
SCORE_DY = 50                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score
a = random.randrange(10,440)
b = random.randrange(10,440)
counter = 0
def clicky_box():
    counter = 0
    # Defining the callback function, which you won't need until Part C
    def on_mouse_down(event):
        
        x = event.get_x()
        y = event.get_y()
        counter = int(gw.box2.get_label())
        if x in range(gw.box.get_x(),gw.box.get_x()+51) and y in range(gw.box.get_y(),gw.box.get_y()+51):
            a2 = random.randrange(10,440)
            b2 = random.randrange(10,440)
            gw.box.set_location(a2,b2)
            counter +=1
            gw.box2.set_label(str(counter))
        else:
            counter = 0
            gw.box2.set_label(str(counter))

        



    # Down here you should initialize the window and draw the initial square
    # Make sure you tab it in so that it is part of the clicky_box function
    
    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    gw.add_event_listener("click",on_mouse_down)
    gw.box = GRect(a,b,SQUARE_SIZE,SQUARE_SIZE)
    gw.box2 = GLabel("0",SCORE_DX,SCORE_DY)
    gw.box2.set_font(SCORE_FONT)
    gw.box.set_filled(True)
    gw.box.set_color("red")
    gw.add(gw.box)
    gw.add(gw.box2)











if __name__ == '__main__':
    clicky_box()
