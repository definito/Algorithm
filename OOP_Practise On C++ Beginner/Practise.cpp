#include<iostream>

using namespace std;

int main()
{
    int i,j,k,n;
   n=5;
   int a[5]={1,2,3,3,4};

    for(i=0;i<n;++i)
        for(j=i+1;j<n;)
        {
            if(a[i]==a[j])
            {
                for(k=j;k<n-1;++k)
                    a[k]=a[k+1];

                --n;
            }
            else
                ++j;
        }

    cout<<"\n";
    for(i=0;i<n;++i)
        cout<<a[i]<<" ";

    return 0;
}
