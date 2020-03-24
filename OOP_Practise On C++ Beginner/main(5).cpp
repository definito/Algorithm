#include <iostream>

using namespace std;
template <class T>
void interchange(T &a ,T &b)
{
    T temp;
    temp=a;
    a=b;
    b=temp;
}
template <class T=char ,int size=50>
class abc{
   T x[size] ;
public:
    abc() {};

   void print(){cout<<sizeof(x)<<endl;}
};



int main()
{
    string a,b;
    a="Deb";
    b="Chandrima";
    interchange(a,b);
    cout <<a<<"+"<<b<<endl;
   abc<> ob;
    ob.print();
    return 0;
}
