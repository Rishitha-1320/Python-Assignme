n=int(input())
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

result=factorial(n)
print(f"Factorial of {n} is:{result}")
