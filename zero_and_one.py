import numpy

size_list = tuple(map(int, input().split(" ")))
print(numpy.zeros(size_list, dtype = numpy.int))
print(numpy.ones(size_list, dtype = numpy.int))

