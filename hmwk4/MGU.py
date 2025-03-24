def myreplace(l1,l2,dict):#仅在列表内做替换
    if dict=={}:
        return
    dk=list(dict.keys())[0]
    dc=dict[dk]
    i=0
    while i<len(l1):    
        l1[i]=l1[i].replace('('+dk+')','('+dc+')')
        if l1[i]==dk:
            l1[i]=dc
        i+=1
    i=0
    while i<len(l2):    
        l2[i]=l2[i].replace('('+dk+')','('+dc+')')#还是用类似正则表达式来解决，如xx会被检测为(xx)，避免xx被x：tony改为tonytony
        if l2[i]==dk:
            l2[i]=dc
        i+=1
    return
            
        
def if_var(sstr):#判断是否为变量
    if sstr[0] in {'u','v','w','x','y','z'}:
        return True
    else :
        return False
    
def real_dif(t_str1,t_str2):
    while ('(' in t_str1)&('(' in t_str2):
        if t_str1[0]==t_str2[0]:
            lp1=t_str1.find('(')
            rp1=t_str1.rfind(')')
            t_str1=t_str1[lp1+1:rp1]
            lp2=t_str2.find('(')
            rp2=t_str2.rfind(')')
            t_str2=t_str2[lp2+1:rp2]#去括号部分b，这里是比较两项结构是否相同，但是实际上因为我未能处理传参问题，这个函数被直接写入difference内
        else :
            break
    return
def difference(str1,str2):
    t_str1=str1
    t_str2=str2
    str1 = de_p(str1)
    str2 = de_p(str2)#去括号部分a，这里是比较两个变量是否相同，如比较f(x)和x。兼有判断是否为变量的功能，如x和a
        
    while ('(' in t_str1)&('(' in t_str2):
        if t_str1[0]==t_str2[0]:
            lp1=t_str1.find('(')
            rp1=t_str1.rfind(')')
            t_str1=t_str1[lp1+1:rp1]
            lp2=t_str2.find('(')
            rp2=t_str2.rfind(')')
            t_str2=t_str2[lp2+1:rp2]#去括号部分b，这里是比较两项结构是否相同，如比较g(x)和f(x)
        else :
            break
        
    if str1==str2:#要么不需替换，要么无法替换
        return {}
        
    elif if_var(t_str1):
        return{t_str1:t_str2}
    elif if_var(t_str2):
        return{t_str2:t_str1}
    else :
        return {}

def de_p(s):#去括号部分a的精简版
    while '(' in s:
        lp=s.find('(')
        rp=s.rfind(')')
        s=s[lp+1:rp]
    return s
    
def MGU(s1,s2):
    lp1=s1.find('(')
    lp2=s2.find('(')
    rp1=s1.rfind(')')
    rp2=s2.rfind(')')
    l1=s1[lp1+1:rp1].split(',')#去括号部分c，这里是将表达式内的项分离，如L(x,y,z)
    l2=s2[lp2+1:rp2].split(',')
    if len(l1)!=len(l2):
        return
    all_dict={}
    
    i=0
    while i<len(l1):
        if l1[i]==l2[i]:
            i+=1
            continue
        else:
            dict=difference(l1[i],l2[i])
            myreplace(l1,l2,dict)
            all_dict.update(dict)
            i+=1
    for key in all_dict:
        s1=s1.replace('('+key+')','('+all_dict[key]+')')
        s1=s1.replace('('+key+',','('+all_dict[key]+',')
        s1=s1.replace(','+key+')',','+all_dict[key]+')')
        s1=s1.replace(','+key+',',','+all_dict[key]+',')
        s2=s2.replace('('+key+')','('+all_dict[key]+')')
        s2=s2.replace('('+key+',','('+all_dict[key]+',')
        s2=s2.replace(','+key+')',','+all_dict[key]+')')
        s2=s2.replace(','+key+',',','+all_dict[key]+',')#手动正则表达式，只是用于区分没有改变和无法归结的情况，但是由于为了将作业3的两函数拼接在一起，留下了这个“待优化”的部分
    if(s1!=s2):
        return {}
    else :
        return all_dict