import numpy

size_list = list(map(int, input().split(" ")))

array_list = []
for _ in range(0,size_list[0] + size_list[1]):
    value = list(map(int, input().split()))
    array_list.append(value)

array_1 = numpy.array(array_list[:size_list[0]])
array_2 = numpy.array(array_list[size_list[0]:])

print(numpy.concatenate((array_1, array_2), axis = 0))



