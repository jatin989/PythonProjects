n = int(input("Enter the Number : "))
def fib(n) :
    if n < 0 :
        print("Invalid Number ")
    if n==0 :
        return 0
    if n==1 or n==2 :
        return 1
    else :
        return fib(n-1) + fib(n-2)
fib(n)
for i in range(n) :
    print(fib(i))






