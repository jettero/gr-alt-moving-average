
from gnuradio import gr
from operator import itemgetter

import numpy, cmath

class wmoving(gr.sync_block):
    """
    weighted moving average
    """

    def __init__(self, alpha=0.5):
        """
        Create the block

        Args:
        alpha: the weight

            avg = ( alpha * new ) + ( (1 - alpha) * avg )
        """

        self._alpha = alpha
        self._beta  = (1 - alpha)
        self._first = True

        gr.sync_block.__init__(self, "wmoving_average", ["float32"], ["float32"])

    def work(self, input_items, output_items):
        p = 0

        if self._first and len(input_items[0]):
            self._avg = input_items[0][p]
            output_items[0][p] = self._avg
            p = 1
            self._first = False;

        while p < len(input_items[0]):
            self._avg = self._alpha * input_items[0][p] + self._beta * self._avg
            output_items[0][p] = self._avg
            p = p + 1

        return len(input_items[0])
