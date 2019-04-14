from whitewater.view.pins import InputPin, OutputPin
from whitewater.view.blocks.block import Block  # MYPY HACK

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from sklearn.svm import SVC


Builder.load_file('whitewater/view/blocks/svmblock.kv')

class SVMBlock(Block):
    out_1 = ObjectProperty()

    def function(self):
        self.out_1.val = SVC()
