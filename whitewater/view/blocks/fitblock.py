from whitewater.view.blocks.block import Block  # MYPY HACK
from whitewater.view.pins import InputPin, OutputPin

from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('whitewater/view/blocks/fitblock.kv')

class FitBlock(Block):
    data_in = ObjectProperty()
    est_in = ObjectProperty()
    est_out = ObjectProperty()

    def function(self):
        X, y = self.data_in.val.iloc[:, :-1], self.data_in.val.iloc[:, -1]
        self.est_out.val = self.est_in.val.fit(X, y)
