def linear_search(arr, x):
    for i, v in enumerate(arr):
        if v == x:
            return i
    return -1

if __name__ == "__main__":
    a = [3,5,2,9,1]
    print(linear_search(a, 9))
    print(linear_search(a, 7))
