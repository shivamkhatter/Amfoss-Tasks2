def collatz(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1
try:
    n=int(input('Enter the number n: '))
    x=collatz(n)
    while True:
        if x==1:
            print(x)
            break
        else:
            print(x)
            x=collatz(x)
        
except ValueError:
    print('Enter a number except 0: ')

