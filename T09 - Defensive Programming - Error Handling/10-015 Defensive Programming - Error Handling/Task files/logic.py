def factorial(n):
    if n==0:
        return 0 # the logical error is caused by returning 0 for factorial(0). It should return 1.
    else:
        return (n*factorial(n-1))
for i in range(1,10):
    print(factorial(i))