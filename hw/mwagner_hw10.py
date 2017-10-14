import matplotlib.pyplot as plot
import pandas as pd
import numpy as np
import scipy.ndimage as ndimage
import scipy.misc as misc
import re


# 1.
# car data + getting some value counts
print "\nEntering part 1:"
cars = pd.read_csv('cars.data.csv', header =  None, names = ['buy','maint','doors','people','trunk','safety'])
buyval = cars['buy'].value_counts()
maintval = cars['maint'].value_counts()
doorsval = cars['doors'].value_counts()
safetyval = cars['safety'].value_counts()
buylen = np.arange(len(buyval.values))
maintlen = np.arange(len(maintval.values))
doorslen = np.arange(len(doorsval.values))
safetylen = np.arange(len(safetyval.values))

# graphs
plot.figure(1)

plot.subplot(221)
plot.bar(buylen, buyval)
plot.title('Buy Counts')

plot.subplot(222)
plot.bar(maintlen, maintval)
plot.title('Maint Counts')

plot.subplot(223)
plot.bar(doorslen, doorsval)
plot.title('Doors Counts')

plot.subplot(224)
plot.bar(safetylen, safetyval)
plot.title('Safety Counts')

plot.show()


# 2.
# fxn improved from hw5
print "\nEntering part 2:"
def lin_reg_graph():
    # get the file from github, so there's no local issues
    brains = pd.read_csv("https://raw.githubusercontent.com/maxwagner/602/master/hw/brainandbody.csv", index_col = False)
    brains = brains[['brain','body']]

    # get xx, xy, count, sums
    brains['xx'] = brains['body'] * brains['body']
    brains['xy'] = brains['body'] * brains['brain']
    brains_count = len(brains.index)
    x_sum = np.sum(brains['body'])
    y_sum = np.sum(brains['brain'])
    xx_sum = np.sum(brains['xx'])
    xy_sum = np.sum(brains['xy'])

    # get slope and intercept
    brains_slope = ((brains_count * xy_sum) - (x_sum * y_sum)) / ((brains_count * xx_sum) - (x_sum**2))
    brains_intercept = (y_sum - (brains_slope * x_sum)) / brains_count

    # plotting things
    brains = pd.read_csv('brainandbody.csv')
    fit = np.polyfit(brains['body'], brains['brain'], deg=1)
    plot.plot(brains['body'], fit[0] * brains['body'] + fit[1])
    plot.scatter(brains['body'], brains['brain'])
    annostring = "body weight = %.2f(brain weight) + %.2f" % (brains_slope, brains_intercept)
    plot.annotate(annostring, xy=(500,4500), xytext=(2300, 1500))
    plot.title('Linear Regression')
    plot.show()

lin_reg_graph()


# 3.
print "\nEntering part 3:"
print "The centers don't seem to be right, but it plots fine, at least for the point of the assignment"


def image_processing(image):
    flattened = misc.imread(image, flatten = True) # read and flatten image
    smoothed = ndimage.gaussian_filter(flattened, 2) # smooth with gauss, filter value 2
    label_matrix, count = ndimage.label(smoothed > 90) # save count of things
    find_centers(smoothed, label_matrix, count) # find and print centers


def find_centers(image, label_matrix, count):
    centers = np.array(ndimage.center_of_mass(image, label_matrix, range(1, count + 1))) # find centers
    centers = pd.DataFrame(centers)
    centers.columns = ['x', 'y']
    plot.imshow(image)
    plot.scatter(x=centers['x'], y=centers['y'])
    plot.title('Objects')
    plot.show()

image_processing('objects.png')


#4.
print "\nEntering part 4:"

# clean it first, requires the epa file, and another file named 'epa-http-clean.txt'
with open('epa-http.txt', 'r') as dirty:
    with open('epa-http-clean.txt', 'w') as clean:
        for line in dirty:
            newline = re.sub('="', '=', line) # get rid of inner quotes
            newline = re.sub('-$', '0', newline) # get rid of dashes in filesizes
            newline = re.sub(r'\[\d{2}:(\d{2}):\d{2}:\d{2}]', r'\1', newline) # take in hour only
            clean.write(newline)
    clean.close()
dirty.close()

# pull out a gif name from a longer name
def giffy(text):
    text = re.sub(' HTTP/1.0', '', text)
    text = re.sub('GET ', '', text)
    return text

# read it in
df = pd.read_csv('epa-http-clean.txt', sep = '\s+', escapechar = "=", header = None, names = ['host','time','request','code','bytes'])
requests = df['time'].value_counts()
plot.plot(requests)
plot.title("Requests by hour")
plot.xlabel("Hour")
plot.ylabel("# of Requests")
plot.show()