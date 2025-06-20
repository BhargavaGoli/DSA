a=[3,1,2,4,5]

a=[3,2,1]
i=0
while i < len(a):
    cur=a[i]-1
            
    if a[i]!=a[cur]:
        a[i],a[cur]=a[cur],a[i]
    else: i+=1
print(a)