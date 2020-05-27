# Uses python3
import numpy as np
def edit_distance(arr, brr):
    rows = len(arr) + 1
    cols = len(brr) + 1
    T=[[0]*cols]*rows
    T= np.array(T)

    for i in range(0,rows):
        for j in range(0,cols):
            if (j==0):
                T[i][j]=i
            if(i==0):
                T[i][j]=j
    # print(T)

    for i in range(len(arr)):
        for j in range(len(brr)):
            # print(i,j)
            arg1 = T[i][j]
            arg2 = T[i + 1][j]
            arg3 = T[i][j + 1]
            if arr[i].casefold() == brr[j].casefold():

                T[i+1][j+1]=T[i][j] #Take the Diagonal Value
            else:
                T[i + 1][j + 1] = 1+min(arg1, arg2, arg3) #Take Minimum Value+1
    # print(T)



    return T[rows-1][cols-1]

if __name__ == "__main__":
    a=input()
    b=input()
    arr=list(a)
    brr=list(b)

    print(edit_distance(arr, brr))
# import numpy
#
#
# def EditDistance(s1, s2):
#     """ Computes the edit distance of two strings
#     (str, str) -> (int, 2D-array) """
#     ln_s1 = len(s1)
#     ln_s2 = len(s2)
#
#     # Initializing the matrix
#     Matrix = numpy.zeros((ln_s1 + 1, ln_s2 + 1))
#     for i in range(ln_s2 + 1):
#         Matrix[0][i] = i
#
#     for i in range(ln_s1 + 1):
#         Matrix[i][0] = i
#
#     # Filling the matrix
#     for i in range(1, ln_s1 + 1):
#         for j in range(1, ln_s2 + 1):
#             insertion = Matrix[i][j - 1] + 1
#             deletion = Matrix[i - 1][j] + 1
#             mismatch = Matrix[i - 1][j - 1] + 1
#             match = Matrix[i - 1][j - 1]
#             if s1[i - 1] == s2[j - 1]:
#                 Matrix[i][j] = min(insertion, deletion, match)
#             if s1[i - 1] != s2[j - 1]:
#                 Matrix[i][j] = min(insertion, deletion, mismatch)
#
#     return (int(Matrix[ln_s1][ln_s2]), Matrix)
#
#
# def OptimalAlignment(Matrix, s1, s2, top, bottom, i, j):
#     """ Finds the optimal alignment of two strings given the edit matrix
#     (2D-array, str, str, str, str, int, int) -> (str, str) """
#
#     if i == 0 and j == 0:
#         return (' '.join(top[::-1]), ' '.join(bottom[::-1]))
#
#     if i > 0 and Matrix[i][j] == Matrix[i - 1][j] + 1:
#         top.append(f'|{s1[i - 1]}|')
#         bottom.append('|-|')
#         return OptimalAlignment(Matrix, s1, s2, top, bottom, i - 1, j)
#
#     elif j > 0 and Matrix[i][j] == Matrix[i][j - 1] + 1:
#         bottom.append(f'|{s2[j - 1]}|')
#         top.append('|-|')
#         return OptimalAlignment(Matrix, s1, s2, top, bottom, i, j - 1)
#
#     else:
#         top.append(f'|{s1[i - 1]}|')
#         bottom.append(f'|{s2[j - 1]}|')
#         return OptimalAlignment(Matrix, s1, s2, top, bottom, i - 1, j - 1)
#
#
# if __name__ == '__main__':
#     s1, s2 = input(), input()
#     edit_distance, Matrix = EditDistance(s1, s2)
#     top, bottom = OptimalAlignment(Matrix, s1, s2, [], [], len(s1), len(s2))
#
#     print(f'Editing distance : {edit_distance}')
#     print(f"Optimal alignment:\n{top}\n{bottom}")