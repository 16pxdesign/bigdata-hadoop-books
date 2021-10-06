# bigdata-hadoop-books
Python scripts to work with Hadoop data

### The number of staff that are working full and part-time.

```python
#mapper.py
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
#validate and pass
if len(words) == 6:
print '%s\t%s' % (words[4], 1)
```
