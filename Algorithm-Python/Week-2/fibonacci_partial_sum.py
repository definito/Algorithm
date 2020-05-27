# Uses python3

def fiball(f,n,m):

    a = 0
    b = 1
    f[0]=a
    f[1]=b
    total=1

    sum=0
    sum2=0

    for i in range(2,61):
        c = a + b
        a = b
        b = c
        f[i]=b%10
        total=total+f[i]

    multiple=int(n/60)
    remd=n%60
    sum= multiple*total

    for i in range(remd):
        sum=sum+f[i]
    if(n==m):
        return f[n%60]
    if(n!=m):
        multiple2=int(m/60)
        remd2=m%60
        sum2= multiple2*total
        for i in range(remd2+1):
            sum2=sum2+f[i]
        tsum=sum2-sum
        # print(f)
        # print(multiple,remd,multiple2,remd2,sum,sum2,tsum)
        return tsum%10


if __name__ == '__main__':
    f = [0] * 61
    a, b = map(int, input().split())
    print(fiball(f,a,b))
