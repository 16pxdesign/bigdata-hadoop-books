import sys

#init
header = True;

#loop
for line in sys.stdin:
	#skip header
	if header:
		header = False
		continue
	
        #prepare
	line = line.strip()
	words = line.split(",")


	#validate
	if len(words) == 6:                       
                print '%s\t%s' % (words[3], 1)
