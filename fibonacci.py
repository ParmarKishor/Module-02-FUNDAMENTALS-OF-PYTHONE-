n= int(input("Enter Value N : "))
a, b = 0, 1
while b < n:
    print(b, end=" ")
    a, b = b, a + b
print()