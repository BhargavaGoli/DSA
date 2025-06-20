#mergesort

def mergesort(a, l, r):
    if l < r:
        mid = l + (r - l) // 2
        mergesort(a, l, mid)
        mergesort(a, mid + 1, r)
        merge(a, l, mid, r)

def merge(a, l, mid, r):
    n = mid - l + 1
    m = r - mid

    x = [0] * n
    y = [0] * m

    for i in range(n):
        x[i] = a[l + i]

    for i in range(m):
        y[i] = a[mid + 1 + i]

    i = j = 0
    k = l

    while i < n and j < m:
        if x[i] < y[j]:
            a[k] = x[i]
            i += 1
        else:
            a[k] = y[j]
            j += 1
        k += 1

    while i < n:
        a[k] = x[i]
        i += 1
        k += 1

    while j < m:
        a[k] = y[j]
        j += 1
        k += 1

# Example usage:
a = [3, 7, 2, 5, 1]
mergesort(a, 0, len(a) - 1)
print(a)
