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
template <class T>
class abc{
   T a ;
public:
    abc() {};
   abc(T x){a=x;}
   void set(T x);
   T get(){T a;}
   void print(){cout<<a<<endl;}
};

template<class T>
class abc<T>::set(T x){};

int main()
{
    string a,b;
    a="Deb";
    b="Chandrima";
    interchange(a,b);
    cout <<a<<"+"<<b<<endl;
   // abc <string> ob;
   // ob.set("Love each other");
   // ob.print();

    return 0;
}
