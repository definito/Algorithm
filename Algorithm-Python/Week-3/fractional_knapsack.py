# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0. #max value
    ratio, values, weights = zip(*sorted(((v / w, v, w) for v, w in zip(values, weights)),reverse=True))
    index = list(range(len(values)))
    # print(ratio,values,weights)

    for i in index:
        if (capacity-weights[i]>=0):
            value += values[i]
            capacity -= weights[i]
            # print("z:\n",value)
        else:
            fraction = capacity / weights[i]
            value += values[i]*fraction
            capacity = int(capacity - (fraction*weights[i]))
            # print(values[i],weights[i])
            break


    return value


if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    # n, capacity = data[0:2]
    # values = data[2:(2 * n + 2):2]
    # weights = data[3:(2 * n + 2):2]
    # opt_value = get_optimal_value(capacity, weights, values)
    # print("{:.10f}".format(opt_value))
    # print(capacity, weights, values)
    x,capacity =map(int,input().split())
    values=[]
    weight=[]
    for i in range(x):
        val, wei =map(int,input().split())
        values.append(val)
        weight.append(wei)

    # print(x, capacity)
    # print(capacity, weight, values)
    opt_value = get_optimal_value(capacity, weight, values)
    print("{:.10f}".format(opt_value))
