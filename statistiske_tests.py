from manimlib.imports import *
from scipy import special


class intro(Scene):
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
        title4 = TextMobject("\\bf FORDELINGSFUNKTION").scale(2).to_edge(LEFT).shift(2*DOWN)
        title3 = TextMobject("\\bf vs").next_to(title4,UP).align_to(title4,LEFT)
        title2 = TextMobject("\\bf TÆTHEDSFUNKTION").scale(2).next_to(title3,UP).align_to(title3,LEFT)
        title1 = TextMobject("\\bf STATISTIK").scale(2).next_to(title2,UP).align_to(title2,LEFT)
        
        color_text = VGroup(title2,title3,title4)
        color_text.set_color_by_gradient(BLUE,GREEN)
        #title2.set_color_by_gradient(BLUE,GREEN)
        #title3.set_color_by_gradient(BLUE,GREEN)

        
#################################################################
#                 _                    _    _
#    __ _  _ __  (_) _ ___ ___   __ _ | |_ (_)  ___   _ __   ___
#   / _` || `_ \ | || `_  \_  \ / _` || __|| | / _ \ | `_ \ / __|
#  | (_| || | | || || | | | | || (_| || |_ | || (_) || | | |\__ \
#   \__,_||_| |_||_||_| |_| |_| \__,_| \__||_| \___/ |_| |_||___/
#
#################################################################
        
        self.wait(1)
        self.play(Write(title1),run_time=1)
        self.wait(1)
        self.play(Write(title2,run_time=1))
        self.play(Write(title3,run_time=1))
        self.play(Write(title4,run_time=1))
        self.wait(3)
        
        self.play(FadeOutAndShiftDown(title1,run_time=2),FadeOutAndShiftDown(title2,run_time=2),FadeOutAndShiftDown(title3,run_time=2),FadeOutAndShiftDown(title4,run_time=2))
        self.wait(4)

class t_test(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 50,
        "x_axis_width" : 5,
        "x_labeled_nums": range(0,55,10),
        "x_axis_label": None,
        "y_min" : 0,
        "y_max" : 1,
        "y_axis_height": 4,
        "y_axis_label": None,
        "function_color" : "#258AE5",
        "axes_color" : WHITE,
        "x_tick_frequency" : 5,
        "y_tick_frequency" : 0.1,
        #"graph_origin": 2.5*LEFT
        #"camera_config" : {"background_color":"#1D153E"},
        #"camera_config" : {"background_color":"#060018"},# kunne godt vÃ¦re den der skal bruges
    }

    def erf_func(self,x):
        return 0.5*special.erf(0.1767766953*x-5.303300859)+0.5

    global sprd
    global middel
    sprd = 4
    middel = 30
	
    def norm_func(self,x):
        #return (x**3)-12*x+11
        return (1/sprd*np.sqrt(2*np.pi))*np.exp(-0.5*((x-middel)/sprd)**2)

    def construct(self):
        self.wait(2)
        #tæthedsfunktion
        tick1 = TextMobject("1,0").scale(0.75).shift(6*LEFT+2*UP)
        tick2 = TextMobject("0,5").scale(0.75).shift(6*LEFT+0*UP)
        tick3 = TextMobject("0,0").scale(0.75).shift(6*LEFT+2*DOWN)
        tal = VGroup(tick1,tick2,tick3)
        titel1 = TextMobject("Tæthedsfunktion").scale(0.75).shift(3*LEFT+2.5*UP)
        self.play(Write(titel1))
        self.graph_origin = 5.5*LEFT + 2*DOWN
        graf1 = self.setup_axes(animate=True)
        self.play(Write(tal))
        tæthedsfunktion = self.get_graph(self.norm_func)
        #gruppe_tæthedsfunktion = VGroup(tæthedsfunktion,titel2)

        #arealer
        areal1 = self.get_riemann_rectangles(tæthedsfunktion,x_min=0,x_max=15,dx=0.1)
        areal1.set_color_by_gradient(GREEN,BLUE)
        areal2 = self.get_riemann_rectangles(tæthedsfunktion,x_min=0,x_max=20,dx=0.1)
        areal2.set_color_by_gradient(GREEN,BLUE)
        areal3 = self.get_riemann_rectangles(tæthedsfunktion,x_min=0,x_max=25,dx=0.1)
        areal3.set_color_by_gradient(GREEN,BLUE)
        areal4 = self.get_riemann_rectangles(tæthedsfunktion,x_min=0,x_max=30,dx=0.1)
        areal4.set_color_by_gradient(GREEN,BLUE)
        areal5 = self.get_riemann_rectangles(tæthedsfunktion,x_min=0,x_max=35,dx=0.1)
        areal5.set_color_by_gradient(GREEN,BLUE)
        areal6 = self.get_riemann_rectangles(tæthedsfunktion,x_min=0,x_max=40,dx=0.1)
        areal6.set_color_by_gradient(GREEN,BLUE)
        areal7 = self.get_riemann_rectangles(tæthedsfunktion,x_min=0,x_max=45,dx=0.1)
        areal7.set_color_by_gradient(GREEN,BLUE)

        #fordelingsfunktion
        tal2 = tal.copy().shift(6.5*RIGHT)
        titel2 = TextMobject("Fordelingsfunktion").scale(0.75).shift(3.5*RIGHT+2.5*UP)
        self.play(Write(titel2))
        self.graph_origin = 1*RIGHT + 2*DOWN
        graf2 = self.setup_axes(animate=True)
        self.play(Write(tal2))
        fordelingsfunktion = self.get_graph(self.erf_func)
        #gruppe_fordelingsfunktion(fordelingsfunktion,titel1)

        #datapunkter
        ctp = self.coords_to_point
        data = [ctp(15,0.0000884172852),ctp(20,0.006209665326),ctp(25,0.1056497737),ctp(30,0.5000000000),ctp(35,0.8943502263),ctp(40,0.9937903347),ctp(45,0.9999115827)]


        punkter = []
        for j in data:
            punkt = Dot([j]).set_color(PURPLE)
            punkter.append(punkt)
        
        #eksempler på aflæsningen af fordelingsfunktion
        dot1 = Dot([ctp(0,0.25)]).set_color(YELLOW)
        dot2 = Dot([ctp(27.30204100,0.25)])
        dot3 = Dot([ctp(27.30204100,0)])
        værdi1 = TextMobject("27,3").scale(0.35).next_to(dot3,DOWN).shift(0.5*DOWN)
        dot4 = Dot([ctp(33,0)]).set_color(YELLOW)
        dot5 = Dot([ctp(33,0.7733726476)])
        dot6 = Dot([ctp(0,0.7733726476)])
        værdi2 = TextMobject("0,773").scale(0.35).next_to(dot6,LEFT)

        lign = TexMobject("p(x)=\\int_{-\\infty}^{x}\\frac{1}{\\sqrt{2\\pi}\\sigma}e^{-0,5(\\frac{x-\\mu}{\\sigma})^2}").scale(0.5).to_edge(DOWN)
        lign1 = TexMobject("p(15)=\\int_{-\\infty}^{15}\\frac{1}{\\sqrt{2\\pi}\\sigma}e^{-0,5(\\frac{x-\\mu}{\\sigma})^2}=0.00009").scale(0.5).to_edge(DOWN)
        lign2 = TexMobject("p(20)=\\int_{-\\infty}^{20}\\frac{1}{\\sqrt{2\\pi}\\sigma}e^{-0,5(\\frac{x-\\mu}{\\sigma})^2}=0.00621").scale(0.5).to_edge(DOWN)
        lign3 = TexMobject("p(25)=\\int_{-\\infty}^{25}\\frac{1}{\\sqrt{2\\pi}\\sigma}e^{-0,5(\\frac{x-\\mu}{\\sigma})^2}=0.10565").scale(0.5).to_edge(DOWN)
        lign4 = TexMobject("p(30)=\\int_{-\\infty}^{30}\\frac{1}{\\sqrt{2\\pi}\\sigma}e^{-0,5(\\frac{x-\\mu}{\\sigma})^2}=0.50000").scale(0.5).to_edge(DOWN)
        lign5 = TexMobject("p(35)=\\int_{-\\infty}^{35}\\frac{1}{\\sqrt{2\\pi}\\sigma}e^{-0,5(\\frac{x-\\mu}{\\sigma})^2}=0.89435").scale(0.5).to_edge(DOWN)
        lign6 = TexMobject("p(40)=\\int_{-\\infty}^{40}\\frac{1}{\\sqrt{2\\pi}\\sigma}e^{-0,5(\\frac{x-\\mu}{\\sigma})^2}=0.99379").scale(0.5).to_edge(DOWN)
        lign7 = TexMobject("p(45)=\\int_{-\\infty}^{45}\\frac{1}{\\sqrt{2\\pi}\\sigma}e^{-0,5(\\frac{x-\\mu}{\\sigma})^2}=0.99991").scale(0.5).to_edge(DOWN)

        #graphs = VGroup(fordelingsfunktion,tæthedsfunktion)
        self.wait(2)
        #self.play(Write(titel1))
        self.play(ShowCreation(tæthedsfunktion,run_time=3))
        self.wait(2)
        #self.play(AnimationGroup(
        #    *anim,lag_ration=0.1,run_time=3
        #    ))
        
        self.play(FadeIn(lign))
        self.wait(1)
        self.play(ShowCreation(areal1),ReplacementTransform(lign,lign1))
        self.wait(1)
        
        self.play(FadeIn(punkter[0]))
        self.wait(1)
        
        self.play(ReplacementTransform(areal1,areal2),ReplacementTransform(lign1,lign2))
        self.wait(1)
        
        self.play(FadeIn(punkter[1]))
        self.wait(1)
        
        self.play(ReplacementTransform(areal2,areal3),ReplacementTransform(lign2,lign3))
        self.wait(1)
        
        self.play(FadeIn(punkter[2]))
        self.wait(1)
        
        self.play(ReplacementTransform(areal3,areal4),ReplacementTransform(lign3,lign4))
        self.wait(1)
        
        self.play(FadeIn(punkter[3]))
        self.wait(1)
        
        self.play(ReplacementTransform(areal4,areal5),ReplacementTransform(lign4,lign5))
        self.wait(1)
        
        self.play(FadeIn(punkter[4]))
        self.wait(1)
        
        self.play(ReplacementTransform(areal5,areal6),ReplacementTransform(lign5,lign6))
        self.wait(1)
        
        self.play(FadeIn(punkter[5]))
        self.wait(1)
        
        self.play(ReplacementTransform(areal6,areal7),ReplacementTransform(lign6,lign7))
        self.wait(1)
        
        self.play(FadeIn(punkter[6]))
        self.wait(1)
        
        self.play(FadeOut(areal7),FadeOut(lign7))
        
        self.wait(2)
        
        
        self.play(ShowCreation(fordelingsfunktion,runtime=3))
        self.wait(2)

        self.play(FadeIn(dot1))
        self.wait(1)
        self.play(ApplyMethod(dot1.move_to,dot2))
        self.play(ApplyMethod(dot1.move_to,dot3))
        self.play(FadeInFrom(værdi1,DOWN))
        self.wait(1)

        self.play(FadeIn(dot4))
        self.wait(1)
        self.play(ApplyMethod(dot4.move_to,dot5))
        self.play(ApplyMethod(dot4.move_to,dot6))
        self.play(FadeInFrom(værdi2,LEFT))
        self.wait(1)