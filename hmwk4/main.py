import copy
from MGU import MGU
count=1#记录一阶逻辑总数
t1_count=0#记录初始逻辑数量
t2_count=0#记录输出空括号时的count，用于回溯输出
l_support=[]#支持集数组，用于确定目标
l_ancestors=[]#祖先过滤策略数组，用于判断是否为最早的祖先
rootmap={}#通过字典寻根，相当于树结构
l_need=set({})#用于收集回溯函数的序号
l_words=[]#用于存储输出语句
def is_grand(ii,jj):#借用findroot函数简单判断两式是否有亲代关系
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

def findroot(count):#递归生成一个亲代序列存于l_need
    global t1_count
    global l_need

    l_need.add(count)
    if count<t1_count:
        return
    findroot(rootmap[count][0])
    findroot(rootmap[count][1])
    
def merge(e1,e2):#调用MGU来处理元组内的一阶逻辑式
    if(e1==e2):
        return
    global t2_count
    global count
    i=0
    while i<len(e1):
        j=0
        while j<len(e2):
            if (e1[i][0]=='~')&(e2[j][0]!='~')|(e1[i][0]!='~')&(e2[j][0]=='~'):#是否为反
                if (e1[i][1:e1[i].index('(')]==e2[j][:e2[j].index('(')])|(e2[j][1:e2[j].index('(')]==e1[i][:e1[i].index('(')]):#一阶逻辑式提取函数部分
                    t_s1=e1[i].replace('~','')
                    t_s2=e2[j].replace('~','')#化为MGU易于处理的形式
                    all_dict=MGU(t_s1,t_s2)
                    if all_dict=={}:#判断空集情况：相同或者无法合一
                        if(t_s1!=t_s2):
                            j+=1
                            continue
                    e3=tuple(set(e1+e2)-{e1[i],e2[j]})#用集合合并元组，每次输出结果都不同的罪魁祸首
                    le3=list(e3)
                    k=0
                    while k<len(le3):
                        for key in all_dict:
                            le3[k]=le3[k].replace('('+key+')','('+all_dict[key]+')')
                            le3[k]=le3[k].replace('('+key+',','('+all_dict[key]+',')
                            le3[k]=le3[k].replace(','+key+')',','+all_dict[key]+')')
                            le3[k]=le3[k].replace(','+key+',',','+all_dict[key]+',')#用低配正则表达式防止出现tony->tonmike的情况
                        k+=1
                    le3=set(le3)#集合去重，因为替换过程中可能再次出现重复
                    e3=tuple(le3)
                    if e3 not in FKB:
                        FKB.append(e3)
                        l_support.append(1)
                        l_ancestors.append(1)
                        myprint(e1, e2, i, j, all_dict, e3)#存储归结步骤
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
    rootmap[count]=[i1,i2]#rootmap在这里存储
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
    global l_words
    i=0
    while i<len(FKB):
        l_ancestors.append(0)
        l_support.append(0)
        l_words.append(str(count)+" "+str(FKB[i]))
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
                if l_support[ii]|l_support[jj]:#支持集策略
                # if (not l_ancestors[ii])|(not l_ancestors[jj])|is_grand(ii,jj):#是否只启用祖先过滤策略
                # if ((not l_ancestors[ii])|(not l_ancestors[jj])|is_grand(ii,jj))&(l_support[ii]|l_support[jj]):#是否同时启用祖先过滤策略和支持集策略
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
                print(l_words[element-1])#终止条件
            return
def myscan(KB):
    n = int(input("请输入行数: "))
    i=0
    while i<n:
        temp_s=input()
        if temp_s[0]!='(':
            KB.append((temp_s,))
        else:
            KB.append(tuple(temp_s[1:len(temp_s)-1].replace('),',') ').split(' ')))
        i+=1
#这里是主函数     
KB=[]
myscan(KB)#把输入处理成可识别的格式
FKB=copy.deepcopy(KB)#祖先备份
ResolutionProb(KB)