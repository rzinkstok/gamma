import numpy
from scipy.interpolate import interp1d

def point_gamma(x, y, ref_xs, ref_ys, delta_x, delta_y):
    """Calculates the 1D gamma value for a single point"""
    dx = numpy.square(numpy.array(ref_xs)-x)/delta_x**2
    dy = numpy.square(numpy.array(ref_ys)-y)/delta_y**2
    return numpy.min(numpy.sqrt(dx+dy))


def full_gamma(xs, ys, ref_xs, ref_ys, delta_x, delta_y):
    """Calculates the 1D gamma values for an array"""
    max_x = min([max(xs), max(ref_xs)])
    g = [[x, point_gamma(x, y, ref_xs, ref_ys, delta_x, delta_y)] for x, y in zip(xs, ys) if x <= max_x]
    return zip(*g)


