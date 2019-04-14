from whitewater.view.pins import InputPin, OutputPin
from whitewater.view.blocks.block import Block  # MYPY HACK

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from sklearn.model_selection import KFold


Builder.load_file('whitewater/view/blocks/tenfoldblock.kv')

class TenFoldBlock(Block):
    out_1 = ObjectProperty()

    def function(self):
        self.out_1.val = KFold()
