from unittest import TestCase
import numpy
import gamma


class TestGamma(TestCase):
    def test1(self):
        xs = numpy.arange(0,100,1)
        ref = numpy.ones(100)
        ys = numpy.zeros(100)
        self.assertEqual(gamma.gamma(xs, ys, ref, 5, delta_x=1, delta_y=1), 1.0)
        self.assertEqual(gamma.gamma(xs, ref, ref, 5.5, delta_x=1, delta_y=1), 0.5)


