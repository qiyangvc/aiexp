from queue import  PriorityQueue
import copy
G={}
Q=PriorityQueue(0)
def F(puzzle):
    global G
    return G[puzzle]+H(puzzle)

def A_star(puzzle):
    global G   
    G={tuple(puzzle):0}# f=g+h
    Q.put((F(puzzle),puzzle))
    while not Q.empty:
        puzzles=Q.get()
        mymove(puzzles[0][1])

    
    
def mymove(puzzle,Q):
    global G
    if is_finished(puzzle):
        return
    i=0
    j=0
    while i<len(puzzle):
        while j<len(puzzle[0]):
            if puzzle[i][j]==0:
                break
            j+=1
        if puzzle[i][j]==0:
            break
        i+=1
    if(i!=len(puzzle)-1):
        puzzle1=copy.deepcopy(puzzle)
        puzzle1[i][j],puzzle1[i+1][j]=puzzle1[i+1][j],puzzle1[i][j]
        if tuple(puzzle1) not in G:
            Q.put((F(puzzle1),puzzle1))
            G[tuple(puzzle1)]=G[tuple(puzzle)]+1
    if(i!=0):
        puzzle2=copy.deepcopy(puzzle)
        puzzle2[i][j],puzzle2[i-1][j]=puzzle2[i-1][j],puzzle2[i][j]
        Q.put((F(puzzle2),puzzle2))
        if tuple(puzzle2) not in G:
            Q.put((F(puzzle2),puzzle2))
            G[tuple(puzzle2)]=G[tuple(puzzle)]+1
    if(j!=len(puzzle[0])-1):
        puzzle3=copy.deepcopy(puzzle)
        puzzle3[i][j],puzzle3[i][j+1]=puzzle[i][j+1],puzzle[i][j]
        Q.put((F(puzzle3),puzzle3))
        if tuple(puzzle3) not in G:
            Q.put((F(puzzle1),puzzle1))
            G[tuple(puzzle1)]=G[tuple(puzzle)]+1
    if(j!=0):
        puzzle4=copy.deepcopy(puzzle)
        puzzle[i][j],puzzle[i][j-1]=puzzle[i][j-1],puzzle[i][j]
        Q.put((F(puzzle4),puzzle4))
        if tuple(puzzle4) not in G:
            Q.put((F(puzzle1),puzzle1))
            G[tuple(puzzle4)]=G[tuple(puzzle)]+1
    

    
def H(puzzle):
    i=0
    c=0
    while i<len(puzzle):
        j=0
        while j<len(puzzle[0]):
            p_value=puzzle[i][j]
            if p_value==0:
                p_value=16
            ri=p_value/len(puzzle)
            rj=p_value%len(puzzle)
            c+=abs(i-ri)+abs(j-rj)
            j+=1
        i+=1
    return c
def is_finished(puzzle):
    i=0
    while i<len(puzzle):
        j=0
        while j<len(puzzle[0]):
            if i*len(puzzle)+j+1!=puzzle[i][j]:
                return False
            j+=1
        i+=1
    return True

puzzle=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[0,13,14,15]]
A_star(puzzle)
    
        