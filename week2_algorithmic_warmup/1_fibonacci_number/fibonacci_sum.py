# Uses python3
def calc_fib(n):
    f = []
    if n >= 1:
        f.append(1)
        f.append(1)
    else:
        return 0

    for i in range(2,n):
        f.append((f[i-1] + f[i-2]) % 10)

    return f[n-1]

def fibonacci_sum(n):
    return (calc_fib(n+2)-1) % 10

n = int(input())
print(fibonacci_sum(n))
