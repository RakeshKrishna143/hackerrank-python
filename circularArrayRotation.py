def circularArrayRotation(a, k, queries):
    n=len(a)
    res = []
    k=k if k<n else k%n
    if k==0:
        for i in queries:
            res.append(a[i])
            
    else:
        a = a[-k:]+a[:(n-k)]
        for i in queries:
            res.append(a[i])
    return res
