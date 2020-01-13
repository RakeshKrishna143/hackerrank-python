
import re
s='aaadaa'
k='aa'
matches = re.finditer('(?=('+k+'))',s)

flag = False
for match in matches:
    flag = True
    print ((match.start(1), match.end(1) - 1))

if flag == False:
    print ((-1, -1))
   
   
o/p
(0, 1)
(1, 2)
(4, 5)
