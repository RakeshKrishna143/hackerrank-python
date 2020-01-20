a=[1,4,4,4,5,3]
b=[0,0,0,0,0,0] #for those 5 types of birds

for i in a:
    b[i]+=1

print(b.index(max(b)))
