def merge(left, right):
    i=j=0; r=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            r.append(left[i]); i+=1
        else:
            r.append(right[j]); j+=1
    r.extend(left[i:]); r.extend(right[j:])
    return r

def mergesort(a):
    if len(a) < 2: return a
    m = len(a)//2
    return merge(mergesort(a[:m]), mergesort(a[m:]))

if __name__ == "__main__":
    print(mergesort([5,2,4,6,1,3]))
