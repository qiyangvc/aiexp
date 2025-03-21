import copy
from MGU import MGU,de_p
count=1
l_support=[]
def merge(e1,e2):
    if(e1==e2):
        return
    global count
    i=0
    while i<len(e1):
        j=0
        while j<len(e2):
            if (e1[i][0]=='~')&(e2[j][0]!='~')|(e1[i][0]!='~')&(e2[j][0]=='~'):
                if (e1[i][1:e1[i].index('(')]==e2[j][:e2[j].index('(')])|(e2[j][1:e2[j].index('(')]==e1[i][:e1[i].index('(')]):
                #     if (i==0)&(j==0):
                #         return e1[1:]+e2[1:]
                #     elif i==0:
                #         return e1[1:]+e2[:j-1]+e2[j+1:]
                #     elif j==0:
                #         return e1[:i-1]+e1[i+1:]+e2[1:]
                    t_s1=e1[i].replace('~','')
                    t_s2=e2[j].replace('~','')
                    all_dict=MGU(t_s1,t_s2)
                    if all_dict=={}:
                        if(t_s1!=t_s2):
                            j+=1
                            continue
                    e3=tuple(set(e1+e2)-{e1[i],e2[j]})
                    le3=list(e3)
                    k=0
                    while k<len(le3):
                        for key in all_dict:
                            le3[k]=le3[k].replace(key,all_dict[key])
                        k+=1
                    e3=tuple(le3)
                    if e3 not in FKB:
                        # print(all_dict)
                        FKB.append(e3)
                        l_support.append(1)
                        myprint(e1, e2, i, j, all_dict, e3)
            j+=1
        i+=1
    return 

def myprint(e1, e2, i, j, all_dict, e3):
    global count
    i1=FKB.index(e1)+1
    i2=FKB.index(e2)+1
    if len(e1)==1&len(e2)==1:
        print(count,' R[',i1,',',i2,']',all_dict,'= ',e3,sep='')
    elif len(e1)==1:
        print(count,' R[',i1,',',i2,chr(97+j),']',all_dict,' = ',e3,sep='')
    elif len(e2)==1:
        print(count,' R[',i1,chr(97+i),',',i2,']',all_dict,' = ',e3,sep='')
    else:
        print(count,' R[',i1,chr(97+i),',',i2,chr(97+j),']',all_dict,' = ',e3,sep='')
    count+=1

SKB={("A(tony)",),("A(mike)",),("A(john)",),("L(tony,rain)",),("L(tony,snow)",),("~A(x)","S(x)","C(x)"),("~C(y)","~L(y,rain)"),("L(z,snow)","~S(z)"),("~L(tony,u)","~L(mike,u)"),("L(tony,v)","L(mike,v)"),("~A(w)","~C(w)","S(w)")}
# SKB={("GradStudent(sue)",),("~GradStudent(x)","Student(x)"),("~Student(x)","HardWorker(x)"),("~HardWorker(sue)",)}#痛，太痛了

# 5
# On(aa,bb)
# On(bb,cc)
# Green(aa)
# ~Green(cc)
# (~On(x,y),~Green(x),Green(y))
KB=list(SKB)
FKB=copy.deepcopy(KB)#祖先备份
def ResolutionProb():
    global count
    i=0

    
    while i<len(FKB):
        l_support.append(0)
        print(count,FKB[i])
        i+=1
        count+=1
    l_support[count-2]=1
    while 1:
        KB=copy.deepcopy(FKB)
        
        ii=0
        while ii<len(KB):
            jj=0
            while jj<len(KB):
                if l_support[ii]|l_support[jj]:
                    merge(KB[ii],KB[jj])
                jj+=1
            ii+=1
                
        if () in FKB:
            print('t')
            return
ResolutionProb() 


# if if_ancestors(c1)||if_ancestors(c2)||if_grand(c1,c2) :
#     merge(c1,c2)
    
    
# def if_ancestors(c) :
#     return c in FKB
# def if_grand(c1,c2):