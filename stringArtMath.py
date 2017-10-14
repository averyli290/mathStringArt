from tkinter import *
import math

#IDEAS#
# Make a "painting" class that has the necessary functions and have a selector screen
# When the button to pop up the art is clicked, it pops another tkinter window up with the link to the painting somewhere on the window of the tkinter version of the art
# You can choose the size of the painting (aka the size of the tkinter window)
#   .-------------.
#   |  _____      |
#   | |Art 1|<======= (Is a button)
#   |             |
#   |_____________|
#    
#
#
# All necessary functions go into the class


window_width = int(input())
window_height = int(input())

root = Tk()
canv = Canvas(root, width=window_width, height=window_height)
canv.grid(row=0, column=0)

def drawCurve(a, b, conv, spacing, color="black", bgcolor=None, deviation="in", width=1):
    verta = []
    vertb = []
    bgverta = []
    bgvertb = []

    ####  Preparing the lists for connecting lines###
    bgspacing = math.ceil((abs(a[0]-conv[0])**2+abs(a[1]+conv[1])**2)**(1/2))
    
    #1## Beginning of working part###
        
    #making bgverta
    for i in range(bgspacing):
        bgverta.append([a[0]-math.floor((a[0]-conv[0])/bgspacing*i), a[1]-math.floor((a[1]-conv[1])/bgspacing*i)])
        
    #making bgvertb
    for i in range(bgspacing):
        bgvertb.append([b[0]-math.floor((b[0]-conv[0])/bgspacing*i), b[1]-math.floor((b[1]-conv[1])/bgspacing*i)])

    #1## End of working part###



    #2### Beginning of making the visible line curve####

    #making verta
    for i in range(spacing):
        verta.append([a[0]-math.floor((a[0]-conv[0])/spacing*i), a[1]-math.floor((a[1]-conv[1])/spacing*i)])

    #making vertb
    for i in range(spacing):
        vertb.append([b[0]-math.floor((b[0]-conv[0])/spacing*i), b[1]-math.floor((b[1]-conv[1])/spacing*i)])
    ####  End of Preparing the lists for connecting lines###

        
    #### Beginning of making the visible line curve (Two choices: inside or outside if there is a bgcolor)####

    #connecting the curve with bgcolor first (if there is one)
    if bgcolor != None:
        for i in range(bgspacing):
            canv.create_line(bgverta[i][0], bgverta[i][1], bgvertb[len(bgvertb)-1-i][0], bgvertb[len(bgvertb)-1-i][1], fill=bgcolor)
            
    #line curve on inside of fill
    if deviation == "in":
        for i in range(0, len(bgvertb), len(bgvertb)//spacing):
            canv.create_line(bgverta[i][0], bgverta[i][1], bgvertb[spacing-1-i][0], bgvertb[spacing-1-i][1], fill=color, width=width)

    #line curve on outside of fill
    else:
        for i in range(spacing):
            canv.create_line(verta[i][0], verta[i][1], vertb[spacing-1-i][0], vertb[spacing-1-i][1], fill=color, width=width)

    
    canv.create_line(a[0], a[1], conv[0], conv[1], fill=color, width=width)
    canv.create_line(b[0], b[1], conv[0], conv[1], fill=color, width=width)
    
    #2## End of making the visible line curve (Two choices: inside or outside if there is a bgcolor)####


#converting rgb to hex
example_color = "#%02x%02x%02x" % (255, 0, 0)



######EXAMPLE FOR drawCurve FUNCTION######
#       This is the bgcolor (background color) of the curve- V
#                                                            |     V -This is the option to have the visible line curve be on the inside of the bgcolor of the curve or not ("in" and "out")
#                       Color of lines of the curve- V       |     |
#                                                    |       |     | -This will automatically go to "out" if there is not input at the end
#                                                    V       V     V     v===This is the width of the curve lines, defaults to 1
#drawCurve((100, 300), (300, 100), (300, 300), 10, "black", None, "out", 1)


def drawSquare(tl, br, color, spacing, bgcolor,  deviation="out", rotate=False):
    if rotate:
        p1 = (math.floor(abs(tl[0]+br[0])/2), tl[1])
        p2 = (br[0], math.floor(abs(tl[1]+br[1])/2))
        p3 = (math.floor(abs(tl[0]+br[0])/2), br[1])
        p4 = (tl[0], math.floor(abs(tl[1]+br[1])/2))

        drawCurve(p1, p3, p2, spacing, color, bgcolor, deviation)
        drawCurve(p2, p4, p3, spacing, color, bgcolor, deviation)
        drawCurve(p3, p1, p4, spacing, color, bgcolor, deviation)
        drawCurve(p4, p2, p1, spacing, color, bgcolor, deviation)
    else:
        for i in range(4):
            if i == 0:
                drawCurve((tl[0], br[1]), (br[0], tl[1]), (tl[0], tl[1]), spacing, color, bgcolor, deviation)
            elif i == 1:
                drawCurve((tl[0], tl[1]), (br[0], br[1]), (br[0], tl[1]), spacing, color, bgcolor, deviation)
            elif i == 2:
                drawCurve((tl[0], br[1]), (br[0], tl[1]), (br[0], br[1]), spacing, color, bgcolor, deviation)
            else:
                drawCurve((tl[0], tl[1]), (br[0], br[1]), (tl[0], br[1]), spacing, color, bgcolor, deviation)

######EXAMPLE FOR drawSurve FUNCTION######
#     Top left corner-|         |- Bottom right corner
#                     |         |
#                     |         |           |-Center of square
#                     V         V           V       V-amount of lines per side
#       drawSquare((0, 0), (600, 600), (300, 300), 34, None, "out", False)
#                                                              ^       ^
#            Whether the curves go in or out of the background-|       |
#                 Rotating the square (basically the midpoint polygon)-|



#Picture 1 (first picture on webpage): https://mathcraft.wonderhowto.com/news/more-string-art-0132077/
def pic1(window_width, window_length, color1, color2):
    tl = [20, 20]
    br = [window_width, window_length]
    center = [math.floor((window_width+20)/2), math.floor((window_length+20)/2)]
    for i in range(15):
        if i % 2 == 0:
            c = color1
            rotate = False
            if i > 1:
                tl = (math.ceil((center[0]+tl[0])/2), math.ceil((center[1]+tl[1])/2))
                br = (math.ceil((center[0]+br[0])/2), math.ceil((center[1]+br[1])/2))
        else:
            c = color2
            rotate = True
            firstsquaresafety=False
        drawSquare((tl[0], tl[1]), (br[0], br[1]), c, 34, None, "out", rotate)

#pic1(window_width, window_height, "#211F2E", "#701A19")
#     ^    ^ 
#     |    |
#so put painting size here

#Picture 2? https://img.wonderhowto.com/img/17/69/63456337855033/0/create-parabolic-curves-using-straight-lines.w1456.jpg
#def pic2

def pic3(window_width, window_length):
    colors = ["red", "orange", "green", "blue", "violet"]
    tl = [20, 20]
    br = [window_width, window_length]
    center = [math.floor((window_width+20)/2), math.floor((window_length+20)/2)]
    for i in range(9):
        if i % 2 == 0:
            drawCurve((tl[0], tl[1]), (br[0], br[1]), (tl[0], br[1]), 50, "black", colors[i%len(colors)] ,"out", 1)
            drawCurve((tl[0], tl[1]), (br[0], br[1]), (br[0], tl[1]), 50, "black", colors[i%len(colors)], "out", 1)
        else:
            drawCurve((tl[0], br[1]), (br[0], tl[1]), (tl[0], tl[1]), 50, "black", colors[i%len(colors)] ,"out", 1)
            drawCurve((tl[0], br[1]), (br[0], tl[1]), (br[0], br[1]), 50, "black", colors[i%len(colors)], "out", 1)
        tl = (math.ceil((center[0]+tl[0])/2), math.ceil((center[1]+tl[1])/2))
        br = (math.ceil((center[0]+br[0])/2), math.ceil((center[1]+br[1])/2))

pic3(window_width, window_height)
