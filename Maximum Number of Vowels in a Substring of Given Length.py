#Sliding window method

s = 'eiuaooo'
k = 4

vowel = set('aeiou')
count,m = 0,0

for i,c in enumerate(s):
    count += (c in vowel)
    if i>=k :
        count -= (s[i-k] in vowel)
    m = max(m,count)
print(m)
