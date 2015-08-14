import numpy
import glob

files=glob.glob('*.txt')

for file in files:
    data = numpy.loadtxt(file)
    avg = data.mean()
    print file,avg

print 'done'
