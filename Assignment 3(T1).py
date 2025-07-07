#Calculate Factorial Using a Function
a= int (input("Enter your number: "))
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

l= factorial(a)
print("Factorial of", a,"is",l)
