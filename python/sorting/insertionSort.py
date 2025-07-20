# l = [5,4,1,2,3]

# n = len(l)

# for i in range(1,n) :
#     val = l[i]
#     j = i - 1
#     while j >= 0 and l[j] > val :
#         l[j + 1] = l[j]
#         j -= 1
#         l[j + 1] = val

# print(l)

a = [0,9,3,7]

for i in range(1, len(a)) :
    j = i - 1
    val = a[i]
    while j >= 0 and a[j] > val :
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = val

print(a)