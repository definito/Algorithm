# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    a = 0
    b = 1
    for i in range(2,m*m+2):
        c = (a + b)%m
        a = b
        b = c
        if(a==0 and b==1):
            return i-1

def get_sum_reminder(n,m):
    pisano_p= get_fibonacci_huge_naive(n, m)
    # print(pisano_p)
    reminder= n%pisano_p
    a=0
    b=1
    if(reminder!=0):
        for i in range(2,reminder+1):
            c= (a+b)%m
            a=b
            b=c
        return b % m
    else:
     return a


if __name__ == '__main__':

    n, m = map(int, input().split())
    print(get_sum_reminder(n, m))
