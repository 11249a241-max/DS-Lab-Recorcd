def quicksort(a):
    if len(a) < 2: return a
    p = a[len(a)//2]
    l = [x for x in a if x < p]
    m = [x for x in a if x == p]
    r = [x for x in a if x > p]
    return quicksort(l) + m + quicksort(r)

if __name__ == "__main__":
    print(quicksort([3,6,8,10,1,2,1]))
