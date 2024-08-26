def find_max(a):
    m = a[0]
    for i in a:
        if i > m:
            m = i
    return m

a = list(map(int, input("enter numbers separated by spaces: ").split()))
print("the maximum number is", find_max(a))
