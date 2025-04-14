
from astar import A_star


l_puzzle=input().split()
i=0
while i<16:
    l_puzzle[i]=int(l_puzzle[i])
    i+=1
puzzle=[l_puzzle[0:4],l_puzzle[4:8],l_puzzle[8:12],l_puzzle[12:16]]

i=1
c=0
l_puzzle.remove(0)
while i<len(l_puzzle):
    j=0
    while j<i:
        if l_puzzle[i]<l_puzzle[j]:
            c+=1
        j+=1
    i+=1
if c%2==0:
    A_star(puzzle)
else:
    print("无解")