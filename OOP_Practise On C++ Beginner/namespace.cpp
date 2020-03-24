#include <iostream>

using namespace std;
///Namespace is always global'
namespace N{
    int a;
    class c{
public :
    int x;
    } ;
    int f();

}

int N::f()
{
    return 2;
}
namespace N{
int b;
}
int main()
{
    N::a=30;
    N::b=50;
    cout<<N::a<<" "<<N::b<<endl;

    using namespace N;
     a =5;

    cout <<a*b<< endl;
    c ob;
    ob.x=5;
    cout<<ob.x<<endl;
    return 0;

}
