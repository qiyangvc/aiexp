def myreplace(l1,l2,dict):
    if dict=={}:
        return
    dk=list(dict.keys())[0]
    dc=dict[dk]
    i=0
    while i<len(l1):    
        l1[i]=l1[i].replace(dk,dc)
        i+=1
    i=0
    while i<len(l2):    
        l2[i]=l2[i].replace(dk,dc)
        i+=1
    return
            
        
def if_var(sstr):
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
            t_str2=t_str2[lp2+1:rp2]
        else :
            break
    return
def difference(str1,str2):
    t_str1=str1
    t_str2=str2
    str1 = de_p(str1)
    str2 = de_p(str2)
        
    while ('(' in t_str1)&('(' in t_str2):
        if t_str1[0]==t_str2[0]:
            lp1=t_str1.find('(')
            rp1=t_str1.rfind(')')
            t_str1=t_str1[lp1+1:rp1]
            lp2=t_str2.find('(')
            rp2=t_str2.rfind(')')
            t_str2=t_str2[lp2+1:rp2]
        else :
            break
        
    if str1==str2:#要么不需替换，要么无法替换
        return {}
        
    elif if_var(t_str1):#这里姑且用str1直接替换str2，如g(x)换f(z)，下同，详见神秘测例
        return{t_str1:t_str2}#fk 神秘测例
    elif if_var(t_str2):
        return{t_str2:t_str1}
    else :
        return {}

def de_p(s):
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
    l1=s1[lp1+1:rp1].split(',')
    l2=s2[lp2+1:rp2].split(',')
    if len(l1)!=len(l2):
        return
    # print(lp1,rp1)
    # print(lp2,rp2)
    # print(l1,l2)
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
    # print(all_dict)
    for key in all_dict:
        s1=s1.replace(key,all_dict[key])
        s2=s2.replace(key,all_dict[key])
    # print(s1)
    # print(s2)        
    if(s1!=s2):
        return {}
    else :
        return all_dict