# Uses python3

#
# def gcd(a, b):
#     if a == 0:
#         return b
#
#     return gcd(b % a, a)


def gcdExtended(a, b):
    # Base Case
    if a == 0:
        x = 0
        y = 1
        return b
    x1 = 1
    y1 = 1  # storing the result
    gcd = gcdExtended(b % a, a)
    # Update x and y with previous calculated values
    x = y1 - (b / a) * x1
    y = x1
    return gcd

if __name__ == "__main__":

    a, b = map(int, input().split())
    print(gcdExtended(a, b))
