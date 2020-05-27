# python3
import numpy as np

# Discrete Knapsack problem without repetition
def partitions(W, w):
    # write your code here
    rows = len(w) + 1
    cols = W +1
    T = [[0] * cols] * rows
    T = np.array(T)
    cout=0
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
            if T[i][j]==W: cout=cout+1
    if (cout<3):
        return print(0)
    else:
        return print(1)

if __name__ == '__main__':
    n = int(input())
    w = [int(i) for i in input().split()]
    total_weight = sum(w)
    if n<3:
        print('0')
    elif total_weight%3 != 0:
        print('0')
    else:
        partitions(total_weight//3, w)
