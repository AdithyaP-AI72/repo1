from manim import *

class DrawCircle(Scene):
    def construct(self):
        # Create a circle with a specific radius and color
        circle = Circle(radius=2, color=BLUE)
        
        # Animate drawing the circle
        self.play(Create(circle))

        # Hold the final frame for a while
        self.wait(2)