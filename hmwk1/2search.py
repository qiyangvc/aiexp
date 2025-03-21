# n=10
# target=35
# nums=[1,2,3,4,5,6,7,8,9,120]
lst=input().split()
n=int(lst[0])
target=int(lst[1])
nums=lst[2:n+2]
l=0
j=0
r=int(n)-1
while l<=r :
    mid=int((l+r)/2)
    if int(nums[mid])>target:
        r=mid-1
    elif int(nums[mid])<target:
        l=mid+1
    else : 
        print("YES")
        j=1
        break
if j==0 :print("NO")
    