#include <iostream>

using namespace std;
int main()
{
    long   N,A[100000],Q,X[10000],R,p;
    cin>>N>>Q;
    for (int i=0;i<N;i++){
        cin>>A[i];
    }
    for (int i=0;i<Q;i++){
        cin>>X[i];
    }
   for (int i=0;i<Q;i++){
        R=0;
        bool isprime=false;
         for (int j=0;j<N;j++){
         R = R = X[i] - X[i] % A[j];

         if (R==X[i])
         {
            for (int k=2;k<=R/2;k++)
            {
                if(R%k==0){
                    R=0;
                };
            };
            if(R==0){
            cout<<"YES"<<endl;
             isprime=true;
                break;
            }
            else {
                isprime=false;
            }

         }

         }
         if(isprime==false){
          cout<<"NO"<<endl;
         }
          }

    return 0;
}
