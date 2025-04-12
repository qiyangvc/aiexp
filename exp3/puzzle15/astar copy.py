from queue import  PriorityQueue
import copy
Qs=[]
Q=PriorityQueue(0)
Ql=PriorityQueue(0)
def F(puzzle,G):
    return G+H(puzzle)

def A_star(puzzle):   # f=g+h
    global Q
    global Qs
    global Ql
    Qs.append(puzzle)
    Q.put((H(puzzle),puzzle))
    Ql.put([])
    while not Q.empty():
        t_puzzle=Q.get()
        if mymove(t_puzzle[1]):
           return
    return 

    
    
def mymove(puzzle):
    global Q
    global Qs
    global Ql
    t_path=Ql.get()
    if is_finished(puzzle):
        print(t_path)
        return True
    i=0
    j=0
    k=0
    while i<len(puzzle):
        j=0
        while j<len(puzzle[0]):
            if puzzle[i][j]==0:
                k=1
                break
            j+=1
        if k:
            break
        i+=1
    if(i!=len(puzzle)-1):
        t_path1=copy.deepcopy(t_path)
        puzzle1=copy.deepcopy(puzzle)
        puzzle1[i][j],puzzle1[i+1][j]=puzzle1[i+1][j],puzzle1[i][j]

        Q.put((F(puzzle1,len(t_path)+1),puzzle1))
        Qs.append(puzzle1)
        t_path1.append(puzzle1[i][j])
        Ql.put(t_path1)
        
    if(i!=0):
        t_path2=copy.deepcopy(t_path)
        puzzle2=copy.deepcopy(puzzle)
        puzzle2[i][j],puzzle2[i-1][j]=puzzle2[i-1][j],puzzle2[i][j]

        Q.put((F(puzzle2,len(t_path)+1),puzzle2))
        Qs.append(puzzle2)
        t_path2.append(puzzle2[i][j])
        Ql.put(t_path2)

    if(j!=len(puzzle[0])-1):
        t_path3=copy.deepcopy(t_path)
        puzzle3=copy.deepcopy(puzzle)
        puzzle3[i][j],puzzle3[i][j+1]=puzzle3[i][j+1],puzzle3[i][j]
        Q.put((F(puzzle3,len(t_path)+1),puzzle3))
        Qs.append(puzzle3)
        t_path3.append(puzzle3[i][j])
        Ql.put(t_path3)
            
    if(j!=0):
        t_path4=copy.deepcopy(t_path)
        puzzle4=copy.deepcopy(puzzle)
        puzzle4[i][j],puzzle4[i][j-1]=puzzle4[i][j-1],puzzle4[i][j]
        Q.put((F(puzzle4,len(t_path)+1),puzzle4))
        Qs.append(puzzle4)
        t_path4.append(puzzle4[i][j])
        Ql.put(t_path4)
    return False


    

    
def H(puzzle):
    i=0
    c=0
    while i<len(puzzle):
        j=0
        while j<len(puzzle[0]):
            p_value=puzzle[i][j]
            if p_value==0:
                p_value=16
            p_value-=1
            ri=int(p_value/len(puzzle))
            rj=int(p_value%len(puzzle))
            c+=abs(i-ri)+abs(j-rj)
            j+=1
        i+=1
    return c
def is_finished(puzzle):
    i=0
    while i<len(puzzle):
        j=0
        while j<len(puzzle[0]):
            p_value=puzzle[i][j]
            if p_value==0:
                p_value=16
            if i*len(puzzle)+j+1!=p_value:
                return False
            j+=1
        i+=1
    print("succes")
    return True

puzzle=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[0,13,14,15]]
A_star(puzzle)
    
        