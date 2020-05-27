# Uses python3
def fib(f, n):
    # 0th and 1st number of
    # the series are 0 and 1
    f[0] = 0
    f[1] = 1

    # Add the previous 2 numbers
    # in the series and store
    # last digit of result
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 10

    return f


# Returns last digit of n'th
# Fibonacci Number
def findLastDigit(n):
    f = [0] * 61

    # Precomputing units digit of
    # first 60 Fibonacci numbers
    f = fib(f, 60)

    return f[n % 60]
# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % 10

if __name__ == '__main__':
    n = int(input())
    print(findLastDigit(n))
