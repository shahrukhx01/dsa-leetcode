# Uses python3
def gcd(a,b):
    if (a%b == 0):
        return b
    elif (a%b == 1):
        return 1
    return gcd(b,a%b)

a,b = input().split(' ')
print(gcd(int(a),int(b)))
