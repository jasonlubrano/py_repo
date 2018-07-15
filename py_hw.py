#py_hw
#jason lubrano

#get numbers from file, find sum, find avg, etc.

#open the file and put it in read mode (r)
with open('numbers.txt', 'r') as numbers:
    line = numbers.read()
    my_sum = sum(int(num) for num in line.split()) #finds the sum of the numbers
    count = len(line.split()) #counts the length of the lines split by empty space
    my_avg = my_sum / count #finds the average
    my_max = max(line.split()) #finds the max
    my_min = min(line.split()) #finds the min
    print('sum: %d' % my_sum)
    print('count: %d' % count)
    print('avg: %d' % my_avg)
    print('max: ' + my_max)
    print('min: ' + my_min)