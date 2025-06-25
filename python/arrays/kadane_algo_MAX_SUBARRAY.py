a=[0,-2,4,5,0,4,-1]

maxsum=cursum=a[0]
for i in range(1,len(a)):
    cursum=max(cursum+a[i],a[i])
    maxsum=max(cursum,maxsum)
print(maxsum)

#more understandle code
maxsum=float('-inf')
cursum=0

for i in range(len(a)):
    cursum += a[i]
    maxsum = max(cursum,maxsum)
    if cursum<0:
        cursum=0
print(maxsum)