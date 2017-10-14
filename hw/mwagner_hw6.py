# Max Wagner


import timeit
setup = '''
import random
import numpy
import copy


# sort with loops
def sortwithloops(input):
    input = list(input)
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            if input[j] < input[i]:
                input[j], input[i] = input[i], input[j]
    return input


# sort without loops
def sortwithoutloops(input):
    return sorted(input)


# sort with numpy
def sortwithnumpy(input):
    return numpy.sort(numpy.array(input))


# search with loops
def searchwithloops(input, value):
    for i in range(len(input)):
        if i == value:
            return True
    return False


# search without loops
def searchwithoutloops(input, value):
    return value in input


def searchwithnumpy(input, value):
    return True in numpy.in1d(numpy.array(input), value)


L = [5,3,6,3,13,5,6]
L2 = random.sample(xrange(10000), 100)
'''

n = 1000
print "#######################################################"
print "#               1000 Trials - Sorting                 #"
print "#                     Short List                      #"
print "#######################################################"
t = timeit.Timer("x=copy.copy(L); sortwithloops(x)", setup=setup)
print 'WithLoops   : ', t.timeit(n)
t = timeit.Timer("x=copy.copy(L); sortwithoutloops(x)", setup=setup)
print 'WithoutLoops: ', t.timeit(n)
t = timeit.Timer("x=copy.copy(L); sortwithnumpy(x)", setup=setup)
print 'WithNumPy   : ', t.timeit(n),"\n"


print "#######################################################"
print "#               1000 Trials - Sorting                 #"
print "#                     Long List                       #"
print "#######################################################"
t = timeit.Timer("x=copy.copy(L2); sortwithloops(x)", setup=setup)
print 'WithLoops   : ', t.timeit(n)
t = timeit.Timer("x=copy.copy(L2); sortwithoutloops(x)", setup=setup)
print 'WithoutLoops: ', t.timeit(n)
t = timeit.Timer("x=copy.copy(L2); sortwithnumpy(x)", setup=setup)
print 'WithNumPy   : ', t.timeit(n), "\n"


print "#######################################################"
print "#               1000 Trials - Searching               #"
print "#                     Short List                      #"
print "#######################################################"
t = timeit.Timer("x=copy.copy(L); searchwithloops(x, 5)", setup=setup)
print 'WithLoops   : ', t.timeit(n)
t = timeit.Timer("x=copy.copy(L); searchwithoutloops(x, 5)", setup=setup)
print 'WithoutLoops: ', t.timeit(n)
t = timeit.Timer("x=copy.copy(L); searchwithnumpy(x, 5)", setup=setup)
print 'WithNumPy   : ', t.timeit(n),"\n"


print "#######################################################"
print "#               1000 Trials - Searching               #"
print "#                     Long List                       #"
print "#######################################################"
t = timeit.Timer("x=copy.copy(L2); searchwithloops(x, 5)", setup=setup)
print 'WithLoops   : ', t.timeit(n)
t = timeit.Timer("x=copy.copy(L2); searchwithoutloops(x, 5)", setup=setup)
print 'WithoutLoops: ', t.timeit(n)
t = timeit.Timer("x=copy.copy(L2); searchwithnumpy(x, 5)", setup=setup)
print 'WithNumPy   : ', t.timeit(n),"\n"


