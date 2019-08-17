import numpy
import pptk

P = numpy.random.rand(100, 3)
v = pptk.viewer(P)
v.set(point_size=0.01)