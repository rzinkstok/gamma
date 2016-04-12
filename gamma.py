import numpy
from scipy.interpolate import interp1d

def point_gamma(xs, ys, refs, x_value, delta_x, delta_y):
    dx = numpy.square(xs-x_value)/delta_x**2
    interpolator = interp1d(xs, refs)
    ref_y = interpolator(x_value)
    dy = numpy.square(ys-ref_y)/delta_y**2
    return numpy.min(numpy.sqrt(dx+dy))


def full_gamma(xs, ys, refs, delta_x, delta_y):
    g = [point_gamma(xs, ys, refs, x, delta_x, delta_y) for x in xs]
    return g


