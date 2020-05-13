#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# cd c:Users\User\manim
# py -m manim try1.py nomdelaclass -pl
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)

class coordonnees2(GraphScene):
    CONFIG = {
        "x_min": -6,
        "x_max": 6,
        "x_axis_width": 9,
        "x_tick_frequency": 1,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": [1],
        "x_axis_label": "",
        "y_min": -4,
        "y_max": 4,
        "y_axis_height": 6,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": [1],
        "y_axis_label": "",
        "axes_color": BLUE,
        "graph_origin": 0 * DOWN + 0 * LEFT,
        "exclude_zero_label": False,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }
    def construct(self):
        self.setup_axes(animate=True)
        A=self.coords_to_point(0,-4)
        B=self.coords_to_point(0,4)
        axex=Arrow(A,B,buff=0).set_color(BLUE)
        A=self.coords_to_point(-6,0)
        B=self.coords_to_point(6,0)
        axey=Arrow(A,B,buff=0).set_color(BLUE)
        self.add(axex,axey)
        labelO=TexMobject("O")
        O=DotCross(self,0,0)
        labelO.next_to(O,DL,buff=0.05)
        self.add(labelO)
        x=3
        y=2
        labelM=TexMobject("M","(",str(x),"{;}",str(y),")")
        parentheses=VGroup(labelM[1],labelM[3],labelM[5])
        labelM[2].set_color(YELLOW)
        labelM[4].set_color(YELLOW)
        M=DotCross(self,x,y)
        M.set_color(GREEN)
        labelM.next_to(M,UR,buff=0.05)
        brace1 = Brace(parentheses, UP, buff = SMALL_BUFF)
        t1 = brace1.get_text("coordonnées")
        xM=self.coords_to_point(x,0)
        absM=TexMobject(str(x)).next_to(xM,DOWN,0.1)
        abscisse=TextMobject("abscisse").next_to(absM,DOWN,0.1)
        yM=self.coords_to_point(0,y)
        ordM=TexMobject(str(y)).next_to(yM,LEFT,0.1)
        ordonnee=TextMobject("ordonnée").next_to(ordM,LEFT,0.1)
        MxM=DashedLine(M,xM)
        MyM=DashedLine(M,yM)
        absM.set_color(YELLOW)
        ordM.set_color(YELLOW)
        self.play(Write(M))
        self.wait()
        self.play(Write(labelM[0]))
        self.wait()
        self.play(Write(MxM))
        self.wait()
        self.play(Write(absM))
        self.wait()
        self.play(Write(abscisse))
        self.wait()
        self.play(Write(MyM))
        self.wait()
        self.play(Write(ordM))
        self.wait()
        self.play(Write(ordonnee))
        self.wait()
        self.play(Write(parentheses))
        self.wait()
        self.play(ReplacementTransform(absM,labelM[2]))
        self.wait()
        self.play(ReplacementTransform(ordM,labelM[4]))
        self.wait()
        self.play(Write(brace1))
        self.wait()
        self.play(Write(t1))
        self.wait()
        x=-4
        y=2
        labelN=TexMobject("M","(",str(x),"{;}",str(y),")")
        labelN[2].set_color(YELLOW)
        labelN[4].set_color(YELLOW)
        N=DotCross(self,x,y)
        N.set_color(GREEN)
        labelN.next_to(N,UP,buff=0.05)
        xN=self.coords_to_point(x,0)
        absN=TexMobject(str(x)).next_to(xN,DOWN,0.1)
        yN=self.coords_to_point(0,y)
        ordN=TexMobject(str(y)).next_to(yN,RIGHT,SMALL_BUFF)
        absN.set_color(YELLOW)
        ordN.set_color(YELLOW)
        NxN=DashedLine(N,xN)
        NyN=DashedLine(N,yN)
        self.remove(abscisse,ordonnee,t1,brace1)
        self.wait()
        self.remove(absM,ordM)
        self.play(
            ReplacementTransform(M,N),
            ReplacementTransform(labelM,labelN),
            ReplacementTransform(MxM,NxN),
            ReplacementTransform(MyM,NyN)
            )
        self.wait()
        self.play(ReplacementTransform(labelN[2],absN))
        self.wait()
        self.play(ReplacementTransform(labelN[4],ordN))
        self.wait()
        self.remove(labelN[1],labelN[3],labelN[5])
        self.wait()
        x=5
        y=-3
        labelO=TexMobject("M","(",str(x),"{;}",str(y),")")
        parentheses=VGroup(labelO[1],labelO[3],labelO[5])
        labelO[2].set_color(YELLOW)
        labelO[4].set_color(YELLOW)
        O=DotCross(self,x,y)
        O.set_color(GREEN)
        labelO.next_to(O,DR,buff=0.05)
        xO=self.coords_to_point(x,0)
        absO=TexMobject(str(x)).next_to(xO,UP,0.1)
        yO=self.coords_to_point(0,y)
        ordO=TexMobject(str(y)).next_to(yO,LEFT,SMALL_BUFF)
        absO.set_color(YELLOW)
        ordO.set_color(YELLOW)
        OxO=DashedLine(O,xO)
        OyO=DashedLine(O,yO)
        self.wait()
        self.remove(absN,ordN)
        self.play(
            ReplacementTransform(N,O),
            ReplacementTransform(labelN[0],labelO[0]),
            ReplacementTransform(NxN,OxO),
            ReplacementTransform(NyN,OyO),
            ReplacementTransform(labelN[2],absO),
            ReplacementTransform(labelN[4],ordO)
            )
        self.wait()
        self.play(Write(parentheses))
        self.wait()
        self.play(ReplacementTransform(absO.copy(),labelO[2]))
        self.wait()
        self.play(ReplacementTransform(ordO.copy(),labelO[4]))
        self.wait()
        x=5
        y=-2
        labelN=TexMobject("M","(",str(x),"{;}",str(y),")")
        labelN[2].set_color(YELLOW)
        labelN[4].set_color(YELLOW)
        N=DotCross(self,x,y)
        N.set_color(GREEN)
        labelN.next_to(N,BOTTOM,buff=0.05)
        xN=self.coords_to_point(x,0)
        absN=TexMobject(str(x)).next_to(xN,UP,0.1)
        yN=self.coords_to_point(0,y)
        ordN=TexMobject(str(y)).next_to(yN,LEFT,SMALL_BUFF)
        absN.set_color(YELLOW)
        ordN.set_color(YELLOW)
        NxN=DashedLine(N,xN)
        NyN=DashedLine(N,yN)
        self.wait()
        self.play(
            ReplacementTransform(O,N),
            ReplacementTransform(labelO,labelN),
            ReplacementTransform(OxO,NxN),
            ReplacementTransform(OyO,NyN),
            ReplacementTransform(ordO,ordN),
            ReplacementTransform(absO,absN)
            )
        self.wait()
        x=5
        y=-1
        labelO=TexMobject("M","(",str(x),"{;}",str(y),")")
        parentheses=VGroup(labelO[1],labelO[3],labelO[5])
        labelO[2].set_color(YELLOW)
        labelO[4].set_color(YELLOW)
        O=DotCross(self,x,y)
        O.set_color(GREEN)
        labelO.next_to(O,BOTTOM,buff=0.05)
        xO=self.coords_to_point(x,0)
        absO=TexMobject(str(x)).next_to(xO,UP,0.1)
        yO=self.coords_to_point(0,y)
        ordO=TexMobject(str(y)).next_to(yO,LEFT,SMALL_BUFF)
        absO.set_color(YELLOW)
        ordO.set_color(YELLOW)
        OxO=DashedLine(O,xO)
        OyO=DashedLine(O,yO)
        self.wait()
        self.play(
            ReplacementTransform(N,O),
            ReplacementTransform(labelN,labelO),
            ReplacementTransform(NxN,OxO),
            ReplacementTransform(NyN,OyO),
            ReplacementTransform(ordN,ordO),
            ReplacementTransform(absN,absO)
            )
        self.wait()
        x=5
        y=-1
        labelN=TexMobject("M","(",str(x),"{;}",str(y),")")
        labelN[2].set_color(YELLOW)
        labelN[4].set_color(YELLOW)
        N=DotCross(self,x,y)
        N.set_color(GREEN)
        labelN.next_to(N,BOTTOM,buff=0.05)
        xN=self.coords_to_point(x,0)
        absN=TexMobject(str(x)).next_to(xN,UP,0.1)
        yN=self.coords_to_point(0,y)
        ordN=TexMobject(str(y)).next_to(yN,LEFT,SMALL_BUFF)
        absN.set_color(YELLOW)
        ordN.set_color(YELLOW)
        NxN=DashedLine(N,xN)
        NyN=DashedLine(N,yN)
        self.wait()
        self.play(
            ReplacementTransform(O,N),
            ReplacementTransform(labelO,labelN),
            ReplacementTransform(OxO,NxN),
            ReplacementTransform(OyO,NyN),
            ReplacementTransform(ordO,ordN),
            ReplacementTransform(absO,absN)
            )
        #self.wait()
        x=5
        y=0
        labelO=TexMobject("M","(",str(x),"{;}",str(y),")")
        parentheses=VGroup(labelO[1],labelO[3],labelO[5])
        labelO[2].set_color(YELLOW)
        labelO[4].set_color(YELLOW)
        O=DotCross(self,x,y)
        O.set_color(GREEN)
        labelO.next_to(O,BOTTOM,buff=0.05)
        xO=self.coords_to_point(x,0)
        absO=TexMobject(str(x)).next_to(xO,UP,0.1)
        yO=self.coords_to_point(0,y)
        ordO=TexMobject(str(y)).next_to(yO,LEFT,SMALL_BUFF)
        absO.set_color(YELLOW)
        ordO.set_color(YELLOW)
        OxO=DashedLine(O,xO)
        OyO=DashedLine(O,yO)
        self.wait()
        self.play(
            ReplacementTransform(N,O),
            ReplacementTransform(labelN,labelO),
            ReplacementTransform(NxN,OxO),
            ReplacementTransform(NyN,OyO),
            ReplacementTransform(ordN,ordO),
            ReplacementTransform(absN,absO)
            )
        self.remove(ordO,absO)
        self.wait()
        x=5
        y=1
        labelN=TexMobject("M","(",str(x),"{;}",str(y),")")
        labelN[2].set_color(YELLOW)
        labelN[4].set_color(YELLOW)
        N=DotCross(self,x,y)
        N.set_color(GREEN)
        labelN.next_to(N,UP,buff=0.05)
        xN=self.coords_to_point(x,0)
        absN=TexMobject(str(x)).next_to(xN,BOTTOM,0.1)
        yN=self.coords_to_point(0,y)
        ordN=TexMobject(str(y)).next_to(yN,LEFT,SMALL_BUFF)
        absN.set_color(YELLOW)
        ordN.set_color(YELLOW)
        NxN=DashedLine(N,xN)
        NyN=DashedLine(N,yN)
        self.wait()
        self.play(
            ReplacementTransform(O,N),
            ReplacementTransform(labelO,labelN),
            ReplacementTransform(OxO,NxN),
            ReplacementTransform(OyO,NyN),
            ReplacementTransform(ordO,ordN),
            ReplacementTransform(absO,absN)
            )
        self.wait()
        x=5
        y=3
        labelO=TexMobject("M","(",str(x),"{;}",str(y),")")
        parentheses=VGroup(labelO[1],labelO[3],labelO[5])
        labelO[2].set_color(YELLOW)
        labelO[4].set_color(YELLOW)
        O=DotCross(self,x,y)
        O.set_color(GREEN)
        labelO.next_to(O,UP,buff=0.05)
        xO=self.coords_to_point(x,0)
        absO=TexMobject(str(x)).next_to(xO,BOTTOM,0.1)
        yO=self.coords_to_point(0,y)
        ordO=TexMobject(str(y)).next_to(yO,LEFT,SMALL_BUFF)
        absO.set_color(YELLOW)
        ordO.set_color(YELLOW)
        OxO=DashedLine(O,xO)
        OyO=DashedLine(O,yO)
        self.wait()
        self.play(
            ReplacementTransform(N,O),
            ReplacementTransform(labelN,labelO),
            ReplacementTransform(NxN,OxO),
            ReplacementTransform(NyN,OyO),
            ReplacementTransform(ordN,ordO),
            ReplacementTransform(absN,absO)
            )
        self.wait()
        x=2
        y=3
        labelN=TexMobject("M","(",str(x),"{;}",str(y),")")
        labelN[2].set_color(YELLOW)
        labelN[4].set_color(YELLOW)
        N=DotCross(self,x,y)
        N.set_color(GREEN)
        labelN.next_to(N,UP,buff=0.05)
        xN=self.coords_to_point(x,0)
        absN=TexMobject(str(x)).next_to(xN,BOTTOM,0.1)
        yN=self.coords_to_point(0,y)
        ordN=TexMobject(str(y)).next_to(yN,LEFT,SMALL_BUFF)
        absN.set_color(YELLOW)
        ordN.set_color(YELLOW)
        NxN=DashedLine(N,xN)
        NyN=DashedLine(N,yN)
        self.wait()
        self.play(
            ReplacementTransform(O,N),
            ReplacementTransform(labelO,labelN),
            ReplacementTransform(OxO,NxN),
            ReplacementTransform(OyO,NyN),
            ReplacementTransform(ordO,ordN),
            ReplacementTransform(absO,absN)
            )
        self.wait()
        x=0
        y=3
        labelO=TexMobject("M","(",str(x),"{;}",str(y),")")
        parentheses=VGroup(labelO[1],labelO[3],labelO[5])
        labelO[2].set_color(YELLOW)
        labelO[4].set_color(YELLOW)
        O=DotCross(self,x,y)
        O.set_color(GREEN)
        labelO.next_to(O,RIGHT,buff=0.05)
        xO=self.coords_to_point(x,0)
        absO=TexMobject(str(x)).next_to(xO,BOTTOM,0.1)
        yO=self.coords_to_point(0,y)
        ordO=TexMobject(str(y)).next_to(yO,LEFT,SMALL_BUFF)
        absO.set_color(YELLOW)
        ordO.set_color(YELLOW)
        OxO=DashedLine(O,xO)
        OyO=DashedLine(O,yO)
        self.wait()
        self.play(
            ReplacementTransform(N,O),
            ReplacementTransform(labelN,labelO),
            ReplacementTransform(NxN,OxO),
            ReplacementTransform(NyN,OyO),
            ReplacementTransform(ordN,ordO),
            ReplacementTransform(absN,absO)
            )
        self.remove(absO,ordO)
        self.wait()
        x=0
        y=2
        labelN=TexMobject("M","(",str(x),"{;}",str(y),")")
        labelN[2].set_color(YELLOW)
        labelN[4].set_color(YELLOW)
        N=DotCross(self,x,y)
        N.set_color(GREEN)
        labelN.next_to(N,RIGHT,buff=0.05)
        xN=self.coords_to_point(x,0)
        absN=TexMobject(str(x)).next_to(xN,BOTTOM,0.1)
        yN=self.coords_to_point(0,y)
        ordN=TexMobject(str(y)).next_to(yN,LEFT,SMALL_BUFF)
        absN.set_color(YELLOW)
        ordN.set_color(YELLOW)
        NxN=DashedLine(N,xN)
        NyN=DashedLine(N,yN)
        self.wait()
        self.play(
            ReplacementTransform(O,N),
            ReplacementTransform(labelO,labelN),
            ReplacementTransform(OxO,NxN),
            ReplacementTransform(OyO,NyN)
            )
        self.wait()
        x=0
        y=0
        #labelO=TexMobject("O","(",str(x),";",str(y),")")
        #parentheses=VGroup(labelO[1],labelO[3],labelO[5])
        #labelO[2].set_color(YELLOW)
        #labelO[4].set_color(YELLOW)
        labelO=TexMobject("O")
        O=DotCross(self,x,y)
        O.set_color(GREEN)
        labelO.next_to(O,DL,buff=0.05)
        xO=self.coords_to_point(x,0)
        absO=TexMobject(str(x)).next_to(xO,BOTTOM,0.1)
        yO=self.coords_to_point(0,y)
        ordO=TexMobject(str(y)).next_to(yO,LEFT,SMALL_BUFF)
        absO.set_color(YELLOW)
        ordO.set_color(YELLOW)
        OxO=DashedLine(O,xO)
        OyO=DashedLine(O,yO)
        self.wait()
        self.play(
            ReplacementTransform(N,O),
            ReplacementTransform(labelN,labelO),
            ReplacementTransform(NxN,OxO),
            ReplacementTransform(NyN,OyO),
            )
        self.remove(absO,ordO)
        A=self.coords_to_point(-3,-2)
        B=self.coords_to_point(0,0)
        fleche=CurvedArrow(A,B)
        textorigin=TextMobject("Origine").next_to(A,LEFT,SMALL_BUFF)
        coordOrigin=TexMobject("O(0{;}0)").next_to(textorigin,BOTTOM,buff=0.01)
        A=self.coords_to_point(0,4)
        B=self.coords_to_point(5,0)
        textaxex=TextMobject("Axe des ordonnées").next_to(A,LEFT,SMALL_BUFF)
        textaxey=TextMobject("Axe des abscisses").next_to(B,DOWN,SMALL_BUFF)
        A=self.coords_to_point(3,2.5)
        titre1=TextMobject("Repérage").next_to(A)
        titre2=TextMobject("dans le plan").next_to(titre1,BOTTOM,buff=0.01)
        titre=VGroup(titre1,titre2)
        cadre=SurroundingRectangle(titre, buff = .1).set_color(RED)
        self.play(Write(fleche),Write(textorigin),Write(coordOrigin),Write(textaxex),Write(textaxey),Write(titre),ShowCreation(cadre))
        self.wait(3)

def DotCross(self,x,y): #Permet de faire une croix à l'emplacement d'un point
    MU=self.coords_to_point(x,y+0.2)
    MD=self.coords_to_point(x,y-0.2)
    ML=self.coords_to_point(x-0.2,y)
    MR=self.coords_to_point(x+0.2,y)
    LV=Line(MU,MD)
    LH=Line(ML,MR)
    return VGroup(LV,LH)

# See old_projects folder for many, many more
