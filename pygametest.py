import pgzrun

WIDTH = 450
HEIGHT = 600
TITLE = "MAHINS AWESOME GAME"

background = (230,140,60)
x=0
y=0
blue = (0,0,255)

def draw():
    screen.fill(background)
    screen.draw.filled_rect(Rect(x,y,50,50),blue)

def on_mouse_move(pos):
    global x
    global y
    x,y = pos
    
pgzrun.go()
