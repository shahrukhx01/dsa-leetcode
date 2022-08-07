# Uses python3
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

n = int(input())
print(calc_fib(n))
