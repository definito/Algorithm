# Uses python3
import sys
import math
##First Way
# def get_change(denominations,money):
#     minCoins = [0] + [math.inf] * money
#     for i in range(1, money + 1):
#         for j in denominations:
#             if i >= j:
#                 coins = minCoins[i - j] + 1
#                 print("1:",i,j,coins)
#                 if coins < minCoins[i]:
#                     minCoins[i] = coins
#                     print("2:", i, j, coins)
#     return minCoins[i]

##2nd Way
def get_change(denominations,money):
    rows=len(denominations)
    col =money+1
    arr=[[math.inf]*col]*rows
    for i in range(rows):
        arr[i][0]=0
    # print(arr[-1][7])
    print(arr)
    for i in range(0, len(denominations)):
        col=[]
        for j in range(1,money+1):
            if denominations[i]>j:
                arr[i][j]=arr[i-1][j]

            else:
                # if(i-1<0):
                #     val=min(math.inf,1+arr[i][j-denominations[i]])
                # else:
                #     val = min(arr[i-1][j], 1 + arr[i][j - denominations[i]])
                arr[i][j] = min(arr[i - 1][j], 1 + arr[i][j - denominations[i]])
                # print(i-1,j,arr[-1][j], 1 + arr[i][j - denominations[i]])

        # print(arr)


        # for j in range(1,money+1):
        #     if(denominations[i]>j):


    return arr[len(denominations)-1][money]
if __name__ == '__main__':
    m = int(input())
    coins=[1,3,4]
    # print(coins)
    print(get_change(coins,m))
