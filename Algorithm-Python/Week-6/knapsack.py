# Uses python3
import sys
import numpy as np

def optimal_weight(W, w):
    # write your code here
    rows = len(w) + 1
    cols = W +1
    T = [[0] * cols] * rows
    T = np.array(T)
    # print(T)
    # result = 0
    for i in range(1,len(w)+1):
        for j in range(1,W+1):
            if(w[i-1]>j):
                T[i][j]= T[i-1][j]
            else:
                val1=T[i-1,j]
                val2=T[i-1, j-w[i-1]]+ w[i-1] #Here we need to maximize W(i)][weight] not profit
                T[i][j]=max(val1,val2)
    return T[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    # W=8
    # w=[3,4,6,5]
    print(optimal_weight(W, w))
