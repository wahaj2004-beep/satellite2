import pgzrun
import random
import time

WIDTH = 800
HEIGHT = 480

num_of_sat = 8

sat1 = []

start_time= 0
end_time= 0
total_time= 0

lines = []
next_satellite= 0



def create_satellite():
    global start_time
    for i in range(num_of_sat):
        satellite1 = Actor("satellite")
        satellite1.pos=random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40)
        sat1.append(satellite1)
    start_time=time.time()


def draw():
    global lines, total_time
    screen.blit("backgroundimage", (0,0))
    number = 1
    for i in sat1:
        screen.draw.text(str(number), (i.pos[0],i.pos[1]+20))
        i.draw()
        number = number+1

        if next_satellite < num_of_sat:
            total_time = time.time() - start_time
            screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)

        else:
            screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)


        for i in lines:
            screen.draw.line(i[0], i[1], "white")

def on_mouse_down(pos):
    global next_satellite, lines
    if sat1[next_satellite].collidepoint(pos):
        if next_satellite:
            lines.append((sat1[next_satellite - 1].pos, sat1[next_satellite].pos))
        next_satellite+=1
    else:
        next_satellite = 0
        lines = []

        
    
    

create_satellite()
pgzrun.go()