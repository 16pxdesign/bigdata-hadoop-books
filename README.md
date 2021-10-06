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
```python
#reduce.py
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
The number of staff that are working in each department
cnt = 1
#display last stack
print '%s\t%s' % (current, cnt)
```
![image](https://user-images.githubusercontent.com/28375942/136125847-81e13ccc-14a3-4ab7-8357-c868a2762d87.png)
### The number of staff that are working in each department
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
print '%s\t%s' % (words[3], 1)
```
```python
###reduce.py
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
The average salary in each department
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
```
![image](https://user-images.githubusercontent.com/28375942/136125904-0c510fba-576b-4c90-824f-7b91fc7a042d.png)
### The average salary in each department
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
print '%s\t%s' % (words[3], words[5])
```
```python
#reduce.py
from operator import itemgetter
import sys
from decimal import Decimal
#init
cnt = 1
current = None
summary = 0
The number of staff that are in each job role
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
```
![image](https://user-images.githubusercontent.com/28375942/136125953-f5290542-5bf8-444c-b0a1-b050e532c3f3.png)
### The number of staff that are in each job role
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
print '%s\t%s' % (words[2], 1)
```
```python
#reduce.py
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
```
![image](https://user-images.githubusercontent.com/28375942/136125998-0328857e-6774-472c-a53e-1782a9b3206d.png)
### Determine how many staff are earning below the average salary for the uni
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
print '%s\t%s' % (words[5], 1)
```
```python
#reduce.py
from operator import itemgetter
import sys
from decimal import Decimal
#init
cnt = 1
current = None
summ = 0
x = {}
#loop and store data to arr
for line in sys.stdin:
#prepare
line = line.strip()
word, count = line.split('\t', 1)
x[word] = count
cnt += int(count)
summ += Decimal(word)
#calc avg
avg = summ/cnt
print ("AVG:" + str(avg))
#iterate arr
under = 0
for z in x.keys():
#compare
if Decimal(z) < avg :
under += 1
print("Under payed are " + str(under) + " employee")
```
![image](https://user-images.githubusercontent.com/28375942/136126071-92fae8d3-c1af-4c62-9f22-ab9ebf24d8cb.png)


