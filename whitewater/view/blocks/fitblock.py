from whitewater.view.blocks.block import Block  # MYPY HACK
from whitewater.view.pins import InputPin, OutputPin

from kivy.properties import ObjectProperty
from kivy.lang import Builder

from time import time


Builder.load_file('whitewater/view/blocks/fitblock.kv')

class FitBlock(Block):
    data_in = ObjectProperty()
    est_in = ObjectProperty()
    est_out = ObjectProperty()

    def function(self):
        t0 = time()
        #X, y = self.data_in.val.iloc[:, :-1], self.data_in.val.iloc[:, -1]
        try:
            # works for Pandas
            X, y = self.data_in.val.iloc[:, :-1], self.data_in.val.iloc[:, -1]
        except:
            # works for cuDF
            X, y = self.data_in.val.loc[:, ['col1', 'col2', 'col3']], self.data_in.val.loc[:, 'y']
            # transform DF to Series
            y = y['y']
        self.est_out.val = self.est_in.val.fit(X, y)
        t1 = time()
        total = t1-t0
        print('\tTime for Fit: ', t1-t0)