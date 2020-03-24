#include <iostream>

using namespace std;
class base{
public:
    int a ;
};

class derive: public base{
public:
    int b;

};

int main()
{
    base b;
    derive *c;
    derive d;
    b.a=5;
    d.b=6;
    cout<<b.a<<"\n"<<d.b<<endl;
    c =&d;
    c->a=5;

    cout<<c->a<<endl;
    return 0;
}
