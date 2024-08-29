def selection_sort(a):
    for i in range(len(a)):
        m = i
        for j in range(i+1, len(a)):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a

a = list(map(int, input("enter numbers separated by spaces: ").split()))
print("sorted list is", selection_sort(a))
