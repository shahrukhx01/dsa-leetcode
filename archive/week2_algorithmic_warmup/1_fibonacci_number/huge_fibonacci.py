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

def huge_fibonacci(n,m):
    pisano_mod = n % pisano_period(m)
    return calc_fib(pisano_mod) % m

n,m = input().split(' ')
print(huge_fibonacci(int(n),int(m)))
