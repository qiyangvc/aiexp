d={"van":"DDW","kingsama":"Bill","power":"gold_ge"}
def ReverseKeyValue(d):
    b=d.keys()
    print(len(d))
    i=0
    a=list(b)
    l=len(d)
    while i<l:
        t1=a[i]
        t2=d[t1]
        del d[t1]
        d[t2]=t1
        i+=1

ReverseKeyValue(d)
print(d)