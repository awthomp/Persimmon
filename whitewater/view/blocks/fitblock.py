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
            # works for cuDF
            X, y = self.data_in.val.iloc[:, '0'], self.data_in.val.iloc[:, '1']
            # X needs to be DF, y series
            X = X.to_frame()
        except:
            # works for Pandas
            X, y = self.data_in.val.iloc[:, :-1], self.data_in.val.iloc[:, -1]
        self.est_out.val = self.est_in.val.fit(X, y)
        t1 = time()
        total = t1-t0
        print('\tTime for Predict: ', t1-t0)