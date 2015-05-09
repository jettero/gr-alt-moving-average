#!/usr/bin/env python2
# coding: utf8

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from gnuradio import analog

from math import cos,sin

import gr_alt_moving_average, cmath, os, time

class qa_root_sync(gr_unittest.TestCase):
    two_pi = cmath.pi * 2

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def _get_output(self, input, alpha):
        inv = blocks.vector_source_f(input)
        avg = gr_alt_moving_average.wmoving(alpha=alpha)
        ouv = blocks.vector_sink_f()

        self.tb.connect(inv, avg)
        self.tb.connect(avg, ouv)
        self.tb.run()

        return ouv.data()

    def test_000(self):
        inp = [15,7,0,9,0,1,0,1,0,1]
        output = self._get_output(input=inp, alpha=0.5)

        x=inp[0]
        for (i,v) in enumerate(inp):
            x = 0.5*x + 0.5*v
            self.assertAlmostEqual(output[i], x, delta=0.0001)

    def test_001(self):
        inp = [15,7,0,9,0,1,0,1,0,1]
        output = self._get_output(input=inp, alpha=1)

        for (i,v) in enumerate(inp):
            self.assertEqual(inp[i], v)

    def test_002(self):
        inp = [15,7,0,9,0,1,0,1,0,1]
        output = self._get_output(input=inp, alpha=0)

        for (i,v) in enumerate(inp):
            self.assertEqual(inp[0], v)

if __name__ == '__main__':
    x = os.getenv("TEST_PREFIX")

    if not x:
        x = "test_"

    gr_unittest.TestLoader.testMethodPrefix = x
    gr_unittest.main ()
