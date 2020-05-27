# Uses python3
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
    lcm=(a*b)/gcdExtended(a, b)
    print(int(lcm))
