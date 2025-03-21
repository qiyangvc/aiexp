import copy
import numpy as np

a0=[int(x) for x in input("请输入a矩阵行数与列数并输入a矩阵").split()]
b0=[int(x) for x in input("请输入b矩阵行数与列数并输入b矩阵").split()]
m=a0[0]
k1=a0[1]
k2=b0[0]
n=b0[1]
print(m,k1,n,k2)
a=[]
b=[]
i0=0
j0=0
while i0<m:
    a.append(a0[i0*k1+2:i0*k1+2+k1])
    i0+=1
while j0<k2 :
    b.append(b0[j0*n+2:j0*n+2+n])
    j0+=1
print(a)
print(b)

def matrixadd(a, b, m, n,k1,k2):
    if m!=k2|n!=k1 :
        print("无法相加")
        return
    i=0
    c=copy.deepcopy(a)
    while i<m:
        j=0
        while j<n:
            c[i][j]=a[i][j]+b[i][j]
            j+=1
        i+=1

c=matrixadd(a, b, m, n,k1,k2)
if c!=None:
    print(c)

def matrixmul(a, b, m, n,k1,k2):
    if k1!=k2 :
        print("无法相乘")
        return
    # d=[]
    # e=0
    # while e<m:
    #     f=0
    #     tm=[]
    #     while f<n:
    #         tm.append(0)
    #         f+=1
    #     d.append(tm)
    #     e+=1
    # print(d)
    d=np.zeros((m,n))
    print(d)
    i=0
    while i<m:
        j=0
        while j<n:
            k=0
            while k<k1:
                d[i][j]+=a[i][k]*b[k][j]
                k+=1
            j+=1
        i+=1
    return d

d=matrixmul(a, b, m, n,k1,k2)

print(d)