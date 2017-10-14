# Max Wagner
# I think I did the assignment correctly, but If I missed something let me know
# and I can add it.

import timeit

setup = '''
import pandas
import numpy
import copy
from scipy.optimize import curve_fit


# get the file we need
brains = pandas.read_csv("https://raw.githubusercontent.com/maxwagner/602/master/hw/brainandbody.csv", index_col = False)
brains = brains[['brain','body']]


# old fxn for linear regression
def lin_reg():
    # get xx, xy, count, sums
    brains['xx'] = brains['body'] * brains['body']
    brains['xy'] = brains['body'] * brains['brain']
    brains_count = len(brains.index)
    x_sum = numpy.sum(brains['body'])
    y_sum = numpy.sum(brains['brain'])
    xx_sum = numpy.sum(brains['xx'])
    xy_sum = numpy.sum(brains['xy'])

    # get slope and intercept
    brains_slope = ((brains_count * xy_sum) - (x_sum * y_sum)) / ((brains_count * xx_sum) - (x_sum**2))
    brains_intercept = (y_sum - (brains_slope * x_sum)) / brains_count
    return [brains_slope, brains_intercept]


# create a model
def func(x, a, b):
    return a * x + b
'''

n = 1000
t = timeit.Timer("x=copy.copy(brains); lin_reg()", setup=setup)
print 'Linear_Wk5   : ', t.timeit(n)
t = timeit.Timer("x=copy.copy(brains); curve_fit(func, x.brain, x.body)", setup=setup)
print 'SciPy        : ', t.timeit(n)