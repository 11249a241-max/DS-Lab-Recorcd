def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if a[j] < a[min_i]: min_i = j
        a[i], a[min_i] = a[min_i], a[i]
    return a

if __name__ == "__main__":
    print(selection_sort([64,25,12,22,11]))
