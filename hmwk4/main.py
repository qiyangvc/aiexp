import copy
from MGU import MGU,de_p
count=1
t1_count=0
t2_count=0
l_support=[]
l_ancestors=[]#祖先过滤算法
rootmap={}#通过字典寻根
l_need=set({})
l_words=[]
def is_grand(ii,jj):
    global l_need
    findroot(ii+1)
    if jj+1 in l_need:
        l_need=set({})
        return True
    l_need=set({})
    findroot(jj+1)
    if jj+1 in l_need:
        l_need=set({})
        return True
    l_need=set({})
    return False
def findroot(count):
    global t1_count
    global l_need
    if count<t1_count:
        return
    l_need.add(count)
    findroot(rootmap[count][0])
    findroot(rootmap[count][1])
    
    
def merge(e1,e2):
    if(e1==e2):
        return
    global t2_count
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
                            le3[k]=le3[k].replace('('+key+')','('+all_dict[key]+')')
                            le3[k]=le3[k].replace('('+key+',','('+all_dict[key]+',')
                            le3[k]=le3[k].replace(','+key+')',','+all_dict[key]+')')
                            le3[k]=le3[k].replace(','+key+',',','+all_dict[key]+',')#答案是低配正则表达式
                            # le3[k]=le3[k].replace(key,all_dict[key])
                        k+=1
                    le3=set(le3)
                    e3=tuple(le3)
                    if e3 not in FKB:
                        # print(all_dict)
                        FKB.append(e3)
                        l_support.append(1)
                        l_ancestors.append(1)
                        myprint(e1, e2, i, j, all_dict, e3)
                        if e3==():
                            t2_count=count
                            return
            j+=1
        i+=1
    return 

def myprint(e1, e2, i, j, all_dict, e3):
    global count
    global rootmap
    global l_words
    i1=FKB.index(e1)+1
    i2=FKB.index(e2)+1
    rootmap[count]=[i1,i2]
    if len(e1)==1&len(e2)==1:
        # print(count,' R[',i1,',',i2,']',all_dict,' = ',e3,sep='')
        l_words.append(str(count)+' R['+str(i1)+','+str(i2)+']'+str(all_dict)+' = '+str(e3))
    elif len(e1)==1:
        # print(count,' R[',i1,',',i2,chr(97+j),']',all_dict,' = ',e3,sep='')
        l_words.append(str(count)+' R['+str(i1)+','+str(i2)+chr(97+j)+']'+str(all_dict)+' = '+str(e3))
    elif len(e2)==1:
        l_words.append(str(count)+' R['+str(i1)+chr(97+i)+','+str(i2)+']'+str(all_dict)+' = '+str(e3))
        # print(count,' R[',i1,chr(97+i),',',i2,']',all_dict,' = ',e3,sep='')
    else:
        l_words.append(str(count)+' R['+str(i1)+chr(97+i)+','+str(i2)+chr(97+j)+']'+str(all_dict)+' = '+str(e3))
        # print(count,' R[',i1,chr(97+i),',',i2,chr(97+j),']',all_dict,' = ',e3,sep='')
    count+=1

def ResolutionProb(KB):
    global t1_count
    global count
    global l_need
    i=0
    while i<len(FKB):
        l_ancestors.append(0)
        l_support.append(0)
        print(count,FKB[i])
        i+=1
        count+=1
    l_ancestors[count-2]=0
    l_support[count-2]=1
    t1_count=count
    while 1:
        KB=copy.deepcopy(FKB)
        
        ii=0
        while ii<len(KB):
            jj=ii
            while jj<len(KB):
                if l_support[ii]|l_support[jj]:
                # if ((not l_ancestors[ii])|(not l_ancestors[jj])|is_grand(ii,jj))&(l_support[ii]|l_support[jj]):
                    merge(KB[ii],KB[jj])
                    if () in FKB:
                        break
                jj+=1
            ii+=1
                
        if () in FKB:
            findroot(t2_count-1)
            l_need=list(l_need)
            l_need.sort()
            for element in l_need:
                print(l_words[element-t1_count])
            return

# KB=[("A(tony)",),("A(mike)",),("A(john)",),("L(tony,rain)",),("L(tony,snow)",),("~A(x)","S(x)","C(x)"),("~C(y)","~L(y,rain)"),("L(z,snow)","~S(z)"),("~L(tony,u)","~L(mike,u)"),("L(tony,v)","L(mike,v)"),("~A(w)","~C(w)","S(w)")]
# KB=[("On(aa,bb)",),("On(bb,cc)",),("Green(aa)",),("~Green(cc)",),("~On(x,y)","~Green(x)","Green(y)")]
KB=[("GradStudent(sue)",),("~GradStudent(x)","Student(x)"),("~Student(x)","HardWorker(x)"),("~HardWorker(sue)",)]#痛，太痛了
# n = int(input("请输入行数: "))
# KB = [(input()) for _ in range(n)]
FKB=copy.deepcopy(KB)#祖先备份

ResolutionProb(KB) 


# if if_ancestors(c1)||if_ancestors(c2)||if_grand(c1,c2) :
#     merge(c1,c2)
    
    
# def if_ancestors(c) :
#     return c in FKB
# def if_grand(c1,c2):