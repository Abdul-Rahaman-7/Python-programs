def linear_search(a, b):
    for i in range(len(a)):
        if a[i] == b:
            return i
    return -1

a = list(map(int, input("enter numbers separated by spaces: ").split()))
b = int(input("enter the number to search: "))
index = linear_search(a, b)
if index != -1:
    print(f"number found at index {index}")
else:
    print("number not found")
