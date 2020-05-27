# Uses python3
import sys

def get_majority_element(arr, size):
    m = {} #//dictionary or hashmap
    for i in range(size):
        if arr[i] in m:
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1
    count = 0
    print(m)
    for key in m:
        if m[key] > size / 2:
            return key
    if(count == 0):
        return -1

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    n=10;
    a=[3, 124554847, 2, 941795895, 2, 2, 2, 2, 3, 756617003]
    # print(a)
    if get_majority_element(a, n) != -1:
        print(1)
    else:
        print(0)
