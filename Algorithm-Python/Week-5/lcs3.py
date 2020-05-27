#Uses python3
import sys
import numpy as np
def lcs3(arr, brr,crr):
    rows = len(arr) + 1
    cols = len(brr) + 1
    z= len(crr)+1
    T = [[[0] * rows] * cols] *z
    T = np.array(T)
    lcsmat=T
    ins=[0]*6

    # print(T)
    # for i in range(len(crr)):
    #     for j in range(len(brr)):
    #         for k in range(len(arr)):
    #         # print(i,j)
    #
    #             arg2 = T[i +1][j+1][k]
    #             arg3 = T[i][j + 1][k+1]
    #             arg1= T[i+1][j][k+1]
    #             arg4= T[i][j][k+1]
    #             arg5=T[i][j+1][k]
    #             arg6=T[i+1][j][k]
    #             if arr[i] == brr[j]==crr[k]:
    #
    #                 T[i+1][j+1][k+1]=1+T[i][j][k] #Take the Diagonal Value
    #             else:
    #                 T[i + 1][j + 1][k+1] = max(arg2, arg3,arg1,arg4,arg5,arg6) #Take Minimum Value+1
    #     ins = [0]*6
    for z in range(1, len(crr) + 1):
        for y in range(1, len(brr) + 1):
            for x in range(1, len(arr) + 1):
                ins[0] = lcsmat[z][y][x-1]
                ins[1] = lcsmat[z][y-1][x]
                ins[2] = lcsmat[z][y-1][x-1]
                ins[3] = lcsmat[z-1][y][x]
                ins[4] = lcsmat[z-1][y][x-1]
                ins[5] = lcsmat[z-1][y-1][x]
                mis = lcsmat[z-1][y-1][x-1]
                mat = lcsmat[z-1][y-1][x-1] + 1
                if arr[x-1] == brr[y-1] == crr[z-1]:
                    lcsmat[z][y][x] = max(max(ins), mat)
                else:
                    lcsmat[z][y][x] = max(max(ins), mis)
    return T[-1][-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))


# import sys
# import numpy as np
# def lcs3(a, b, c):
#     #write your code here
#     lcsmat = [[[0 for x in range(len(a) + 1)] for y in range(len(b) + 1)] for z in range(len(c) + 1)]
#     print(type(lcsmat))
#     lcsmat= np.array(lcsmat)
#     ins = [0]*6
#     for z in range(1, len(c) + 1):
#         for y in range(1, len(b) + 1):
#             for x in range(1, len(a) + 1):
#                 ins[0] = lcsmat[z][y][x-1]
#                 ins[1] = lcsmat[z][y-1][x]
#                 ins[2] = lcsmat[z][y-1][x-1]
#                 ins[3] = lcsmat[z-1][y][x]
#                 ins[4] = lcsmat[z-1][y][x-1]
#                 ins[5] = lcsmat[z-1][y-1][x]
#                 mis = lcsmat[z-1][y-1][x-1]
#                 mat = lcsmat[z-1][y-1][x-1] + 1
#                 if a[x-1] == b[y-1] == c[z-1]:
#                     lcsmat[z][y][x] = max(max(ins), mat)
#                 else:
#                     lcsmat[z][y][x] = max(max(ins), mis)
#     # print(lcsmat)
#     return lcsmat[-1][-1][-1]
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     an = data[0]
#     data = data[1:]
#     a = data[:an]
#     data = data[an:]
#     bn = data[0]
#     data = data[1:]
#     b = data[:bn]
#     data = data[bn:]
#     cn = data[0]
#     data = data[1:]
#     c = data[:cn]
#     print(lcs3(a, b, c))
