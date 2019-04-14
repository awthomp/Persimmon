from whitewater.view.blocks.block import Block  # MYPY HACK
from whitewater.view.pins import OutputPin

from kivy.properties import ObjectProperty
from kivy.lang import Builder

from sklearn.linear_model import SGDClassifier

Builder.load_file('whitewater/view/blocks/sgdblock.kv')

class SGDBlock(Block):
    est_out = ObjectProperty()

    def function(self):
        self.est_out.val = SGDClassifier()
