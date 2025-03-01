
from svgpathtools import svg2paths2, Arc 
from turtle import Turtle, Screen
import random

WIDTH = 1000
HEIGHT = 800

SVG_FILE = ''       # put absolute path to svg here

TRACER = 1
SPEED = 1

HexCodes = '0123456789ABCDEF'
# HexCodes = '01234567'

# innitialize turtle cursor and screen
t = Turtle()
sc = Screen()

# ------------------------- #
## Speed & Tracer Controls ##
# ------------------------- #

def speed_Up():
    global SPEED
    if SPEED < 10:
        SPEED += 1
        t.speed(SPEED)

def speed_Down():
    global SPEED
    if SPEED > 0:
        SPEED -= 1
        t.speed(SPEED)

def trace_Up():
    global TRACER
    TRACER += 10
    sc.tracer(TRACER, delay=0)

def trace_Down():
    global TRACER
    if TRACER > 1:
        TRACER = max(1, TRACER - 10 if TRACER > 10 else TRACER - 1)
        sc.tracer(TRACER, delay=0)

# ---------------------------- #
## Open and get info from svg ##
# ---------------------------- #

def read_svg(svg_file):
    # get paths attributes of paths and attributes of svg file
    paths, attributes, svg_attributes = svg2paths2(svg_file)
    viewbox = [float(f) for f in svg_attributes['viewBox'].split(' ')]      # get viewbox from svg attributes

    return paths, attributes, viewbox

# -------- #
## Colors ##
# -------- #

# simple function to generate random hex codes
def random_Color():
    return '#'+''.join(random.choice(HexCodes) for _ in range(6))

# simple function to get colors from path attributes, if no fill attribute go with just black
def getColors(attributes):
    return [attribute.get('fill', 'black') for attribute in attributes]

# ---------------------- #
## Get & Draw svg Paths ##
# ---------------------- #

# function to convert svg paths into actual turtle points with x,y coordinates
#  svg path may have many paths
#   each path have segments
#    each segment have points
#     so loop through all this stuff and reach to actual points(complex numbers)
#     then go back
#    put point into points array
#   put points array into segments array
#  put segments array into turtle_paths array
# return that ready to go turtle_paths array :))
# you can control x and y scale if you want
def get_svg_coordinates(paths, xscale=1, yscale=-1):
    turtle_paths = []
    for p in paths[:-1]:                # not last path because sometimes last path fills whole picture with solid color, so avoid it
        segments = []
        for segment in p:
            points = []
            # skipping Arcs because idk how to deal with them)
            if type(segment) == Arc:
                continue
            for point in segment:
                # real burt of complex num goes to x and imaginary part goes to y
                x, y = float(point.real), float(point.imag)
                points.append((x*xscale, y*yscale))
            segments.append(points)
        turtle_paths.append(segments)
    return turtle_paths

# function to draw converted points onto turtle screen
#  same thing as in get_svg_coordinates, but drawing points on screen at the bottom level of loop
# it can draw with or without filling paths
# also supports filling paths with random colors :)
def draw_paths(turtle_paths, colors, isRandomColor=False):
    for path_index, turtle_path in enumerate(turtle_paths):
        try:
            t.penup()
            t.goto(turtle_paths[path_index][0][0])              # go to the first point of nth path

            if colors:
                t.color(random_Color()) if isRandomColor else t.color(colors[path_index])
                t.begin_fill()

            t.pendown()
            for segment_index, turtle_segment in enumerate(turtle_path):
                t.penup()
                t.goto(turtle_path[segment_index][0])           # go to the first point of nth segment
                t.pendown()
                for turtle_point in turtle_segment:
                    x, y = turtle_point
                    t.goto(x, y)                        # go to actual point
            if colors:
                t.end_fill()
        except(IndexError):         # Prevent crashing on malformed paths
            pass

# ------ #
## Main ##
# ------ #

def main(isColors=True, isRandomColors=False):
    global SPEED, TRACER

    paths, attributes, viewbox = read_svg(SVG_FILE)         # read and get info from svg
    turtle_paths = get_svg_coordinates(paths, 1, -1)        # convert svg paths into turtle points

    # add speed&tracer functions to the keys
    sc.listen()
    sc.onkeypress(speed_Up, 'd')
    sc.onkeypress(speed_Down, 'a')
    sc.onkeypress(trace_Up, 'w')
    sc.onkeypress(trace_Down, 's')

    sc.setworldcoordinates(viewbox[0], -viewbox[3], viewbox[2], -viewbox[1])    # set viewbox
    sc.mode(mode='world')                                                       # set world mode
    sc.tracer(n=TRACER, delay=0)                                                # set tracer(images per turn)
    sc.setup(WIDTH, HEIGHT)                                                     # set screen size

    if isColors:
        colors = getColors(attributes)
    else:
        colors = []
        
    t.speed(SPEED)                                                              # set cursor speed
    draw_paths(turtle_paths, colors, isRandomColors)                            # draw svg on screen

    t.screen.mainloop()

if __name__ == '__main__':
    main()