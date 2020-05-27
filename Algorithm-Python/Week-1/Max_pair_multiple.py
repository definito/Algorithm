# import random
# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                 numbers[first] * numbers[second])
#
#     return max_product

def max_product_fast(numbers):
    size=len(numbers)
    max_i=0
    max_ii=0
    for i in range(1,size):
        if(numbers[i]>numbers[max_i]):
           max_i = i
    p1=numbers[max_i]
    numbers.remove(numbers[max_i])
    # print(numbers)

    for j in range(1,size-1):
        if (numbers[j] > numbers[max_ii]):
            max_ii = j
    # print(max_ii)

    return p1* numbers[max_ii]


if __name__ == '__main__':

    # a = [5, 5, 2, 5, 6, 6]
    # # print(max_pairwise_product(a))
    input_n = int(input())
    a = [int(x) for x in input().split()]
    # print(a)
    # print(max_pairwise_product(a))
    print(max_product_fast(a))

    # mylist=[]
    # while(True):
    #
    #     n=random.randint(5,600)
    #     # print(n)
    #     for i in range(n):
    #         rand= random.randint(i,n)
    #     # print(rand)
    #         mylist.append(rand)
    #     print(mylist)
    #
    #     res1=max_pairwise_product(mylist)
    #     res2=max_product_fast(mylist)
    #     if(res1==res2):
    #         print("OK\n")
    #         print(res1,res2)
    #     else:
    #         print("Doesn't Match")
    #         print(res1, res2)
    #         break
    #     mylist = []
























