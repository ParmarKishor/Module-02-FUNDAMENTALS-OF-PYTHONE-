#Write a Python program to get the Factorial number of given number.

n = int (input("Enter a Number : "))
fact = 1
if  n>0:
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
