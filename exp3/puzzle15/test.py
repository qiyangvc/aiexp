l=[1,14,3,4,5,7,8,9,10,11,12,6,13,2,15]
i=1
c=0
while i<len(l):
    j=0
    while j<i:
        if l[i]<l[j]:
            c+=1
        j+=1
    i+=1
print(c)
    