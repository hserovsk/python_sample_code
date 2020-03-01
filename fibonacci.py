true = 1
def fibonacci(n):
    if n == 0:
        print('0')
    elif n == 1:
        print('1')
    elif n > 1:
        i = 0
        j = 1
        k = 0
        fib = 0
        while i < n:
            fib = j + k
            j = k
            k = fib
            i = i + 1
        print(fib)
    else:
        print('blad')


while true:
    n = int(input("podaj który wyraz ciągu chcesz obliczyć: \n"))
    fibonacci(n)
    if n < 0:
        break

