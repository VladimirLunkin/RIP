from Figures.figure import Figure
from Figures.color import FigureColor
import math

class Circle(Figure):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, r_parm, color_param):
        self.r = r_parm
        self.fc = FigureColor()
        self.fc.colorproperty = color_param

    def square(self):
        return math.pi * (self.r ** 2)

    def __repr__(self):
        return '{} {} радиусом {} площадью {}'.format(
            Circle.get_figure_type(),
            self.fc.colorproperty,
            self.r,
            self.square()
        )
