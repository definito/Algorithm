#include <iostream>

using namespace std;

int main()
{
    int N,A[100],j=0;
    cin>>N;
   for(int i=0;i<N;i++)
   {
     cin>>A[i];
     if(A[i]==1)
     {
       j=j+1;
     }
     if(i==N-1) break;
   }
 /*  for(int i=0;i<N;i++)
   {
     if(A[i]==1)
     {
       j=j+1;
     }
   }*/
    cout<<j<< endl;
    return 0;
}
