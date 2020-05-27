#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    for i in range(len(a)):
        maxa=max(a)
        maxb=max(b)
        a.remove(maxa)
        b.remove(max(b))
        res += maxa*maxb
    return res

if __name__ == '__main__':
    x=int(input())
    a= [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(max_dot_product(a, b))
    
