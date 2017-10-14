from tkinter import *
import math

####Ideas
# [ ] Make a gui for all the options
# [ ] Make a spacing option
# [ ] Make a color option (for lines)
# [ ] Make a bgcolor option
# [ ] Make "in" and "out" option
# [ ] Make a line thickness change function
# [ ] Make a drawStar function (specify a center then the points)
# [ ] Make an undo option !!!!!
# [ ] Make it so you can change from drawStar to drawCurve
####
# [ ] Make a helpDraw option (if you click near an existing point, it makes the thing you clicked go there, so like a smart click function)
# [ ] Make a highlight verticies option
# [ ] Make a helper options window that has checkboxes for helpDraw and highlight verticies
####
# [ ] Pop-up window for each option
####
# [ ] UPLOAD TO GitHub !!!!!!!!!


class DrawingProgram(Canvas):
    def __init__(self, root, w, h):
        Canvas.__init__(self, root, width=w, height=h)
        self.grid(row=0, column=0)
        self.clist = []
        self.totalclist = []

    def drawCurve(self, a, b, conv, spacing, color="black", bgcolor=None, deviation="in", width=1):
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
                self.create_line(bgverta[i][0], bgverta[i][1], bgvertb[len(bgvertb)-1-i][0], bgvertb[len(bgvertb)-1-i][1], fill=bgcolor)
                
        #line curve on inside of fill
        if deviation == "in":
            for i in range(0, len(bgvertb), len(bgvertb)//spacing):
                self.create_line(bgverta[i][0], bgverta[i][1], bgvertb[spacing-1-i][0], bgvertb[spacing-1-i][1], fill=color, width=width)

        #line curve on outside of fill
        else:
            for i in range(spacing):
                self.create_line(verta[i][0], verta[i][1], vertb[spacing-1-i][0], vertb[spacing-1-i][1], fill=color, width=width)

        
        self.create_line(a[0], a[1], conv[0], conv[1], fill=color, width=width)
        self.create_line(b[0], b[1], conv[0], conv[1], fill=color, width=width)
        
        #2## End of making the visible line curve (Two choices: inside or outside if there is a bgcolor)####


    #converting rgb to hex
    example_color = "#%02x%02x%02x" % (255, 0, 0)



    ######EXAMPLE FOR self.drawCurve FUNCTION######
    #       This is the bgcolor (background color) of the curve- V
    #                                                            |     V -This is the option to have the visible line curve be on the inside of the bgcolor of the curve or not ("in" and "out")
    #                       Color of lines of the curve- V       |     |
    #                                                    |       |     | -This will automatically go to "out" if there is not input at the end
    #                                                    V       V     V     v===This is the width of the curve lines, defaults to 1
    #self.drawCurve((100, 300), (300, 100), (300, 300), 10, "black", None, "out", 1)


    def drawSquare(self, tl, br, color, spacing, bgcolor,  deviation="out", rotate=False):
        if rotate:
            p1 = (math.floor(abs(tl[0]+br[0])/2), tl[1])
            p2 = (br[0], math.floor(abs(tl[1]+br[1])/2))
            p3 = (math.floor(abs(tl[0]+br[0])/2), br[1])
            p4 = (tl[0], math.floor(abs(tl[1]+br[1])/2))

            self.drawCurve(p1, p3, p2, spacing, color, bgcolor, deviation)
            self.drawCurve(p2, p4, p3, spacing, color, bgcolor, deviation)
            self.drawCurve(p3, p1, p4, spacing, color, bgcolor, deviation)
            self.drawCurve(p4, p2, p1, spacing, color, bgcolor, deviation)
        else:
            for i in range(4):
                if i == 0:
                    self.drawCurve((tl[0], br[1]), (br[0], tl[1]), (tl[0], tl[1]), spacing, color, bgcolor, deviation)
                elif i == 1:
                    self.drawCurve((tl[0], tl[1]), (br[0], br[1]), (br[0], tl[1]), spacing, color, bgcolor, deviation)
                elif i == 2:
                    self.drawCurve((tl[0], br[1]), (br[0], tl[1]), (br[0], br[1]), spacing, color, bgcolor, deviation)
                else:
                    self.drawCurve((tl[0], tl[1]), (br[0], br[1]), (tl[0], br[1]), spacing, color, bgcolor, deviation)

    ######EXAMPLE FOR drawSurve FUNCTION######
    #     Top left corner-|         |- Bottom right corner
    #                     |         |
    #                     |         |           |-Center of square
    #                     V         V           V       V-amount of lines per side
    #       drawSquare((0, 0), (600, 600), (300, 300), 34, None, "out", False)
    #                                                              ^       ^
    #            Whether the curves go in or out of the background-|       |
    #                 Rotating the square (basically the midpoint polygon)-|


    def leftClick(self, event):
        self.clist.append((event.x, event.y))
        if len(self.clist) == 3:
            self.totalclist.append((event.x, event.y))
            self.drawCurve(self.clist[0], self.clist[2], self.clist[1], 20, "black", None, "out", 1)
            for i in range(len(self.clist)):
                self.clist.remove(self.clist[0])

    def rightClick(self, event):
        for i in range(len(self.clist)):
            self.clist.remove(self.clist[0])
            #self.totalclist.remove()



root = Tk()
d = DrawingProgram(root, 600, 600)
d.bind("<Button-1>", d.leftClick)
d.bind("<Button-3>", d.rightClick)


root.mainloop()
