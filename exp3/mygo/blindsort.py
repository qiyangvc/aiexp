def DFS(puzzle,i,j,sorted,route):
    # if i<0|j<0:
    #     return False
    if sorted[i][j]==1:
        return False
    else:
        sorted[i][j]=1
        
    p_value=puzzle[i][j]
    if p_value=='1':
        return False
    elif p_value=='E':
        route.append((i,j))
        return True
    elif (p_value=='0')|(p_value=='S'):
        is_route=(DFS(puzzle,i,j+1,sorted,route)|DFS(puzzle,i,j-1,sorted,route)|DFS(puzzle,i+1,j,sorted,route)|DFS(puzzle,i-1,j,sorted,route))
        if is_route:
            route.append((i,j))
        return is_route
def UCS(puzzle,i,j,sorted,route):
        # if i<0|j<0:
    #     return False
    if sorted[i][j]==1:
        return 100000
    else:
        sorted[i][j]=1
        
    p_value=puzzle[i][j]
    if p_value=='1':
        return 100000
    elif p_value=='E':
        route.append((i,j))#貌似未运行
        return 1
    elif (p_value=='0'):
        route_l1=UCS(puzzle,i,j+1,sorted,route)
        route_l2=UCS(puzzle,i,j-1,sorted,route)
        route_l3=UCS(puzzle,i+1,j,sorted,route)
        route_l4=UCS(puzzle,i-1,j,sorted,route)
        is_route=min(route_l1,route_l2,route_l3,route_l4)

        if is_route<100000:
            route.append((i,j))
        return is_route+1
    elif (p_value=='S'):#最后也没有搞明白为什么这样遍历
        route_l1=UCS(puzzle,i,j+1,sorted,route)
        route_l2=UCS(puzzle,i,j-1,sorted,route)
        route_l3=UCS(puzzle,i+1,j,sorted,route)
        route_l4=UCS(puzzle,i-1,j,sorted,route)
        is_route=min(route_l1,route_l2,route_l3,route_l4)

        if is_route<100000:
            route.append((i,j))
        return is_route+1
        
puzzle=[]
route=[]
sorted=[]
while 1:
    data=input()
    if data=='':
        break
    puzzle.append(data)
m=len(puzzle)
n=len(puzzle[0])
i=0
j=0
while i<m:
    j=0
    line=[]
    while j<n:
        line.append(0)
        j+=1
    sorted.append(line)
    i+=1
i=0
j=0
end=0
while i<m:
    if end:
        break
    j=0
    while j<n:
        if(puzzle[i][j]=='S'):
            end=1
            break
        j+=1
    i+=1
    
UCS(puzzle,i,j,sorted,route)
route.reverse()
print(route)
