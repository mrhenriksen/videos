from manimlib.imports import *

class intro(Scene):
    CONFIG = {
       #"camera_config" : {"background_color":"#1D153E"},
       #"camera_config" : {"background_color":"#060018"},# kunne godt være den der skal bruges
    }
    def construct(self):
    
#################################################################
#              _
#   ___   ___ | |_  _   _  __ 
#  / __| / _ \| __|| | | || _ \
#  \__ \|  __/| |_ | |_| || __/
#  |___/ \___| \__| \___/ |_|
#
#################################################################  
        
        #***********************************
        #
        #         TITLEPAGE
        #
        #***********************************
        
        
        title3 = TextMobject("\\bf UDEN CAS").scale(4).to_edge(LEFT).shift(2*DOWN)
        title2 = TextMobject("\\bf MONOTONIFORHOLD").scale(2).next_to(title3,UP).align_to(title3,LEFT)
        title1 = TextMobject("\\bf BESTEM {}").scale(2).next_to(title2,UP).align_to(title2,LEFT)
        
        title11 = TextMobject("\\bf BESTEM {}").to_corner(UL).shift(0.1*DOWN)
        title21 = TextMobject("\\bf MONOTONIFORHOLD").next_to(title11,RIGHT)
        
        title3.set_color_by_gradient(RED,YELLOW)
        
        
        #***********************************
        #
        #         INTRO
        #
        #***********************************
        
        text1 = TextMobject("Bestem monotoniforhold for funktionen").scale(0.65).to_edge(LEFT).shift(2.5*UP)
        lign1 = TexMobject("f(x)","=","{x}","^3","-12x","+11").scale(0.65).next_to(text1,DOWN).align_to(text1,LEFT)
        
        
#################################################################
#                 _                    _    _
#    __ _  _ __  (_) _ ___ ___   __ _ | |_ (_)  ___   _ __   ___
#   / _ˋ || ˋ_ \ | || ˋ_  \_  \ / _ˋ || __|| | / _ \ | ˋ_ \ / __|
#  | (_| || | | || || | | | | || (_| || |_ | || (_) || | | |\__ \
#   \__,_||_| |_||_||_| |_| |_| \__,_| \__||_| \___/ |_| |_||___/
#
#################################################################
        
        #SCENE1 - intro
        self.play(Write(title1),Write(title2))
        self.play(Write(title3,run_time=2))
        self.wait(2)
        self.play(ReplacementTransform(title1,title11),ReplacementTransform(title2,title21,run_time = 2),FadeOut(title3,run_time=3))
        
        #SCENE2 - funktion
        #      TEKST OG FUNKTION
        self.play(FadeOut(title11),FadeOut(title21),Write(text1),run_time=2)
        self.wait(2)
        self.play(Write(lign1,run_time=2))
        self.wait(4)
        
        
class ver3(GraphScene):
    CONFIG = {
        "x_min" : -5,
        "x_max" : 5,
        "x_axis_width" : 6,
        "y_min" : -15,
        "y_max" : 30,
        "graph_origin" : 1.75*DOWN + 3.5*RIGHT,
        "function_color" : "#258AE5",
        "axes_color" : WHITE,
        "x_tick_frequency" : 10,
        "y_tick_frequency" : 45,
        #"camera_config" : {"background_color":"#1D153E"},
        #"camera_config" : {"background_color":"#060018"},# kunne godt være den der skal bruges
    }
    
    def  func_to_graph(self,x):
        return (x**3)-12*x+11
    
    def construct(self):
    
#################################################################
#              _
#   ___   ___ | |_  _   _  __ 
#  / __| / _ \| __|| | | || _ \
#  \__ \|  __/| |_ | |_| || __/
#  |___/ \___| \__| \___/ |_|
#
################################################################# 
    
        def alignEQ(eq1name,eq2name):
            a = 0
            b = 0
            pos1 = 0
            pos2 = 0
        
            for i in (eq1name):
                a += 1
        
            for i in (eq2name):
                b += 1
        
            for i in range(a):
                x = eq1name[i]
                for y in ("="):
                    if x == eq1name.get_part_by_tex(y):
                        pos1 = i
        
            for i in range(b):
                x = eq2name[i]
                for y in ("="):
                    if x == eq2name.get_part_by_tex(y):
                        pos2 = i
        
            eq2name[pos2].align_to(eq1name[pos1],LEFT)
        
            eq2name[0:pos2].next_to(eq2name[pos2],LEFT)
            eq2name[pos2+1:b].next_to(eq2name[pos2],RIGHT)
    
    #***********************************
    #
    #         INTRO
    #
    #***********************************
    
        title = TextMobject("BESTEM MONOTONIFORHOLD").to_corner(UL).shift(0.1*DOWN)
    
        text1 = TextMobject("Bestem monotoniforhold for funktionen").scale(0.65).to_edge(LEFT).shift(2.5*UP)
        lign1 = TexMobject("f(x)","=","{x}","^3","-12x","+11").scale(0.65).next_to(text1,DOWN).align_to(text1,LEFT)
        
        self.add(text1,lign1)
        
        
    #***********************************
    #
    #         GRAF
    #
    #***********************************
    
        
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph,self.function_color)
        
        
    #************************************************
    #
    #      INTERVAL ON GRAPH
    #
    #************************************************
    
        int_g1 = self.get_graph(self.func_to_graph, color = "#DAADEB", x_min = -5, x_max = -2)
        int_g2 = self.get_graph(self.func_to_graph, color = "#DAADEB", x_min = -2, x_max = 2)
        int_g3 = self.get_graph(self.func_to_graph, color = "#DAADEB", x_min = 2, x_max = 5)
    
    #***********************************
    #
    #         EKSTREMA
    #
    #*********************************** 
        
        # generate the location of extrema
        label_coord1 = self.input_to_graph_point(-2,func_graph)
        label_coord2 = self.input_to_graph_point(2,func_graph)
        
        # generate a circle to mark the extrema
        circle1 = Circle(radius=0.15, color="#FED735").move_to(label_coord1)
        circle2 = Circle(radius=0.15, color="#FED735").move_to(label_coord2)
        
        # generate text for the extrema
        spg = TextMobject("?")
        
        spg1 = spg.copy().next_to(circle1,UP)
        spg2 = spg.copy().next_to(circle2,DOWN)
        
        maxi = TextMobject("maksimum").scale(0.65).next_to(circle1,UP)
        mini = TextMobject("minimum").scale(0.65).next_to(circle2,DOWN)
    
    #***********************************
    #
    #         TEKST
    #
    #***********************************
    
        text2 = TextMobject("L\\o s ligningen").scale(0.65).next_to(lign1,DOWN).align_to(lign1,LEFT)
        lign2 = TexMobject("f'(x)","=","0").scale(0.65).next_to(text2,RIGHT)
        
    #***********************************
    #
    #        BEREGNINGER
    #
    #***********************************
        
        lign3 = TexMobject("f'(x)","=","3","{x}","^{3-1}","-12").scale(0.65).next_to(lign2,DOWN)
        lign31 = TexMobject("f'(x)","=","3","x","^2","-12").scale(0.65).move_to(lign3)
        lign311 = TexMobject("f'(x)","=","3","{x}","^2","-12").scale(0.65).move_to(lign3)
        
        lign6 = TexMobject("{x}","^2","=","{12","\\over","3}").scale(0.65).next_to(lign3,DOWN)
        
        lign4 = TexMobject("3","{x}","^2","-12","=","0").scale(0.65).next_to(lign6)
        lign41 = TexMobject("3","{x}","^2","-","12","=","0").scale(0.65).next_to(lign6)
        lign5 = TexMobject("3","{x}","^2","=","12").scale(0.65).move_to(lign6)
        lign61 = TexMobject("{x}","^2","=","12","\\over","3","=","4").scale(0.65).move_to(lign6)
        lign7 = TexMobject("{x}","=","\\sqrt{4}").scale(0.65).move_to(lign6)
        lign71 = TexMobject("x","=","\\pm 2").scale(0.65).move_to(lign6)
        
        alignEQ(lign2,lign3)
        alignEQ(lign2,lign31)
        alignEQ(lign2,lign311)
        alignEQ(lign2,lign6)
        alignEQ(lign2,lign4)
        alignEQ(lign2,lign41)
        alignEQ(lign2,lign5)
        alignEQ(lign2,lign61)
        alignEQ(lign2,lign7)
        alignEQ(lign2,lign71)
        
    #************************************************
    #
    #      TICKS 1
    #
    #************************************************
        
        START = [0,-0.1,0]
        END = [0,0.1,0]
        tick = Line(START, END, width=2)
        
        graf_axis = self.get_graph(lambda x : 0*x)
        
        tick_coord0 = self.input_to_graph_point(-5,graf_axis)
        tick_coord1 = self.input_to_graph_point(-2,graf_axis)
        tick_coord2 = self.input_to_graph_point(2,graf_axis)
        tick_coord3 = self.input_to_graph_point(5,graf_axis)
        
        tick0 = tick.copy().move_to(tick_coord0)
        tick1 = tick.copy().move_to(tick_coord1)
        tick2 = tick.copy().move_to(tick_coord2)
        tick3 = tick.copy().move_to(tick_coord3)
        
    #************************************************
    #
    #      VISUELT MAKS/MIN
    #
    #************************************************
        
        vert_line1 = self.get_vertical_line_to_graph(-2,func_graph,color="#48FFBA")
        vert_line2 = self.get_vertical_line_to_graph(2,func_graph,color="#48FFBA")
        
        x1 = TextMobject("-2").scale(0.65)
        x2 = TextMobject("2").scale(0.65)
        
        x1.next_to(vert_line1,DOWN) 
        x2.next_to(vert_line2,UP)
        
    #************************************************
    #
    #      INTERVAL ON AXIS
    #
    #************************************************
        
        ctp = self.coords_to_point
        
        int_line_a1 = Line(ctp(-5,0),ctp(-2,0),color="#FED735")
        int_line_a2 = Line(ctp(-2,0),ctp(2,0),color="#FED735")
        int_line_a3 = Line(ctp(2,0),ctp(5,0),color="#FED735")
        
        int_a1 = VGroup(tick0.copy().set_color("#FED735"),int_line_a1,tick1.copy().set_color("#FED735"))
        int_a2 = VGroup(tick1.copy().set_color("#FED735"),int_line_a2,tick2.copy().set_color("#FED735"))
        int_a3 = VGroup(tick2.copy().set_color("#FED735"),int_line_a3,tick3.copy().set_color("#FED735"))
        
    #************************************************
    #
    #      TICKS 2
    #
    #************************************************
        
        mark_coord1 = self.input_to_graph_point(-5,graf_axis)
        mark_coord2 = self.input_to_graph_point(-3,graf_axis)
        mark_coord3 = self.input_to_graph_point(0,graf_axis)
        mark_coord4 = self.input_to_graph_point(5,graf_axis)
        mark_coord5 = self.input_to_graph_point(3,graf_axis)
        
        mark1 = tick.copy().move_to(tick_coord1).set_color("#FED735")
        mark2 = tick.copy().move_to(mark_coord3).set_color("#FED735")
        mark3 = tick.copy().move_to(tick_coord2).set_color("#FED735")
        
        num1 = TexMobject("-3").next_to(mark_coord2,DOWN).set_color("#FED735").scale(0.65)
        num2 = TexMobject("0").next_to(mark2,DOWN).set_color("#FED735").scale(0.65)#.shift(0.2*RIGHT)
        num3 = TexMobject("3").next_to(mark_coord5,DOWN).set_color("#FED735").scale(0.65)
        
    #************************************************
    #
    #      FORTEGNSUNDERSØGELSE
    #
    #************************************************
        
        text3 = TextMobject("Bestem fortegn for $f'$").scale(0.65).next_to(lign6,DOWN).align_to(text1,LEFT)
        
        lign8 = TexMobject("f'(","x",")","=","3\\cdot(","{x}",")^2","-12").scale(0.65).next_to(text3,DOWN)
        lign9 = TexMobject("f'(","-3",")","=","3\\cdot(","{-3}",")^2","-12","=","{+}","15").scale(0.65).move_to(lign8)
        lign10 = TexMobject("f'(","0",")","=","3\\cdot(","{0}",")^2","-12","=","{-}","12").scale(0.65).move_to(lign9)
        lign11 = TexMobject("f'(","3",")","=","3\\cdot(","{3}",")^2","-12","=","{+}","15").scale(0.65).move_to(lign10)
        
        alignEQ(lign2,lign8)
        alignEQ(lign2,lign9)
        alignEQ(lign2,lign10)
        alignEQ(lign2,lign11)
        
    #************************************************
    #
    #      VISUELT HÆLDNING
    #
    #************************************************
        
        label_coord3 = self.input_to_graph_point(-3.5,func_graph)
        label_coord4 = self.input_to_graph_point(0,func_graph)
        label_coord5 = self.input_to_graph_point(3.5,func_graph)
        
        plus1 = lign9.get_part_by_tex("{+}").copy().move_to(label_coord3,RIGHT+DOWN).shift(0.1*LEFT)
        minus = lign10.get_part_by_tex("{-}").copy().move_to(label_coord4,LEFT+DOWN).shift(0.1*RIGHT)
        plus2 = lign11.get_part_by_tex("{+}").copy().move_to(label_coord5,LEFT+UP).shift(0.1*RIGHT)
        
    #************************************************
    #
    #      KONKLUSION
    #
    #************************************************
        
        text4 = TextMobject("$f$ er voksende i intervallerne $]-\\infty ,-2[$ og $]2 ,\\infty[$").scale(0.65).shift(2.25*DOWN).align_to(text1,LEFT)
        text5 = TextMobject("og aftagende i intervallet $]-2 ,2[$").scale(0.65).next_to(text4,DOWN).align_to(text1,LEFT)
        
        konkl = Group(text4,text5)
        
        box = Rectangle(height=0.75)
        box.surround(konkl)
        
        
#################################################################
#                 _                    _    _
#    __ _  _ __  (_) _ ___ ___   __ _ | |_ (_)  ___   _ __   ___
#   / _ˋ || ˋ_ \ | || ˋ_  \_  \ / _ˋ || __|| | / _ \ | ˋ_ \ / __|
#  | (_| || | | || || | | | | || (_| || |_ | || (_) || | | |\__ \
#   \__,_||_| |_||_||_| |_| |_| \__,_| \__||_| \___/ |_| |_||___/
#
#################################################################
        
        
        
        #SCENE3 - koordinatsystem og graf
        #      KOORDINATSYSTEM
        self.setup_axes(animate=True)
        self.wait(2)
        #      GRAF
        self.play(ShowCreation(func_graph, run_time=4))
        self.wait(4)
        
        #SCENE4 - voksende og faldende
        self.play(FadeIn(int_g1),FadeIn(int_g3))
        self.wait(2)
        self.play(FadeOut(int_g1),FadeOut(int_g3))
        self.wait(4)
        self.play(FadeIn(int_g2))
        self.wait(2)
        self.play(FadeOut(int_g2))
        self.wait(4)
    
        #SCENE5 - ekstrema
        #      EXTREMA
        self.play(GrowFromCenter(circle1),GrowFromCenter(circle2))
        self.wait(4)
        self.play(FadeOut(circle1),FadeOut(circle2))
        self.wait(4)
        
        #SCENE6 - ligning vi skal løse
        #      TEXT 2
        self.play(Write(text2))
        self.play(Write(lign2))
        self.wait(4)
        
        #SCENE7 - differentiation
        #      CALCULATIONS
        self.play(ReplacementTransform(lign1.get_part_by_tex("f(x)").copy(),lign3.get_part_by_tex("f'(x)"),run_time=2))
        self.play(ReplacementTransform(lign1.get_part_by_tex("=").copy(),lign3.get_part_by_tex("="),run_time=2))
        self.wait(4)
        self.play(ReplacementTransform(lign1.get_part_by_tex("^3").copy(),lign3.get_part_by_tex("3"),run_time=2))
        self.wait(1)
        self.play(ReplacementTransform(lign1.get_part_by_tex("{x}").copy(),lign3.get_part_by_tex("{x}"),run_time=2))
        self.wait(1)
        self.play(ReplacementTransform(lign1.get_part_by_tex("^3").copy(),lign3.get_part_by_tex("^{3-1}"),run_time=2))
        self.wait(1)
        self.play(ReplacementTransform(lign1.get_part_by_tex("-12x").copy(),lign3.get_part_by_tex("-12"),run_time=2))
        self.wait(2)
        self.play(ReplacementTransform(lign3,lign31,run_time=2))
        self.wait(4)
    
        #SCENE8 - beregning
        self.play(*[
            ReplacementTransform(
                lign311.get_part_by_tex(tex),
                lign4.get_part_by_tex(tex),
                run_time=2
            )
            for tex in ("3","{x}","^2","-12")
        ])
        self.play(*[
            Write(
                lign4.get_part_by_tex(tex1),
                run_time=2
            )
            for tex1 in ("=","0")
        ])
        self.wait(2)
        self.remove(lign4)
        self.play(*[
            ReplacementTransform(
                lign41.get_part_by_tex(tex),
                lign5.get_part_by_tex(tex),
                run_time=2
            )
            for tex in ("3","{x}","^2","=","12")
            ]+[
                FadeOut(lign4)
        ])
        self.wait(2)
        self.play(*[
            ReplacementTransform(
                lign5.get_part_by_tex(tex),
                lign6.get_part_by_tex(tex),
                run_time = 2
            )
            for tex in ("3","{x}","^2","=","12",)
            ]+[
            #    Write(lign6.get_part_by_tex("over"))
            FadeIn(lign6.get_part_by_tex("over"))
        ])
        self.wait(2)
        self.play(*[
            Transform(
                lign6.get_part_by_tex(tex1),
                lign61.get_part_by_tex("4").next_to(lign6.get_part_by_tex("=")),
                run_time=2
            )
            for tex1 in ("{12","over","3}")
        ])
        self.wait(2)
        self.play(ReplacementTransform(lign6,lign7,run_time=2))
        self.wait(2)
        self.play(ReplacementTransform(lign7,lign71,run_time=2))
        self.wait(4)
    
        #SCENE9 - tjek af løsning
    
        #SCENE10 - løsning visuelt
        #      VISUELT MAKS/MIN
        self.play(
            ShowCreation(tick1),
            ShowCreation(tick2),
            ReplacementTransform(lign71.get_part_by_tex("\\pm 2").copy(),x1),
            ReplacementTransform(lign71.get_part_by_tex("\\pm 2").copy(),x2),
            run_time=2
        ) # ADDS TICKMARKS AND NUMBERS
        self.wait(2)
        self.play(ShowCreation(DashedVMobject(vert_line1)),ShowCreation(DashedVMobject(vert_line2)),run_time=2) # ADDS VERTICAL LINES
        self.wait(2)
        self.play(GrowFromCenter(circle1),GrowFromCenter(circle2))
        self.wait(4)
        self.play(FadeInFrom(spg1,direction=DOWN),FadeInFrom(spg2,direction=UP))
        self.wait(2)
        self.play(FadeOut(spg1),FadeOut(spg2))
        self.play(FadeOut(circle1),FadeOut(circle2))
        self.wait(4)
        
        #SCENE11 - intervaller
        self.play(FadeIn(int_a1))
        self.play(FadeIn(int_a2),ApplyMethod(int_a1.shift,DOWN))
        self.play(FadeIn(int_a3),ApplyMethod(int_a2.shift,DOWN))
        self.play(ApplyMethod(int_a3.shift,DOWN))
        self.wait(4)
        self.play(WiggleOutThenIn(int_a1))
        self.wait(1)
        self.play(WiggleOutThenIn(int_a2))
        self.wait(1)
        self.play(WiggleOutThenIn(int_a3))
        self.wait(4)
        self.play(ApplyMethod(int_a3.shift,UP))
        self.play(ApplyMethod(int_a2.shift,UP),FadeOut(int_a3))
        self.play(ApplyMethod(int_a1.shift,UP),FadeOut(int_a2))
        self.play(FadeOut(int_a1))
        self.wait(4)
        
    
        #SCENE12 - fortegnsvariation
        #      tekst
        self.play(Write(text3))
        self.wait(4)
        
        #      TICK 2
        #first interval
        self.play(ApplyMethod(mark1.move_to,mark_coord1))
        self.play(ApplyMethod(mark1.move_to,tick_coord1))
        self.play(ApplyMethod(mark1.move_to,mark_coord2))
        self.play(FadeIn(num1))
        
        self.play(Write(lign8))
        self.wait(4)
        #self.play(ReplacementTransform(num1,lign8.get_part_by_tex("x")),ReplacementTransform(num1.copy(),lign8.get_part_by_tex("{x}")))
        self.play(ReplacementTransform(lign8,lign9[0:8]),ReplacementTransform(num1,lign9.get_part_by_tex("-3")),ReplacementTransform(num1.copy(),lign9.get_part_by_tex("{-3}")))
        self.wait(2)
        self.play(Write(lign9[8:11]))
        self.wait(4)
        self.play(FadeIn(int_g1))
        self.wait(2)
        self.play(FadeOut(int_g1))
        self.wait(2)
        self.play(ReplacementTransform(lign9.get_part_by_tex("{+}").copy(),plus1))
        #self.play(ApplyMethod(lign9.get_part_by_tex("{+}").copy().move_to,label_coord3,RIGHT+DOWN))
        self.play(FadeOut(mark1))
        self.wait(4)
        
         #second interval
        self.play(ApplyMethod(mark2.move_to,tick_coord1))
        self.play(ApplyMethod(mark2.move_to,tick_coord2))
        self.play(ApplyMethod(mark2.move_to,mark_coord3))
        self.play(FadeIn(num2))
        
        self.play(FadeOut(lign9),FadeIn(lign8))
        #self.remove(lign9)
        #self.add(lign8)
        #self.play(FadeIn(lign8))
        self.play(ReplacementTransform(lign8,lign10[0:8]),ReplacementTransform(num2,lign10.get_part_by_tex("0")),ReplacementTransform(num2.copy(),lign10.get_part_by_tex("{0}")))
        #self.play(ReplacementTransform(lign9[0:8],lign10[0:8]))
        self.wait(2)
        self.play(Write(lign10[8:11]))
        self.wait(4)
        self.play(FadeIn(int_g2))
        self.wait(2)
        self.play(FadeOut(int_g2))
        self.wait(2)
        self.play(ReplacementTransform(lign10.get_part_by_tex("{-}").copy(),minus))
        #self.play(ApplyMethod(lign10.get_part_by_tex("{-}").copy().move_to,label_coord4,LEFT+DOWN))
        self.play(FadeOut(mark2))
        self.wait(4)
        
         #third interval
        self.play(ApplyMethod(mark3.move_to,mark_coord4))
        self.play(ApplyMethod(mark3.move_to,tick_coord2))
        self.play(ApplyMethod(mark3.move_to,mark_coord5))
        self.play(FadeIn(num3))
        
        self.play(FadeOut(lign10[8:11]))
        self.play(ReplacementTransform(lign10[0:8],lign11[0:8]),ReplacementTransform(num3,lign11.get_part_by_tex("3")),ReplacementTransform(num3.copy(),lign11.get_part_by_tex("{3}")))
        self.wait(2)
        self.play(Write(lign11[8:11]))
        self.wait(4)
        self.play(FadeIn(int_g3))
        self.wait(2)
        self.play(FadeOut(int_g3))
        self.wait(2)
        self.play(ReplacementTransform(lign11.get_part_by_tex("{+}").copy(),plus2))
        #self.play(ApplyMethod(lign11.get_part_by_tex("{+}").copy().move_to,label_coord5,LEFT+UP))
        self.play(FadeOut(mark3))
        self.wait(4)
        
        #SCENE13 - konklusion
        self.play(ShowCreation(box,run_time=2),Write(text4))
        self.play(Write(text5))
        self.wait(4)
    
class outro(Scene):
    CONFIG = {
       #"camera_config" : {"background_color":"#1D153E"},
       #"camera_config" : {"background_color":"#060018"},# kunne godt være den der skal bruges
    }
    def construct(self):

#################################################################
#              _
#   ___   ___ | |_  _   _  __ 
#  / __| / _ \| __|| | | || _ \
#  \__ \|  __/| |_ | |_| || __/
#  |___/ \___| \__| \___/ |_|
#
#################################################################

        github_logo = SVGMobject('github').scale(0.6)
        github_logo.set_color(WHITE)
        github_logo.move_to(1.6*LEFT)
        
        github = TexMobject('\\texttt{github.com/mrhenriksen}').scale(0.6)
        github.next_to(github_logo,RIGHT)
        github_3b1b = TexMobject('\\texttt{github.com/3b1b/manim}').scale(0.6)
        github_3b1b.next_to(github_logo,RIGHT)
        
        see_description = TextMobject("Se beskrivelse for kildekode").scale(1.2)
        see_description.set_color_by_gradient(RED,BLUE,RED)
        
        acknowledge_3b1b = TextMobject(
            'Lavet med Manim ',
            '(skabt af ',
            '3Blue',
            '1Brown',
            ')'
        ).scale(1.2)
        acknowledge_3b1b[0].set_color_by_gradient(YELLOW,GREEN)
        acknowledge_3b1b[1].set_color(WHITE)
        acknowledge_3b1b[2].set_color(BLUE)
        acknowledge_3b1b[3].set_color(GREY_BROWN)
        acknowledge_3b1b[4].set_color(WHITE)
        acknowledge_3b1b.move_to(1.2*UP)
        
#################################################################
#                 _                    _    _
#    __ _  _ __  (_) _ ___ ___   __ _ | |_ (_)  ___   _ __   ___
#   / _ˋ || ˋ_ \ | || ˋ_  \_  \ / _ˋ || __|| | / _ \ | ˋ_ \ / __|
#  | (_| || | | || || | | | | || (_| || |_ | || (_) || | | |\__ \
#   \__,_||_| |_||_||_| |_| |_| \__,_| \__||_| \___/ |_| |_||___/
#
#################################################################
        
        self.play(
            Write(see_description),
            run_time = 2
        )
        
        self.play(
            ApplyMethod(see_description.shift,1.2*UP)
        )    
        
        self.play(
            Write(github_logo),
            Write(github),
            run_time = 2
        )
        
        self.wait(4)
        
        self.play(
            ReplacementTransform(github,github_3b1b),
            ReplacementTransform(see_description,acknowledge_3b1b),
            run_time = 2
        )
        
        self.wait(4)
        
        self.play(
            FadeOut(github_3b1b),
            FadeOut(acknowledge_3b1b),
            FadeOut(github_logo),
            run_time = 8
        )
        
        self.wait()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
