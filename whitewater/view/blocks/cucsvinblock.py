from whitewater.view.pins import OutputPin
from whitewater.view.util import FileDialog
from whitewater.view.blocks.block import Block  # MYPY HACK

from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder

import cudf
from time import time

Builder.load_file('whitewater/view/blocks/cucsvinblock.kv')

class cuCSVInBlock(Block):
    out_1 = ObjectProperty()
    file_chosen = StringProperty()
    file_dialog = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_dialog = FileDialog(dir='~', filters=['*.csv'],
                                      size_hint=(0.8, 0.8))
        # This binds two properties together
        self.file_dialog.bind(file_chosen=self.setter('file_chosen'))
        self.tainted = True
        self.tainted_msg = 'File not chosen in block {}!'.format(self.title)

    def function(self):
        t0 = time()
        self.out_1.val = cudf.read_csv(self.file_chosen, header=0)
        t1 = time()
        print('\tTime for CSV Read of ', self.file_chosen, ': ', t1-t0)

    def on_file_chosen(self, instance, value):
        self.tainted = not value.endswith('.csv')
