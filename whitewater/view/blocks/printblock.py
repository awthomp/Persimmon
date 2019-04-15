from whitewater.view.pins import InputPin
from whitewater.view.util import Notification
from whitewater.view.blocks.block import Block  # MYPY HACK
from kivy.lang import Builder
from kivy.properties import ObjectProperty


Builder.load_file('whitewater/view/blocks/printblock.kv')

class PrintBlock(Block):
    in_1 = ObjectProperty()

    def function(self):
        try:
            gdf = in_1.val.to_pandas()
            Notification(title='Print results',
                         message=str(gdf)).open()
        except:
            Notification(title='Print results',
                         message=str(self.in_1.val)).open()
            
