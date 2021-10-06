from operator import itemgetter
import sys
from decimal import Decimal

#init
cnt = 1
current = None
summary = 0

#loop
for line in sys.stdin:
    #prepare	
    line = line.strip()
    word, count = line.split('\t', 1)
    count = Decimal(count)
	
    if current == word:
	#count
        cnt += 1
	summary += count
    else:
	#for first iteration
        if current:
            print '%s\t%s' % (current, summary/cnt)
	#reset values
        current = word
	summary = count
        cnt = 1
#display last stack
print '%s\t%s' % (current, summary/cnt)
        

   
