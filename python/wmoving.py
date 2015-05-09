
from gnuradio import gr
from operator import itemgetter

import numpy, cmath, os

class wmoving(gr.sync_block):
    """
    weighted moving average
    """

    def __init__(self, alpha=0.5, samples=False):
        """
        Create the block

        Args:
        alpha: the weight of new information (vs the weight ov the average)

            avg = ( alpha * new ) + ( (1 - alpha) * avg )

        samples:
            alpha = (samples * (samples+1.0))/2.0
            avg = ( alpha * new ) + ( (1 - alpha) * avg )

        If both alpha and samples are given as arguments, samples overrides whatever
        is set for alpha.
        """

        if samples:
            self.set_samples(samples)

        else:
            self.set_alpha(alpha)

        self._first = True

        gr.sync_block.__init__(self, "wmoving_average", ["float32"], ["float32"])

    def set_alpha(self,alpha):
        self._alpha = numpy.float64(alpha) # promote some greater precision by invoking numpy 64
        self._beta  = (1 - alpha)

    def set_samples(self,samples):
        self.set_alpha( numpy.float64(2) / (1 + samples) )

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

        return p
