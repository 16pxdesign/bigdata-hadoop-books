from operator import itemgetter
import sys
from decimal import Decimal

#init
cnt = 1
current = None
summ = 0
x = {}
#loop
for line in sys.stdin:
    #prepare	
    line = line.strip()
    word, count = line.split('\t', 1)
    x[word] =  count
    cnt += int(count)
    summ += Decimal(word)


avg = summ/cnt
print ("AVG:" + str(avg))
under = 0
for z in x.keys():
	if Decimal(z) < avg :
		under += 1
		
print("Under payed are " + str(under) + " employee")






   
