# Uses python3
def gcd(a,b):
    if (a%b == 0):
        return b
    elif (a%b == 1):
        return 1
    return gcd(b,a%b)

def lcm(a,b):
    return int((a*b)//gcd(a,b))

a,b = input().split(' ')
print(lcm(int(a),int(b)))
