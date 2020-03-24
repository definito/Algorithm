#include <iostream>

using namespace std;

int Bigmod(int a, int b, int c)
{
    if(b==0) return 1;

    if(b%2==0)
    {
        int x=Bigmod(a,b/2,c);
        cout<<"Before: " <<b<<endl;
        return (x*x)%c;
        cout<<"After:: "<<x<<endl;
    }
    else {
            int half1 =Bigmod(a,b-1,c);
            int half2 =a%c;
            cout<<"Half Value: "<<b<<" + "<<half2<<endl;
            return (half1* half2)%c;
    }
}

int main(){

   // freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);

    int B,P,M;
        B=2;
        P=30;
        M=11;
    //while(cin>>B>>P>>M)
        cout<<Bigmod(B,P,M)<<endl;

	return 0;
}
