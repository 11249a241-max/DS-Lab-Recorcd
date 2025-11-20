def binary_search(arr, x):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            lo = mid+1
        else:
            hi = mid-1
    return -1

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7]
    print(binary_search(a, 4))
    print(binary_search(a, 8))
