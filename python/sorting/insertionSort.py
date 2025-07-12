l = [5,4,1,2,3]

n = len(l)

for i in range(1,n) :
    val = l[i]
    j = i - 1
    while j >= 0 and l[j] > val :
        l[j + 1] = l[j]
        j -= 1
        l[j + 1] = val

print(l)
