from operator import itemgetter
import sys
from decimal import Decimal

#init
cnt = 1
current = None

#loop
for line in sys.stdin:
    #prepare	
    line = line.strip()
    word, count = line.split('\t', 1)
	
    if current == word:
	#count
        cnt += 1
    else:
	#for first iteration
        if current:
            print '%s\t%s' % (current, cnt)
	#reset values
        current = word
        cnt = 1
#display last stack
print '%s\t%s' % (current, cnt)
        

   
