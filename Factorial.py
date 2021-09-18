def fact(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        p=1
        while(n>1):
            p*=n
            n-=1
        return p
while(True):
    number=int(input("What number will you like to find its factorial:"))
    print("The factorial of", number, "is", fact(number) )
