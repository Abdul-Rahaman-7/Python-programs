#With a temporary variable 

print("Before swap")
a= int(input())
b= int(input())

print(a)
print(b)

t=a
a=b
b=t

print("After swap")

print("a=",a)
print("b=",b)

# Without a temporary variable 

print("Before swap")

x= int(input())
y= int(input())

print(x)
print(y)

x = x+y
y = x-y
x = x-y

print("After swap")

print("x=",x)
print("y=",y)