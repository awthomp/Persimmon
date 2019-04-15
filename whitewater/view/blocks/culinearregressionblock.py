from whitewater.view.pins import OutputPin
from whitewater.view.blocks.block import Block  # MYPY HACK

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from cuml.linear_model import LinearRegression


Builder.load_file('whitewater/view/blocks/culinearregressionblock.kv')

class cuLinearRegressionBlock(Block):
    out_1 = ObjectProperty()

    def function(self):
        self.out_1.val = LinearRegression()