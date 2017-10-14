# Max Wagner
# The slope seems at least close to correct
# The intercept is questionable

import pandas
import numpy


def lin_reg():
    # get the file from github, so there's no local issues
    brains = pandas.read_csv("https://raw.githubusercontent.com/maxwagner/602/master/hw/brainandbody.csv", index_col = False)
    brains = brains[['brain','body']]

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
    print "Calculated Solution:"
    print "body weight = b(brain weight) + a"
    print "body weight = %.2f(brain weight) + %.2f" % (brains_slope, brains_intercept)


if __name__ == "__main__":
    lin_reg()