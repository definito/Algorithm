# python3
import sys


# def compute_min_refills(distance,  mileage, stops):
#     # write your code here
#     travel=0
#     refill= mileage
#     status=0
#     max_stn = max(stops)
#     if (max_stn + mileage >= distance):
#         while travel<=distance:
#
#             near_r= min(stops, key=lambda x: abs(x -refill))
#             # print(near_r)
#
#             if (near_r<=refill):
#                 status=status+1
#                 refill=near_r+mileage #next-refill
#                 travel=refill
#                 # print('refil:', refill)
#             else:
#                 travel=mileage
#                 status=-1
#                 break
#     else:
#         status=-1
#     return status

# def compute_min_refills(distance,  mileage,n, stops):
#     # write your code here
#     numRefil=0
#     currentRefil=0
#     if (max(stops) + mileage >= distance):
#         while currentRefil<n-1:
#             lastRefil=currentRefil
#
#             while(currentRefil<n-1 and stops[currentRefil+1]-stops[lastRefil]<=mileage):
#                 currentRefil=currentRefil+1
#                 # print('c:',currentRefil)
#             if (currentRefil==lastRefil):
#                 return -1
#
#             if(currentRefil<n):
#                 numRefil=numRefil+1
#         return numRefil
#     else:
#         return -1
def car_fueling(dist,miles,n,gas_stations):
    num_refill, curr_refill, limit = 0,0,miles
    while limit < dist:  # While the destination cannot be reached with current fuel
        if curr_refill >= n or gas_stations[curr_refill] > limit:
            # Cannot reach the destination nor the next gas station
            return -1
        # Find the furthest gas station we can reach
        while curr_refill < n-1 and gas_stations[curr_refill+1] <= limit:
            curr_refill += 1
        num_refill += 1  # Stop to tank
        limit = gas_stations[curr_refill] + miles  # Fill up the tank
        curr_refill += 1
    return num_refill


if __name__ == '__main__':

    d=int(input())
    m= int(input())
    n=int(input())
    stops = [int(x) for x in input().split()]

    refill=car_fueling(d,m,n,stops)

    # print(car_fueling(10, 3, 4, [1, 2, 5, 9]))
    # print(d, m, n,stops)
    print(refill)
    # print(car_fueling(10, 3, 4, [1, 2, 5, 9]))
