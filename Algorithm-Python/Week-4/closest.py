#Uses python3
import sys
import math

from bisect import bisect_left, bisect_right
from itertools import combinations, islice
from math import hypot
from operator import itemgetter


# def minimum_distance(x, y):
#     #write your code here
#     return 10 ** 18
#
# def distance(p, q):
#     "Return the Euclidean distance between points p and q."
#     return hypot(p[0] - q[0], p[1] - q[1])
#
# _Y_COORD = itemgetter(1)
#
# def closest_distance(P):
#     "Return the closest Euclidean distance between two points in the list P."
#     P = sorted(P)
#     PX = [x for x, _ in P]
#     print(P)
#
#     def _closest(start, stop):
#         if stop - start <= 3: #8 Performs well
#             return min(distance(p, q)
#                        for p, q in combinations(P[start:stop], 2))
#
#         mid = (start + stop) // 2
#         dist = min(_closest(start, mid), _closest(mid, stop))
#
#         mid_x = PX[mid]
#         left = bisect_left(PX, mid_x - dist, lo=start, hi=mid)
#         right = bisect_right(PX, mid_x + dist, lo=mid, hi=stop)
#         strip = sorted(P[mid:right], key=_Y_COORD)
#         strip_y = list(map(_Y_COORD, strip))
#
#
#         for p in P[left:mid]:
#             y = p[1]
#             i = bisect_left(strip_y, y - dist)
#             j = bisect_right(strip_y, y + dist)
#             assert j - i <= 6
#             for q in strip[i:j]:
#                 dist = min(dist, distance(p, q))
#
#         return dist
#
#     return _closest(0, len(P))
def square(x):
    return x * x


def square_distance(p0, p1):
    return square(p0[0] - p1[0]) + square(p0[1] - p1[1])


def closest(P, n):
    P.sort() # sort by x coordinates
    return math.sqrt(_closest_square_distance(P, n))


def _closest_square_distance(P, n):
    if n == 2:
        return square_distance(P[0], P[1])
    if n == 3:
        return min(square_distance(P[0], P[1]), square_distance(P[0], P[2]), square_distance(P[1], P[2]))

    mid = n // 2
    dl = _closest_square_distance(P[:mid], mid)
    dr = _closest_square_distance(P[mid:], n - mid)

    closest_square_distance = min(dl, dr)
    closest_distance_so_far = math.sqrt(closest_square_distance)

    mid_x = P[mid][0]
    strip = []
    strip_length = 0
    for i in range(n):
        p = P[i]
        if abs(p[0] - mid_x) < closest_distance_so_far:
            strip.append(p)
            strip_length += 1

    strip.sort(key=lambda x: x[1]) # sort strip by y coordinates

    for i in range(strip_length):
        js = min(strip_length, i + 7) # sufficient to compute next 6 neighbors
        for j in range(i + 1, js):
            ds = square_distance(strip[i], strip[j])
            if ds < closest_square_distance:
                closest_square_distance = ds

    return closest_square_distance
if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # x = data[1::2]
    # y = data[2::2]
    # n=int(input())
    # P =[list(map(int,input().split())) for i in range(n)]
    P=[[4, 4], [-2, -2], [-3, -4], [-1, 3], [2, 3], [-4, 0], [1, 1], [-1, -1], [3, -1], [-4, 2], [-2, 4]]
    print(P)
    # print("{0:.9f}".format(closest_distance(P)))
    print("{0:.9f}".format(closest(P,len(P))))


