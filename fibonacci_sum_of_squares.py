# Uses python3
def pisano_period(m):
    f = []
    first_mod = 0
    second_mod = 0
    if m > 1:
        second_mod = 1
        f.append(1)
        f.append(1)
    elif m == 1:
        return 1
    else:
        return 0

    for i in range(2,m*m):
        first_mod = second_mod
        f.append(f[i-1] + f[i-2])
        second_mod = f[i] % m
        if first_mod == 0 and second_mod == 1:
            return i

def calc_fib(n):
    f = []
    if n >= 1:
        f.append(1)
        f.append(1)
    else:
        return 0

    for i in range(2,n):
        f.append(f[i-1] + f[i-2])

    return f[n-1]

def fibonacci_last_digit(n):
    m = 100
    pisano_mod = (n+2) % pisano_period(m)
    return ((calc_fib(pisano_mod) % m)-1)%10

def fibonacci_partial_sum(n,m):
        return (fibonacci_last_digit(m)-fibonacci_last_digit(n-1))%10

def fibonacci_sum_of_squares(n):
    x = fibonacci_partial_sum(n,n)
    y = fibonacci_partial_sum(n-1,n-1)
    return ((x+y)*x)%10

n= input()
print(fibonacci_sum_of_squares(int(n)))
