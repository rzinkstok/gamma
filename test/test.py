from unittest import TestCase
import numpy
import math
import gamma

NUMPOINTS = 101


class TestGamma(TestCase):
    def test_point_gamma(self):
        xs = numpy.arange(0, NUMPOINTS, 1)
        ref = numpy.ones(NUMPOINTS)
        ys = numpy.zeros(NUMPOINTS)
        self.assertEqual(gamma.point_gamma(xs, ys, ref, 5, delta_x=1, delta_y=1), 1.0)
        self.assertEqual(gamma.point_gamma(xs, ref, ref, 5.5, delta_x=1, delta_y=1), 0.5)

    def test_full_gamma(self):
        npoints = 4*NUMPOINTS
        xs = numpy.arange(0, npoints, 1)
        ref = numpy.array([math.sin(2*math.pi*x/npoints) for x in xs])
        shift = 6
        ys = numpy.array([math.sin(2*math.pi*(x-shift)/npoints) for x in xs])
        g = gamma.full_gamma(xs, ys, ref, 1, 1)
        self.assertAlmostEqual(g[0], math.sin(2*math.pi*shift/npoints), 6)
        self.assertAlmostEqual(g[npoints/4 + shift/2], 0, 6)

