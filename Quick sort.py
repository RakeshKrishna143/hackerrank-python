def qsort(l):
    if l==[]: return []
    return qsort([x for x in l[1:] if x<l[0]]) + l[0:1] + qsort([x for x in l[1:] if x>=l[0]])
    
ls = [23,12,45,99,2,6,1,0]

print(qsort(ls))
