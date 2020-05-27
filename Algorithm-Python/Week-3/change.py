# Uses python3
import sys

def get_change(m):
    #write your code here
    coin=0
    if(m>=10):
        val=int(m/10)
        m= m- val*10
        coin=coin+val
    if(m>=5):
        val=int(m/5)
        m=m-val*5
        coin=coin+val
    if(m<5):
        coin=coin+m
    return coin

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))



