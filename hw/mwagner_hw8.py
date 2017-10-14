# Max Wagner


import numpy
import scipy.ndimage as ndimage
import scipy.misc as misc


def image_processing(image):
    flattened = misc.imread(image, flatten = True) # read and flatten image
    smoothed = ndimage.gaussian_filter(flattened, 2) # smooth with gauss, filter value 2
    label_matrix, count = ndimage.label(smoothed > 90) # save count of things
    print "There are " + str(count) + " centers." # print count of things
    find_centers(smoothed, label_matrix, count) # find and print centers


def find_centers(image, label_matrix, count):
    centers = numpy.array(ndimage.center_of_mass(image, label_matrix, range(1, count + 1))) # find centers
    for center in centers:
        print "A center is located at: " + str(center)


print "############################# circles.png #############################"
image_processing('circles.png')
print "#######################################################################"

print "\n############################# objects.png #############################"
image_processing('objects.png')
print "#######################################################################"

print "\n############################# peppers.png #############################"
image_processing('peppers.png')
print "#######################################################################"