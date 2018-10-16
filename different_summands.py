# Uses python3
import sys

def optimal_summands(n):
    summands = []
    sum = 0
    i = 1
    #write your code here
    while True:

        if (n-sum)-i > i :
            sum += i
            summands.append(i)
        else:
            summands.append(n-sum)
            break
        i += 1
    return summands

if __name__ == '__main__':
    input = input()#sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
