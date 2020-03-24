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
template <class T1 ,class T2>
class abc{
   T1 a ;
   T2 b;
public:
    abc() {};
   abc(T1 x,T2 y){a=x;b=y;}
   void set(T1 x,T2 y);
   T1 geta(){return a;}
   T2 getb(){return b;}
   void print(){cout<<a<<" "<<b<<endl;}
};
template<class T1,class T2>
void abc<T1,T2>:: set(T1 x,T2 y){
     a = x ;
     b= y;
}


int main()
{
    string a,b;
    a="Deb";
    b="Chandrima";
    interchange(a,b);
    cout <<a<<"+"<<b<<endl;
    abc <string,string> ob;
    ob.set("Love each other","100%");
    ob.print();

    return 0;
}
