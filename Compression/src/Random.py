# generate random floating point values
from random import seed
from random import random
# seed random number generator
seed(1)
# generate random numbers between 0-1
OutputFile= open('RawData.txt','w')

for _ in range(100000):
	value =1000*random()
	OutputFile.write(str(value)+'\n' )
#	OutputFile.write("\n")
OutputFile.close	
