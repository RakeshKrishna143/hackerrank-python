from collections import defaultdict
from _collections import defaultdict

a = [1,3,9,9,27,81]
r=3

d1 = defaultdict(int)
d2 = defaultdict(int)
count = 0

for i in reversed(a):
    if i*r in d2:
        count+= d2[i*r]
        
    if i*r in d1:
        d2[i]+=d1[i*r]
        
    d1[i]+=1
    print(d1,d2,count)
    
    
print(count)
        
