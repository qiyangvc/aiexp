st_tr1='P(f(g(x)))'
t_str2='P(f(a))'
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
            
