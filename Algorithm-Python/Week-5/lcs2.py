#Uses python3

import sys
import numpy as np
def lcs2(arr, brr):
    rows = len(arr) + 1
    cols = len(brr) + 1
    T = [[0] * cols] * rows
    T = np.array(T)
    # print(T)
    for i in range(len(arr)):
        for j in range(len(brr)):
            # print(i,j)

            arg2 = T[i + 1][j]
            arg3 = T[i][j + 1]
            if arr[i] == brr[j]:

                T[i+1][j+1]=1+T[i][j] #Take the Diagonal Value
            else:
                T[i + 1][j + 1] = max(arg2, arg3) #Take Minimum Value+1

    return T[rows-1][cols-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]
    # a=[2,7,8,3]
    # b=[5,2,8,7]
    print(lcs2(a, b))
