import copy
count=1
def merge(e1,e2):
    global count
    i=0
    while i<len(e1):
        j=0
        while j<len(e2):
            if (e1[i][0]=='~')&(e2[j][0]!='~')|(e1[i][0]!='~')&(e2[j][0]=='~'):
                if (e1[i][1:]==e2[j])|(e2[j][1:]==e1[i]):
                #     if (i==0)&(j==0):
                #         return e1[1:]+e2[1:]
                #     elif i==0:
                #         return e1[1:]+e2[:j-1]+e2[j+1:]
                #     elif j==0:
                #         return e1[:i-1]+e1[i+1:]+e2[1:]
                    e3=tuple(set(e1+e2)-{e1[i],e2[j]})
                    if e3 not in FKB:
                        FKB.append(e3)
                        i1=FKB.index(e1)+1
                        i2=FKB.index(e2)+1
                        if len(e1)==1&len(e2)==1:
                            print(count,' R[',i1,',',i2,'] = ',e3,sep='')
                        elif len(e1)==1:
                            print(count,' R[',i1,',',i2,chr(97+j),'] = ',e3,sep='')
                        elif len(e2)==1:
                            print(count,' R[',i1,chr(97+i),',',i2,'] = ',e3,sep='')
                        else:
                            print(count,' R[',i1,chr(97+i),',',i2,chr(97+j),'] = ',e3,sep='')
                        count+=1
            j+=1
        i+=1
    return 

SKB={("FirstGrade",),("~FirstGrade","Child"),("~Child",)}#痛，太痛了
KB=list(SKB)
FKB=copy.deepcopy(KB)#祖先备份
def ResolutionProb():
    global count
    i=0
    while i<len(FKB):
        print(count,FKB[i])
        i+=1
        count+=1
    while 1:
        KB=copy.deepcopy(FKB)
        for element1 in KB:
            for element2  in KB:
                merge(element1,element2)
        if () in FKB:
            print('t')
            return
ResolutionProb() 


# if if_ancestors(c1)||if_ancestors(c2)||if_grand(c1,c2) :
#     merge(c1,c2)
    
    
# def if_ancestors(c) :
#     return c in FKB
# def if_grand(c1,c2):

    