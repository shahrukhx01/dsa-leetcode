#Uses python3
import sys

def largest_number(a):
    #write your code here
    res = ""
    while len(a) > 0:
        maxDigit = '0'
        maxIndex = 0
        for index,x in enumerate(a):
            if IsGreaterOrEqual(x,maxDigit):
                maxDigit = x
                maxIndex = index
        del a[maxIndex]
        res += maxDigit
    return res

def IsGreaterOrEqual(digit,maxDigit):
    if (int((digit+maxDigit)) > int(maxDigit+digit)):
        return True
    else:
        return False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
