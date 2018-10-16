# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [10,5,1]
    cointCount = 0
    for index,val in enumerate(coins):
        if m % val == m:
            continue
        cointCount += m // val
        m = m % val
    return cointCount

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
