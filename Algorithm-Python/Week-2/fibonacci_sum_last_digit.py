# Uses python3

def fiball(f,n):
    a = 0
    b = 1
    f[0]=a
    f[1]=b
    total=1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,61):
            c = a + b
            a = b
            b = c
            f[i]=b%10
            total=total+f[i]

    multiple=int(n/60)
    remd=n%60
    sum= multiple*total
    for i in range(0,remd+1):
        sum=sum+f[i]
    print(sum)
    return sum%10


if __name__ == '__main__':
    f = [0] * 61
    n = int(input())
    print(fiball(f,n))
