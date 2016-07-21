import numpy
from scipy.interpolate import interp1d

def point_gamma(x, y, ref_xs, ref_ys, delta_x, delta_y):
    """Calculates the 1D gamma value for a single point"""
    # Calculate the scaled squared distance between x and all ref_x values
    dx = numpy.square(numpy.array(ref_xs)-x)/delta_x**2
    # Calculate the scaled squared distance between y and all ref_y values
    dy = numpy.square(numpy.array(ref_ys)-y)/delta_y**2
    # Calcuate the total gamma values
    gammas = numpy.sqrt(dx+dy)
    # Return the minimum gamma
    return numpy.min(gammas)


def full_gamma(xs, ys, ref_xs, ref_ys, delta_x, delta_y):
    """Calculates the 1D gamma values for an array"""
    # Determine the smallest and largest common x coordinate
    min_x = max([min(xs), min(ref_xs)])
    max_x = min([max(xs), max(ref_xs)])

    # For all x coordinates within the shared range, calculate the gamma
    g = [[x, point_gamma(x, y, ref_xs, ref_ys, delta_x, delta_y)] for x, y in zip(xs, ys) if min_x <= x <= max_x]

    # Return the list of xs and the list of corresponding gammas
    return zip(*g)


